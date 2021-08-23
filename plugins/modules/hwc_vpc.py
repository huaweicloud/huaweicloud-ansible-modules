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
module: hwc_vpc
description:
    - Creates and manages a Huawei Cloud VPC.
short_description: Creates a Huawei Cloud VPC
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
    name:
        description:
            - Specifies the name of vpc.
        type: str
        required: true
    cidr:
        description:
            - Specifies the range of available subnets in the vpc.
        type: str
        required: true
    description:
        description:
            - Specifies the description of the vpc.
        type: str
        required: false
    enterprise_project_id:
        description:
            - Specifies the enterprise project id of the vpc.
        type: str
        required: false
    tags:
        description:
            - Specifies the key/value pairs to associate with the vpc.
        type: dict
        required: false
extends_documentation_fragment:
  - hwceco.hwcollection.hwc_auth_options
'''

EXAMPLES = '''
- name: create a vpc
  hwc_vpc:
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
    description:
        description:
            - Specifies the description of the vpc.
        type: str
        returned: success
    enterprise_project_id:
        description:
            - Specifies the enterprise project id of the vpc.
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
        type: dict
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
'''

###############################################################################
# Imports
###############################################################################

from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleBase
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import HwcModuleException
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import are_different_dicts
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import navigate_value
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import is_empty_value
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import build_tags_parameters
from ansible_collections.hwceco.hwcollection.plugins.module_utils.hwc_utils import tags_to_dict

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkvpc.v2 import *


class HwcVpc(HwcModuleBase):
    def __init__(self):
        self.argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            cidr=dict(required=True, type='str'),
            description=dict(type='str'),
            enterprise_project_id=dict(type='str'),
            tags=dict(type='dict')
        )

        self.results = dict(
            changed=False,
            state=dict()
        )

        super(HwcVpc, self).__init__(self.argument_spec, supports_check_mode=True)

    def exec_module(self, **kwargs):

        self.results['check_mode'] = self.check_mode

        try:
            resource = None
            if self.module.params['id']:
                resource = True
            else:
                v = self.search_resource()
                if len(v) > 1:
                    raise Exception('find more than one resources(%s)' % ', '.join([
                                    navigate_value(i, ['id']) for i in v]))

                if len(v) == 1:
                    resource = v[0]
                    self.module.params['id'] = navigate_value(resource, ['id'])

            result = {}
            changed = False
            if self.module.params['state'] == 'present':
                if resource is None:
                    if not self.module.check_mode:
                        self.create()
                    changed = True

                current = self.read()
                self.log('vpc current: %s' % current)
                expect = user_input_parameters(self.module)
                set_readonly_options(expect, current)
                self.log('vpc expect: %s' % expect)
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
                request = ListVpcsRequest(limit=10, marker=marker)
                self.log('list vpc request: %s' % request)
                response = self.vpc_client.list_vpcs(request)
                self.log('list vpc response: %s' % response)
            except exceptions.ClientRequestException as e:
                raise HwcModuleException(
                        'search vpc failed: %s' % e.error_msg)
            r = navigate_value(response.to_json_object(), ['vpcs'], None)

            if not r:
                break

            for item in r:
                item = fill_list_resp_body(item)
                self.log('vpc identity_obj: %s' % identity_obj)
                self.log('vpc item: %s' % item)
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
            request = CreateVpcRequest(request_body)
            self.log('create vpc request body: %s' %request)
            response = self.vpc_client.create_vpc(request)
            self.log('create vpc response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Create vpc failed: %s' % e)

        self.module.params['id'] = response.to_json_object()['vpc']['id']

        # set tags
        if opts['tags']:
            try:
                request_body = build_tags_parameters(opts, 'create')
                request = BatchCreateVpcTagsRequest(self.module.params['id'], request_body)
                self.log('create vpc tags request body: %s' %request)
                response = self.vpc_client.batch_create_vpc_tags(request)
                self.log('create vpc tags response body: %s' %request)
            except exceptions.ClientRequestException as e:
                self.fail('Create vpc tags failed: %s' % e)    

    def read(self):
        try:
            request = ShowVpcRequest(self.module.params['id'])
            self.log('read vpc request body: %s' %request)
            response = self.vpc_client.show_vpc(request)
            self.log('read vpc response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read vpc failed: %s' % e)

        response_attrs = response.to_json_object()['vpc']

        # fetch vpc tags
        try:
            request = ShowVpcTagsRequest(self.module.params['id'])
            self.log('read vpc tags request body: %s' %request)
            response = self.vpc_client.show_vpc_tags(request)
            self.log('read vpc tags response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read vpc tags failed: %s' % e)

        tags_raw = response.to_json_object()['tags']
        if len(tags_raw) > 0:
            tags = tags_to_dict(tags_raw)
            response_attrs['tags'] = tags

        return (response_attrs)

    def update(self, current):
        opts = user_input_parameters(self.module)
        try:
            requset_body = build_update_parameters(opts)
            request = UpdateVpcRequest(self.module.params['id'], requset_body)
            self.log('Update vpc request body: %s' %request)
            response = self.vpc_client.update_vpc(request)
            self.log('Update vpc response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Update vpc failed: %s' % e)

        # update tags
        if opts['tags']:
            if  'tags' not in current.keys():
                try:
                    request_body = build_tags_parameters(opts, 'create')
                    request = BatchCreateVpcTagsRequest(self.module.params['id'], request_body)
                    self.log('create vpc tags request body: %s' %request)
                    response = self.vpc_client.batch_create_vpc_tags(request)
                    self.log('create vpc tags response body: %s' %request)
                except exceptions.ClientRequestException as e:
                    self.fail('Create vpc vpc tags failed: %s' % e)

            elif current['tags'] != opts['tags']:
                try:
                    request_body = build_tags_parameters(current, 'delete')
                    request = BatchDeleteVpcTagsRequest(self.module.params['id'], request_body)
                    self.log('delete vpc tags request body: %s' %request)
                    response = self.vpc_client.batch_delete_vpc_tags(request)
                    self.log('delete vpc tags response body: %s' % response)
                except exceptions.ClientRequestException as e:
                    self.fail('delete vpc tags failed: %s' % e)

                try:
                    request_body = build_tags_parameters(opts, 'create')
                    request = BatchCreateVpcTagsRequest(self.module.params['id'], request_body)
                    self.log('create vpc tags request body: %s' %request)
                    response = self.vpc_client.batch_create_vpc_tags(request)
                    self.log('create vpc tags response body: %s' %request)
                except exceptions.ClientRequestException as e:
                    self.fail('Create vpc tags failed: %s' % e)
        else:
            if  'tags' in current.keys():
                try:
                    request_body = build_tags_parameters(current, 'delete')
                    request = BatchDeleteVpcTagsRequest(self.module.params['id'], request_body)
                    self.log('delete vpc tags request body: %s' %request)
                    response = self.vpc_client.batch_delete_vpc_tags(request)
                    self.log('delete vpc tags response body: %s' % response)
                except exceptions.ClientRequestException as e:
                    self.fail('delete vpc tags failed: %s' % e)

    def delete(self):
        try:
            request = DeleteVpcRequest(self.module.params['id'])
            self.log('delete vpc request body: %s' %request)
            response = self.vpc_client.delete_vpc(request)
            self.log('delete vpc response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Delete vpc failed: %s' % e)

def set_readonly_options(opts, states):
    opts['id'] = states.get('id')

    opts['status'] = states.get('status')

    opts['routes'] = states.get('routes')

    if not opts['enterprise_project_id']:
        opts['enterprise_project_id'] = states.get('enterprise_project_id')
    
    if not opts['tags']:
        opts.pop('tags')

    

def user_input_parameters(module):
    return {
        'name': module.params.get('name'),
        'description': module.params.get('description'),
        'cidr': module.params.get('cidr'),
        'enterprise_project_id': module.params.get('enterprise_project_id'),
        'tags': module.params.get('tags'),
    }

def build_create_parameters(opts):
    params = dict()

    v = navigate_value(opts, ['name'], None)
    if not is_empty_value(v):
        params['name'] = v

    v = navigate_value(opts, ['cidr'], None)
    if not is_empty_value(v):
        params['cidr'] = v

    v = navigate_value(opts, ['description'], None)
    if not is_empty_value(v):
        params['description'] = v

    v = navigate_value(opts, ['enterprise_project_id'], None)
    if not is_empty_value(v):
        params['enterprise_project_id'] = v

    if not params:
        return params

    params = {'vpc': params}

    return params

def build_update_parameters(opts):
    params = dict()

    v = navigate_value(opts, ['name'], None)
    if not is_empty_value(v):
        params['name'] = v

    v = navigate_value(opts, ['cidr'], None)
    if not is_empty_value(v):
        params['cidr'] = v

    v = navigate_value(opts, ['description'], None)
    if not is_empty_value(v):
        params['description'] = v

    if not params:
        return params

    params = {'vpc': params}

    return params


def fill_list_resp_body(body):
    result = dict()

    result['name'] = body.get('name')

    result['cidr'] = body.get('cidr')

    result['description'] = body.get('description')

    result['enterprise_project_id'] = body.get('enterprise_project_id')

    result['id'] = body.get('id')

    result['status'] = body.get('status')

    tags_raw = body.get('tags')
    if tags_raw:
        result['tags'] = tags_to_dict(tags_raw)

    return result

def _build_identity_object(module, opts):

    result = dict()

    v = navigate_value(opts, ['name'], None)
    result['name'] = v

    v = navigate_value(opts, ['cidr'], None)
    result['cidr'] = v

    v = navigate_value(opts, ['description'], None)
    result['description'] = v

    v = navigate_value(opts, ['enterprise_project_id'], None)
    result['enterprise_project_id'] = v

    result['id'] = None

    result['status'] = None

    return result

def main():
    HwcVpc()

if __name__ == '__main__':
    main()
