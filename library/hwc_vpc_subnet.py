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
    - subnet management.
short_description: Creates a resource of Vpc/Subnet in Huawei Cloud
version_added: 2.9
author: Huawei Inc. (@huaweicloud)
requirements:
    - python >= 2.7
    - keystoneauth1 >= 3.6.0
options:
    state:
        description:
            - Whether the given object should exist in Huawei Cloud.
        choices: ['present', 'absent']
        default: 'present'
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
    availability_zone:
        description:
            - Specifies the AZ to which the subnet belongs.
        required: false
    cidr:
        description:
            - Specifies the subnet CIDR block. The value must be within the VPC
              CIDR block and be in CIDR format. The subnet mask cannot be
              greater than 28.
        required: true
    dhcp_enable:
        description:
            - Specifies whether DHCP is enabled for the subnet. The value can
              be true (enabled) or false(disabled), and default value is true.
              If this parameter is set to false, newly created ECSs cannot
              obtain IP addresses, and usernames and passwords cannot be
              injected using Cloud-init.
        required: false
        type: bool
    dns_address:
        description:
            - Specifies the DNS server addresses for subnet. Note: the address
              in the head will be used first.
        required: false
    gateway_ip:
        description:
            - Specifies the gateway of the subnet. The value must be an IP
              address in the subnet.
        required: true
    name:
        description:
            - Specifies the subnet name. The value is a string of 1 to 64
              characters that can contain letters, digits, underscores C(_),
              hyphens (-), and periods (.).
        required: true
    vpc_id:
        description:
            - Specifies the ID of the VPC to which the subnet belongs.
        required: true
extends_documentation_fragment: hwc
'''

EXAMPLES = '''
# create subnet
- name: create vpc
  hwc_network_vpc:
      cidr: "192.168.100.0/24"
      name: "ansible_network_vpc_test"
  register: vpc
- name: create subnet
  hwc_vpc_subnet:
      vpc_id: "{{ vpc.id }}"
      cidr: "192.168.100.0/26"
      gateway_ip: "192.168.100.32"
      name: "ansible_network_subnet_test"
      dhcp_enable: True
'''

RETURN = '''
    availability_zone:
        description:
            - Specifies the AZ to which the subnet belongs.
        returned: success
        type: str
    cidr:
        description:
            - Specifies the subnet CIDR block. The value must be within the VPC
              CIDR block and be in CIDR format. The subnet mask cannot be
              greater than 28.
        returned: success
        type: str
    dhcp_enable:
        description:
            - Specifies whether DHCP is enabled for the subnet. The value can
              be true (enabled) or false(disabled), and default value is true.
              If this parameter is set to false, newly created ECSs cannot
              obtain IP addresses, and usernames and passwords cannot be
              injected using Cloud-init.
        returned: success
        type: bool
    dns_address:
        description:
            - Specifies the DNS server addresses for subnet. Note: the address
              in the head will be used first.
        returned: success
        type: list
    gateway_ip:
        description:
            - Specifies the gateway of the subnet. The value must be an IP
              address in the subnet.
        returned: success
        type: str
    name:
        description:
            - Specifies the subnet name. The value is a string of 1 to 64
              characters that can contain letters, digits, underscores C(_),
              hyphens (-), and periods (.).
        returned: success
        type: str
    vpc_id:
        description:
            - Specifies the ID of the VPC to which the subnet belongs.
        returned: success
        type: str
'''

###############################################################################
# Imports
###############################################################################

from ansible.module_utils.hwc_utils import (Config, HwcClientException,
                                            HwcClientException404, HwcModule,
                                            are_different_dicts, get_region,
                                            is_empty_value, build_path,
                                            navigate_value, wait_to_finish)

###############################################################################
# Main
###############################################################################


def main():
    """Main function"""

    module = HwcModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'],
                       type='str'),
            timeouts=dict(type='dict', options=dict(
                create=dict(default='15m', type='str'),
                update=dict(default='15m', type='str'),
            ), default=dict()),
            availability_zone=dict(type='str'),
            cidr=dict(required=True, type='str'),
            dhcp_enable=dict(type='bool'),
            dns_address=dict(type='list', elements='str'),
            gateway_ip=dict(required=True, type='str'),
            name=dict(required=True, type='str'),
            vpc_id=dict(required=True, type='str')
        ),
        supports_check_mode=True,
    )

    config = Config(module, "vpc")
    try:
        resource = fetch_resource(config)
        if resource:
            module.params['id'] = navigate_value(resource, ["id"])

        result = {}
        changed = False
        if module.params['state'] == 'present':
            if resource is None:
                if not module.check_mode:
                    result = create(config)
                    result['id'] = module.params.get('id')
                changed = True

            else:
                current = read_resource(config, exclude_output=True)
                expect = user_input_parameters(module)
                if are_different_dicts(expect, current):
                    if not module.check_mode:
                        result = update(config)
                    changed = True
                else:
                    result = read_resource(config)
                result['id'] = module.params.get('id')
        else:
            if resource:
                if not module.check_mode:
                    delete(config)
                changed = True

    except Exception as ex:
        module.fail_json(msg=str(ex))

    else:
        result['changed'] = changed
        module.exit_json(**result)


def user_input_parameters(module):
    return {
        "availability_zone": module.params.get("availability_zone"),
        "cidr": module.params.get("cidr"),
        "dhcp_enable": module.params.get("dhcp_enable"),
        "dns_address": module.params.get("dns_address"),
        "gateway_ip": module.params.get("gateway_ip"),
        "name": module.params.get("name"),
        "vpc_id": module.params.get("vpc_id"),
    }


def create(config):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")
    timeout = 60 * int(module.params['timeouts']['create'].rstrip('m'))
    opts = user_input_parameters(module)

    params = build_create_parameters(opts)
    r = send_create_request(module, params, client)
    obj = async_wait_create(config, r, client, timeout)
    module.params['id'] = navigate_value(obj, ["subnet", "id"])

    return read_resource(config)


def update(config):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")
    timeout = 60 * int(module.params['timeouts']['update'].rstrip('m'))
    opts = user_input_parameters(module)

    params = build_update_parameters(opts)
    if params:
        r = send_update_request(module, params, client)
        async_wait_update(config, r, client, timeout)

    return read_resource(config)


def delete(config):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")

    send_delete_request(module, None, client)

    url = build_path(module, "subnets/{id}")

    def _refresh_status():
        try:
            client.get(url)
        except HwcClientException404:
            return True, "Done"

        except Exception:
            return None, ""

        return True, "Pending"

    timeout = 60 * int(module.params['timeouts']['create'].rstrip('m'))
    try:
        wait_to_finish(["Done"], ["Pending"], _refresh_status, timeout)
    except Exception as ex:
        module.fail_json(msg="module(hwc_vpc_subnet): error "
                             "waiting for api(delete) to "
                             "be done, error= %s" % str(ex))


def read_resource(config, exclude_output=False):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")

    res = {}
    r = send_read_request(module, client)
    fill_read_resp_body(r)
    res["read"] = r

    return update_properties(module, res, exclude_output)


def fetch_resource(config):
    module = config.module
    client = config.client(get_region(module), "vpc", "project")
    opts = user_input_parameters(module)
    identity = {
        "vpc_id": navigate_value(opts, ["vpc_id"]),
        "name": navigate_value(opts, ["name"]),
    }

    link = "subnets"
    query_link = "?marker={marker}&limit=10&vpc_id=" + str(identity["vpc_id"])
    link += query_link

    p = {'marker': ''}
    while True:
        url = link.format(**p)
        r = send_list_request(module, client, url)
        if not r:
            return None
        for item in r:
            for k, v in identity.items():
                if item[k] != v:
                    break
            else:
                return item

        p['marker'] = r[-1].get('id')


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


def send_create_request(module, params, client):
    url = "subnets"
    try:
        r = client.post(url, params)
    except HwcClientException as ex:
        msg = ("module(hwc_vpc_subnet): error running "
               "api(create), error: %s" % str(ex))
        module.fail_json(msg=msg)

    return r


def async_wait_create(config, result, client, timeout):
    module = config.module

    path_parameters = {
        "subnet_id": ["subnet", "id"],
    }
    data = {
        key: navigate_value(result, path)
        for key, path in path_parameters.items()
    }

    url = build_path(module, "subnets/{subnet_id}", data)

    def _query_status():
        r = None
        try:
            r = client.get(url, timeout=timeout)
        except HwcClientException:
            return None, ""

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
        module.fail_json(msg="module(hwc_vpc_subnet): error "
                             "waiting for api(create) to "
                             "be done, error= %s" % str(ex))


def build_update_parameters(opts):
    params = dict()

    v = navigate_value(opts, ["dhcp_enable"], None)
    if v is not None:
        params["dhcp_enable"] = v

    v = expand_update_dns_list(opts, None)
    if not is_empty_value(v):
        params["dnsList"] = v

    v = navigate_value(opts, ["name"], None)
    if not is_empty_value(v):
        params["name"] = v

    v = expand_update_primary_dns(opts, None)
    if not is_empty_value(v):
        params["primary_dns"] = v

    v = expand_update_secondary_dns(opts, None)
    if not is_empty_value(v):
        params["secondary_dns"] = v

    if not params:
        return params

    params = {"subnet": params}

    return params


def expand_update_dns_list(d, array_index):
    v = navigate_value(d, ["dns_address"], array_index)
    return v if (v and len(v) > 2) else []


def expand_update_primary_dns(d, array_index):
    v = navigate_value(d, ["dns_address"], array_index)
    return v[0] if v else ""


def expand_update_secondary_dns(d, array_index):
    v = navigate_value(d, ["dns_address"], array_index)
    return v[1] if (v and len(v) > 1) else ""


def send_update_request(module, params, client):
    url = build_path(module, "vpcs/{vpc_id}/subnets/{id}")

    try:
        r = client.put(url, params)
    except HwcClientException as ex:
        msg = ("module(hwc_vpc_subnet): error running "
               "api(update), error: %s" % str(ex))
        module.fail_json(msg=msg)

    return r


def async_wait_update(config, result, client, timeout):
    module = config.module

    path_parameters = {
        "subnet_id": ["subnet", "id"],
    }
    data = {
        key: navigate_value(result, path)
        for key, path in path_parameters.items()
    }

    url = build_path(module, "subnets/{subnet_id}", data)

    def _query_status():
        r = None
        try:
            r = client.get(url, timeout=timeout)
        except HwcClientException:
            return None, ""

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
        module.fail_json(msg="module(hwc_vpc_subnet): error "
                             "waiting for api(update) to "
                             "be done, error= %s" % str(ex))


def send_delete_request(module, params, client):
    url = build_path(module, "vpcs/{vpc_id}/subnets/{id}")

    try:
        r = client.delete(url, params)
    except HwcClientException as ex:
        msg = ("module(hwc_vpc_subnet): error running "
               "api(delete), error: %s" % str(ex))
        module.fail_json(msg=msg)

    return r


def send_read_request(module, client):
    url = build_path(module, "subnets/{id}")

    r = None
    try:
        r = client.get(url)
    except HwcClientException as ex:
        msg = ("module(hwc_vpc_subnet): error running "
               "api(read), error: %s" % str(ex))
        module.fail_json(msg=msg)

    return navigate_value(r, ["subnet"], None)


def fill_read_resp_body(body):

    body.setdefault("availability_zone", None)

    body.setdefault("cidr", None)

    body.setdefault("dhcp_enable", None)

    body.setdefault("dnsList", None)

    body.setdefault("gateway_ip", None)

    body.setdefault("id", None)

    body.setdefault("name", None)

    body.setdefault("neutron_network_id", None)

    body.setdefault("neutron_subnet_id", None)

    body.setdefault("primary_dns", None)

    body.setdefault("secondary_dns", None)

    body.setdefault("status", None)

    body.setdefault("vpc_id", None)


def update_properties(module, response, exclude_output=False):
    r = user_input_parameters(module)

    v = navigate_value(response, ["read", "availability_zone"], None)
    r["availability_zone"] = v

    v = navigate_value(response, ["read", "cidr"], None)
    r["cidr"] = v

    v = navigate_value(response, ["read", "dhcp_enable"], None)
    r["dhcp_enable"] = v

    v = navigate_value(response, ["read", "dnsList"], None)
    r["dns_address"] = v

    v = navigate_value(response, ["read", "gateway_ip"], None)
    r["gateway_ip"] = v

    v = navigate_value(response, ["read", "name"], None)
    r["name"] = v

    v = navigate_value(response, ["read", "vpc_id"], None)
    r["vpc_id"] = v

    return r


def send_list_request(module, client, url):

    r = None
    try:
        r = client.get(url)
    except HwcClientException as ex:
        msg = ("module(hwc_vpc_subnet): error running "
               "api(list), error: %s" % str(ex))
        module.fail_json(msg=msg)

    return navigate_value(r, ["subnets"], None)


if __name__ == '__main__':
    main()
