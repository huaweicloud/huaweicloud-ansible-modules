#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Huawei
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

###############################################################################
# Documentation
###############################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ["preview"],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: hwc_vpc_subnet
description:
    - Creates and manages a resource of Vpc/Subnet in Huawei Cloud.
short_description: Creates a resource of Vpc/Subnet in Huawei Cloud
version_added: '1.0.0'
author: Huawei (@huaweicloud)
requirements:
    - huaweicloudsdkcore >= 3.0.47
    - huaweicloudsdkvpc >= 3.0.47
options:
    state:
        description:
            - Whether the given object should exist in Huawei Cloud.
        type: str
        choices: ['present', 'absent']
        default: 'present'
    filters:
        description:
            - A list of filters to apply when deciding whether existing
              resources match and should be altered. The item of filters
              is the name of input options.
        type: list
        required: true
    timeouts:
        description:
            - The timeouts for each operations.
        type: dict
        suboptions:
            create:
                description:
                    - The timeouts for create operation.
                type: str
                default: '15m'
            update:
                description:
                    - The timeouts for update operation.
                type: str
                default: '15m'
    cidr:
        description:
            - Specifies the subnet CIDR block. The value must be within the VPC
              CIDR block and be in CIDR format. The subnet mask cannot be
              greater than 28.
        type: str
        required: true
    gateway_ip:
        description:
            - Specifies the gateway of the subnet. The value must be an IP
              address in the subnet.
        type: str
        required: true
    name:
        description:
            - Specifies the subnet name. The value is a string of 1 to 64
              characters that can contain letters, digits, underscores C(_),
              hyphens (-), and periods (.).
        type: str
        required: true
    vpc_id:
        description:
            - Specifies the ID of the VPC to which the subnet belongs.
        type: str
        required: true
    availability_zone:
        description:
            - Specifies the AZ to which the subnet belongs.
        type: str
        required: false
    dhcp_enable:
        description:
            - Specifies whether DHCP is enabled for the subnet.
        type: bool
        default: 'yes'
        required: false
    ipv6_enable:
        description:
            - Specifies whether the IPv6 function is enabled for the subnet.
        type: bool
        default: 'no'
        required: false
    dns_address:
        description:
            - Specifies the DNS server addresses for subnet. The address
              in the head will be used first.
        type: list
        required: false
    tags:
        description:
            - Specifies the key/value pairs to associate with the subnet.
        type: dict
        required: false
extends_documentation_fragment:
  - hwceco.hwcollection.hwc_auth_options
'''

EXAMPLES = '''
# create subnet
- name: create vpc
  hwc_vpc:
      cidr: "192.168.100.0/24"
      name: "ansible_network_vpc_test"
  register: vpc
- name: create subnet
  hwc_vpc_subnet:
      filters:
          - "name"
      vpc_id: "{{ vpc.state.id }}"
      cidr: "192.168.100.0/26"
      gateway_ip: "192.168.100.32"
      name: "ansible_network_subnet_test"
      dhcp_enable: True
'''

RETURN = '''
    cidr:
        description:
            - Specifies the subnet CIDR block. The value must be within the VPC
              CIDR block and be in CIDR format. The subnet mask cannot be
              greater than 28.
        type: str
        returned: success
    gateway_ip:
        description:
            - Specifies the gateway of the subnet. The value must be an IP
              address in the subnet.
        type: str
        returned: success
    name:
        description:
            - Specifies the subnet name. The value is a string of 1 to 64
              characters that can contain letters, digits, underscores C(_),
              hyphens (-), and periods (.).
        type: str
        returned: success
    vpc_id:
        description:
            - Specifies the ID of the VPC to which the subnet belongs.
        type: str
        returned: success
    availability_zone:
        description:
            - Specifies the AZ to which the subnet belongs.
        type: str
        returned: success
    dhcp_enable:
        description:
            - Specifies whether DHCP is enabled for the subnet.
        type: bool
        returned: success
    ipv6_enable:
        description:
            - Specifies whether the IPv6 function is enabled for the subnet.
        type: bool
        returned: success
    dns_address:
        description:
            - Specifies the DNS server addresses for subnet. Note that the address
              in the head will be used first.
        type: list
        returned: success
    tags:
        description:
            - Specifies the key/value pairs to associate with the subnet.
        type: dict
        returned: success
'''

from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleBase
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleException
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import are_different_dicts
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import navigate_value
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import is_empty_value
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import build_tags_parameters
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import tags_to_dict
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import wait_to_finish

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkvpc.v2 import *


class HwcVpcSubnet(HwcModuleBase):
    def __init__(self):
        self.argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'],
                       type='str'),
            filters=dict(required=True, type='list', elements='str'),
            timeouts=dict(type='dict', options=dict(
                create=dict(default='15m', type='str'),
                update=dict(default='15m', type='str'),
            ), default=dict()),
            cidr=dict(type='str', required=True),
            gateway_ip=dict(type='str', required=True),
            name=dict(type='str', required=True),
            vpc_id=dict(type='str', required=True),
            dhcp_enable=dict(default=True, type='bool'),
            ipv6_enable=dict(default=False, type='bool'),
            dns_address=dict(type='list', elements='str'),
            availability_zone=dict(type='str'),
            tags=dict(type='dict')
        )

        self.results = dict(
            changed=False,
            state=dict()
        )

        super(HwcVpcSubnet, self).__init__(self.argument_spec, supports_check_mode=True)

    def exec_module(self, **kwargs):

        self.results['check_mode'] = self.check_mode

        try:
            resource = None
            if self.module.params['id']:
                resource = True
            else:
                v = self.search_resource()
                if len(v) > 1:
                    raise Exception("find more than one resources(%s)" % ", ".join([
                                    navigate_value(i, ["id"]) for i in v]))

                if len(v) == 1:
                    resource = v[0]
                    self.module.params['id'] = navigate_value(resource, ["id"])

            result = {}
            changed = False
            if self.module.params['state'] == 'present':
                if resource is None:
                    if not self.module.check_mode:
                        self.create()
                    changed = True

                current = self.read()
                self.log('subnet current: %s' % current)
                expect = user_input_parameters(self.module)
                self.log('subnet expect: %s' % expect)
                if are_different_dicts(expect, current):
                    if not self.module.check_mode:
                        self.update(current)
                    changed = True

                result = self.read()
                result['id'] = self.module.params.get('id')
            else:
                if resource:
                    if not self.module.check_mode:
                        self.delete()
                        result['status'] = 'Deleted'
                    changed = True

        except Exception as ex:
            self.module.fail_json(msg=str(ex))

        else:
            self.results['state'] = result
            self.results['changed'] = changed
            
        return self.results

    def search_resource(self):
        opts = user_input_parameters(self.module)
        identity_obj = _build_identity_object(self.module, opts)
        result = []
        marker = ''

        while True:
            try:
                request = ListSubnetsRequest(limit=10, marker=marker)
                self.log('list subnet request: %s' % request)
                response = self.vpc_client.list_subnets(request)
                self.log('list subnet response: %s' % response)
            except exceptions.ClientRequestException as e:
                raise HwcModuleException(
                        'search subnet failed: %s' % e.error_msg)
            r = navigate_value(response.to_json_object(), ['subnets'], None)

            if not r:
                break

            for item in r:
                item = fill_list_resp_body(item)
                self.log('subnet identity_obj: %s' % identity_obj)
                self.log('subnet item: %s' % item)
                if not are_different_dicts(identity_obj, item):
                    result.append(item)

            if len(result) > 1:
                break

            marker = r[-1].get('id')

        return result

    def create(self):
        opts = user_input_parameters(self.module)
        timeout = 60 * int(self.module.params['timeouts']['create'].rstrip('m'))
        try:
            request_body = build_create_parameters(opts)
            request = CreateSubnetRequest(request_body)
            self.log('create subnet request body: %s' %request)
            response = self.vpc_client.create_subnet(request)
            self.log('create subnet response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Create subnet failed: %s' % e)

        subnet_id = response.to_json_object()['subnet']['id']

        obj = self.async_wait_create(subnet_id, timeout)

        self.module.params['id'] = navigate_value(obj, ["subnet", "id"])

        # set tags
        if opts['tags']:
            try:
                request_body = build_tags_parameters(opts, 'create')
                request = BatchCreateSubnetTagsRequest(self.module.params['id'], request_body)
                self.log('create subnet tags request body: %s' %request)
                response = self.vpc_client.batch_create_subnet_tags(request)
                self.log('create subnet tags response body: %s' %request)
            except exceptions.ClientRequestException as e:
                self.fail('Create subnet tags failed: %s' % e)

    def read(self):
        try:
            request = ShowSubnetRequest(self.module.params['id'])
            self.log('read subnet request body: %s' %request)
            response = self.vpc_client.show_subnet(request)
            self.log('read subnet response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read subnet failed: %s' % e)

        response_attrs = update_properties(self.module, response.to_json_object()['subnet'])

        # fetch vpc tags
        try:
            request = ShowSubnetTagsRequest(self.module.params['id'])
            self.log('read subnet tags request body: %s' %request)
            response = self.vpc_client.show_subnet_tags(request)
            self.log('read subnet tags response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read subnet tags failed: %s' % e)

        tags_raw = response.to_json_object()['tags']
        if len(tags_raw) > 0:
            tags = tags_to_dict(tags_raw)
            response_attrs['tags'] = tags

        return (response_attrs)

    def update(self, current):
        opts = user_input_parameters(self.module)
        try:
            requset_body = build_update_parameters(opts)
            request = UpdateSubnetRequest(self.module.params['vpc_id'], self.module.params['id'], requset_body)
            self.log('Update subnet request body: %s' %request)
            response = self.vpc_client.update_subnet(request)
            self.log('Update subnet response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Update subnet failed: %s' % e)

        # update tags
        if opts['tags']:
            if  'tags' not in current.keys():
                try:
                    request_body = build_tags_parameters(opts, 'create')
                    request = BatchCreateSubnetTagsRequest(self.module.params['id'], request_body)
                    self.log('create subnet tags request body: %s' %request)
                    response = self.vpc_client.batch_create_Subnet_tags(request)
                    self.log('create subnet tags response body: %s' %request)
                except exceptions.ClientRequestException as e:
                    self.fail('Create subnet tags failed: %s' % e)

            elif current['tags'] != opts['tags']:
                try:
                    request_body = build_tags_parameters(current, 'delete')
                    request = BatchDeleteSubnetTagsRequest(self.module.params['id'], request_body)
                    self.log('delete subnet tags request body: %s' %request)
                    response = self.vpc_client.batch_delete_subnet_tags(request)
                    self.log('delete subnet tags response body: %s' % response)
                except exceptions.ClientRequestException as e:
                    self.fail('delete subnet tags failed: %s' % e)

                try:
                    request_body = build_tags_parameters(opts, 'create')
                    request = BatchCreateSubnetTagsRequest(self.module.params['id'], request_body)
                    self.log('create subnet tags request body: %s' %request)
                    response = self.vpc_client.batch_create_subnet_tags(request)
                    self.log('create subnet tags response body: %s' %request)
                except exceptions.ClientRequestException as e:
                    self.fail('Create subnet tags failed: %s' % e)
        else:
            if current['tags']:
                try:
                    request_body = build_tags_parameters(current, 'delete')
                    request = BatchDeleteSubnetTagsRequest(self.module.params['id'], request_body)
                    self.log('delete subnet tags request body: %s' %request)
                    response = self.vpc_client.batch_delete_Subnet_tags(request)
                    self.log('delete subnet tags response body: %s' % response)
                except exceptions.ClientRequestException as e:
                    self.fail('delete Subnet tags failed: %s' % e)

    def delete(self):
        try:
            request = DeleteSubnetRequest(self.module.params['vpc_id'], self.module.params['id'])
            self.log('delete subnet request body: %s' %request)
            response = self.vpc_client.delete_subnet(request)
            self.log('delete subnet response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Delete subnet failed: %s' % e)

    def async_wait_create(self, subnet_id, timeout):
        def _query_status():
            r = None
            try:
                request = ShowSubnetRequest(subnet_id)
                self.log('read subnet request body: %s' %request)
                response = self.vpc_client.show_subnet(request)
                self.log('read subnet response body: %s' % response)
            except exceptions.ClientRequestException as e:
                self.fail('read subnet failed: %s' % e)

            r = response.to_json_object()

            try:
                s = navigate_value(r, ["subnet", "status"])
                return r, s
            except Exception:
                return None, ""

        try:
            return wait_to_finish(
                ["ACTIVE"],
                ["UNKNOWN"],
                _query_status, timeout)
        except Exception as ex:
            self.module.fail_json(msg="module(hwc_vpc_subnet): error "
                                "waiting for api(create) to "
                                "be done, error= %s" % str(ex))
                                

def user_input_parameters(module):
    return {
        "availability_zone": module.params.get("availability_zone"),
        "cidr": module.params.get("cidr"),
        "dhcp_enable": module.params.get("dhcp_enable"),
        "ipv6_enable": module.params.get("ipv6_enable"),
        "dns_address": module.params.get("dns_address"),
        "gateway_ip": module.params.get("gateway_ip"),
        "name": module.params.get("name"),
        "vpc_id": module.params.get("vpc_id"),
        'tags': module.params.get('tags'),
    }


def build_create_parameters(opts):
    params = dict()

    v = navigate_value(opts, ["availability_zone"], None)
    if not is_empty_value(v):
        params["availability_zone"] = v

    v = navigate_value(opts, ["cidr"], None)
    if not is_empty_value(v):
        params["cidr"] = v

    v = navigate_value(opts, ["dhcp_enable"], None)
    if v is not None:
        params["dhcp_enable"] = v

    v = navigate_value(opts, ["ipv6_enable"], None)
    if v is not None:
        params["ipv6_enable"] = v

    v = expand_create_dns_list(opts, None)
    if not is_empty_value(v):
        params["dnsList"] = v

    v = navigate_value(opts, ["gateway_ip"], None)
    if not is_empty_value(v):
        params["gateway_ip"] = v

    v = navigate_value(opts, ["name"], None)
    if not is_empty_value(v):
        params["name"] = v

    v = expand_create_primary_dns(opts, None)
    if not is_empty_value(v):
        params["primary_dns"] = v

    v = expand_create_secondary_dns(opts, None)
    if not is_empty_value(v):
        params["secondary_dns"] = v

    v = navigate_value(opts, ["vpc_id"], None)
    if not is_empty_value(v):
        params["vpc_id"] = v

    if not params:
        return params

    params = {"subnet": params}

    return params


def expand_create_dns_list(d, array_index):
    v = navigate_value(d, ["dns_address"], array_index)
    return v if (v and len(v) > 2) else []


def expand_create_primary_dns(d, array_index):
    v = navigate_value(d, ["dns_address"], array_index)
    return v[0] if v else ""


def expand_create_secondary_dns(d, array_index):
    v = navigate_value(d, ["dns_address"], array_index)
    return v[1] if (v and len(v) > 1) else ""

def build_update_parameters(opts):
    params = dict()

    v = navigate_value(opts, ["dhcp_enable"], None)
    if v is not None:
        params["dhcp_enable"] = v

    v = navigate_value(opts, ["ipv6_enable"], None)
    if v is not None:
        params["ipv6_enable"] = v

    v = expand_update_dns_list(opts, None)
    if v is not None and v != []:
        params["dnsList"] = v

    v = navigate_value(opts, ["name"], None)
    if not is_empty_value(v):
        params["name"] = v

    v = expand_update_primary_dns(opts, None)
    if v is not None and v != "":
        params["primary_dns"] = v

    v = expand_update_secondary_dns(opts, None)
    if v is not None and v != "" :
        params["secondary_dns"] = v

    if not params:
        return params

    params = {"subnet": params}

    return params


def expand_update_dns_list(d, array_index):
    v = navigate_value(d, ["dns_address"], array_index)
    if v:
        if len(v) > 2:
            return v
        return None
    return []

def expand_update_primary_dns(d, array_index):
    v = navigate_value(d, ["dns_address"], array_index)
    return v[0] if v else ""

def expand_update_secondary_dns(d, array_index):
    v = navigate_value(d, ["dns_address"], array_index)
    return v[1] if (v and len(v) > 1) else ""

def _build_identity_object(module, all_opts):
    filters = module.params.get("filters")
    opts = dict()
    for k, v in all_opts.items():
        opts[k] = v if k in filters else None

    result = dict()

    v = navigate_value(opts, ["availability_zone"], None)
    result["availability_zone"] = v

    v = navigate_value(opts, ["cidr"], None)
    result["cidr"] = v

    v = navigate_value(opts, ["dhcp_enable"], None)
    result["dhcp_enable"] = v

    v = navigate_value(opts, ["ipv6_enable"], None)
    result["ipv6_enable"] = v

    v = navigate_value(opts, ["dns_address"], None)
    result["dnsList"] = v

    v = navigate_value(opts, ["gateway_ip"], None)
    result["gateway_ip"] = v

    result["id"] = None

    v = navigate_value(opts, ["name"], None)
    result["name"] = v

    result["neutron_network_id"] = None

    result["neutron_subnet_id"] = None

    result["primary_dns"] = None

    result["secondary_dns"] = None

    result["status"] = None

    v = navigate_value(opts, ["vpc_id"], None)
    result["vpc_id"] = v

    return result


def fill_list_resp_body(body):
    result = dict()

    result["availability_zone"] = body.get("availability_zone")

    result["cidr"] = body.get("cidr")

    result["dhcp_enable"] = body.get("dhcp_enable")

    result["ipv6_enable"] = body.get("ipv6_enable")

    result["dnsList"] = body.get("dnsList")

    result["gateway_ip"] = body.get("gateway_ip")

    result["id"] = body.get("id")

    result["name"] = body.get("name")

    result["neutron_network_id"] = body.get("neutron_network_id")

    result["neutron_subnet_id"] = body.get("neutron_subnet_id")

    result["primary_dns"] = body.get("primary_dns")

    result["secondary_dns"] = body.get("secondary_dns")

    result["status"] = body.get("status")

    result["vpc_id"] = body.get("vpc_id")

    return result

def update_properties(module, response):
    r = user_input_parameters(module)

    if r["availability_zone"]:
        v = navigate_value(response, ["availability_zone"])
        r["availability_zone"] = v

    v = navigate_value(response, ["cidr"], None)
    r["cidr"] = v

    v = navigate_value(response, ["dhcp_enable"], None)
    r["dhcp_enable"] = v

    v = navigate_value(response, ["ipv6_enable"], None)
    r["ipv6_enable"] = v

    v = navigate_value(response, ["dnsList"], None)
    r["dns_address"] = v

    v = navigate_value(response, ["gateway_ip"], None)
    r["gateway_ip"] = v

    v = navigate_value(response, ["name"], None)
    r["name"] = v

    v = navigate_value(response, ["vpc_id"], None)
    r["vpc_id"] = v

    return r

def main():
    HwcVpcSubnet()

if __name__ == '__main__':
    main()
