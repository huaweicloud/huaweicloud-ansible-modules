#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Huawei
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import argparse
import re
import yaml
import configparser
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from time import time
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkecs.v2 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.http.http_config import HttpConfig


class EcsInventory(object):

    def _empty_inventory(self):
        return {"_meta": {"hostvars": {}}}

    def __init__(self):
        ''' Main execution path '''

        self.inventory = self._empty_inventory()

        # Index of hostname (address) to instance ID
        self.index = {}

        # Huaweicloud credentials.
        self.credentials = {}

        # Init some variables
        self.destination_variable = ""
        self.hostname_variable = ""
        self.ecs_instance_states = []

        self.cache_path_cache = ""
        self.cache_path_index = ""
        self.cache_max_age = 0

        self.nested_groups = False
        self.replace_dash_in_groups = True

        self.pattern_include = None
        self.pattern_exclude = None

        self.ecs_instance_filters = dict(page_size=100)

        # Read settings and parse CLI arguments
        self.args = None
        self.parse_cli_args()
        self.read_settings()

        # Cache
        if self.args.refresh_cache:
            self.do_api_calls_update_cache()
        elif os.path.isfile(self.cache_path_cache) and os.path.isfile(self.cache_path_index):
            if os.path.getmtime(self.cache_path_cache) + self.cache_max_age < time():
                self.do_api_calls_update_cache()
        else:
            self.do_api_calls_update_cache()

        # Data to print
        if self.args.host:
            data_to_print = self.get_host_info()

        elif self.args.list:
            # Display list of instances for inventory
            if self.inventory == self._empty_inventory():
                data_to_print = self.get_inventory_from_cache()
            else:
                data_to_print = self.json_format_dict(self.inventory, True)

        print(data_to_print)

    def parse_cli_args(self):
        ''' Command line argument processing '''

        parser = argparse.ArgumentParser(description='Produce an Ansible Inventory file based on ECS')
        parser.add_argument('--list', action='store_true', default=True,
                            help='List instances (default: True)')
        parser.add_argument('--host', action='store',
                            help='Get all the variables about a specific instance')
        parser.add_argument('--refresh-cache', action='store_true', default=False,
                            help='Force refresh of cache by making API requests to ECS (default: False - use cache files)')
        self.args = parser.parse_args()

    def read_settings(self):
        ''' Reads the settings from the hwc_ecs.ini file '''

        config = configparser.ConfigParser()

        ecs_default_ini_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'hwc_ecs.ini')
        ecs_ini_path = os.path.expanduser(os.path.expandvars(os.environ.get('ANSIBLE_HWC_INI_PATH', ecs_default_ini_path)))
        config.read(ecs_ini_path)

        access_key = os.environ.get('ANSIBLE_HWC_ACCESS_KEY', None)
        if not access_key:
            access_key = self.get_option(config, 'credentials', 'access_key')

        secret_key = os.environ.get('ANSIBLE_HWC_SECRET_KEY', None)
        if not secret_key:
            secret_key = self.get_option(config, 'credentials', 'secret_key')

        region = os.environ.get('ANSIBLE_HWC_REGION', None)
        if not region:
            region = self.get_option(config, 'credentials', 'region')

        project_id = os.environ.get('ANSIBLE_HWC_PROJECT_ID', None)
        if not project_id:
            project_id = self.get_option(config, 'credentials', 'project_id')

        cloud = os.environ.get('ANSIBLE_HWC_CLOUD', None)
        if not cloud:
            cloud = self.get_option(config, 'credentials', 'cloud')

        identity_endpoint = os.environ.get('ANSIBLE_HWC_IDENTITY_ENDPOINT', None)
        if not identity_endpoint:
            identity_endpoint = self.get_option(config, 'credentials', 'identity_endpoint')

        self.credentials = {
            'access_key': access_key,
            'secret_key': secret_key,
            'project_id': project_id,
            'region': region,
            'cloud': cloud,
            'identity_endpoint': identity_endpoint,
        }

        # Region
        self.region = region
       
        # # Destination addresses
        self.destination_variable = self.get_option(config, 'ecs', 'destination_variable', "")

        self.hostname_variable = self.get_option(config, 'ecs', 'hostname_variable', "")


        # Instance states to be gathered in inventory. Default is 'running'.
        ecs_valid_instance_states = ['ACTIVE', 'BUILD', 'ERROR', 'HARD_REBOOT', 'MIGRATING', 'REBOOT', 'REBUILD', 'RESIZE', 'REVERT_RESIZE', 'SHUTOFF', 'VERIFY_RESIZE']

        if self.get_option(config, 'ecs', 'all_instances'):
            self.ecs_instance_states.extend(ecs_valid_instance_states)
        elif self.get_option(config, 'ecs', 'instance_states'):
            for instance_state in self.get_option(config, 'ecs', 'instance_states').split(","):
                instance_state = instance_state.strip()
                if instance_state not in ecs_valid_instance_states:
                    continue
                self.ecs_instance_states.append(instance_state)
        else:
            self.ecs_instance_states.append('active')

        # Cache related
        cache_dir = os.path.expanduser(self.get_option(config, 'ecs', 'cache_path'))
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        cache_name = 'ansible-huaweicloud'
        self.cache_path_cache = cache_dir + "/%s.cache" % cache_name
        self.cache_path_index = cache_dir + "/%s.index" % cache_name
        self.cache_max_age = float(self.get_option(config, 'ecs', 'cache_max_age'))

        self.expand_csv_tags = self.get_option(config, 'ecs', 'expand_csv_tags')

        # Configure nested groups instead of flat namespace.
        self.nested_groups = self.get_option(config, 'ecs', 'nested_groups')

        # Configure which groups should be created.
        group_by_options = [
            'group_by_instance_id',
            'group_by_region',
            'group_by_availability_zone',
            'group_by_image_id',
            'group_by_vpc_id',
            'group_by_security_group',
        ]
        for option in group_by_options:
            setattr(self, option, self.get_option(config, 'ecs', option))

        # Do we need to just include hosts that match a pattern?
        try:
            pattern_include = self.get_option(config, 'ecs', 'pattern_include')
            if pattern_include and len(pattern_include) > 0:
                self.pattern_include = re.compile(pattern_include)
        except configparser.NoOptionError:
            raise

        # Do we need to exclude hosts that match a pattern?
        try:
            pattern_exclude = self.get_option(config, 'ecs', 'pattern_exclude')
            if pattern_exclude and len(pattern_exclude) > 0:
                self.pattern_exclude = re.compile(pattern_exclude)
        except configparser.NoOptionError:
            raise

    def do_api_calls_update_cache(self):
        ''' Do API calls to each region, and save data in cache files '''

        self.get_instances_by_region(self.region)

        self.write_to_cache(self.inventory, self.cache_path_cache)
        self.write_to_cache(self.index, self.cache_path_index)

    def log(self, msg, pretty_print=False):
        # Use only during module development
        pass
        
        # log_file = open('hwc_module.log', 'a')
        # if pretty_print:
        #     log_file.write(json.dumps(msg, indent=4, sort_keys=True))
        # else:
        #     log_file.write(msg + u'\n')

    def ecs_client(self, region):
        self.log('Geting ECS client')
        config = HttpConfig.get_default_config()
        config.ignore_ssl_verification = True
        if self.credentials["project_id"]:
            _credentials = BasicCredentials(self.credentials["access_key"], self.credentials["secret_key"], self.credentials["project_id"])

            if self.credentials["identity_endpoint"]:
                _credentials.iam_endpoint = self.credentials["identity_endpoint"]

            endpoint = 'https://ecs.{}.{}'.format(region, self.credentials["cloud"])
            ecs_client = EcsClient.new_builder() \
            .with_http_config(config) \
            .with_credentials(_credentials) \
            .with_endpoint(endpoint) \
            .build()
        else:
            raise HwcModuleException(
                    'Getting ECS client failed: "project_id" is required for ECS client')

        return ecs_client

    def get_instances_by_region(self, region):
        ''' List ECS instances in a specified region '''
        ecs_client = self.ecs_client(region)

        instances = []
        offset = 1

        while True:
            try:
                request = ListServersDetailsRequest(limit=10, offset=offset)
                self.log('list ecs request: %s' % request)
                response = ecs_client.list_servers_details(request)
                self.log('list ecs response: %s' % response)
            except exceptions.ClientRequestException as e:
                raise HwcModuleException(
                        'search ecs failed: %s' % e.error_msg)
            insts = self.navigate_value(response.to_json_object(), ['servers'], None)

            if not insts:
                break

            instances.extend(insts)

            offset += 1

        for instance in instances:
            self.add_instance(instance, region)

    def get_instance_by_id(self, region, instance_id):
        ''' Fetch ECS instance in a specified instance ID '''
        ecs_client = self.ecs_client(region)

        try:
            request = ShowServerRequest(instance_id)
            self.log('read ecs request body: %s' %request)
            response = ecs_client.show_server(request)
            self.log('read ecs response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read ecs failed: %s' % e)

        r = response.to_json_object()['server']

        return r

    def add_instance(self, instance, region):
        ''' Adds an instance to the inventory and index, as long as it is addressable '''

        if instance['status'] not in self.ecs_instance_states:
            return

        # Select the best destination address
        if self.destination_variable:
            nics = self.navigate_value(instance, ['addresses'], None)

            for id, addresses in nics.items():
                for address in addresses:
                    self.log('address: %s' % address)
                    if address['OS-EXT-IPS:type'] == 'fixed':
                        fixed_ip = address['addr']
                    if address['OS-EXT-IPS:type'] == 'floating':
                        eip = address['addr']


            if self.destination_variable == 'private_ip_address':
                dest = fixed_ip
            elif self.destination_variable == 'public_ip_address':
                dest = eip


        self.log('dest: %s' % dest)

        if not dest:
            # Skip instances we cannot address
            return

        # Set the inventory name
        hostname = None
        if self.hostname_variable:
            hostname = self.navigate_value(instance, [self.hostname_variable], None)

        # If we can't get a nice hostname, use the destination address
        if not hostname:
            hostname = dest
        else:
            hostname = self.to_safe(hostname).lower()

        # if we only want to include hosts that match a pattern, skip those that don't
        if self.pattern_include and not self.pattern_include.match(hostname):
            return

        # if we need to exclude hosts that match a pattern, skip those
        if self.pattern_exclude and self.pattern_exclude.match(hostname):
            return

        # # Add to index
        self.index[hostname] = [region, instance['id'], instance['name']]

        # Inventory: Group by instance ID (always a group of 1)
        if self.group_by_instance_id:
            self.push(self.inventory, instance['id'], hostname)
            if self.nested_groups:
                self.push_group(self.inventory, 'instances', instance['id'])

        # Inventory: Group by region
        if self.group_by_region:
            self.push(self.inventory, region, hostname)
            if self.nested_groups:
                self.push_group(self.inventory, 'regions', region)

        # Inventory: Group by availability zone
        if self.group_by_availability_zone:
            self.push(self.inventory, instance['OS-EXT-AZ:availability_zone'], hostname)
            if self.nested_groups:
                if self.group_by_region:
                    self.push_group(self.inventory, region, instance['OS-EXT-AZ:availability_zone'])
                self.push_group(self.inventory, 'zones', instance['OS-EXT-AZ:availability_zone'])

        # Inventory: Group by Huaweicloud Machine Image ID
        if self.group_by_image_id:
            key = self.to_safe('image_id_' + instance['image']['id'])
            self.push(self.inventory, key, hostname)
            if self.nested_groups:
                self.push_group(self.inventory, 'images', key)

        # Inventory: Group by VPC
        if self.group_by_vpc_id:
            key = self.to_safe('vpc_id_' + instance['metadata']['vpc_id'])
            self.push(self.inventory, key, hostname)
            if self.nested_groups:
                self.push_group(self.inventory, 'vpcs', key)

        # Inventory: Group by security group
        if self.group_by_security_group:
            for group in instance['security_groups']:
                key = self.to_safe("security_group_id_" + group['id'])
                self.push(self.inventory, key, hostname)
                if self.nested_groups:
                    self.push_group(self.inventory, 'security_groups', key)

        self.push(self.inventory, 'huaweicloud', hostname)

        self.inventory["_meta"]["hostvars"][hostname] = instance
        self.inventory["_meta"]["hostvars"][hostname]['ansible_ssh_host'] = dest

    def get_host_info(self):
        ''' Get variables about a specific host '''

        if len(self.index) == 0:
            # Need to load index from cache
            self.load_index_from_cache()

        if self.args.host not in self.index:
            # try updating the cache
            self.do_api_calls_update_cache()
            if self.args.host not in self.index:
                # host might not exist anymore
                return self.json_format_dict({}, True)

        region, instance_id, instance_name = self.index[self.args.host]

        instance = self.get_instance_by_id(region, instance_id)
        return self.json_format_dict(instance, True)

    def get_option(self, config, module, name, default=None):
        # Check module args and then return them from option
        option = None
        if config.has_option(module, name):
            option = config.get(module, name)
        if option is None:
            return default
        # if str.lower()option in
        return yaml.safe_load(option)

    def push(self, my_dict, key, element):
        ''' Push an element into an array that may not have been defined in the dict '''
        group_info = my_dict.setdefault(key, [])
        if isinstance(group_info, dict):
            host_list = group_info.setdefault('hosts', [])
            host_list.append(element)
        else:
            group_info.append(element)

    def push_group(self, my_dict, key, element):
        ''' Push a group as a child of another group. '''
        parent_group = my_dict.setdefault(key, {})
        if not isinstance(parent_group, dict):
            parent_group = my_dict[key] = {'hosts': parent_group}
        child_groups = parent_group.setdefault('children', [])
        if element not in child_groups:
            child_groups.append(element)

    def get_inventory_from_cache(self):
        ''' Reads the inventory from the cache file and returns it as a JSON object '''

        cache = open(self.cache_path_cache, 'r')
        json_inventory = cache.read()
        return json_inventory

    def load_index_from_cache(self):
        ''' Reads the index from the cache file sets self.index '''
        if not os.path.isfile(self.cache_path_cache) or not os.path.isfile(self.cache_path_index):
            self.write_to_cache(self.inventory, self.cache_path_cache)
            self.write_to_cache(self.index, self.cache_path_index)
        cache = open(self.cache_path_index, 'r')
        json_index = cache.read()
        self.index = json.loads(json_index)

    def write_to_cache(self, data, filename):
        ''' Writes data in JSON format to a file '''
        json_data = self.json_format_dict(data, True)
        cache = open(filename, 'w')
        cache.write(json_data)
        cache.close()

    def to_safe(self, word):
        ''' Converts 'bad' characters in a string to underscores so they can be used as Ansible groups '''
        regex = r"[^A-Za-z0-9\_"
        if not self.replace_dash_in_groups:
            regex += r"\-"
        return re.sub(regex + "]", "_", word)

    def json_format_dict(self, data, pretty=False):
        ''' Converts a dict to a JSON object and dumps it as a formatted string '''

        if pretty:
            return json.dumps(data, sort_keys=True, indent=2)
        else:
            return json.dumps(data)

    def navigate_value(self, data, index, array_index=None):
        if array_index and (not isinstance(array_index, dict)):
            raise HwcModuleException("array_index must be dict")

        d = data
        for n in range(len(index)):
            if d is None:
                return None

            if not isinstance(d, dict):
                raise HwcModuleException(
                    "can't navigate value from a non-dict object")

            i = index[n]
            if i not in d:
                raise HwcModuleException(
                    "navigate value failed: key(%s) is not exist in dict" % i)
            d = d[i]

            if not array_index:
                continue

            k = ".".join(index[: (n + 1)])
            if k not in array_index:
                continue

            if d is None:
                return None

            if not isinstance(d, list):
                raise HwcModuleException(
                    "can't navigate value from a non-list object")

            j = array_index.get(k)
            if j >= len(d):
                raise HwcModuleException(
                    "navigate value failed: the index is out of list")
            d = d[j]

        return d


class HwcModuleException(Exception):
    def __init__(self, message):
        super(HwcModuleException, self).__init__()

        self._message = message

    def __str__(self):
        return "[HwcException] message=%s" % self._message


if __name__ == '__main__':
    EcsInventory()
