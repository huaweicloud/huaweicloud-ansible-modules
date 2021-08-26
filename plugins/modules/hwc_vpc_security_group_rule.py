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
module: hwc_vpc_security_group_rule
description:
    - Creates and manages a resource of Vpc/SecurityGroupRule in Huawei Cloud.
short_description: Creates a resource of Vpc/SecurityGroupRule in Huawei Cloud
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
    direction:
        description:
            - Specifies the direction of access control. The value can be
              egress or ingress.
        type: str
        required: true
    security_group_id:
        description:
            - Specifies the security group rule ID, which uniquely identifies
              the security group rule.
        type: str
        required: true
    description:
        description:
            - Provides supplementary information about the security group rule.
              The value is a string of no more than 255 characters that can
              contain letters and digits.
        type: str
        required: false
    ethertype:
        description:
            - Specifies the IP protocol version. The value can be IPv4 or IPv6.
              If you do not set this parameter, IPv4 is used by default.
        type: str
        required: false
    port_range_max:
        description:
            - Specifies the end port number. The value ranges from 1 to 65535.
              If the protocol is not icmp, the value cannot be smaller than the
              port_range_min value. An empty value indicates all ports.
        type: int
        required: false
    port_range_min:
        description:
            - Specifies the start port number. The value ranges from 1 to
              65535. The value cannot be greater than the port_range_max value.
              An empty value indicates all ports.
        type: int
        required: false
    protocol:
        description:
            - Specifies the protocol type. The value can be icmp, tcp, or udp.
              If the parameter is left blank, the security group supports all
              protocols.
        type: str
        required: false
    remote_group_id:
        description:
            - Specifies the ID of the peer security group. The value is
              exclusive with parameter remote_ip_prefix.
        type: str
        required: false
    remote_ip_prefix:
        description:
            - Specifies the remote IP address. If the access control direction
              is set to egress, the parameter specifies the source IP address.
              If the access control direction is set to ingress, the parameter
              specifies the destination IP address. The value can be in the
              CIDR format or IP addresses. The parameter is exclusive with
              parameter remote_group_id.
        type: str
        required: false
extends_documentation_fragment:
  - hwceco.hwcollection.hwc_auth_options
'''

EXAMPLES = '''
# create a security group rule
- name: create a security group
  hwc_vpc_security_group:
    name: "ansible_network_security_group_test"
    filters:
      - "name"
  register: sg
- name: create a security group rule
  hwc_vpc_security_group_rule:
    direction: "ingress"
    protocol: "tcp"
    ethertype: "IPv4"
    port_range_max: 22
    security_group_id: "{{ sg.state.id }}"
    port_range_min: 22
    filters:
      - "security_group_id"
    remote_ip_prefix: "0.0.0.0/0"
'''

RETURN = '''
    direction:
        description:
            - Specifies the direction of access control. The value can be
              egress or ingress.
        type: str
        returned: success
    security_group_id:
        description:
            - Specifies the security group rule ID, which uniquely identifies
              the security group rule.
        type: str
        returned: success
    description:
        description:
            - Provides supplementary information about the security group rule.
              The value is a string of no more than 255 characters that can
              contain letters and digits.
        type: str
        returned: success
    ethertype:
        description:
            - Specifies the IP protocol version. The value can be IPv4 or IPv6.
              If you do not set this parameter, IPv4 is used by default.
        type: str
        returned: success
    port_range_max:
        description:
            - Specifies the end port number. The value ranges from 1 to 65535.
              If the protocol is not icmp, the value cannot be smaller than the
              port_range_min value. An empty value indicates all ports.
        type: int
        returned: success
    port_range_min:
        description:
            - Specifies the start port number. The value ranges from 1 to
              65535. The value cannot be greater than the port_range_max value.
              An empty value indicates all ports.
        type: int
        returned: success
    protocol:
        description:
            - Specifies the protocol type. The value can be icmp, tcp, or udp.
              If the parameter is left blank, the security group supports all
              protocols.
        type: str
        returned: success
    remote_group_id:
        description:
            - Specifies the ID of the peer security group. The value is
              exclusive with parameter remote_ip_prefix.
        type: str
        returned: success
    remote_ip_prefix:
        description:
            - Specifies the remote IP address. If the access control direction
              is set to egress, the parameter specifies the source IP address.
              If the access control direction is set to ingress, the parameter
              specifies the destination IP address. The value can be in the
              CIDR format or IP addresses. The parameter is exclusive with
              parameter remote_group_id.
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


class HwcVpcSecGroupRule(HwcModuleBase):
    def __init__(self):
        self.argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'],
                       type='str'),
            filters=dict(required=True, type='list', elements='str'),
            direction=dict(type='str', required=True),
            security_group_id=dict(type='str', required=True),
            description=dict(type='str'),
            ethertype=dict(type='str'),
            port_range_max=dict(type='int'),
            port_range_min=dict(type='int'),
            protocol=dict(type='str'),
            remote_group_id=dict(type='str'),
            remote_ip_prefix=dict(type='str')
        )

        self.results = dict(
            changed=False,
            state=dict()
        )

        super(HwcVpcSecGroupRule, self).__init__(self.argument_spec, supports_check_mode=True)

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
                request = ListSecurityGroupRulesRequest(limit=10, marker=marker, security_group_id=self.module.params['security_group_id'])
                self.log('list security group rules request: %s' % request)
                response = self.vpc_client.list_security_group_rules(request)
                self.log('list security group rules response: %s' % response)
            except exceptions.ClientRequestException as e:
                raise HwcModuleException(
                        'search security group failed: %s' % e.error_msg)
            r = navigate_value(response.to_json_object(), ['security_group_rules'], None)

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
            request = CreateSecurityGroupRuleRequest(request_body)
            self.log('create security group rule request body: %s' %request)
            response = self.vpc_client.create_security_group_rule(request)
            self.log('create security group rule response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Create security group rule failed: %s' % e)

        self.module.params['id'] = response.to_json_object()['security_group_rule']['id']

    def read(self):
        try:
            request = ShowSecurityGroupRuleRequest(self.module.params['id'])
            self.log('read security group rule request body: %s' %request)
            response = self.vpc_client.show_security_group_rule(request)
            self.log('read security group rule response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read security group rule failed: %s' % e)

        res = {}
        res["read"] = fill_read_resp_body(response.to_json_object()['security_group_rule'])

        return update_properties(self.module, res, None, exclude_output=False)

    def delete(self):
        try:
            request = DeleteSecurityGroupRuleRequest(self.module.params['id'])
            self.log('delete security group rule request body: %s' %request)
            response = self.vpc_client.delete_security_group_rule(request)
            self.log('delete security group rule response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Delete security group rule failed: %s' % e)

def user_input_parameters(module):
    return {
        "description": module.params.get("description"),
        "direction": module.params.get("direction"),
        "ethertype": module.params.get("ethertype"),
        "port_range_max": module.params.get("port_range_max"),
        "port_range_min": module.params.get("port_range_min"),
        "protocol": module.params.get("protocol"),
        "remote_group_id": module.params.get("remote_group_id"),
        "remote_ip_prefix": module.params.get("remote_ip_prefix"),
        "security_group_id": module.params.get("security_group_id"),
    }


def build_create_parameters(opts):
    params = dict()

    v = navigate_value(opts, ["description"], None)
    if not is_empty_value(v):
        params["description"] = v

    v = navigate_value(opts, ["direction"], None)
    if not is_empty_value(v):
        params["direction"] = v

    v = navigate_value(opts, ["ethertype"], None)
    if not is_empty_value(v):
        params["ethertype"] = v

    v = navigate_value(opts, ["port_range_max"], None)
    if not is_empty_value(v):
        params["port_range_max"] = v

    v = navigate_value(opts, ["port_range_min"], None)
    if not is_empty_value(v):
        params["port_range_min"] = v

    v = navigate_value(opts, ["protocol"], None)
    if not is_empty_value(v):
        params["protocol"] = v

    v = navigate_value(opts, ["remote_group_id"], None)
    if not is_empty_value(v):
        params["remote_group_id"] = v

    v = navigate_value(opts, ["remote_ip_prefix"], None)
    if not is_empty_value(v):
        params["remote_ip_prefix"] = v

    v = navigate_value(opts, ["security_group_id"], None)
    if not is_empty_value(v):
        params["security_group_id"] = v

    if not params:
        return params

    params = {"security_group_rule": params}

    return params


def fill_read_resp_body(body):
    result = dict()

    result["description"] = body.get("description")

    result["direction"] = body.get("direction")

    result["ethertype"] = body.get("ethertype")

    result["id"] = body.get("id")

    result["port_range_max"] = body.get("port_range_max")

    result["port_range_min"] = body.get("port_range_min")

    result["protocol"] = body.get("protocol")

    result["remote_address_group_id"] = body.get("remote_address_group_id")

    result["remote_group_id"] = body.get("remote_group_id")

    result["remote_ip_prefix"] = body.get("remote_ip_prefix")

    result["security_group_id"] = body.get("security_group_id")

    return result


def update_properties(module, response, array_index, exclude_output=False):
    r = user_input_parameters(module)

    v = navigate_value(response, ["read", "description"], array_index)
    r["description"] = v

    v = navigate_value(response, ["read", "direction"], array_index)
    r["direction"] = v

    v = navigate_value(response, ["read", "ethertype"], array_index)
    r["ethertype"] = v

    v = navigate_value(response, ["read", "port_range_max"], array_index)
    r["port_range_max"] = v

    v = navigate_value(response, ["read", "port_range_min"], array_index)
    r["port_range_min"] = v

    v = navigate_value(response, ["read", "protocol"], array_index)
    r["protocol"] = v

    v = navigate_value(response, ["read", "remote_group_id"], array_index)
    r["remote_group_id"] = v

    v = navigate_value(response, ["read", "remote_ip_prefix"], array_index)
    r["remote_ip_prefix"] = v

    v = navigate_value(response, ["read", "security_group_id"], array_index)
    r["security_group_id"] = v

    return r


def _build_identity_object(module, all_opts):
    filters = module.params.get("filters")
    opts = dict()
    for k, v in all_opts.items():
        opts[k] = v if k in filters else None

    result = dict()

    v = navigate_value(opts, ["description"], None)
    result["description"] = v

    v = navigate_value(opts, ["direction"], None)
    result["direction"] = v

    v = navigate_value(opts, ["ethertype"], None)
    result["ethertype"] = v

    result["id"] = None

    v = navigate_value(opts, ["port_range_max"], None)
    result["port_range_max"] = v

    v = navigate_value(opts, ["port_range_min"], None)
    result["port_range_min"] = v

    v = navigate_value(opts, ["protocol"], None)
    result["protocol"] = v

    result["remote_address_group_id"] = None

    v = navigate_value(opts, ["remote_group_id"], None)
    result["remote_group_id"] = v

    v = navigate_value(opts, ["remote_ip_prefix"], None)
    result["remote_ip_prefix"] = v

    v = navigate_value(opts, ["security_group_id"], None)
    result["security_group_id"] = v

    return result


def fill_list_resp_body(body):
    result = dict()

    result["description"] = body.get("description")

    result["direction"] = body.get("direction")

    result["ethertype"] = body.get("ethertype")

    result["id"] = body.get("id")

    result["port_range_max"] = body.get("port_range_max")

    result["port_range_min"] = body.get("port_range_min")

    result["protocol"] = body.get("protocol")

    result["remote_address_group_id"] = body.get("remote_address_group_id")

    result["remote_group_id"] = body.get("remote_group_id")

    result["remote_ip_prefix"] = body.get("remote_ip_prefix")

    result["security_group_id"] = body.get("security_group_id")

    return result


def main():
    HwcVpcSecGroupRule()

if __name__ == '__main__':
    main()
