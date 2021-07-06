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
module: hwc_vpc_security_group
description:
    - vpc security group management.
short_description: Creates a resource of Vpc/SecurityGroup in Huawei Cloud
version_added: '2.9'
author: Huawei Inc. (@huaweicloud)
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
    name:
        description:
            - Specifies the security group name. The value is a string of 1 to
              64 characters that can contain letters, digits, underscores C(_),
              hyphens (-), and periods (.).
        type: str
        required: true
    enterprise_project_id:
        description:
            - Specifies the enterprise project ID. When creating a security
              group, associate the enterprise project ID with the security
              group.
        type: str
        required: false
extends_documentation_fragment: hwc
'''

EXAMPLES = '''
# create a security group
- name: create a security group
  hwc_vpc_security_group:
    name: "ansible_network_security_group_test"
    filters:
      - "name"
'''

RETURN = '''
    name:
        description:
            - Specifies the security group name. The value is a string of 1 to
              64 characters that can contain letters, digits, underscores C(_),
              hyphens (-), and periods (.).
        type: str
        returned: success
    enterprise_project_id:
        description:
            - Specifies the enterprise project ID. When creating a security
              group, associate the enterprise project ID with the security
              group.
        type: str
        returned: success
    description:
        description:
            - Specifies supplementary information about the security group.
        type: str
        returned: success
    rules:
        description:
            - Specifies the security group rule, which ensures that resources
              in the security group can communicate with one another.
        type: complex
        returned: success
        contains:
            description:
                description:
                    - Provides supplementary information about the security
                      group rule.
                type: str
                returned: success
            direction:
                description:
                    - Specifies the direction of access control. The value can
                      be egress or ingress.
                type: str
                returned: success
            ethertype:
                description:
                    - Specifies the IP protocol version. The value can be IPv4
                      or IPv6.
                type: str
                returned: success
            id:
                description:
                    - Specifies the security group rule ID.
                type: str
                returned: success
            port_range_max:
                description:
                    - Specifies the end port number. The value ranges from 1 to
                      65535. If the protocol is not icmp, the value cannot be
                      smaller than the port_range_min value. An empty value
                      indicates all ports.
                type: int
                returned: success
            port_range_min:
                description:
                    - Specifies the start port number. The value ranges from 1
                      to 65535. The value cannot be greater than the
                      port_range_max value. An empty value indicates all ports.
                type: int
                returned: success
            protocol:
                description:
                    - Specifies the protocol type. The value can be icmp, tcp,
                      udp, or others. If the parameter is left blank, the
                      security group supports all protocols.
                type: str
                returned: success
            remote_address_group_id:
                description:
                    - Specifies the ID of remote IP address group.
                type: str
                returned: success
            remote_group_id:
                description:
                    - Specifies the ID of the peer security group.
                type: str
                returned: success
            remote_ip_prefix:
                description:
                    - Specifies the remote IP address. If the access control
                      direction is set to egress, the parameter specifies the
                      source IP address. If the access control direction is set
                      to ingress, the parameter specifies the destination IP
                      address.
                type: str
                returned: success
'''

from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleBase
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleException
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import are_different_dicts
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import navigate_value
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import is_empty_value

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkvpc.v2 import *


class HwcVpcSecGroup(HwcModuleBase):
    def __init__(self):
        self.argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'],
                       type='str'),
            filters=dict(required=True, type='list', elements='str'),
            name=dict(type='str', required=True),
            enterprise_project_id=dict(type='str'),
        )

        self.results = dict(
            changed=False,
            state=dict()
        )

        super(HwcVpcSecGroup, self).__init__(self.argument_spec, supports_check_mode=True)

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
            self.results['changed'] = changed
            self.results['state'] = result

        return self.results


    def search_resource(self):
        opts = user_input_parameters(self.module)
        identity_obj = _build_identity_object(self.module, opts)
        result = []
        marker = ''

        while True:
            try:
                request = ListSecurityGroupsRequest(limit=10, marker=marker)
                self.log('list security group request: %s' % request)
                response = self.vpc_client.list_security_groups(request)
                self.log('list security group response: %s' % response)
            except exceptions.ClientRequestException as e:
                raise HwcModuleException(
                        'search security group failed: %s' % e.error_msg)
            r = navigate_value(response.to_json_object(), ['security_groups'], None)

            if not r:
                break

            for item in r:
                item = fill_list_resp_body(item)
                self.log('security group identity_obj: %s' % identity_obj)
                self.log('security group item: %s' % item)
                if not are_different_dicts(identity_obj, item):
                    result.append(item)

            if len(result) > 1:
                break

            marker = r[-1].get('id')

        return result

    def create(self):
        opts = user_input_parameters(self.module)
        try:
            request_body = build_create_parameters(opts)
            request = CreateSecurityGroupRequest(request_body)
            self.log('create security group request body: %s' %request)
            response = self.vpc_client.create_security_group(request)
            self.log('create security group response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Create security group failed: %s' % e)

        self.module.params['id'] = response.to_json_object()['security_group']['id']

    def read(self):
        try:
            request = ShowSecurityGroupRequest(self.module.params['id'])
            self.log('read security group request body: %s' %request)
            response = self.vpc_client.show_security_group(request)
            self.log('read security group response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read security group failed: %s' % e)

        response_attrs = update_properties(self.module, response.to_json_object()['security_group'])
        return (response_attrs)

    def delete(self):
        try:
            request = DeleteSecurityGroupRequest(self.module.params['id'])
            self.log('delete security group request body: %s' %request)
            response = self.vpc_client.delete_security_group(request)
            self.log('delete security group response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Delete security group failed: %s' % e)

def user_input_parameters(module):
    return {
        "enterprise_project_id": module.params.get("enterprise_project_id"),
        "name": module.params.get("name"),
    }

def build_create_parameters(opts):
    params = dict()

    v = navigate_value(opts, ["enterprise_project_id"], None)
    if not is_empty_value(v):
        params["enterprise_project_id"] = v

    v = navigate_value(opts, ["name"], None)
    if not is_empty_value(v):
        params["name"] = v

    if not params:
        return params

    params = {"security_group": params}

    return params


def update_properties(module, response, array_index=None, exclude_output=False):
    r = user_input_parameters(module)

    if not exclude_output:
        v = navigate_value(response, ["description"], array_index)
        r["description"] = v

    v = navigate_value(response, ["enterprise_project_id"],
                       array_index)
    r["enterprise_project_id"] = v

    v = navigate_value(response, ["name"], array_index)
    r["name"] = v

    if not exclude_output:
        v = r.get("rules")
        v = flatten_rules(response, array_index, v, exclude_output)
        r["rules"] = v

    return r


def flatten_rules(d, array_index, current_value, exclude_output):
    n = 0
    result = current_value
    has_init_value = True
    if result:
        n = len(result)
    else:
        has_init_value = False
        result = []
        v = navigate_value(d, ["security_group_rules"],
                           array_index)
        if not v:
            return current_value
        n = len(v)

    new_array_index = dict()
    if array_index:
        new_array_index.update(array_index)

    for i in range(n):
        new_array_index["security_group_rules"] = i

        val = dict()
        if len(result) >= (i + 1) and result[i]:
            val = result[i]

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "description"],
                               new_array_index)
            val["description"] = v

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "direction"],
                               new_array_index)
            val["direction"] = v

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "ethertype"],
                               new_array_index)
            val["ethertype"] = v

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "id"],
                               new_array_index)
            val["id"] = v

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "port_range_max"],
                               new_array_index)
            val["port_range_max"] = v

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "port_range_min"],
                               new_array_index)
            val["port_range_min"] = v

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "protocol"],
                               new_array_index)
            val["protocol"] = v

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "remote_address_group_id"],
                               new_array_index)
            val["remote_address_group_id"] = v

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "remote_group_id"],
                               new_array_index)
            val["remote_group_id"] = v

        if not exclude_output:
            v = navigate_value(d, ["security_group_rules", "remote_ip_prefix"],
                               new_array_index)
            val["remote_ip_prefix"] = v

        if len(result) >= (i + 1):
            result[i] = val
        else:
            for v in val.values():
                if v is not None:
                    result.append(val)
                    break

    return result if (has_init_value or result) else current_value


def _build_identity_object(module, all_opts):
    filters = module.params.get("filters")
    opts = dict()
    for k, v in all_opts.items():
        opts[k] = v if k in filters else None

    result = dict()

    result["description"] = None

    v = navigate_value(opts, ["enterprise_project_id"], None)
    result["enterprise_project_id"] = v

    result["id"] = None

    v = navigate_value(opts, ["name"], None)
    result["name"] = v

    result["security_group_rules"] = None

    return result


def fill_list_resp_body(body):
    result = dict()

    result["description"] = body.get("description")

    result["enterprise_project_id"] = body.get("enterprise_project_id")

    result["id"] = body.get("id")

    result["name"] = body.get("name")

    v = fill_list_resp_security_group_rules(body.get("security_group_rules"))
    result["security_group_rules"] = v

    return result


def fill_list_resp_security_group_rules(value):
    if not value:
        return None

    result = []
    for item in value:
        val = dict()

        val["description"] = item.get("description")

        val["direction"] = item.get("direction")

        val["ethertype"] = item.get("ethertype")

        val["id"] = item.get("id")

        val["port_range_max"] = item.get("port_range_max")

        val["port_range_min"] = item.get("port_range_min")

        val["protocol"] = item.get("protocol")

        val["remote_address_group_id"] = item.get("remote_address_group_id")

        val["remote_group_id"] = item.get("remote_group_id")

        val["remote_ip_prefix"] = item.get("remote_ip_prefix")

        val["security_group_id"] = item.get("security_group_id")

        result.append(val)

    return result

def main():
    HwcVpcSecGroup()

if __name__ == '__main__':
    main()
