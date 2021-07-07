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
module: hwc_cce_node
description:
    - instance management.
short_description: Creates a resource of cce node in Huawei Cloud
version_added: '2.9'
author: Huawei Inc. (@huaweicloud)
requirements:
    - huaweicloudsdkcore >= 3.0.47
    - huaweicloudsdkcce >= 3.0.47
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
                default: '30m'
            delete:
                description:
                    - The timeouts for delete operation.
                type: str
                default: '30m'
    availability_zone:
        description:
            - Specifies the name of the AZ where the node is located.
        type: str
        required: true
    flavor_id:
        description:
            - Specifies the ID of the node flavor.
        type: str
        required: true
    cluster_id:
        description:
            - Specifies the ID of the cluster to which the node belongs.
        type: str
        required: true
    name:
        description:
            - "Specifies the node name. Value requirements: Consists of 1 to 64
              characters, including letters, digits, hyphens
              (-), periods (.)."
        type: str
        required: false
    os:
        description:
            - Specifies the operating System of the node.
        type: str
        required: false
    key_pair:
        description:
            - Specifies the key pair name when logging in to select the key pair mode.
        type: str
        required: false
    password:
        description:
            - Specifies the root password when logging in to select the password mode.
        type: str
        required: false
    root_volume:
        description:
            - Specifies the system disk of the node.
        type: complex
        required: true
        suboptions:
            volume_type:
                description:
                    - Specifies the disk type.
                    - SATA is common I/O disk type.
                    - SAS is high I/O disk type.
                    - SSD is ultra-high I/O disk type.
                type: str
                required: true
            size:
                description:
                    - Specifies the system disk size, in GB. The value range is
                      40 to 1024. 
                type: int
                required: true
    data_volumes:
        description:
            - Specifies the data disks of the node.
        type: complex
        required: true
        suboptions:
            volume_type:
                description:
                    - Specifies the disk type.
                    - SATA is common I/O disk type.
                    - SAS is high I/O disk type.
                    - SSD is ultra-high I/O disk type.
                type: str
                required: true
            size:
                description:
                    - Specifies the system disk size, in GB. The value range is
                      100 to 32768. 
                type: int
                required: true
    subnet_id:
        description:
            - Specifies the ID of the subnet to which the NIC belongs.
        type: str
        required: false
    fixed_ip:
        description:
            - Specifies fixed IP of the NIC.
        type: str
        required: false
    eip_id:
        description:
            - Specifies the ID of the elastic IP address assigned to the node.
              Only elastic IP addresses in the DOWN state can be
              assigned.
        type: str
        required: false
    ecs_group_id:
        description:
            - Specifies the ecs group id. If specified, the node will be created under the cloud server group.
        type: str
        required: false
    max_pods:
        description:
            - Specifies the maximum number of instances a node is allowed to create.
        type: int
        required: false
    pretinstall:
        description:
            - Specifies the script required before installation. The input value must be a Base64 encoded.
        type: str
        required: false
    postinstall:
        description:
            - Specifies the script required after installation. The input value must be a Base64 encoded.
        type: str
        required: false
    extend_param:
        description:
            - Specifies the extend parameter of the node, key/value pair format.
        type: dict
        required: false
    tags:
        description:
            - Specifies the tags of the node, key/value pair format.
        type: dict
        required: false
    k8s_tags:
        description:
            - Specifies the tags of the kubernetes node, key/value pair format.
        type: dict
        required: false
    taints:
        description:
            - You can add taints to created nodes to configure anti-affinity.
        type: complex
        required: false
        suboptions:
            key:
                description:
                    - A key must contain 1 to 63 characters starting with a letter or digit.
                      Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed.
                      A DNS subdomain name can be used as the prefix of a key.
                type: str
                required: true
            value:
                description:
                    - A value must start with a letter or digit and can contain a maximum of 63 characters,
                      including letters, digits, hyphens (-), underscores (_), and periods (.).
                type: int
                required: true
            effect:
                description:
                    - Available options are NoSchedule, PreferNoSchedule, and NoExecute.
                type: int
                required: true
extends_documentation_fragment:
  - hwceco.hwcollection.hwc_auth_options
'''

EXAMPLES = '''
# create an cce node instance
- name: create a vpc
  hwc_vpc:
    cidr: "192.168.100.0/24"
    name: "ansible_vpc_test"
  register: vpc

- name: create a subnet
  hwc_vpc_subnet:
    gateway_ip: "192.168.100.32"
    name: "ansible_subnet_test"
    dhcp_enable: true
    vpc_id: "{{ vpc.state.id }}"
    cidr: "192.168.100.0/26"
    # dns is required for cce node installing
    dns_address:
      - "100.125.1.250"
      - "100.125.21.250"
    filters:
      - "name"
  register: subnet

- name: create a cce cluster
    hwc_cce_cluster:
      filters:
        - "name"
        
      name: "ansible-cce-cluster-test"
      description: "ansible cce cluster test"
      flavor_id: "cce.s1.small"
      vpc_id: "{{ vpc.state.id }}"
      subnet_id: "{{ subnet.state.id }}"
      container_network_type: "overlay_l2"
      authentication_mode: "rbac"
    register: cluster

- name: create a cce node
      hwc_cce_node:
        filters:
          - "name"
        
        name: "ansible-cce-node-test"
        cluster_id: "{{ cluster.state.id }}"
        flavor_id: "s6.large.2"
        availability_zone: "cn-north-4a"
        subnet_id: "{{ subnet.state.id }}"
        key_pair: "test-key-pair"
        root_volume:
          size: 40
          volume_type: "SAS"
        data_volumes:
          - size: 100
            volume_type: "SAS"
'''

RETURN = '''
    availability_zone:
        description:
            - Specifies the name of the AZ where the node is located.
        type: str
        returned: success
    flavor_id:
        description:
            - Specifies the ID of the node flavor.
        type: str
        returned: success
    cluster_id:
        description:
            - Specifies the ID of the cluster to which the node belongs.
        type: str
        returned: success
    name:
        description:
            - "Specifies the node name. Value requirements: Consists of 1 to 64
              characters, including letters, digits, hyphens
              (-), periods (.)."
        type: str
        returned: success
    os:
        description:
            - Specifies the operating System of the node.
        type: str
        returned: success
    key_pair:
        description:
            - Specifies the key pair name when logging in to select the key pair mode.
        type: str
        returned: success
    password:
        description:
            - Specifies the root password when logging in to select the password mode.
        type: str
        returned: success
    root_volume:
        description:
            - Specifies the system disk of the node.
        type: complex
        returned: success
        suboptions:
            volume_type:
                description:
                    - Specifies the disk type.
                    - SATA is common I/O disk type.
                    - SAS is high I/O disk type.
                    - SSD is ultra-high I/O disk type.
                type: str
                returned: success
            size:
                description:
                    - Specifies the system disk size, in GB. The value range is
                      40 to 1024. 
                type: int
                returned: success
    data_volumes:
        description:
            - Specifies the data disks of the node.
        type: complex
        returned: success
        suboptions:
            volume_type:
                description:
                    - Specifies the disk type.
                    - SATA is common I/O disk type.
                    - SAS is high I/O disk type.
                    - SSD is ultra-high I/O disk type.
                type: str
                returned: success
            size:
                description:
                    - Specifies the system disk size, in GB. The value range is
                      100 to 32768. 
                type: int
                returned: success
    subnet_id:
        description:
            - Specifies the ID of the subnet to which the NIC belongs.
        type: str
        returned: success
    fixed_ip:
        description:
            - Specifies fixed IP of the NIC.
        type: str
        returned: success
    eip_id:
        description:
            - Specifies the ID of the elastic IP address assigned to the node.
              Only elastic IP addresses in the DOWN state can be
              assigned.
        type: str
        returned: success
    ecs_group_id:
        description:
            - Specifies the ecs group id. If specified, the node will be created under the cloud server group.
        type: str
        returned: success
    max_pods:
        description:
            - Specifies the maximum number of instances a node is allowed to create.
        type: int
        returned: success
    pretinstall:
        description:
            - Specifies the script required before installation. The input value must be a Base64 encoded.
        type: str
        returned: success
    postinstall:
        description:
            - Specifies the script required after installation. The input value must be a Base64 encoded.
        type: str
        returned: success
    extend_param:
        description:
            - Specifies the extend parameter of the node, key/value pair format.
        type: dict
        returned: success
    tags:
        description:
            - Specifies the tags of the node, key/value pair format.
        type: dict
        returned: success
    k8s_tags:
        description:
            - Specifies the tags of the kubernetes node, key/value pair format.
        type: dict
        returned: success
    taints:
        description:
            - You can add taints to created nodes to configure anti-affinity.
        type: complex
        returned: success
        suboptions:
            key:
                description:
                    - A key must contain 1 to 63 characters starting with a letter or digit.
                      Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed.
                      A DNS subdomain name can be used as the prefix of a key.
                type: str
                returned: success
            value:
                description:
                    - A value must start with a letter or digit and can contain a maximum of 63 characters,
                      including letters, digits, hyphens (-), underscores (_), and periods (.).
                type: int
                returned: success
            effect:
                description:
                    - Available options are NoSchedule, PreferNoSchedule, and NoExecute.
                type: int
                returned: success
    status:
        description:
            - Specifies the node status.
        type: str
        returned: success
'''

from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleBase
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleException
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import are_different_dicts
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import navigate_value
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import is_empty_value
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import wait_to_finish
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import tags_to_dict

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcce.v3 import *


class HwcCceNode(HwcModuleBase):
    def __init__(self):
        self.argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'],
                       type='str'),
            filters=dict(required=True, type='list', elements='str'),
            timeouts=dict(type='dict', options=dict(
                create=dict(default='30m', type='str'),
                delete=dict(default='30m', type='str'),
            ), default=dict()),
            
            cluster_id=dict(type='str', required=True),
            name=dict(type='str'),
            flavor_id=dict(type='str', required=True),
            availability_zone=dict(type='str', required=True),
            os=dict(type='str'),
            key_pair=dict(type='str'),
            password=dict(type='str', no_log=True),
            root_volume=dict(type='dict', required=True, options=dict(
                volume_type=dict(type='str', required=True),
                size=dict(type='int', required=True)
            )),
            data_volumes=dict(type='list', required=True, elements='dict', options=dict(
                volume_type=dict(type='str', required=True),
                size=dict(type='int', required=True)
            )),
            subnet_id=dict(type='str'),
            fixed_ip=dict(type='str'),
            eip_id=dict(type='str'),
            ecs_group_id=dict(type='str'),
            max_pods=dict(type='str'),
            preinstall=dict(type='str'),
            postinstall=dict(type='str'),
            extend_param=dict(type='dict'),
            taints=dict(type='list', elements='dict', options=dict(
                key=dict(type='str', required=True),
                value=dict(type='int', required=True),
                effect=dict(type='str', required=True)
            )),
            tags=dict(type='dict'),
            k8s_tags=dict(type='dict')
        )

        self.results = dict(
            changed=False,
            state=dict()
        )

        super(HwcCceNode, self).__init__(self.argument_spec, supports_check_mode=True)

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
                    self.module.params['id'] = navigate_value(resource, ["metadata", "uid"])

            result = {}
            changed = False

            if self.module.params['state'] == 'present':
                if not resource:
                    if not self.module.check_mode:
                        self.create()
                    changed = True

                inputv = user_input_parameters(self.module)
                resp, array_index = self.read()
                result = build_state(inputv, resp, array_index)
                set_readonly_options(inputv, result)
                if are_different_dicts(inputv, result):
                    if not self.module.check_mode:
                        self.update(inputv, result)
                        inputv = user_input_parameters(self.module)
                        resp, array_index = self.read()
                        result = build_state(inputv, resp, array_index)
                        set_readonly_options(inputv, result)
                        if are_different_dicts(inputv, result):
                            raise Exception("Update resource failed, "
                                            "some attributes are not updated")

                    changed = True

                result['id'] = self.module.params.get('id')
            else:
                result = dict()
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

        try:
            request = ListNodesRequest(self.module.params["cluster_id"])
            self.log('list cce node request: %s' % request)
            response = self.cce_client.list_nodes(request)
            self.log('list cce node response: %s' % response)
        except exceptions.ClientRequestException as e:
            raise HwcModuleException(
                    'search cce node failed: %s' % e.error_msg)

        r = navigate_value(response.to_json_object(), ['items'], None)

        if not r:
            return result

        for item in r:
            item = fill_list_resp_body(item)
            self.log('cce node identity_obj: %s' % identity_obj)
            self.log('cce node item: %s' % item)
            if not are_different_dicts(identity_obj, item):
                result.append(item)

        if len(result) > 1:
            return result

        return result


    def create(self):
        opts = user_input_parameters(self.module)
        timeout = 60 * int(self.module.params['timeouts']['create'].rstrip('m'))
        try:
            request_body = build_create_parameters(opts)
            request = CreateNodeRequest(cluster_id=self.module.params["cluster_id"], body=request_body)
            self.log('create cce node request body: %s' %request)
            response = self.cce_client.create_node(request)
            self.log('create cce node response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Create cce node failed: %s' % e)

        job_id = response.to_json_object()['status']['jobID']

        obj = self.async_wait(job_id, timeout)

        sub_job_identity = {
            "type": "CreateNode",
        }
        for item in navigate_value(obj, ["spec", "subJobs"]):
            for k, v in sub_job_identity.items():
                if item["spec"][k] != v:
                    break
            else:
                obj = item
                break
        else:
            raise Exception("Can't find the sub job")

        self.module.params['id'] = navigate_value(obj, ["spec", "resourceID"])

    def read(self):
        try:
            request = ShowNodeRequest(cluster_id=self.module.params["cluster_id"], node_id=self.module.params['id'])
            self.log('read cce node request body: %s' %request)
            response = self.cce_client.show_node(request)
            self.log('read cce node response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read cce node failed: %s' % e)

        r = response.to_json_object()
        res = {}
        res["read"] = fill_read_resp_body(r)

        return res, None

    def update(self, expect_state, current_state):
        self.log('expect_state: %s' % expect_state)
        self.log('current_state: %s' % current_state)

        params = build_update_parameters(expect_state)
        params1 = build_update_parameters(current_state)

        self.log('params: %s' % params)
        self.log('params1: %s' % params1)

        if params and are_different_dicts(params, params1):
            try:
                request = UpdateNodeRequest(cluster_id=self.module.params["cluster_id"], node_id=self.module.params['id'], body=params)
                self.log('Update cce node request body: %s' %request)
                response = self.cce_client.update_node(request)
                self.log('Update cce node response body: %s' % response)
            except exceptions.ClientRequestException as e:
                self.fail('Update cce node failed: %s' % e)


    def delete(self):
        timeout = 60 * int(self.module.params['timeouts']['delete'].rstrip('m'))
        try:
            request = DeleteNodeRequest(cluster_id=self.module.params["cluster_id"], node_id=self.module.params['id'])
            self.log('delete cce node request body: %s' %request)
            response = self.cce_client.delete_node(request)
            self.log('delete cce node response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Delete cce node failed: %s' % e)

        job_id = response.to_json_object()['status']['jobID']

        self.async_wait(job_id, timeout)

    def async_wait(self, job_id, timeout):
        def _query_status():
            r = None
            try:
                request = ShowJobRequest(job_id)
                self.log('show job request body: %s' %request)
                response = self.cce_client.show_job(request)
                self.log('show job response body: %s' % response)
            except exceptions.ClientRequestException as e:
                self.fail('show job failed: %s' % e)

            r = response.to_json_object()

            try:
                s = navigate_value(r, ["status", "phase"])
                return r, s
            except Exception:
                return None, ""

        try:
            return wait_to_finish(
                ["Success"],
                ["Running", "Initializing"],
                _query_status, timeout)
        except Exception as ex:
            self.module.fail_json(msg="module(hwc_cce_cluster): error "
                                "waiting to be done, error= %s" % str(ex))


def user_input_parameters(module):
    return {
        "name": module.params.get("name"),
        "id": module.params.get("id"),
        "flavor_id": module.params.get("flavor_id"),
        "availability_zone": module.params.get("availability_zone"),
        "os": module.params.get("os"),
        "key_pair": module.params.get("key_pair"),
        "password": module.params.get("password"),
        "root_volume": module.params.get("root_volume"),
        "data_volumes": module.params.get("data_volumes"),
        "subnet_id": module.params.get("subnet_id"),
        "fixed_ip": module.params.get("fixed_ip"),
        "eip_id": module.params.get("eip_id"),
        "ecs_group_id": module.params.get("ecs_group_id"),
        "max_pods": module.params.get("max_pods"),
        "preinstall": module.params.get("preinstall"),
        "postinstall": module.params.get("postinstall"),
        "extend_param": module.params.get("extend_param"),
        "taints": module.params.get("taints"),
        "tags": module.params.get("tags"),
        "k8s_tags": module.params.get("k8s_tags")
    }


def build_state(opts, response, array_index):
    states = flatten_options(response, array_index)
    set_unreadable_options(opts, states)
    return states


def set_unreadable_options(opts, states):
    states["max_pods"] = opts.get("max_pods")

    states["preinstall"] = opts.get("preinstall")

    states["postinstall"] = opts.get("postinstall")


def build_create_parameters(opts):
    params = dict()

    params["kind"] = "Node"

    params["apiversion"] = "v3"

    v = expand_create_matadata(opts, None)
    if not is_empty_value(v):
        params["metadata"] = v

    v = expand_create_spec(opts, None)
    if not is_empty_value(v):
        params["spec"] = v

    return params


def expand_create_matadata(d, array_index):
    r = dict()

    v = navigate_value(d, ["name"], array_index)
    if not is_empty_value(v):
        r["name"] = v

    return r


def expand_create_spec(d, array_index):
    r = dict()

    v = navigate_value(d, ["flavor_id"], array_index)
    if not is_empty_value(v):
        r["flavor"] = v

    v = navigate_value(d, ["availability_zone"], array_index)
    if not is_empty_value(v):
        r["az"] = v

    v = navigate_value(d, ["os"], array_index)
    if not is_empty_value(v):
        r["os"] = v

    v = expand_create_login(d, None)
    if not is_empty_value(v):
        r["login"] = v

    v = expand_create_root_volume(d, None)
    if not is_empty_value(v):
        r["rootVolume"] = v

    v = expand_create_data_volumes(d, None)
    if not is_empty_value(v):
        r["dataVolumes"] = v

    v = expand_create_public_ip(d, None)
    if not is_empty_value(v):
        r["publicIP"] = v

    v = expand_create_nic_spec(d, None)
    if not is_empty_value(v):
        r["nodeNicSpec"] = v

    v = navigate_value(d, ["ecs_group_id"], array_index)
    if not is_empty_value(v):
        r["ecsGroupId"] = v

    v = navigate_value(d, ["k8s_tags"], array_index)
    if not is_empty_value(v):
        r["k8sTags"] = v

    v = expand_create_extendparam(d, None)
    if not is_empty_value(v):
        r["extendParam"] = v

    v = expand_create_tags(d, None)
    if not is_empty_value(v):
        r["userTags"] = v

    v = navigate_value(d, ["taints"], array_index)
    if not is_empty_value(v):
        r["taints"] = v

    r["count"] = 1

    return r


def expand_create_login(d, array_index):
    r = dict()

    v = navigate_value(d, ["key_pair"], array_index)
    if not is_empty_value(v):
        r["sshKey"] = v

    v = navigate_value(d, ["password"], array_index)
    if not is_empty_value(v):
        r["userPassword"] = {"password": v}

    return r


def expand_create_root_volume(d, array_index):
    r = dict()

    v = navigate_value(d, ["root_volume", "size"], array_index)
    if not is_empty_value(v):
        r["size"] = v

    v = navigate_value(d, ["root_volume", "volume_type"], array_index)
    if not is_empty_value(v):
        r["volumetype"] = v

    return r


def expand_create_data_volumes(d, array_index):
    new_ai = dict()
    if array_index:
        new_ai.update(array_index)

    req = []

    v = navigate_value(
        d, ["data_volumes"], new_ai)

    if not v:
        return req
    n = len(v)
    for i in range(n):
        new_ai["data_volumes"] = i
        transformed = dict()

        v = navigate_value(d, ["data_volumes", "size"], new_ai)
        if not is_empty_value(v):
            transformed["size"] = v

        v = navigate_value(d, ["data_volumes", "volume_type"], new_ai)
        if not is_empty_value(v):
            transformed["volumetype"] = v

        if transformed:
            req.append(transformed)

    return req


def expand_create_public_ip(d, array_index):
    r = dict()

    v = navigate_value(d, ["eip_id"], array_index)
    if not is_empty_value(v):
        r["ids"] = [v]
        r["count"] = 1

    return r


def expand_create_nic_spec(d, array_index):
    r = dict()

    v = navigate_value(d, ["subnet_id"], array_index)
    if not is_empty_value(v):
        r["subnetId"] = v

    v = navigate_value(d, ["fixed_ip"], array_index)
    if not is_empty_value(v):
        r["fixedIps"] = [v]

    if r:
        r = {"primaryNic": r}

    return r


def expand_create_extendparam(d, array_index):
    r = dict()

    v = navigate_value(d, ["max_pods"], array_index)
    if not is_empty_value(v):
        r["maxPods"] = v

    v = navigate_value(d, ["preinstall"], array_index)
    if not is_empty_value(v):
        r["alpha.cce/preInstall"] = v

    v = navigate_value(d, ["postinstall"], array_index)
    if not is_empty_value(v):
        r["alpha.cce/postInstall"] = v

    v = navigate_value(d, ["extend_param"], array_index)
    if v:
        r.update(v)

    return r


def expand_create_tags(d, array_index):
    tags = []
    tags_raw = navigate_value(d, ['tags'], array_index)
    if tags_raw:
        for k, v in tags_raw.items():
            tag = {
                "key": k,
                "value": v
            }
            tags.append(tag)

    return tags


def build_update_parameters(opts):
    params = dict()

    v = navigate_value(opts, ["name"], None)
    if not is_empty_value(v):
        params["name"] = v

    if not params:
        return params

    params = {"metadata": params}

    return params


def fill_read_resp_body(body):
    result = dict()

    v = fill_read_resp_metadata(body.get("metadata"))
    if v:
        result["metadata"] = v

    v = fill_read_resp_spec(body.get("spec"))
    if v:
        result["spec"] = v

    v = fill_read_resp_status(body.get("status"))
    if v:
        result["status"] = v

    return result


def fill_read_resp_metadata(value):
    if not value:
        return None

    result = dict()

    result["name"] = value.get("name")

    result["uid"] = value.get("uid")

    return result


def fill_read_resp_status(value):
    if not value:
        return None

    result = dict()

    result["phase"] = value.get("phase")

    return result


def fill_read_resp_spec(value):
    if not value:
        return None

    result = dict()

    result["flavor"] = value.get("flavor")
    result["az"] = value.get("az")
    result["os"] = value.get("os")
    result["taints"] = value.get("taints")
    result["k8sTags"] = value.get("k8sTags")
    result["ecsGroupId"] = value.get("ecsGroupId")
    result["extendParam"] = value.get("extendParam")
    result["userTags"] = value.get("userTags")

    v = fill_read_resp_login(value.get("login"))
    result["login"] = v
    
    v = fill_read_resp_root_volume(value.get("rootVolume"))
    result["rootVolume"] = v

    v = fill_read_resp_data_volumes(value.get("dataVolumes"))
    result["dataVolumes"] = v

    v = fill_read_resp_public_ip(value.get("publicIP"))
    result["publicIP"] = v

    v = fill_read_resp_nic_spec(value.get("nodeNicSpec"))
    result["nodeNicSpec"] = v

    return result


def fill_read_resp_login(value):
    if not value:
        return None

    result = dict()

    result["sshKey"] = value.get("sshKey")

    result["userPassword"] = None

    v = value.get("userPassword")

    if v:
        result["userPassword"] = {"password": v.get("password")}

    return result


def fill_read_resp_root_volume(value):
    if not value:
        return None

    result = dict()

    result["size"] = value.get("size")

    result["volumetype"] = value.get("volumetype")

    return result


def fill_read_resp_data_volumes(value):
    if not value:
        return None

    result = []
    for item in value:
        val = dict()

        val["size"] = item.get("size")

        val["volumetype"] = item.get("volumetype")

        result.append(val)

    return result


def fill_read_resp_public_ip(value):
    if not value:
        return None

    result = dict()

    result["ids"] = value.get("ids")

    return result


def fill_read_resp_nic_spec(value):
    if not value:
        return None

    result = dict()

    result["primaryNic"] = None
    v = value.get("primaryNic")
    if v:
        result["primaryNic"] = {"subnetId": v.get("subnetId"), "fixedIps": v.get("fixedIps")}

    return result


def flatten_options(response, array_index):
    r = dict()

    v = navigate_value(
        response, ["read", "metadata", "name"], array_index)
    r["name"] = v

    v = navigate_value(
        response, ["read", "metadata", "uid"], array_index)
    r["id"] = v

    v = navigate_value(response, ["read", "spec", "flavor"], array_index)
    r["flavor_id"] = v

    v = navigate_value(response, ["read", "spec", "az"], array_index)
    r["availability_zone"] = v

    v = navigate_value(response, ["read", "spec", "os"], array_index)
    r["os"] = v

    v = navigate_value(response, ["read", "spec", "taints"], array_index)
    r["taints"] = v

    v = navigate_value(response, ["read", "spec", "k8sTags"], array_index)
    r["k8s_tags"] = v

    v = navigate_value(response, ["read", "spec", "ecsGroupId"], array_index)
    r["ecs_group_id"] = v

    v = navigate_value(response, ["read", "spec", "userTags"], array_index)
    r["tags"] = tags_to_dict(v) if v else None

    v = navigate_value(response, ["read", "spec", "login", "sshKey"], array_index)
    r["key_pair"] = v

    v = navigate_value(response, ["read", "spec", "login", "userPassword", "password"], array_index)
    r["password"] = v

    v = flatten_root_volume(response, array_index)
    r["root_volume"] = v

    v = flatten_data_volumes(response, array_index)
    r["data_volumes"] = v

    v = navigate_value(response, ["read", "spec", "publicIP", "ids"], {"read.spec.publicIP.ids": 0})
    r["eip_id"] = v



    v = navigate_value(response, ["read", "spec", "nodeNicSpec", "primaryNic", "subnetId"], array_index)
    r["subnet_id"] = v

    v = navigate_value(response, ["read", "spec", "nodeNicSpec", "primaryNic", "fixedIps"], array_index)
    r["fixed_ip"] = v[0] if v else None

    
    v = navigate_value(response, ["read", "spec", "extendParam"], array_index)
    r["extend_param"] = v

    v = navigate_value(response, ["read", "status", "phase"])
    r["status"] = v

    return r


def flatten_root_volume(d, array_index):
    result = dict()

    v = navigate_value(d, ["read", "spec", "rootVolume", "size"], array_index)
    result["size"] = v

    v = navigate_value(d, ["read", "spec", "rootVolume", "volumetype"], array_index)
    result["volume_type"] = v

    for v in result.values():
        if v is not None:
            return result
    return None


def flatten_data_volumes(d, array_index):
    v = navigate_value(d, ["read", "spec", "dataVolumes"],
                       array_index)
    if not v:
        return None
    n = len(v)
    result = []

    new_ai = dict()
    if array_index:
        new_ai.update(array_index)

    for i in range(n):
        new_ai["read.spec.dataVolumes"] = i

        val = dict()

        v = navigate_value(
            d, ["read", "spec", "dataVolumes", "size"], new_ai)
        val["size"] = v

        v = navigate_value(
            d, ["read", "spec", "dataVolumes", "volumetype"], new_ai)
        val["volume_type"] = v

        for v in val.values():
            if v is not None:
                result.append(val)
                break

    return result if result else None


def set_readonly_options(opts, states):

    opts["status"] = states.get("status")


def _build_identity_object(module, all_opts):
    filters = module.params.get("filters")
    opts = dict()
    for k, v in all_opts.items():
        opts[k] = v if k in filters else None

    result = dict()

    v = expand_list_matadata(opts, None)
    result["metadata"] = v

    v = expand_list_spec(opts, None)
    result["spec"] = v

    return result


def expand_list_matadata(d, array_index):
    r = dict()

    v = navigate_value(d, ["name"], array_index)
    r["name"] = v

    v = navigate_value(d, ["id"], array_index)
    r["uid"] = v

    return r


def expand_list_spec(d, array_index):
    r = dict()

    v = navigate_value(d, ["flavor_id"], array_index)
    r["flavor"] = v

    v = navigate_value(d, ["availability_zone"], array_index)
    r["az"] = v

    v = navigate_value(d, ["os"], array_index)
    r["os"] = v

    r["login"] = None

    v = expand_list_root_volume(d, None)
    r["rootVolume"] = v

    v = expand_list_data_volumes(d, None)
    r["dataVolumes"] = v if v else None

    v = expand_list_public_ip(d, None)
    r["publicIP"] = v

    v = expand_list_nic_spec(d, None)
    r["nodeNicSpec"] = v

    v = navigate_value(d, ["ecs_group_id"], array_index)
    r["ecsGroupId"] = v

    v = navigate_value(d, ["k8s_tags"], array_index)
    r["k8sTags"] = v

    v = expand_list_extendparam(d, None)
    r["extendParam"] = v if v else None

    v = expand_list_tags(d, None)
    r["userTags"] = v if v else None

    v = navigate_value(d, ["taints"], array_index)
    r["taints"] = v

    return r


def expand_list_login(d, array_index):
    r = dict()

    v = navigate_value(d, ["key_pair"], array_index)
    r["sshKey"] = v

    v = navigate_value(d, ["password"], array_index)
    r["userPassword"] = {"password": v}

    return r


def expand_list_root_volume(d, array_index):
    r = dict()

    v = navigate_value(d, ["root_volume", "size"], array_index)
    r["size"] = v

    v = navigate_value(d, ["root_volume", "volume_type"], array_index)
    r["volumetype"] = v

    return r


def expand_list_data_volumes(d, array_index):
    new_ai = dict()
    if array_index:
        new_ai.update(array_index)

    req = []

    v = navigate_value(
        d, ["data_volumes"], new_ai)

    if not v:
        return req
    n = len(v)
    for i in range(n):
        new_ai["data_volumes"] = i
        transformed = dict()

        v = navigate_value(d, ["data_volumes", "size"], new_ai)
        transformed["size"] = v

        v = navigate_value(d, ["data_volumes", "volume_type"], new_ai)
        transformed["volumetype"] = v

        if transformed:
            req.append(transformed)

    return req


def expand_list_public_ip(d, array_index):
    r = dict()

    v = navigate_value(d, ["eip_id"], array_index)
    r["ids"] = [v] if v else None

    return r


def expand_list_nic_spec(d, array_index):
    r = dict()

    v = navigate_value(d, ["subnet_id"], array_index)
    r["subnetId"] = v

    v = navigate_value(d, ["fixed_ip"], array_index)
    r["fixedIps"] = [v] if v else None

    if r:
        r = {"primaryNic": r}

    return r


def expand_list_extendparam(d, array_index):
    r = dict()

    v = navigate_value(d, ["max_pods"], array_index)
    if not is_empty_value(v):
        r["maxPods"] = v

    v = navigate_value(d, ["preinstall"], array_index)
    if not is_empty_value(v):
        r["alpha.cce/preInstall"] = v

    v = navigate_value(d, ["postinstall"], array_index)
    if not is_empty_value(v):
        r["alpha.cce/postInstall"] = v

    v = navigate_value(d, ["extend_param"], array_index)
    if v:
        r.update(v)

    return r


def expand_list_tags(d, array_index):
    tags = []
    tags_raw = navigate_value(d, ['tags'], array_index)
    if tags_raw:
        for k, v in tags_raw.items():
            tag = {
                "key": k,
                "value": v
            }
            tags.append(tag)

    return tags


def fill_list_resp_body(body):
    result = dict()

    v = fill_list_resp_metadata(body.get("metadata"))
    result["metadata"] = v

    v = fill_list_resp_spec(body.get("spec"))
    result["spec"] = v

    return result


def fill_list_resp_metadata(value):
    if not value:
        return None

    result = dict()

    result["name"] = value.get("name")

    result["uid"] = value.get("uid")

    return result


def fill_list_resp_spec(value):
    if not value:
        return None

    result = dict()

    result["flavor"] = value.get("flavor")
    result["az"] = value.get("az")
    result["os"] = value.get("os")
    result["taints"] = value.get("taints")
    result["k8sTags"] = value.get("k8sTags")
    result["ecsGroupId"] = value.get("ecsGroupId")
    result["extendParam"] = value.get("extendParam")
    result["userTags"] = value.get("userTags")

    v = fill_list_resp_login(value.get("login"))
    result["login"] = v
    
    v = fill_list_resp_root_volume(value.get("rootVolume"))
    result["rootVolume"] = v

    v = fill_list_resp_data_volumes(value.get("dataVolumes"))
    result["dataVolumes"] = v

    v = fill_list_resp_public_ip(value.get("publicIP"))
    result["publicIP"] = v

    v = fill_list_resp_nic_spec(value.get("nodeNicSpec"))
    result["nodeNicSpec"] = v

    return result


def fill_list_resp_login(value):
    if not value:
        return None

    result = dict()

    result["sshKey"] = value.get("sshKey")

    result["userPassword"] = None

    v = value.get("userPassword")

    if v:
        result["userPassword"] = {"password": v.get("password")}

    return result


def fill_list_resp_root_volume(value):
    if not value:
        return None

    result = dict()

    result["size"] = value.get("size")

    result["volumetype"] = value.get("volumetype")

    return result


def fill_list_resp_data_volumes(value):
    if not value:
        return None

    result = []
    for item in value:
        val = dict()

        val["size"] = item.get("size")

        val["volumetype"] = item.get("volumetype")

        result.append(val)

    return result


def fill_list_resp_public_ip(value):
    if not value:
        return None

    result = dict()

    result["ids"] = value.get("ids")

    return result


def fill_list_resp_nic_spec(value):
    if not value:
        return None

    result = dict()

    result["primaryNic"] = None
    v = value.get("primaryNic")
    if v:
        result["primaryNic"] = {"subnetId": v.get("subnetId"), "fixedIps": v.get("fixedIps")}

    return result


def main():
    HwcCceNode()


if __name__ == '__main__':
    main()
