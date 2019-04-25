#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Huawei
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
module: hwc_network_vpc
description:
    - Represents an vpc resource.
short_description: Creates a Huawei Cloud VPC
version_added: '2.8'
author: Huawei Inc. (@huaweicloud)
requirements:
    - requests >= 2.18.4
    - keystoneauth1 >= 3.6.0
options:
    state:
        description:
            - Whether the given object should exist in vpc.
        type: str
        choices: ['present', 'absent']
        default: 'present'
    name:
        description:
            - the name of vpc.
        type: str
        required: true
    cidr:
        description:
            - the range of available subnets in the vpc.
        type: str
        required: true
extends_documentation_fragment: hwc
'''

EXAMPLES = '''
- name: create a vpc
  hwc_network_vpc:
      identity_endpoint: "{{ identity_endpoint }}"
      user: "{{ user }}"
      password: "{{ password }}"
      domain: "{{ domain }}"
      project: "{{ project }}"
      region: "{{ region }}"
      name: "vpc_1"
      cidr: "192.168.100.0/24"
      state: present
'''

RETURN = '''
    id:
        description:
            - the id of vpc.
        type: str
        returned: success
    name:
        description:
            - the name of vpc.
        type: str
        returned: success
    cidr:
        description:
            - the range of available subnets in the vpc.
        type: str
        returned: success
    status:
        description:
            - the status of vpc.
        type: str
        returned: success
    routes:
        description:
            - the route information.
        type: complex
        returned: success
        contains:
            destination:
                description:
                    - the destination network segment of a route.
                type: str
                returned: success
            next_hop:
                description:
                    - the next hop of a route.
                type: str
                returned: success
    enable_shared_snat:
        description:
            - show whether the shared snat is enabled.
        type: bool
        returned: success
'''

###############################################################################
# Imports
###############################################################################

from ansible.module_utils.hwc_utils import (Config, HwcModule, get_region,
                                            HwcClientException, navigate_value,
                                            HwcClientException404,
                                            remove_nones_from_dict, build_path,
                                            remove_empty_from_dict,
                                            are_dicts_different)
import re
import time

###############################################################################
# Main
###############################################################################


def main():
    """Main function"""

    module = HwcModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            cidr=dict(required=True, type='str')
        ),
        supports_check_mode=True,
    )
    config = Config(module, 'vpc')

    state = module.params['state']

    if (not module.params.get("id")) and module.params.get("name"):
        module.params['id'] = get_id_by_name(config)

    fetch = None
    link = self_link(module)
    # the link will include Nones if required format parameters are missed
    if not re.search('/None/|/None$', link):
        client = config.client(get_region(module), "vpc", "project")
        fetch = fetch_resource(module, client, link)
        if fetch:
            fetch = fetch.get('vpc')
    changed = False

    if fetch:
        if state == 'present':
            expect = _get_editable_properties(module)
            current_state = response_to_hash(module, fetch)
            if are_dicts_different(expect, current_state):
                if not module.check_mode:
                    fetch = update(config, self_link(module))
                    fetch = response_to_hash(module, fetch.get('vpc'))
                changed = True
            else:
                fetch = current_state
        else:
            if not module.check_mode:
                delete(config, self_link(module))
                fetch = {}
            changed = True
    else:
        if state == 'present':
            if not module.check_mode:
                fetch = create(config, "vpcs")
                fetch = response_to_hash(module, fetch.get('vpc'))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(config, link):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")

    r = None
    try:
        r = client.post(link, resource_to_create(module))
    except HwcClientException as ex:
        msg = ("module(hwc_network_vpc): error creating "
               "resource, error: %s" % str(ex))
        module.fail_json(msg=msg)

    wait_done = wait_for_operation(config, 'create', r)
    v = ""
    try:
        v = navigate_value(wait_done, ['vpc', 'id'])
    except Exception as ex:
        module.fail_json(msg=str(ex))

    url = build_path(module, 'vpcs/{op_id}', {'op_id': v})
    return fetch_resource(module, client, url)


def update(config, link):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")

    r = None
    try:
        r = client.put(link, resource_to_update(module))
    except HwcClientException as ex:
        msg = ("module(hwc_network_vpc): error updating "
               "resource, error: %s" % str(ex))
        module.fail_json(msg=msg)

    wait_for_operation(config, 'update', r)

    return fetch_resource(module, client, link)


def delete(config, link):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")

    try:
        client.delete(link)
    except HwcClientException as ex:
        msg = ("module(hwc_network_vpc): error deleting "
               "resource, error: %s" % str(ex))
        module.fail_json(msg=msg)

    wait_for_delete(module, client, link)


def fetch_resource(module, client, link):
    try:
        return client.get(link)
    except HwcClientException as ex:
        msg = ("module(hwc_network_vpc): error fetching "
               "resource, error: %s" % str(ex))
        module.fail_json(msg=msg)


def get_id_by_name(config):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")
    name = module.params.get("name")
    link = "vpcs"
    query_link = "?marker={marker}&limit=10"
    link += query_link
    not_format_keys = re.findall("={marker}", link)
    none_values = re.findall("=None", link)

    if not (not_format_keys or none_values):
        r = None
        try:
            r = client.get(link)
        except Exception:
            pass
        if r is None:
            return None
        r = r.get('vpcs', [])
        ids = [
            i.get('id') for i in r if i.get('name', '') == name
        ]
        if not ids:
            return None
        elif len(ids) == 1:
            return ids[0]
        else:
            module.fail_json(msg="Multiple resources with same name are found.")
    elif none_values:
        module.fail_json(
            msg="Can not find id by name because url includes None.")
    else:
        p = {'marker': ''}
        ids = set()
        while True:
            r = None
            try:
                r = client.get(link.format(**p))
            except Exception:
                pass
            if r is None:
                break
            r = r.get('vpcs', [])
            if r == []:
                break
            for i in r:
                if i.get('name') == name:
                    ids.add(i.get('id'))
            if len(ids) >= 2:
                module.fail_json(
                    msg="Multiple resources with same name are found.")

            p['marker'] = r[-1].get('id')

        return ids.pop() if ids else None


def self_link(module):
    return build_path(module, "vpcs/{id}")


def resource_to_create(module):
    request = remove_empty_from_dict({
        u'name': module.params.get('name'),
        u'cidr': module.params.get('cidr')
    })
    return {'vpc': request}


def resource_to_update(module):
    request = remove_nones_from_dict({
        u'name': module.params.get('name'),
        u'cidr': module.params.get('cidr')
    })
    return {'vpc': request}


def _get_editable_properties(module):
    request = remove_nones_from_dict({
        "name": module.params.get("name"),
        "cidr": module.params.get("cidr"),
    })

    return request


def response_to_hash(module, response):
    """ Remove unnecessary properties from the response.
        This is for doing comparisons with Ansible's current parameters.
    """
    return {
        u'id': response.get(u'id'),
        u'name': response.get(u'name'),
        u'cidr': response.get(u'cidr'),
        u'status': response.get(u'status'),
        u'routes': VpcRoutesArray(response.get(u'routes', []), module).from_response(),
        u'enable_shared_snat': response.get(u'enable_shared_snat')
    }


def wait_for_operation(config, op_type, op_result):
    module = config.module
    op_id = ""
    try:
        op_id = navigate_value(op_result, ['vpc', 'id'])
    except Exception as ex:
        module.fail_json(msg=str(ex))

    url = build_path(module, "vpcs/{op_id}", {'op_id': op_id})
    timeout = 60 * int(module.params['timeouts'][op_type].rstrip('m'))
    states = {
        'create': {
            'allowed': ['CREATING', 'DONW', 'OK'],
            'complete': ['OK'],
        },
        'update': {
            'allowed': ['PENDING_UPDATE', 'DONW', 'OK'],
            'complete': ['OK'],
        }
    }

    return wait_for_completion(url, timeout, states[op_type]['allowed'],
                               states[op_type]['complete'], config)


def wait_for_completion(op_uri, timeout, allowed_states,
                        complete_states, config):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")
    end = time.time() + timeout
    while time.time() <= end:
        try:
            op_result = fetch_resource(module, client, op_uri)
        except Exception:
            time.sleep(1.0)
            continue

        try:
            status = navigate_value(op_result, ['vpc', 'status'])
        except Exception:
            pass
        else:
            if status not in allowed_states:
                module.fail_json(
                    msg="Invalid async operation status %s" % status)
            if status in complete_states:
                return op_result

        time.sleep(1.0)

    module.fail_json(msg="Timeout to wait completion.")


def wait_for_delete(module, client, link):
    end = time.time() + 60 * int(
        module.params['timeouts']['delete'].rstrip('m'))
    while time.time() <= end:
        try:
            client.get(link)
        except HwcClientException404:
            return
        except Exception:
            pass

        time.sleep(1.0)

    module.fail_json(msg="Timeout to wait for deletion to be complete.")


class VpcRoutesArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return {
            u'destination': item.get('destination'),
            u'nexthop': item.get('next_hop')
        }

    def _response_from_item(self, item):
        return {
            u'destination': item.get(u'destination'),
            u'next_hop': item.get(u'nexthop')
        }


if __name__ == '__main__':
    main()
