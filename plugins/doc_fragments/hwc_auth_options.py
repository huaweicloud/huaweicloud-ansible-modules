#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Huawei
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

class ModuleDocFragment(object):

    # Huaweicloud doc fragment
    DOCUMENTATION = r'''
    options:
        access_key:
            description:
                - Specifies the access key of the HuaweiCloud to use.
            type: str
            required: true
        secret_key:
            description:
                - Specifies the secret key of the HuaweiCloud to use.
            type: str
            required: true
        project_id:
            description:
                - Specifies the of ID of the project to login with.
            type: str
            required: true
        region:
            description:
                - Specifies the Huawei Cloud region.
            type: str
            required: true
        identity_endpoint:
            description:
                - Specifies the Identity authentication URL.
                  Required if you are using other cloud supported by Huaweicloud.
            type: str
            default: "https://iam.myhuaweicloud.com:443/v3"
            required: false
        cloud:
            description:
                - Specifies the endpoint of the cloud.
                  Required if you are using other cloud supported by Huaweicloud.
            type: str
            default: "myhuaweicloud.com"
            required: false
    notes:
        
        - For authentication, you can set access_key using the `ANSIBLE_HWC_ACCESS_KEY' env variable.
        - For authentication, you can set secret_key using the `ANSIBLE_HWC_SECRET_KEY' env variable.
        - For authentication, you can set project_id using the `ANSIBLE_HWC_PROJECT_ID' env variable.
        - For authentication, you can set region using the `ANSIBLE_HWC_REGION' env variable.
        - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT' env variable.
        - For authentication, you can set cloud using the `ANSIBLE_HWC_CLOUD' env variable.
        - Environment variables values will only be used if the playbook values are not set.
    '''
