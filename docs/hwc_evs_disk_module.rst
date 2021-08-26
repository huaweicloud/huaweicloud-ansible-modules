.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.hwceco.hwcollection.hwc_evs_disk_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

hwceco.hwcollection.hwc_evs_disk -- Creates a resource of Evs/Disk in Huawei Cloud
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `hwceco.hwcollection collection <https://galaxy.ansible.com/hwceco/hwcollection>`_ (version 1.0.5).

    To install it use: :code:`ansible-galaxy collection install hwceco.hwcollection`.

    To use it in a playbook, specify: :code:`hwceco.hwcollection.hwc_evs_disk`.

.. version_added

.. versionadded:: 1.0.0 of hwceco.hwcollection

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates and manages a resource of Evs/Disk in Huawei Cloud.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- huaweicloudsdkcore >= 3.0.47
- huaweicloudsdkevs >= 3.0.47


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-access_key"></div>
                    <b>access_key</b>
                    <a class="ansibleOptionLink" href="#parameter-access_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the access key of the HuaweiCloud to use.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-availability_zone"></div>
                    <b>availability_zone</b>
                    <a class="ansibleOptionLink" href="#parameter-availability_zone" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the AZ where you want to create the disk.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-backup_id"></div>
                    <b>backup_id</b>
                    <a class="ansibleOptionLink" href="#parameter-backup_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ID of the backup that can be used to create a disk. This parameter is mandatory when you use a backup to create the disk.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-cloud"></div>
                    <b>cloud</b>
                    <a class="ansibleOptionLink" href="#parameter-cloud" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"myhuaweicloud.com"</div>
                                    </td>
                                                                <td>
                                            <div>Specifies the endpoint of the cloud. Required if you are using other cloud supported by Huaweicloud.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the disk description. The value can contain a maximum of 255 bytes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enable_full_clone"></div>
                    <b>enable_full_clone</b>
                    <a class="ansibleOptionLink" href="#parameter-enable_full_clone" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If the disk is created from a snapshot and linked cloning needs to be used, set this parameter to True.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enable_scsi"></div>
                    <b>enable_scsi</b>
                    <a class="ansibleOptionLink" href="#parameter-enable_scsi" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If this parameter is set to True, the disk device type will be SCSI, which allows ECS OSs to directly access underlying storage media. SCSI reservation command is supported. If this parameter is set to False, the disk device type will be VBD, which supports only simple SCSI read/write commands.</div>
                                            <div>NOTE: If parameter enable_share is set to True and this parameter is not specified, shared SCSI disks are created. SCSI EVS disks cannot be created from backups, which means that this parameter cannot be True if backup_id has been specified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enable_share"></div>
                    <b>enable_share</b>
                    <a class="ansibleOptionLink" href="#parameter-enable_share" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the disk is shareable. The default value is False.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-encryption_id"></div>
                    <b>encryption_id</b>
                    <a class="ansibleOptionLink" href="#parameter-encryption_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the encryption ID. The length of it fixes at 36 bytes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enterprise_project_id"></div>
                    <b>enterprise_project_id</b>
                    <a class="ansibleOptionLink" href="#parameter-enterprise_project_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the enterprise project ID. This ID is associated with the disk during the disk creation. If it is not specified, the disk is bound to the default enterprise project.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-filters"></div>
                    <b>filters</b>
                    <a class="ansibleOptionLink" href="#parameter-filters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of filters to apply when deciding whether existing resources match and should be altered. The item of filters is the name of input options.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-identity_endpoint"></div>
                    <b>identity_endpoint</b>
                    <a class="ansibleOptionLink" href="#parameter-identity_endpoint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"https://iam.myhuaweicloud.com:443/v3"</div>
                                    </td>
                                                                <td>
                                            <div>Specifies the Identity authentication URL. Required if you are using other cloud supported by Huaweicloud.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#parameter-image_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the image ID. If this parameter is specified, the disk is created from an image.</div>
                                            <div>NOTE: BMS system disks cannot be created from BMS images.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the disk name. The value can contain a maximum of 255 bytes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-project_id"></div>
                    <b>project_id</b>
                    <a class="ansibleOptionLink" href="#parameter-project_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the of ID of the project to login with.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#parameter-region" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the Huawei Cloud region.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secret_key"></div>
                    <b>secret_key</b>
                    <a class="ansibleOptionLink" href="#parameter-secret_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the secret key of the HuaweiCloud to use.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the disk size, in GB. Its values are as follows: System disk: 1 GB to 1024 GB, Data disk: 10 GB to 32768 GB. This parameter is mandatory when you create an empty disk or use an image or a snapshot to create a disk. If you use an image or a snapshot to create a disk, the disk size must be greater than or equal to the image or snapshot size. This parameter is optional when you use a backup to create a disk. If this parameter is not specified, the disk size is equal to the backup size.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-snapshot_id"></div>
                    <b>snapshot_id</b>
                    <a class="ansibleOptionLink" href="#parameter-snapshot_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the snapshot ID. If this parameter is specified, the disk is created from a snapshot.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the given object should exist in Huawei Cloud.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-timeouts"></div>
                    <b>timeouts</b>
                    <a class="ansibleOptionLink" href="#parameter-timeouts" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The timeouts for each operations.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-timeouts/create"></div>
                    <b>create</b>
                    <a class="ansibleOptionLink" href="#parameter-timeouts/create" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"30m"</div>
                                    </td>
                                                                <td>
                                            <div>The timeouts for create operation.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-timeouts/delete"></div>
                    <b>delete</b>
                    <a class="ansibleOptionLink" href="#parameter-timeouts/delete" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"30m"</div>
                                    </td>
                                                                <td>
                                            <div>The timeouts for delete operation.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-timeouts/update"></div>
                    <b>update</b>
                    <a class="ansibleOptionLink" href="#parameter-timeouts/update" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"30m"</div>
                                    </td>
                                                                <td>
                                            <div>The timeouts for update operation.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-volume_type"></div>
                    <b>volume_type</b>
                    <a class="ansibleOptionLink" href="#parameter-volume_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the disk type. Currently, the value can be SSD, SAS, or SATA.</div>
                                            <div>SSD: specifies the ultra-high I/O disk type.</div>
                                            <div>SAS: specifies the high I/O disk type.</div>
                                            <div>SATA: specifies the common I/O disk type.</div>
                                            <div>NOTE: If the specified disk type is not available in the AZ, the disk will fail to create. If the EVS disk is created from a snapshot, the volume_type field must be the same as that of the snapshot&#x27;s source disk.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes

Notes
-----

.. note::
   - For authentication, you can set access_key using the `ANSIBLE_HWC_ACCESS_KEY' env variable.
   - For authentication, you can set secret_key using the `ANSIBLE_HWC_SECRET_KEY' env variable.
   - For authentication, you can set project_id using the `ANSIBLE_HWC_PROJECT_ID' env variable.
   - For authentication, you can set region using the `ANSIBLE_HWC_REGION' env variable.
   - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT' env variable.
   - For authentication, you can set cloud using the `ANSIBLE_HWC_CLOUD' env variable.
   - Environment variables values will only be used if the playbook values are not set.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    # test create disk
    - name: create a disk
      hwc_evs_disk:
        filters:
          - "name"
        availability_zone: "cn-north-1a"
        name: "ansible_evs_disk_test"
        volume_type: "SATA"
        size: 10




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-attachments"></div>
                    <b>attachments</b>
                    <a class="ansibleOptionLink" href="#return-attachments" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk attachment information.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-attachments/attached_at"></div>
                    <b>attached_at</b>
                    <a class="ansibleOptionLink" href="#return-attachments/attached_at" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the time when the disk was attached. Time format: UTC YYYY-MM-DDTHH:MM:SS.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-attachments/attachment_id"></div>
                    <b>attachment_id</b>
                    <a class="ansibleOptionLink" href="#return-attachments/attachment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the attachment information.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-attachments/device"></div>
                    <b>device</b>
                    <a class="ansibleOptionLink" href="#return-attachments/device" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the device name.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-attachments/server_id"></div>
                    <b>server_id</b>
                    <a class="ansibleOptionLink" href="#return-attachments/server_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the server to which the disk is attached.</div>
                                        <br/>
                                    </td>
            </tr>
                    
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-availability_zone"></div>
                    <b>availability_zone</b>
                    <a class="ansibleOptionLink" href="#return-availability_zone" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the AZ where you want to create the disk.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-backup_id"></div>
                    <b>backup_id</b>
                    <a class="ansibleOptionLink" href="#return-backup_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the backup that can be used to create a disk. This parameter is mandatory when you use a backup to create the disk.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-backup_policy_id"></div>
                    <b>backup_policy_id</b>
                    <a class="ansibleOptionLink" href="#return-backup_policy_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the backup policy ID.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-created_at"></div>
                    <b>created_at</b>
                    <a class="ansibleOptionLink" href="#return-created_at" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the time when the disk was created. Time format: UTC YYYY-MM-DDTHH:MM:SS.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk description. The value can contain a maximum of 255 bytes.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-enable_full_clone"></div>
                    <b>enable_full_clone</b>
                    <a class="ansibleOptionLink" href="#return-enable_full_clone" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>If the disk is created from a snapshot and linked cloning needs to be used, set this parameter to True.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-enable_scsi"></div>
                    <b>enable_scsi</b>
                    <a class="ansibleOptionLink" href="#return-enable_scsi" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>If this parameter is set to True, the disk device type will be SCSI, which allows ECS OSs to directly access underlying storage media. SCSI reservation command is supported. If this parameter is set to False, the disk device type will be VBD, which supports only simple SCSI read/write commands.</div>
                                            <div>NOTE: If parameter enable_share is set to True and this parameter is not specified, shared SCSI disks are created. SCSI EVS disks cannot be created from backups, which means that this parameter cannot be True if backup_id has been specified.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-enable_share"></div>
                    <b>enable_share</b>
                    <a class="ansibleOptionLink" href="#return-enable_share" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies whether the disk is shareable. The default value is False.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-encryption_id"></div>
                    <b>encryption_id</b>
                    <a class="ansibleOptionLink" href="#return-encryption_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the encryption ID. The length of it fixes at 36 bytes.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-enterprise_project_id"></div>
                    <b>enterprise_project_id</b>
                    <a class="ansibleOptionLink" href="#return-enterprise_project_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the enterprise project ID. This ID is associated with the disk during the disk creation. If it is not specified, the disk is bound to the default enterprise project.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#return-image_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the image ID. If this parameter is specified, the disk is created from an image. NOTE: BMS system disks cannot be created from BMS images.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-is_bootable"></div>
                    <b>is_bootable</b>
                    <a class="ansibleOptionLink" href="#return-is_bootable" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies whether the disk is bootable.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-is_readonly"></div>
                    <b>is_readonly</b>
                    <a class="ansibleOptionLink" href="#return-is_readonly" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies whether the disk is read-only or read/write. True: indicates that the disk is read-only. False: indicates that the disk is read/write.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk name. The value can contain a maximum of 255 bytes.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#return-size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk size, in GB. Its values are as follows: System disk: 1 GB to 1024 GB, Data disk: 10 GB to 32768 GB. This parameter is mandatory when you create an empty disk or use an image or a snapshot to create a disk. If you use an image or a snapshot to create a disk, the disk size must be greater than or equal to the image or snapshot size. This parameter is optional when you use a backup to create a disk. If this parameter is not specified, the disk size is equal to the backup size.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-snapshot_id"></div>
                    <b>snapshot_id</b>
                    <a class="ansibleOptionLink" href="#return-snapshot_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the snapshot ID. If this parameter is specified, the disk is created from a snapshot.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-source_volume_id"></div>
                    <b>source_volume_id</b>
                    <a class="ansibleOptionLink" href="#return-source_volume_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the source disk ID. This parameter has a value if the disk is created from a source disk.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#return-status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk status.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-tags"></div>
                    <b>tags</b>
                    <a class="ansibleOptionLink" href="#return-tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk tags.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-volume_type"></div>
                    <b>volume_type</b>
                    <a class="ansibleOptionLink" href="#return-volume_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk type. Currently, the value can be SSD, SAS, or SATA.</div>
                                            <div>SSD: specifies the ultra-high I/O disk type.</div>
                                            <div>SAS: specifies the high I/O disk type.</div>
                                            <div>SATA: specifies the common I/O disk type.</div>
                                            <div>NOTE: If the specified disk type is not available in the AZ, the disk will fail to create. If the EVS disk is created from a snapshot, the volume_type field must be the same as that of the snapshot&#x27;s source disk.</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Huawei (@huaweicloud)



.. Parsing errors

