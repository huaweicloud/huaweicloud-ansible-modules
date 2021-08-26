.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.hwceco.hwcollection.hwc_ecs_instance_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

hwceco.hwcollection.hwc_ecs_instance -- Creates a resource of Ecs/Instance in Huawei Cloud
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `hwceco.hwcollection collection <https://galaxy.ansible.com/hwceco/hwcollection>`_ (version 1.0.5).

    To install it use: :code:`ansible-galaxy collection install hwceco.hwcollection`.

    To use it in a playbook, specify: :code:`hwceco.hwcollection.hwc_ecs_instance`.

.. version_added

.. versionadded:: 1.0.0 of hwceco.hwcollection

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates and manages a resource of Ecs/Instance in Huawei Cloud


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- huaweicloudsdkcore >= 3.0.47
- huaweicloudsdkecs >= 3.0.47


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
                    <div class="ansibleOptionAnchor" id="parameter-admin_pass"></div>
                    <b>admin_pass</b>
                    <a class="ansibleOptionLink" href="#parameter-admin_pass" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the initial login password of the administrator account for logging in to an ECS using password authentication. The Linux administrator is root, and the Windows administrator is Administrator. Password complexity requirements, consists of 8 to 26 characters. The password must contain at least three of the following character types &quot;uppercase letters, lowercase letters, digits, and special characters (!@$%^-_=+[{}]:,./?)&quot;. The password cannot contain the username or the username in reverse. The Windows ECS password cannot contain the username, the username in reverse, or more than two consecutive characters in the username.</div>
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
                                            <div>Specifies the name of the AZ where the ECS is located.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-data_volumes"></div>
                    <b>data_volumes</b>
                    <a class="ansibleOptionLink" href="#parameter-data_volumes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the data disks of ECS instance.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_volumes/device"></div>
                    <b>device</b>
                    <a class="ansibleOptionLink" href="#parameter-data_volumes/device" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the disk device name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_volumes/volume_id"></div>
                    <b>volume_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_volumes/volume_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the disk ID.</div>
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
                                            <div>Specifies the description of an ECS, which is a null string by default. Can contain a maximum of 85 characters. Cannot contain special characters, such as &lt; and &gt;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-eip_id"></div>
                    <b>eip_id</b>
                    <a class="ansibleOptionLink" href="#parameter-eip_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ID of the elastic IP address assigned to the ECS. Only elastic IP addresses in the DOWN state can be assigned.</div>
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
                                            <div>Specifies the ID of the enterprise project to which the ECS belongs.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-filters"></div>
                    <b>filters</b>
                    <a class="ansibleOptionLink" href="#parameter-filters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of filters to apply when deciding whether existing resources match and should be altered. The item of filters is the name of input options.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-flavor_name"></div>
                    <b>flavor_name</b>
                    <a class="ansibleOptionLink" href="#parameter-flavor_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the name of the system flavor.</div>
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
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ID of the system image.</div>
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
                                            <div>Specifies the ECS name. Value requirements: Consists of 1 to 64 characters, including letters, digits, underscores <code>_</code>, hyphens (-), periods (.).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-nics"></div>
                    <b>nics</b>
                    <a class="ansibleOptionLink" href="#parameter-nics" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the NIC information of the ECS. Constraints the network of the NIC must belong to the VPC specified by vpc_id. A maximum of 12 NICs can be attached to an ECS.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-nics/ip_address"></div>
                    <b>ip_address</b>
                    <a class="ansibleOptionLink" href="#parameter-nics/ip_address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the IP address of the NIC. The value is an IPv4 address. Its value must be an unused IP address in the network segment of the subnet.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-nics/subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#parameter-nics/subnet_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ID of subnet.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-root_volume"></div>
                    <b>root_volume</b>
                    <a class="ansibleOptionLink" href="#parameter-root_volume" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the configuration of the ECS&#x27;s system disks.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-root_volume/size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-root_volume/size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the system disk size, in GB. The value range is 1 to 1024. The system disk size must be greater than or equal to the minimum system disk size supported by the image (min_disk attribute of the image). If this parameter is not specified or is set to 0, the default system disk size is the minimum value of the system disk in the image (min_disk attribute of the image).</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-root_volume/snapshot_id"></div>
                    <b>snapshot_id</b>
                    <a class="ansibleOptionLink" href="#parameter-root_volume/snapshot_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the snapshot ID or ID of the original data disk contained in the full-ECS image.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-root_volume/volume_type"></div>
                    <b>volume_type</b>
                    <a class="ansibleOptionLink" href="#parameter-root_volume/volume_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ECS system disk type.</div>
                                            <div>SATA is common I/O disk type.</div>
                                            <div>SAS is high I/O disk type.</div>
                                            <div>SSD is ultra-high I/O disk type.</div>
                                            <div>co-p1 is high I/O (performance-optimized I) disk type.</div>
                                            <div>uh-l1 is ultra-high I/O (latency-optimized) disk type.</div>
                                            <div>NOTE is For HANA, HL1, and HL2 ECSs, use co-p1 and uh-l1 disks. For other ECSs, do not use co-p1 or uh-l1 disks.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-security_groups"></div>
                    <b>security_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-security_groups" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the security groups of the ECS. If this parameter is left blank, the default security group is bound to the ECS by default.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-server_metadata"></div>
                    <b>server_metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-server_metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the metadata of ECS to be created.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-server_tags"></div>
                    <b>server_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-server_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the tags of an ECS. When you create ECSs, one ECS supports up to 10 tags.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssh_key_name"></div>
                    <b>ssh_key_name</b>
                    <a class="ansibleOptionLink" href="#parameter-ssh_key_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the name of the SSH key used for logging in to the ECS.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-user_data"></div>
                    <b>user_data</b>
                    <a class="ansibleOptionLink" href="#parameter-user_data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the user data to be injected during the ECS creation process. Text, text files, and gzip files can be injected. The content to be injected must be encoded with base64. The maximum size of the content to be injected (before encoding) is 32 KB. For Linux ECSs, this parameter does not take effect when adminPass is used. Examples are provided as follows &#x27;Linux #! /bin/bash echo user_test &amp;gt;&amp;gt; /home/user.txt Windows rem cmd echo 111 &amp;gt; c:aa.tx.&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-vpc_id"></div>
                    <b>vpc_id</b>
                    <a class="ansibleOptionLink" href="#parameter-vpc_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ID of the VPC to which the ECS belongs.</div>
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

    
    # create an ecs instance
    - name: create a vpc
      hwc_network_vpc:
        cidr: "192.168.100.0/24"
        name: "ansible_network_vpc_test"
      register: vpc
    - name: create a subnet
      hwc_vpc_subnet:
        gateway_ip: "192.168.100.32"
        name: "ansible_network_subnet_test"
        dhcp_enable: true
        vpc_id: "{{ vpc.state.id }}"
        filters:
          - "name"
        cidr: "192.168.100.0/26"
      register: subnet
    - name: create a eip
      hwc_vpc_eip:
        dedicated_bandwidth:
          charge_mode: "traffic"
          name: "ansible_test_dedicated_bandwidth"
          size: 1
        type: "5_bgp"
        filters:
          - "type"
          - "dedicated_bandwidth"
      register: eip
    - name: create a disk
      hwc_evs_disk:
        filters:
          - "name"
        availability_zone: "cn-north-1a"
        name: "ansible_evs_disk_test"
        volume_type: "SATA"
        size: 10
      register: disk
    - name: create an instance
      hwc_ecs_instance:
        data_volumes:
          - volume_id: "{{ disk.state.id }}"
        eip_id: "{{ eip.state.id }}"
        name: "ansible_ecs_instance_test"
        availability_zone: "cn-north-1a"
        nics:
          - subnet_id: "{{ subnet.state.id }}"
            ip_address: "192.168.100.33"
          - subnet_id: "{{ subnet.state.id }}"
            ip_address: "192.168.100.34"
        server_tags:
          my_server: "my_server"
        image_id: "8da46d6d-6079-4e31-ad6d-a7167efff892"
        flavor_name: "s3.small.1"
        filters:
          - "name"
        vpc_id: "{{ vpc.state.id }}"
        root_volume:
          volume_type: "SAS"




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
                    <div class="ansibleOptionAnchor" id="return-admin_pass"></div>
                    <b>admin_pass</b>
                    <a class="ansibleOptionLink" href="#return-admin_pass" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the initial login password of the administrator account for logging in to an ECS using password authentication. The Linux administrator is root, and the Windows administrator is Administrator. Password complexity requirements consists of 8 to 26 characters. The password must contain at least three of the following character types &quot;uppercase letters, lowercase letters, digits, and special characters (!@$%^-_=+[{}]:,./?)&quot;. The password cannot contain the username or the username in reverse. The Windows ECS password cannot contain the username, the username in reverse, or more than two consecutive characters in the username.</div>
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
                                            <div>Specifies the name of the AZ where the ECS is located.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-config_drive"></div>
                    <b>config_drive</b>
                    <a class="ansibleOptionLink" href="#return-config_drive" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the configuration driver.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-created"></div>
                    <b>created</b>
                    <a class="ansibleOptionLink" href="#return-created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the time when an ECS was created.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-data_volumes"></div>
                    <b>data_volumes</b>
                    <a class="ansibleOptionLink" href="#return-data_volumes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the data disks of ECS instance.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-data_volumes/device"></div>
                    <b>device</b>
                    <a class="ansibleOptionLink" href="#return-data_volumes/device" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk device name.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-data_volumes/volume_id"></div>
                    <b>volume_id</b>
                    <a class="ansibleOptionLink" href="#return-data_volumes/volume_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk ID.</div>
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
                                            <div>Specifies the description of an ECS, which is a null string by default. Can contain a maximum of 85 characters. Cannot contain special characters, such as &lt; and &gt;.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-disk_config_type"></div>
                    <b>disk_config_type</b>
                    <a class="ansibleOptionLink" href="#return-disk_config_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk configuration type. MANUAL is The image space is not expanded. AUTO is the image space of the system disk will be expanded to be as same as the flavor.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-eip_id"></div>
                    <b>eip_id</b>
                    <a class="ansibleOptionLink" href="#return-eip_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the elastic IP address assigned to the ECS. Only elastic IP addresses in the DOWN state can be assigned.</div>
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
                                            <div>Specifies the ID of the enterprise project to which the ECS belongs.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-flavor_name"></div>
                    <b>flavor_name</b>
                    <a class="ansibleOptionLink" href="#return-flavor_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the name of the system flavor.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-host_name"></div>
                    <b>host_name</b>
                    <a class="ansibleOptionLink" href="#return-host_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the host name of the ECS.</div>
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
                                            <div>Specifies the ID of the system image.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-image_name"></div>
                    <b>image_name</b>
                    <a class="ansibleOptionLink" href="#return-image_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the image name of the ECS.</div>
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
                                            <div>Specifies the ECS name. Value requirements &quot;Consists of 1 to 64 characters, including letters, digits, underscores <code>_</code>, hyphens (-), periods (.)&quot;.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-nics"></div>
                    <b>nics</b>
                    <a class="ansibleOptionLink" href="#return-nics" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the NIC information of the ECS. The network of the NIC must belong to the VPC specified by vpc_id. A maximum of 12 NICs can be attached to an ECS.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-nics/ip_address"></div>
                    <b>ip_address</b>
                    <a class="ansibleOptionLink" href="#return-nics/ip_address" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the IP address of the NIC. The value is an IPv4 address. Its value must be an unused IP address in the network segment of the subnet.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-nics/port_id"></div>
                    <b>port_id</b>
                    <a class="ansibleOptionLink" href="#return-nics/port_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the port ID corresponding to the IP address.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-nics/subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#return-nics/subnet_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of subnet.</div>
                                        <br/>
                                    </td>
            </tr>
                    
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-power_state"></div>
                    <b>power_state</b>
                    <a class="ansibleOptionLink" href="#return-power_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the power status of the ECS.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-root_volume"></div>
                    <b>root_volume</b>
                    <a class="ansibleOptionLink" href="#return-root_volume" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the configuration of the ECS&#x27;s system disks.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-root_volume/device"></div>
                    <b>device</b>
                    <a class="ansibleOptionLink" href="#return-root_volume/device" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk device name.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-root_volume/size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#return-root_volume/size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the system disk size, in GB. The value range is 1 to 1024. The system disk size must be greater than or equal to the minimum system disk size supported by the image (min_disk attribute of the image). If this parameter is not specified or is set to 0, the default system disk size is the minimum value of the system disk in the image (min_disk attribute of the image).</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-root_volume/snapshot_id"></div>
                    <b>snapshot_id</b>
                    <a class="ansibleOptionLink" href="#return-root_volume/snapshot_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the snapshot ID or ID of the original data disk contained in the full-ECS image.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-root_volume/volume_id"></div>
                    <b>volume_id</b>
                    <a class="ansibleOptionLink" href="#return-root_volume/volume_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk ID.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-root_volume/volume_type"></div>
                    <b>volume_type</b>
                    <a class="ansibleOptionLink" href="#return-root_volume/volume_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ECS system disk type.</div>
                                            <div>SATA is common I/O disk type.</div>
                                            <div>SAS is high I/O disk type.</div>
                                            <div>SSD is ultra-high I/O disk type.</div>
                                            <div>co-p1 is high I/O (performance-optimized I) disk type.</div>
                                            <div>uh-l1 is ultra-high I/O (latency-optimized) disk type.</div>
                                            <div>NOTE is For HANA, HL1, and HL2 ECSs, use co-p1 and uh-l1 disks. For other ECSs, do not use co-p1 or uh-l1 disks.</div>
                                        <br/>
                                    </td>
            </tr>
                    
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-security_groups"></div>
                    <b>security_groups</b>
                    <a class="ansibleOptionLink" href="#return-security_groups" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the security groups of the ECS. If this parameter is left blank, the default security group is bound to the ECS by default.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-server_alias"></div>
                    <b>server_alias</b>
                    <a class="ansibleOptionLink" href="#return-server_alias" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ECS alias.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-server_metadata"></div>
                    <b>server_metadata</b>
                    <a class="ansibleOptionLink" href="#return-server_metadata" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the metadata of ECS to be created.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-server_tags"></div>
                    <b>server_tags</b>
                    <a class="ansibleOptionLink" href="#return-server_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the tags of an ECS. When you create ECSs, one ECS supports up to 10 tags.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ssh_key_name"></div>
                    <b>ssh_key_name</b>
                    <a class="ansibleOptionLink" href="#return-ssh_key_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the name of the SSH key used for logging in to the ECS.</div>
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
                                            <div>Specifies the ECS status. Options are ACTIVE, REBOOT, HARD_REBOOT, REBUILD, MIGRATING, BUILD, SHUTOFF, RESIZE, VERIFY_RESIZE, ERROR, and DELETED.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-user_data"></div>
                    <b>user_data</b>
                    <a class="ansibleOptionLink" href="#return-user_data" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the user data to be injected during the ECS creation process. Text, text files, and gzip files can be injected. The content to be injected must be encoded with base64. The maximum size of the content to be injected (before encoding) is 32 KB. For Linux ECSs, this parameter does not take effect when adminPass is used. Examples are provided as follows &#x27;Linux #! /bin/bash echo user_test &amp;gt;&amp;gt; /home/user.txt Windows rem cmd echo 111 &amp;gt; c:aa.tx&#x27;.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-vpc_id"></div>
                    <b>vpc_id</b>
                    <a class="ansibleOptionLink" href="#return-vpc_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the VPC to which the ECS belongs.</div>
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

