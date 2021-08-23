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
module: hwc_cce_cluster
description:
    - Creates and manages a resource of cce cluster in Huawei Cloud.
short_description: Creates a resource of cce cluster in Huawei Cloud
version_added: '1.0.0'
author: Huawei (@huaweicloud)
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
    name:
        description:
            - Specifies the name of the cluster.
        type: str
        required: true
    flavor_id:
        description:
            - Specifies the cluster specifications.
            - cce.s1.small is small-scale single cluster (up to 50 nodes).
            - cce.s1.medium is medium-scale single cluster (up to 200 nodes).
            - cce.s1.large is large-scale single cluster (up to 1000 nodes).
            - cce.s2.small is small-scale HA cluster (up to 50 nodes).
            - cce.s2.medium is medium-scale HA cluster (up to 200 nodes).
            - cce.s2.large is large-scale HA cluster (up to 1000 nodes).
            - cce.t1.small is small-scale single physical machine cluster (up to 10 nodes).
            - cce.t1.medium is medium-scale single physical machine cluster (up to 100 nodes).
            - cce.t1.large is large-scale single physical machine cluster (up to 500 nodes).
            - cce.t2.small is small-scale HA physical machine cluster (up to 10 nodes).
            - cce.t2.medium is medium-scale HA physical machine cluster (up to 100 nodes).
            - cce.t2.large is large-scale HA physical machine cluster (up to 500 nodes).
        type: str
        required: true
    cluster_version:
        description:
            - Specifies the cluster version, defaults to the latest supported version.
        type: str
        required: false
    cluster_type:
        description:
            - Specifies the cluster type, possible values are VirtualMachine, BareMetal and ARM64.
        type: str
        default: 'VirtualMachine'
        required: false
    description:
        description:
            - Specifies the cluster description.
        type: str
        required: false
    vpc_id:
        description:
            - Specifies the ID of the VPC used to create the node.
        type: str
        required: true
    subnet_id:
        description:
            - Specifies the ID of the subnet used to create the node.
        type: str
        required: true
    container_network_type:
        description:
            - Specifies the container network type.
        type: str
        required: true
    container_network_cidr:
        description:
            - Specifies the container network segment.
        type: str
        required: false
    service_network_cidr:
        description:
            - Specifies the service network segment.
        type: str
        required: false
    eni_subnet_id:
        description:
            - Specifies the ENI subnet id.
              Specified when creating a CCE Turbo cluster.
        type: str
        required: false
    eni_subnet_cidr:
        description:
            - Specifies the ENI network segment.
              Specified when creating a CCE Turbo cluster.
        type: str
        required: false
    authentication_mode:
        description:
            - Specifies the Authentication mode of the cluster,
              possible values are x509 and rbac.
        type: str
        default: 'rbac'
        required: false
    authenticating_proxy_ca:
        description:
            - Specifies the CA root certificate provided in the authenticating_proxy mode.
              The CA root certificate is encoded to the Base64 format.
        type: str
        required: false
    multi_az:
        description:
            - Specifies whether enable multiple AZs for the cluster,
              only when using HA flavors.
        type: bool
        required: false
    eip:
        description:
            - Specifies the EIP address of the cluster. 
        type: str
        required: false
    kube_proxy_mode:
        description:
            - Specifies the service forwarding mode.
            - "iptables: Traditional kube-proxy uses iptables rules to implement service load balancing.
              In this mode, too many iptables rules will be generated when many services are deployed.
              In addition, non-incremental updates will cause a latency and even obvious performance issues
              in the case of heavy service traffic."
            - "ipvs: Optimized kube-proxy mode with higher throughput and faster speed.
              This mode supports incremental updates and can keep connections uninterrupted during service updates.
              It is suitable for large-sized clusters."
        type: str
        required: false
    extend_param:
        description:
            - Specifies the extended parameter. 
        type: dict
        required: false
    enterprise_project_id:
        description:
            - Specifies enterprise project id of the cce cluster.
        type: dict
        required: false
extends_documentation_fragment:
  - hwceco.hwcollection.hwc_auth_options
'''

EXAMPLES = '''
# create an cce cluster
- name: create a vpc
  hwc_vpc:
    cidr: "192.168.100.0/24"
    name: "ansible_vpc_test"
  register: vpc

- name: create a subnet
  hwc_vpc_subnet:
    filters:
      - "name"

    gateway_ip: "192.168.100.32"
    name: "ansible_subnet_test"
    dhcp_enable: true
    vpc_id: "{{ vpc.state.id }}"
    cidr: "192.168.100.0/26"
    # dns is required for cce node installing
    dns_address:
      - "100.125.1.250"
      - "100.125.21.250"
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
'''

RETURN = '''
    name:
        description:
            - Specifies the name of the cluster.
        type: str
        returned: success
    flavor_id:
        description:
            - Specifies the cluster specifications.
            - cce.s1.small is small-scale single cluster (up to 50 nodes).
            - cce.s1.medium is medium-scale single cluster (up to 200 nodes).
            - cce.s1.large is large-scale single cluster (up to 1000 nodes).
            - cce.s2.small is small-scale HA cluster (up to 50 nodes).
            - cce.s2.medium is medium-scale HA cluster (up to 200 nodes).
            - cce.s2.large is large-scale HA cluster (up to 1000 nodes).
            - cce.t1.small is small-scale single physical machine cluster (up to 10 nodes).
            - cce.t1.medium is medium-scale single physical machine cluster (up to 100 nodes).
            - cce.t1.large is large-scale single physical machine cluster (up to 500 nodes).
            - cce.t2.small is small-scale HA physical machine cluster (up to 10 nodes).
            - cce.t2.medium is medium-scale HA physical machine cluster (up to 100 nodes).
            - cce.t2.large is large-scale HA physical machine cluster (up to 500 nodes).
        type: str
        returned: success
    cluster_version:
        description:
            - Specifies the cluster version, defaults to the latest supported version.
        type: str
        returned: success
    cluster_type:
        description:
            - Specifies the cluster type, possible values are VirtualMachine, BareMetal and ARM64.
        type: str
        returned: success
    description:
        description:
            - Specifies the cluster description.
        type: str
        returned: success
    vpc_id:
        description:
            - Specifies the ID of the VPC used to create the node.
        type: str
        returned: success
    subnet_id:
        description:
            - Specifies the ID of the subnet used to create the node.
        type: str
        returned: success
    container_network_type:
        description:
            - Specifies the container network type.
        type: str
        returned: success
    container_network_cidr:
        description:
            - Specifies the container network segment.
        type: str
        returned: success
    service_network_cidr:
        description:
            - Specifies the service network segment.
        type: str
        returned: success
    eni_subnet_id:
        description:
            - Specifies the ENI subnet id.
              Specified when creating a CCE Turbo cluster.
        type: str
        returned: success
    eni_subnet_cidr:
        description:
            - Specifies the ENI network segment.
              Specified when creating a CCE Turbo cluster.
        type: str
        returned: success
    authentication_mode:
        description:
            - Specifies the Authentication mode of the cluster,
              possible values are x509 and rbac.
        type: str
        returned: success
    authenticating_proxy_ca:
        description:
            - Specifies the CA root certificate provided in the authenticating_proxy mode.
              The CA root certificate is encoded to the Base64 format.
        type: str
        returned: success
    multi_az:
        description:
            - Specifies whether enable multiple AZs for the cluster,
              only when using HA flavors.
        type: bool
        returned: success
    eip:
        description:
            - Specifies the EIP address of the cluster. 
        type: str
        returned: success
    kube_proxy_mode:
        description:
            - Specifies the service forwarding mode.
            - "iptables: Traditional kube-proxy uses iptables rules to implement service load balancing.
              In this mode, too many iptables rules will be generated when many services are deployed.
              In addition, non-incremental updates will cause a latency and even obvious performance issues
              in the case of heavy service traffic."
            - "ipvs: Optimized kube-proxy mode with higher throughput and faster speed.
              This mode supports incremental updates and can keep connections uninterrupted during service updates.
              It is suitable for large-sized clusters."
        type: str
        returned: success
    extend_param:
        description:
            - Specifies the extended parameter. 
        type: dict
        returned: success
    enterprise_project_id:
        description:
            - Specifies enterprise project id of the cce cluster.
        type: str
        returned: success
    status:
        description:
            - Specifies the cce cluster status.
        type: str
        returned: success
'''

from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleBase
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleException
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import are_different_dicts
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import navigate_value
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import is_empty_value
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import wait_to_finish


from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcce.v3 import *


class HwcCceCluster(HwcModuleBase):
    def __init__(self):
        self.argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'],
                       type='str'),
            filters=dict(required=True, type='list', elements='str'),
            timeouts=dict(type='dict', options=dict(
                create=dict(default='30m', type='str'),
                delete=dict(default='30m', type='str'),
            ), default=dict()),

            name=dict(type='str', required=True),
            flavor_id=dict(type='str', required=True),
            cluster_version=dict(type='str'),
            cluster_type=dict(default='VirtualMachine', type='str'),
            description=dict(type='str'),
            vpc_id=dict(type='str', required=True),
            subnet_id=dict(type='str', required=True),
            container_network_type=dict(type='str',
                choices=['overlay_l2', 'underlay_ipvlan', 'vpc-router', 'eni'], required=True),
            container_network_cidr=dict(type='str'),
            service_network_cidr=dict(type='str'),
            eni_subnet_id=dict(type='str'),
            eni_subnet_cidr=dict(type='str'),
            authentication_mode=dict(type='str'),
            authenticating_proxy_ca=dict(type='str'),
            multi_az=dict(type='bool'),
            eip=dict(type='str'),
            kube_proxy_mode=dict(type='str'),
            extend_param=dict(type='dict'),
            enterprise_project_id=dict(type='str')
        )

        self.results = dict(
            changed=False,
            state=dict()
        )

        super(HwcCceCluster, self).__init__(self.argument_spec, supports_check_mode=True)

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
            request = ListClustersRequest()
            self.log('list cce cluster request: %s' % request)
            response = self.cce_client.list_clusters(request)
            self.log('list cce cluster response: %s' % response)
        except exceptions.ClientRequestException as e:
            raise HwcModuleException(
                    'search cce cluster failed: %s' % e.error_msg)
        r = navigate_value(response.to_json_object(), ['items'], None)

        if not r:
            return result

        for item in r:
            item = fill_list_resp_body(item)
            self.log('cce cluster identity_obj: %s' % identity_obj)
            self.log('cce cluster item: %s' % item)
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
            request = CreateClusterRequest(request_body)
            self.log('create cce cluster request body: %s' %request)
            response = self.cce_client.create_cluster(request)
            self.log('create cce cluster response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Create cce cluster failed: %s' % e)

        job_id = response.to_json_object()['status']['jobID']

        obj = self.async_wait(job_id, timeout)

        self.module.params['id'] = navigate_value(obj, ["spec", "clusterUID"])

    def read(self):
        try:
            request = ShowClusterRequest(self.module.params['id'])
            self.log('read cce cluster request body: %s' %request)
            response = self.cce_client.show_cluster(request)
            self.log('read cce cluster response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read cce cluster failed: %s' % e)

        r = response.to_json_object()
        res = {}
        res["read"] = fill_read_resp_body(r)

        return res, None

    def update(self, expect_state, current_state):
        self.log('expect_state: %s' % expect_state)
        self.log('current_state: %s' % current_state)

        params = build_update_parameters(expect_state)
        params1 = build_update_parameters(current_state)
        if params and are_different_dicts(params, params1):
            try:
                request = UpdateClusterRequest(self.module.params['id'], body=params)
                self.log('Update cce cluster request body: %s' %request)
                response = self.cce_client.update_cluster(request)
                self.log('Update cce cluster response body: %s' % response)
            except exceptions.ClientRequestException as e:
                self.fail('Update cce cluster failed: %s' % e)


    def delete(self):
        timeout = 60 * int(self.module.params['timeouts']['delete'].rstrip('m'))
        try:
            request = DeleteClusterRequest(self.module.params['id'])
            self.log('delete cce cluster request body: %s' %request)
            response = self.cce_client.delete_cluster(request)
            self.log('delete cce cluster response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Delete cce cluster failed: %s' % e)

        job_id = response.to_json_object()['status']['jobID']

        self.async_wait(job_id, timeout)

    def async_wait(self, job_id, timeout):
        def _query_status():
            r = None
            try:
                request = ShowJobRequest(job_id)
                self.log('show job request body: %s' % request)
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
        "cluster_version": module.params.get("cluster_version"),
        "cluster_type": module.params.get("cluster_type"),
        "description": module.params.get("description"),
        "vpc_id": module.params.get("vpc_id"),
        "subnet_id": module.params.get("subnet_id"),
        "container_network_type": module.params.get("container_network_type"),
        "container_network_cidr": module.params.get("container_network_cidr"),
        "service_network_cidr": module.params.get("service_network_cidr"),
        "eni_subnet_id": module.params.get("eni_subnet_id"),
        "eni_subnet_cidr": module.params.get("eni_subnet_cidr"),
        "authentication_mode": module.params.get("authentication_mode"),
        "authenticating_proxy_ca":
            module.params.get("authenticating_proxy_ca"),
        "multi_az": module.params.get("multi_az"),
        "eip": module.params.get("eip"),
        "kube_proxy_mode": module.params.get("kube_proxy_mode"),
        "extend_param": module.params.get("extend_param"),
        "enterprise_project_id": module.params.get("enterprise_project_id"),
    }


def build_state(opts, response, array_index):
    states = flatten_options(response, array_index)
    return states


def build_create_parameters(opts):
    params = dict()

    params["kind"] = "Cluster"

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

    v = navigate_value(d, ["cluster_type"], array_index)
    if not is_empty_value(v):
        r["type"] = v

    v = navigate_value(d, ["flavor_id"], array_index)
    if not is_empty_value(v):
        r["flavor"] = v

    v = navigate_value(d, ["cluster_version"], array_index)
    if not is_empty_value(v):
        r["version"] = v

    v = navigate_value(d, ["description"], array_index)
    if not is_empty_value(v):
        r["description"] = v

    v = expand_create_host_network(d, None)
    if not is_empty_value(v):
        r["hostNetwork"] = v

    v = expand_create_container_network(d, None)
    if not is_empty_value(v):
        r["containerNetwork"] = v

    v = expand_create_eni_network(d, None)
    if not is_empty_value(v):
        r["eniNetwork"] = v

    v = expand_create_authentication(d, None)
    if not is_empty_value(v):
        r["authentication"] = v

    v = navigate_value(d, ["service_network_cidr"], array_index)
    if not is_empty_value(v):
        r["kubernetesSvcIpRange"] = v

    v = navigate_value(d, ["kube_proxy_mode"], array_index)
    if not is_empty_value(v):
        r["kubeProxyMode"] = v

    v = expand_create_extendparam(d, None)
    if not is_empty_value(v):
        r["extendParam"] = v

    return r


def expand_create_host_network(d, array_index):
    r = dict()

    v = navigate_value(d, ["vpc_id"], array_index)
    if not is_empty_value(v):
        r["vpc"] = v

    v = navigate_value(d, ["subnet_id"], array_index)
    if not is_empty_value(v):
        r["subnet"] = v

    return r


def expand_create_container_network(d, array_index):
    r = dict()

    v = navigate_value(d, ["container_network_type"], array_index)
    if not is_empty_value(v):
        r["mode"] = v

    v = navigate_value(d, ["container_network_cidr"], array_index)
    if not is_empty_value(v):
        r["cidr"] = v

    return r


def expand_create_eni_network(d, array_index):
    r = dict()

    v = navigate_value(d, ["eni_subnet_id"], array_index)
    if not is_empty_value(v):
        r["eniSubnetId"] = v

    v = navigate_value(d, ["eni_subnet_cidr"], array_index)
    if not is_empty_value(v):
        r["eniSubnetCIDR"] = v

    return r


def expand_create_authentication(d, array_index):
    r = dict()

    v = navigate_value(d, ["authentication_mode"], array_index)
    if not is_empty_value(v):
        r["mode"] = v

    v = navigate_value(d, ["authenticating_proxy_ca"], array_index)
    if not is_empty_value(v):
        r["authenticatingProxy"] = {"ca": v}

    return r


def expand_create_extendparam(d, array_index):
    r = dict()

    v = navigate_value(d, ["multi_az"], array_index)
    if v:
        r["clusterAZ"] = "multu_az"

    v = navigate_value(d, ["enterprise_project_id"], array_index)
    if not is_empty_value(v):
        r["enterpriseProjectId"] = v

    v = navigate_value(d, ["eip"], array_index)
    if not is_empty_value(v):
        r["clusterExternalIP"] = v

    v = navigate_value(d, ["extend_param"], array_index)
    if v:
        r.update(v)

    return r


def build_update_parameters(opts):
    params = dict()

    v = navigate_value(opts, ["description"], None)
    if not is_empty_value(v):
        params["description"] = v

    if not params:
        return params

    params = {"spec": params}

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

    result["type"] = value.get("type")
    result["flavor"] = value.get("flavor")
    result["version"] = value.get("version")
    result["description"] = value.get("description")
    result["kubernetesSvcIpRange"] = value.get("kubernetesSvcIpRange")
    result["kubeProxyMode"] = value.get("kubeProxyMode")
    result["extendParam"] = value.get("extendParam")

    v = fill_read_resp_host_network(value.get("hostNetwork"))
    result["hostNetwork"] = v

    v = fill_read_resp_container_network(value.get("containerNetwork"))
    result["containerNetwork"] = v

    v = fill_read_resp_eni_network(value.get("eniNetwork"))
    result["eniNetwork"] = v

    v = fill_read_resp_authentication(value.get("authentication"))
    result["authentication"] = v

    return result


def fill_read_resp_host_network(value):
    if not value:
        return None

    result = dict()

    result["vpc"] = value.get("vpc")

    result["subnet"] = value.get("subnet")

    return result


def fill_read_resp_container_network(value):
    if not value:
        return None

    result = dict()

    result["mode"] = value.get("mode")

    result["cidr"] = value.get("cidr")

    return result


def fill_read_resp_eni_network(value):
    if not value:
        return None

    result = dict()

    result["eniSubnetId"] = value.get("eniSubnetId")

    result["eniSubnetCIDR"] = value.get("eniSubnetCIDR")

    return result


def fill_read_resp_authentication(value):
    if not value:
        return None

    result = dict()

    result["mode"] = value.get("mode")

    result["authenticatingProxy"] = None
    v = value.get("authenticatingProxy")
    if v:
        result["authenticatingProxy"] = {"ca": v.get("ca")}

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

    v = navigate_value(response, ["read", "spec", "type"], array_index)
    r["cluster_type"] = v

    v = navigate_value(response, ["read", "spec", "version"], array_index)
    r["cluster_version"] = v

    v = navigate_value(response, ["read", "spec", "description"], array_index)
    r["description"] = v

    v = navigate_value(response, ["read", "spec", "hostNetwork", "vpc"],
                       array_index)
    r["vpc_id"] = v

    v = navigate_value(response, ["read", "spec", "hostNetwork", "subnet"],
                       array_index)
    r["subnet_id"] = v

    v = navigate_value(response, ["read", "spec", "containerNetwork", "mode"],
                       array_index)
    r["container_network_type"] = v

    v = navigate_value(response, ["read", "spec", "containerNetwork", "cidr"],
                       array_index)
    r["container_network_cidr"] = v

    v = navigate_value(response, ["read", "spec", "kubernetesSvcIpRange"],
                       array_index)
    r["service_network_cidr"] = v

    v = navigate_value(response, ["read", "spec", "eniNetwork", "eniSubnetId"],
                       array_index)
    r["eni_subnet_id"] = v

    v = navigate_value(response, ["read", "spec", "eniNetwork",
                                  "eniSubnetCIDR"], array_index)
    r["eni_subnet_cidr"] = v

    v = navigate_value(response, ["read", "spec", "authentication", "mode"],
                       array_index)
    r["authentication_mode"] = v

    v = navigate_value(response, ["read", "spec", "authentication",
                       "authenticatingProxy"], array_index)
    r["authenticating_proxy_ca"] = v

    v = navigate_value(response, ["read", "spec", "kubeProxyMode"],
                       array_index)
    r["kube_proxy_mode"] = v

    v = navigate_value(response, ["read", "spec", "extendParam"], array_index)
    r["extend_param"] = v

    if v:
        r["multi_az"] = True if v.get("clusterAZ") else False

        r["eip"] = v.get("clusterInternalIP")

        r["enterprise_project_id"] = v.get("enterpriseProjectId")

    v = navigate_value(response, ["read", "status", "phase"])
    r["status"] = v

    return r


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

    v = navigate_value(d, ["cluster_type"], array_index)
    r["type"] = v

    v = navigate_value(d, ["flavor_id"], array_index)
    r["flavor"] = v

    v = navigate_value(d, ["cluster_version"], array_index)
    r["version"] = v

    v = navigate_value(d, ["description"], array_index)
    r["description"] = v

    v = expand_list_host_network(d, None)
    r["hostNetwork"] = v

    v = expand_list_container_network(d, None)
    r["containerNetwork"] = v

    r["eniNetwork"] = None

    v = expand_list_authentication(d, None)
    r["authentication"] = v

    v = navigate_value(d, ["service_network_cidr"], array_index)
    r["kubernetesSvcIpRange"] = v

    v = navigate_value(d, ["kube_proxy_mode"], array_index)
    r["kubeProxyMode"] = v

    r["extendParam"] = None

    return r


def expand_list_host_network(d, array_index):
    r = dict()

    v = navigate_value(d, ["vpc_id"], array_index)
    r["vpc"] = v

    v = navigate_value(d, ["subnet_id"], array_index)
    r["subnet"] = v

    return r


def expand_list_container_network(d, array_index):
    r = dict()

    v = navigate_value(d, ["container_network_type"], array_index)
    r["mode"] = v

    v = navigate_value(d, ["container_network_cidr"], array_index)
    r["cidr"] = v

    return r


def expand_list_eni_network(d, array_index):
    r = dict()

    v = navigate_value(d, ["eni_subnet_id"], array_index)
    r["eniSubnetId"] = v

    v = navigate_value(d, ["eni_subnet_cidr"], array_index)
    r["eniSubnetCIDR"] = v

    return r


def expand_list_authentication(d, array_index):
    r = dict()

    v = navigate_value(d, ["authentication_mode"], array_index)
    r["mode"] = v

    r["authenticatingProxy"] = None
    v = navigate_value(d, ["authenticating_proxy_ca"], array_index)
    if v:
        r["authenticatingProxy"] = {"ca": v}

    return r


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

    result["type"] = value.get("type")
    result["flavor"] = value.get("flavor")
    result["version"] = value.get("version")
    result["description"] = value.get("description")

    v = fill_list_resp_host_network(value.get("hostNetwork"))
    result["hostNetwork"] = v

    v = fill_list_resp_container_network(value.get("containerNetwork"))
    result["containerNetwork"] = v

    v = fill_list_resp_eni_network(value.get("eniNetwork"))
    result["eniNetwork"] = v

    v = fill_list_resp_authentication(value.get("authentication"))
    result["authentication"] = v

    result["extendParam"] = value.get("extendParam")

    result["kubernetesSvcIpRange"] = value.get("kubernetesSvcIpRange")

    result["kubeProxyMode"] = value.get("kubeProxyMode")

    return result


def fill_list_resp_host_network(value):
    if not value:
        return None

    result = dict()

    result["vpc"] = value.get("vpc")

    result["subnet"] = value.get("subnet")

    return result


def fill_list_resp_container_network(value):
    if not value:
        return None

    result = dict()

    result["mode"] = value.get("mode")

    result["cidr"] = value.get("cidr")

    return result


def fill_list_resp_eni_network(value):
    if not value:
        return None

    result = dict()

    result["eniSubnetId"] = value.get("eniSubnetId")

    result["eniSubnetCIDR"] = value.get("eniSubnetCIDR")

    return result


def fill_list_resp_authentication(value):
    if not value:
        return None

    result = dict()

    result["mode"] = value.get("mode")

    result["authenticatingProxy"] = None
    v = value.get("authenticatingProxy")
    if v:
        result["authenticating_proxy"] = {"ca": v.get("ca")}

    return result


def main():
    HwcCceCluster()


if __name__ == '__main__':
    main()
