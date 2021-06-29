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
module: hwc_evs_disk
description:
    - block storage management.
short_description: Creates a resource of Evs/Disk in Huawei Cloud
version_added: '2.9'
author: Huawei Inc. (@huaweicloud)
requirements:
    - keystoneauth1 >= 3.6.0
options:
    state:
        description:
            - Whether the given object should exist in Huawei Cloud.
        choices: ['present', 'absent']
        default: 'present'
    filters:
        description:
            - A list of filters to apply when deciding whether existing
              resources match and should be altered. The item of filters
              is the name of input options.
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
            update:
                description:
                    - The timeouts for update operation.
                type: str
                default: '30m'
            delete:
                description:
                    - The timeouts for delete operation.
                type: str
                default: '30m'
    availability_zone:
        description:
            - Specifies the AZ where you want to create the disk.
        required: true
    name:
        description:
            - Specifies the disk name. The value can contain a maximum of 255
              bytes.
        required: true
    volume_type:
        description:
            - Specifies the disk type. Currently, the value can be SSD, SAS, or
              SATA.
            - SSD: specifies the ultra-high I/O disk type.
            - SAS: specifies the high I/O disk type.
            - SATA: specifies the common I/O disk type.
            - NOTE: If the specified disk type is not available in the AZ, the
              disk will fail to create. If the EVS disk is created from a
              snapshot, the volume_type field must be the same as that of the
              snapshot's source disk.
        required: true
    backup_id:
        description:
            - Specifies the ID of the backup that can be used to create a disk.
              This parameter is mandatory when you use a backup to create the
              disk.
        required: false
    description:
        description:
            - Specifies the disk description. The value can contain a maximum
              of 255 bytes.
        required: false
    enable_full_clone:
        description:
            - If the disk is created from a snapshot and linked cloning needs
              to be used, set this parameter to True.
        type: bool
        required: false
    enable_scsi:
        description:
            - If this parameter is set to True, the disk device type will be
              SCSI, which allows ECS OSs to directly access underlying storage
              media. SCSI reservation command is supported. If this parameter
              is set to False, the disk device type will be VBD, which supports
              only simple SCSI read/write commands.
            - NOTE: If parameter enable_share is set to True and this parameter
              is not specified, shared SCSI disks are created. SCSI EVS disks
              cannot be created from backups, which means that this parameter
              cannot be True if backup_id has been specified.
        type: bool
        required: false
    enable_share:
        description:
            - Specifies whether the disk is shareable. The default value is
              False.
        type: bool
        required: false
    encryption_id:
        description:
            - Specifies the encryption ID. The length of it fixes at 36 bytes.
        required: false
    enterprise_project_id:
        description:
            - Specifies the enterprise project ID. This ID is associated with
              the disk during the disk creation. If it is not specified, the
              disk is bound to the default enterprise project.
        required: false
    image_id:
        description:
            - Specifies the image ID. If this parameter is specified, the disk
              is created from an image. NOTE: BMS system disks cannot be
              created from BMS images.
        required: false
    size:
        description:
            - Specifies the disk size, in GB. Its values are as follows: System
              disk: 1 GB to 1024 GB, Data disk: 10 GB to 32768 GB. This
              parameter is mandatory when you create an empty disk or use an
              image or a snapshot to create a disk. If you use an image or a
              snapshot to create a disk, the disk size must be greater than or
              equal to the image or snapshot size. This parameter is optional
              when you use a backup to create a disk. If this parameter is not
              specified, the disk size is equal to the backup size.
        required: false
    snapshot_id:
        description:
            - Specifies the snapshot ID. If this parameter is specified, the
              disk is created from a snapshot.
        required: false
extends_documentation_fragment: hwc
'''

EXAMPLES = '''
# test create disk
- name: create a disk
  hwc_evs_disk:
    filters:
      - "name"
    availability_zone: "cn-north-1a"
    name: "ansible_evs_disk_test"
    volume_type: "SATA"
    size: 10
'''

RETURN = '''
    availability_zone:
        description:
            - Specifies the AZ where you want to create the disk.
        type: str
        returned: success
    name:
        description:
            - Specifies the disk name. The value can contain a maximum of 255
              bytes.
        type: str
        returned: success
    volume_type:
        description:
            - Specifies the disk type. Currently, the value can be SSD, SAS, or
              SATA.
            - SSD: specifies the ultra-high I/O disk type.
            - SAS: specifies the high I/O disk type.
            - SATA: specifies the common I/O disk type.
            - NOTE: If the specified disk type is not available in the AZ, the
              disk will fail to create. If the EVS disk is created from a
              snapshot, the volume_type field must be the same as that of the
              snapshot's source disk.
        type: str
        returned: success
    backup_id:
        description:
            - Specifies the ID of the backup that can be used to create a disk.
              This parameter is mandatory when you use a backup to create the
              disk.
        type: str
        returned: success
    description:
        description:
            - Specifies the disk description. The value can contain a maximum
              of 255 bytes.
        type: str
        returned: success
    enable_full_clone:
        description:
            - If the disk is created from a snapshot and linked cloning needs
              to be used, set this parameter to True.
        type: bool
        returned: success
    enable_scsi:
        description:
            - If this parameter is set to True, the disk device type will be
              SCSI, which allows ECS OSs to directly access underlying storage
              media. SCSI reservation command is supported. If this parameter
              is set to False, the disk device type will be VBD, which supports
              only simple SCSI read/write commands.
            - NOTE: If parameter enable_share is set to True and this parameter
              is not specified, shared SCSI disks are created. SCSI EVS disks
              cannot be created from backups, which means that this parameter
              cannot be True if backup_id has been specified.
        type: bool
        returned: success
    enable_share:
        description:
            - Specifies whether the disk is shareable. The default value is
              False.
        type: bool
        returned: success
    encryption_id:
        description:
            - Specifies the encryption ID. The length of it fixes at 36 bytes.
        type: str
        returned: success
    enterprise_project_id:
        description:
            - Specifies the enterprise project ID. This ID is associated with
              the disk during the disk creation. If it is not specified, the
              disk is bound to the default enterprise project.
        type: str
        returned: success
    image_id:
        description:
            - Specifies the image ID. If this parameter is specified, the disk
              is created from an image. NOTE: BMS system disks cannot be
              created from BMS images.
        type: str
        returned: success
    size:
        description:
            - Specifies the disk size, in GB. Its values are as follows: System
              disk: 1 GB to 1024 GB, Data disk: 10 GB to 32768 GB. This
              parameter is mandatory when you create an empty disk or use an
              image or a snapshot to create a disk. If you use an image or a
              snapshot to create a disk, the disk size must be greater than or
              equal to the image or snapshot size. This parameter is optional
              when you use a backup to create a disk. If this parameter is not
              specified, the disk size is equal to the backup size.
        type: int
        returned: success
    snapshot_id:
        description:
            - Specifies the snapshot ID. If this parameter is specified, the
              disk is created from a snapshot.
        type: str
        returned: success
    attachments:
        description:
            - Specifies the disk attachment information.
        type: complex
        returned: success
        contains:
            attached_at:
                description:
                    - Specifies the time when the disk was attached. Time
                      format: UTC YYYY-MM-DDTHH:MM:SS.
                type: str
                returned: success
            attachment_id:
                description:
                    - Specifies the ID of the attachment information.
                type: str
                returned: success
            device:
                description:
                    - Specifies the device name.
                type: str
                returned: success
            server_id:
                description:
                    - Specifies the ID of the server to which the disk is
                      attached.
                type: str
                returned: success
    backup_policy_id:
        description:
            - Specifies the backup policy ID.
        type: str
        returned: success
    created_at:
        description:
            - Specifies the time when the disk was created. Time format: UTC
              YYYY-MM-DDTHH:MM:SS.
        type: str
        returned: success
    is_bootable:
        description:
            - Specifies whether the disk is bootable.
        type: bool
        returned: success
    is_readonly:
        description:
            - Specifies whether the disk is read-only or read/write. True:
              indicates that the disk is read-only. False: indicates that the
              disk is read/write.
        type: bool
        returned: success
    source_volume_id:
        description:
            - Specifies the source disk ID. This parameter has a value if the
              disk is created from a source disk.
        type: str
        returned: success
    status:
        description:
            - Specifies the disk status.
        type: str
        returned: success
    tags:
        description:
            - Specifies the disk tags.
        type: dict
        returned: success
'''

from ansible.module_utils.hwc_utils import HwcModuleBase
from ansible.module_utils.hwc_utils import HwcModuleException
from ansible.module_utils.hwc_utils import are_different_dicts
from ansible.module_utils.hwc_utils import navigate_value
from ansible.module_utils.hwc_utils import is_empty_value
from ansible.module_utils.hwc_utils import wait_to_finish

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkevs.v2 import *



class HwcEvsDisk(HwcModuleBase):
    def __init__(self):
        self.argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'],
                       type='str'),
            filters=dict(required=True, type='list', elements='str'),
            timeouts=dict(type='dict', options=dict(
                create=dict(default='30m', type='str'),
                update=dict(default='30m', type='str'),
                delete=dict(default='30m', type='str'),
            ), default=dict()),
            availability_zone=dict(type='str', required=True),
            name=dict(type='str', required=True),
            volume_type=dict(type='str', required=True),
            backup_id=dict(type='str'),
            description=dict(type='str'),
            enable_full_clone=dict(type='bool'),
            enable_scsi=dict(type='bool'),
            enable_share=dict(type='bool'),
            encryption_id=dict(type='str'),
            enterprise_project_id=dict(type='str'),
            image_id=dict(type='str'),
            size=dict(type='int'),
            snapshot_id=dict(type='str')
        )

        self.results = dict(
            changed=False,
            state=dict()
        )

        super(HwcEvsDisk, self).__init__(self.argument_spec, supports_check_mode=True)

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
        marker = ''

        while True:
            try:
                request = ListVolumesRequest(limit=10, marker=marker)
                self.log('list evs disk request: %s' % request)
                response = self.evs_client.list_volumes(request)
                self.log('list evs disk response: %s' % response)
            except exceptions.ClientRequestException as e:
                raise HwcModuleException(
                        'search evs disk failed: %s' % e.error_msg)
            r = navigate_value(response.to_json_object(), ['volumes'], None)

            if not r:
                break

            for item in r:
                item = fill_list_resp_body(item)
                self.log('evs disk identity_obj: %s' % identity_obj)
                self.log('evs disk item: %s' % item)
                if not are_different_dicts(identity_obj, item):
                    result.append(item)

            if len(result) > 1:
                break

            marker = r[-1].get('id')

        return result


    def create(self):
        timeout = 60 * int(self.module.params['timeouts']['create'].rstrip('m'))
        opts = user_input_parameters(self.module)

        try:
            request_body = build_create_parameters(opts)
            request = CreateVolumeRequest(request_body)
            self.log('create evs disk request body: %s' %request)
            response = self.evs_client.create_volume(request)
            self.log('create evs disk response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Create evs disk failed: %s' % e)

        job_id = response.to_json_object()['job_id']

        obj = self.async_wait(job_id, timeout)

        self.module.params['id'] = navigate_value(obj, ["entities", "volume_id"])


    def read(self):
        try:
            request = ShowVolumeRequest(self.module.params['id'])
            self.log('read evs disk request body: %s' %request)
            response = self.evs_client.show_volume(request)
            self.log('read evs disk response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('read evs disk failed: %s' % e)

        r = response.to_json_object()['volume']
        res = {}
        res["read"] = fill_read_resp_body(r)

        return res, None

    def update(self, expect_state, current_state):
        expect_state["current_state"] = current_state
        current_state["current_state"] = current_state
        timeout = 60 * int(self.module.params['timeouts']['update'].rstrip('m'))

        params = build_update_parameters(expect_state)
        params1 = build_update_parameters(current_state)
        if params and are_different_dicts(params, params1):
            try:
                request = UpdateVolumeRequest(self.module.params['id'], params)
                self.log('Update evs disk request body: %s' %request)
                response = self.evs_client.update_volume(request)
                self.log('Update evs disk response body: %s' % response)
            except exceptions.ClientRequestException as e:
                self.fail('Update evs disk failed: %s' % e)

        params = build_extend_disk_parameters(expect_state)
        params1 = build_extend_disk_parameters(current_state)
        if params and are_different_dicts(params, params1):
            try:
                request = ResizeVolumeRequest(self.module.params['id'], params)
                self.log('Resize evs disk request body: %s' %request)
                response = self.evs_client.resize_volume(request)
                self.log('Resize evs disk response body: %s' % response)
            except exceptions.ClientRequestException as e:
                self.fail('Resize evs disk failed: %s' % e)

            job_id = response.to_json_object()['job_id']
            self.async_wait(job_id, timeout)


    def delete(self):
        timeout = 60 * int(self.module.params['timeouts']['delete'].rstrip('m'))

        try:
            request = DeleteVolumeRequest(self.module.params['id'])
            self.log('delete evs disk request body: %s' %request)
            response = self.evs_client.delete_volume(request)
            self.log('delete evs disk response body: %s' % response)
        except exceptions.ClientRequestException as e:
            self.fail('Delete evs disk failed: %s' % e)

        job_id = response.to_json_object()['job_id']

        self.async_wait(job_id, timeout)


    def async_wait(self, job_id, timeout):
        def _query_status():
            r = None
            try:
                request = ShowJobRequest(job_id)
                self.log('show job request body: %s' %request)
                response = self.evs_client.show_job(request)
                self.log('show job response body: %s' % response)
            except exceptions.ClientRequestException as e:
                self.fail('show job failed: %s' % e)

            r = response.to_json_object()

            try:
                s = navigate_value(r, ["status"])
                return r, s
            except Exception:
                return None, ""

        try:
            return wait_to_finish(
                ["SUCCESS"],
                ["RUNNING", "INIT"],
                _query_status, timeout)
        except Exception as ex:
            self.module.fail_json(msg="module(hwc_evs_disk): error "
                                "waiting to be done, error= %s" % str(ex))


def user_input_parameters(module):
    return {
        "availability_zone": module.params.get("availability_zone"),
        "backup_id": module.params.get("backup_id"),
        "description": module.params.get("description"),
        "enable_full_clone": module.params.get("enable_full_clone"),
        "enable_scsi": module.params.get("enable_scsi"),
        "enable_share": module.params.get("enable_share"),
        "encryption_id": module.params.get("encryption_id"),
        "enterprise_project_id": module.params.get("enterprise_project_id"),
        "image_id": module.params.get("image_id"),
        "name": module.params.get("name"),
        "size": module.params.get("size"),
        "snapshot_id": module.params.get("snapshot_id"),
        "volume_type": module.params.get("volume_type"),
    }


def build_state(opts, response, array_index):
    states = flatten_options(response, array_index)
    set_unreadable_options(opts, states)
    return states


def build_create_parameters(opts):
    params = dict()

    v = navigate_value(opts, ["availability_zone"], None)
    if not is_empty_value(v):
        params["availability_zone"] = v

    v = navigate_value(opts, ["backup_id"], None)
    if not is_empty_value(v):
        params["backup_id"] = v

    v = navigate_value(opts, ["description"], None)
    if not is_empty_value(v):
        params["description"] = v

    v = navigate_value(opts, ["enterprise_project_id"], None)
    if not is_empty_value(v):
        params["enterprise_project_id"] = v

    v = navigate_value(opts, ["image_id"], None)
    if not is_empty_value(v):
        params["imageRef"] = v

    v = expand_create_metadata(opts, None)
    if not is_empty_value(v):
        params["metadata"] = v

    v = navigate_value(opts, ["enable_share"], None)
    if not is_empty_value(v):
        params["multiattach"] = v

    v = navigate_value(opts, ["name"], None)
    if not is_empty_value(v):
        params["name"] = v

    v = navigate_value(opts, ["size"], None)
    if not is_empty_value(v):
        params["size"] = v

    v = navigate_value(opts, ["snapshot_id"], None)
    if not is_empty_value(v):
        params["snapshot_id"] = v

    v = navigate_value(opts, ["volume_type"], None)
    if not is_empty_value(v):
        params["volume_type"] = v

    if not params:
        return params

    params = {"volume": params}

    return params


def expand_create_metadata(d, array_index):
    r = dict()

    v = navigate_value(d, ["encryption_id"], array_index)
    if not is_empty_value(v):
        r["__system__cmkid"] = v

    v = expand_create_metadata_system_encrypted(d, array_index)
    if not is_empty_value(v):
        r["__system__encrypted"] = v

    v = expand_create_metadata_full_clone(d, array_index)
    if not is_empty_value(v):
        r["full_clone"] = v

    v = expand_create_metadata_hw_passthrough(d, array_index)
    if not is_empty_value(v):
        r["hw:passthrough"] = v

    return r


def expand_create_metadata_system_encrypted(d, array_index):
    v = navigate_value(d, ["encryption_id"], array_index)
    return "1" if v else ""


def expand_create_metadata_full_clone(d, array_index):
    v = navigate_value(d, ["enable_full_clone"], array_index)
    return "0" if v else ""


def expand_create_metadata_hw_passthrough(d, array_index):
    v = navigate_value(d, ["enable_scsi"], array_index)
    if v is None:
        return v
    return "true" if v else "false"


def build_update_parameters(opts):
    params = dict()

    v = navigate_value(opts, ["description"], None)
    if v is not None:
        params["description"] = v

    v = navigate_value(opts, ["name"], None)
    if not is_empty_value(v):
        params["name"] = v

    if not params:
        return params

    params = {"volume": params}

    return params


def build_extend_disk_parameters(opts):
    params = dict()

    v = expand_extend_disk_os_extend(opts, None)
    if not is_empty_value(v):
        params["os-extend"] = v

    return params


def expand_extend_disk_os_extend(d, array_index):
    r = dict()

    v = navigate_value(d, ["size"], array_index)
    if not is_empty_value(v):
        r["new_size"] = v

    return r


def fill_read_resp_body(body):
    result = dict()

    v = fill_read_resp_attachments(body.get("attachments"))
    result["attachments"] = v

    result["availability_zone"] = body.get("availability_zone")

    result["bootable"] = body.get("bootable")

    result["created_at"] = body.get("created_at")

    result["description"] = body.get("description")

    result["enterprise_project_id"] = body.get("enterprise_project_id")

    result["id"] = body.get("id")

    v = fill_read_resp_metadata(body.get("metadata"))
    result["metadata"] = v

    result["multiattach"] = body.get("multiattach")

    result["name"] = body.get("name")

    result["size"] = body.get("size")

    result["snapshot_id"] = body.get("snapshot_id")

    result["source_volid"] = body.get("source_volid")

    result["status"] = body.get("status")

    result["tags"] = body.get("tags")

    v = fill_read_resp_volume_image_metadata(body.get("volume_image_metadata"))
    result["volume_image_metadata"] = v

    result["volume_type"] = body.get("volume_type")

    return result


def fill_read_resp_attachments(value):
    if not value:
        return None

    result = []
    for item in value:
        val = dict()

        val["attached_at"] = item.get("attached_at")

        val["attachment_id"] = item.get("attachment_id")

        val["device"] = item.get("device")

        val["server_id"] = item.get("server_id")

        result.append(val)

    return result


def fill_read_resp_metadata(value):
    if not value:
        return None

    result = dict()

    result["__system__cmkid"] = value.get("__system__cmkid")

    result["attached_mode"] = value.get("attached_mode")

    result["full_clone"] = value.get("full_clone")

    result["hw:passthrough"] = value.get("hw:passthrough")

    result["policy"] = value.get("policy")

    result["readonly"] = value.get("readonly")

    return result


def fill_read_resp_volume_image_metadata(value):
    if not value:
        return None

    result = dict()

    result["id"] = value.get("id")

    return result


def flatten_options(response, array_index):
    r = dict()

    v = flatten_attachments(response, array_index)
    r["attachments"] = v

    v = navigate_value(response, ["read", "availability_zone"], array_index)
    r["availability_zone"] = v

    v = navigate_value(response, ["read", "metadata", "policy"], array_index)
    r["backup_policy_id"] = v

    v = navigate_value(response, ["read", "created_at"], array_index)
    r["created_at"] = v

    v = navigate_value(response, ["read", "description"], array_index)
    r["description"] = v

    v = flatten_enable_full_clone(response, array_index)
    r["enable_full_clone"] = v

    v = flatten_enable_scsi(response, array_index)
    r["enable_scsi"] = v

    v = navigate_value(response, ["read", "multiattach"], array_index)
    r["enable_share"] = v

    v = navigate_value(
        response, ["read", "metadata", "__system__cmkid"], array_index)
    r["encryption_id"] = v

    v = navigate_value(
        response, ["read", "enterprise_project_id"], array_index)
    r["enterprise_project_id"] = v

    v = navigate_value(
        response, ["read", "volume_image_metadata", "id"], array_index)
    r["image_id"] = v

    v = flatten_is_bootable(response, array_index)
    r["is_bootable"] = v

    v = flatten_is_readonly(response, array_index)
    r["is_readonly"] = v

    v = navigate_value(response, ["read", "name"], array_index)
    r["name"] = v

    v = navigate_value(response, ["read", "size"], array_index)
    r["size"] = v

    v = navigate_value(response, ["read", "snapshot_id"], array_index)
    r["snapshot_id"] = v

    v = navigate_value(response, ["read", "source_volid"], array_index)
    r["source_volume_id"] = v

    v = navigate_value(response, ["read", "status"], array_index)
    r["status"] = v

    v = navigate_value(response, ["read", "tags"], array_index)
    r["tags"] = v

    v = navigate_value(response, ["read", "volume_type"], array_index)
    r["volume_type"] = v

    return r


def flatten_attachments(d, array_index):
    v = navigate_value(d, ["read", "attachments"],
                       array_index)
    if not v:
        return None
    n = len(v)
    result = []

    new_ai = dict()
    if array_index:
        new_ai.update(array_index)

    for i in range(n):
        new_ai["read.attachments"] = i

        val = dict()

        v = navigate_value(d, ["read", "attachments", "attached_at"], new_ai)
        val["attached_at"] = v

        v = navigate_value(d, ["read", "attachments", "attachment_id"], new_ai)
        val["attachment_id"] = v

        v = navigate_value(d, ["read", "attachments", "device"], new_ai)
        val["device"] = v

        v = navigate_value(d, ["read", "attachments", "server_id"], new_ai)
        val["server_id"] = v

        for v in val.values():
            if v is not None:
                result.append(val)
                break

    return result if result else None


def flatten_enable_full_clone(d, array_index):
    v = navigate_value(d, ["read", "metadata", "full_clone"],
                       array_index)
    if v is None:
        return v
    return True if v == "0" else False


def flatten_enable_scsi(d, array_index):
    v = navigate_value(d, ["read", "metadata", "hw:passthrough"],
                       array_index)
    if v is None:
        return v
    return True if v in ["true", "True"] else False


def flatten_is_bootable(d, array_index):
    v = navigate_value(d, ["read", "bootable"], array_index)
    if v is None:
        return v
    return True if v in ["true", "True"] else False


def flatten_is_readonly(d, array_index):
    v = navigate_value(d, ["read", "metadata", "readonly"],
                       array_index)
    if v is None:
        return v
    return True if v in ["true", "True"] else False


def set_unreadable_options(opts, states):
    states["backup_id"] = opts.get("backup_id")


def set_readonly_options(opts, states):
    opts["attachments"] = states.get("attachments")

    opts["backup_policy_id"] = states.get("backup_policy_id")

    opts["created_at"] = states.get("created_at")

    opts["is_bootable"] = states.get("is_bootable")

    opts["is_readonly"] = states.get("is_readonly")

    opts["source_volume_id"] = states.get("source_volume_id")

    opts["status"] = states.get("status")

    opts["tags"] = states.get("tags")


def _build_identity_object(module, all_opts):
    filters = module.params.get("filters")
    opts = dict()
    for k, v in all_opts.items():
        opts[k] = v if k in filters else None

    result = dict()

    result["attachments"] = None

    v = navigate_value(opts, ["availability_zone"], None)
    result["availability_zone"] = v

    result["bootable"] = None

    result["created_at"] = None

    v = navigate_value(opts, ["description"], None)
    result["description"] = v

    v = navigate_value(opts, ["enterprise_project_id"], None)
    result["enterprise_project_id"] = v

    result["id"] = None

    v = expand_list_metadata(opts, None)
    result["metadata"] = v

    v = navigate_value(opts, ["enable_share"], None)
    result["multiattach"] = v

    v = navigate_value(opts, ["name"], None)
    result["name"] = v

    v = navigate_value(opts, ["size"], None)
    result["size"] = v

    v = navigate_value(opts, ["snapshot_id"], None)
    result["snapshot_id"] = v

    result["source_volid"] = None

    result["status"] = None

    result["tags"] = None

    v = expand_list_volume_image_metadata(opts, None)
    result["volume_image_metadata"] = v

    v = navigate_value(opts, ["volume_type"], None)
    result["volume_type"] = v

    return result


def expand_list_metadata(d, array_index):
    r = dict()

    v = navigate_value(d, ["encryption_id"], array_index)
    r["__system__cmkid"] = v

    r["attached_mode"] = None

    v = navigate_value(d, ["enable_full_clone"], array_index)
    r["full_clone"] = v

    v = navigate_value(d, ["enable_scsi"], array_index)
    r["hw:passthrough"] = v

    r["policy"] = None

    r["readonly"] = None

    for v in r.values():
        if v is not None:
            return r
    return None


def expand_list_volume_image_metadata(d, array_index):
    r = dict()

    v = navigate_value(d, ["image_id"], array_index)
    r["id"] = v

    for v in r.values():
        if v is not None:
            return r
    return None


def fill_list_resp_body(body):
    result = dict()

    v = fill_list_resp_attachments(body.get("attachments"))
    result["attachments"] = v

    result["availability_zone"] = body.get("availability_zone")

    result["bootable"] = body.get("bootable")

    result["created_at"] = body.get("created_at")

    result["description"] = body.get("description")

    result["enterprise_project_id"] = body.get("enterprise_project_id")

    result["id"] = body.get("id")

    v = fill_list_resp_metadata(body.get("metadata"))
    result["metadata"] = v

    result["multiattach"] = body.get("multiattach")

    result["name"] = body.get("name")

    result["size"] = body.get("size")

    result["snapshot_id"] = body.get("snapshot_id")

    result["source_volid"] = body.get("source_volid")

    result["status"] = body.get("status")

    result["tags"] = body.get("tags")

    v = fill_list_resp_volume_image_metadata(body.get("volume_image_metadata"))
    result["volume_image_metadata"] = v

    result["volume_type"] = body.get("volume_type")

    return result


def fill_list_resp_attachments(value):
    if not value:
        return None

    result = []
    for item in value:
        val = dict()

        val["attached_at"] = item.get("attached_at")

        val["attachment_id"] = item.get("attachment_id")

        val["device"] = item.get("device")

        val["server_id"] = item.get("server_id")

        result.append(val)

    return result


def fill_list_resp_metadata(value):
    if not value:
        return None

    result = dict()

    result["__system__cmkid"] = value.get("__system__cmkid")

    result["attached_mode"] = value.get("attached_mode")

    result["full_clone"] = value.get("full_clone")

    result["hw:passthrough"] = value.get("hw:passthrough")

    result["policy"] = value.get("policy")

    result["readonly"] = value.get("readonly")

    return result


def fill_list_resp_volume_image_metadata(value):
    if not value:
        return None

    result = dict()

    result["id"] = value.get("id")

    return result


def main():
    HwcEvsDisk()


if __name__ == '__main__':
    main()
