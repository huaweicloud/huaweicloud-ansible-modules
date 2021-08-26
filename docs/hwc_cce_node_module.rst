.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.hwceco.hwcollection.hwc_cce_node_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

hwceco.hwcollection.hwc_cce_node -- Creates a resource of CCE/Node in Huawei Cloud
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `hwceco.hwcollection collection <https://galaxy.ansible.com/hwceco/hwcollection>`_ (version 1.0.5).

    To install it use: :code:`ansible-galaxy collection install hwceco.hwcollection`.

    To use it in a playbook, specify: :code:`hwceco.hwcollection.hwc_cce_node`.

.. version_added

.. versionadded:: 1.0.0 of hwceco.hwcollection

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates and manages a resource of CCE/Node in Huawei Cloud


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- huaweicloudsdkcore >= 3.0.47
- huaweicloudsdkcce >= 3.0.47


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
                                            <div>Specifies the name of the AZ where the node is located.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-cluster_id"></div>
                    <b>cluster_id</b>
                    <a class="ansibleOptionLink" href="#parameter-cluster_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ID of the cluster to which the node belongs.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_volumes"></div>
                    <b>data_volumes</b>
                    <a class="ansibleOptionLink" href="#parameter-data_volumes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the data disks of the node.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_volumes/size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-data_volumes/size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the system disk size, in GB. The value range is 100 to 32768.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_volumes/volume_type"></div>
                    <b>volume_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_volumes/volume_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the disk type.</div>
                                            <div>SATA is common I/O disk type.</div>
                                            <div>SAS is high I/O disk type.</div>
                                            <div>SSD is ultra-high I/O disk type.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ecs_group_id"></div>
                    <b>ecs_group_id</b>
                    <a class="ansibleOptionLink" href="#parameter-ecs_group_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ecs group id. If specified, the node will be created under the cloud server group.</div>
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
                                            <div>Specifies the ID of the elastic IP address assigned to the node. Only elastic IP addresses in the DOWN state can be assigned.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-extend_param"></div>
                    <b>extend_param</b>
                    <a class="ansibleOptionLink" href="#parameter-extend_param" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the extend parameter of the node, key/value pair format.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-fixed_ip"></div>
                    <b>fixed_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-fixed_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies fixed IP of the NIC.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-flavor_id"></div>
                    <b>flavor_id</b>
                    <a class="ansibleOptionLink" href="#parameter-flavor_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ID of the node flavor.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-k8s_tags"></div>
                    <b>k8s_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-k8s_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the tags of the kubernetes node, key/value pair format.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-key_pair"></div>
                    <b>key_pair</b>
                    <a class="ansibleOptionLink" href="#parameter-key_pair" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the key pair name when logging in to select the key pair mode.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-max_pods"></div>
                    <b>max_pods</b>
                    <a class="ansibleOptionLink" href="#parameter-max_pods" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the maximum number of instances a node is allowed to create.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the node name. Value requirements: Consists of 1 to 64 characters, including letters, digits, hyphens (-), periods (.).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-os"></div>
                    <b>os</b>
                    <a class="ansibleOptionLink" href="#parameter-os" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the operating System of the node.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the root password when logging in to select the password mode.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-postinstall"></div>
                    <b>postinstall</b>
                    <a class="ansibleOptionLink" href="#parameter-postinstall" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the script required after installation. The input value must be a Base64 encoded.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-pretinstall"></div>
                    <b>pretinstall</b>
                    <a class="ansibleOptionLink" href="#parameter-pretinstall" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the script required before installation. The input value must be a Base64 encoded.</div>
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
                                            <div>Specifies the system disk of the node.</div>
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
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the system disk size, in GB. The value range is 40 to 1024.</div>
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
                                            <div>Specifies the disk type.</div>
                                            <div>SATA is common I/O disk type.</div>
                                            <div>SAS is high I/O disk type.</div>
                                            <div>SSD is ultra-high I/O disk type.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#parameter-subnet_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ID of the subnet to which the NIC belongs.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-tags"></div>
                    <b>tags</b>
                    <a class="ansibleOptionLink" href="#parameter-tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the tags of the node, key/value pair format.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-taints"></div>
                    <b>taints</b>
                    <a class="ansibleOptionLink" href="#parameter-taints" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>You can add taints to created nodes to configure anti-affinity.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-taints/effect"></div>
                    <b>effect</b>
                    <a class="ansibleOptionLink" href="#parameter-taints/effect" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Available options are NoSchedule, PreferNoSchedule, and NoExecute.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-taints/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-taints/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A key must contain 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed. A DNS subdomain name can be used as the prefix of a key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-taints/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-taints/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A value must start with a letter or digit and can contain a maximum of 63 characters, including letters, digits, hyphens (-), underscores (_), and periods (.).</div>
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
                    <div class="ansibleOptionAnchor" id="return-availability_zone"></div>
                    <b>availability_zone</b>
                    <a class="ansibleOptionLink" href="#return-availability_zone" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the name of the AZ where the node is located.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-cluster_id"></div>
                    <b>cluster_id</b>
                    <a class="ansibleOptionLink" href="#return-cluster_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the cluster to which the node belongs.</div>
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
                                            <div>Specifies the data disks of the node.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-data_volumes/size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#return-data_volumes/size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the system disk size, in GB. The value range is 100 to 32768.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-data_volumes/volume_type"></div>
                    <b>volume_type</b>
                    <a class="ansibleOptionLink" href="#return-data_volumes/volume_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the disk type.</div>
                                            <div>SATA is common I/O disk type.</div>
                                            <div>SAS is high I/O disk type.</div>
                                            <div>SSD is ultra-high I/O disk type.</div>
                                        <br/>
                                    </td>
            </tr>
                    
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ecs_group_id"></div>
                    <b>ecs_group_id</b>
                    <a class="ansibleOptionLink" href="#return-ecs_group_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ecs group id. If specified, the node will be created under the cloud server group.</div>
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
                                            <div>Specifies the ID of the elastic IP address assigned to the node. Only elastic IP addresses in the DOWN state can be assigned.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-extend_param"></div>
                    <b>extend_param</b>
                    <a class="ansibleOptionLink" href="#return-extend_param" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the extend parameter of the node, key/value pair format.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-fixed_ip"></div>
                    <b>fixed_ip</b>
                    <a class="ansibleOptionLink" href="#return-fixed_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies fixed IP of the NIC.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-flavor_id"></div>
                    <b>flavor_id</b>
                    <a class="ansibleOptionLink" href="#return-flavor_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the node flavor.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-k8s_tags"></div>
                    <b>k8s_tags</b>
                    <a class="ansibleOptionLink" href="#return-k8s_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the tags of the kubernetes node, key/value pair format.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-key_pair"></div>
                    <b>key_pair</b>
                    <a class="ansibleOptionLink" href="#return-key_pair" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the key pair name when logging in to select the key pair mode.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-max_pods"></div>
                    <b>max_pods</b>
                    <a class="ansibleOptionLink" href="#return-max_pods" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the maximum number of instances a node is allowed to create.</div>
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
                                            <div>Specifies the node name. Value requirements: Consists of 1 to 64 characters, including letters, digits, hyphens (-), periods (.).</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-os"></div>
                    <b>os</b>
                    <a class="ansibleOptionLink" href="#return-os" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the operating System of the node.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#return-password" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the root password when logging in to select the password mode.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-postinstall"></div>
                    <b>postinstall</b>
                    <a class="ansibleOptionLink" href="#return-postinstall" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the script required after installation. The input value must be a Base64 encoded.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-pretinstall"></div>
                    <b>pretinstall</b>
                    <a class="ansibleOptionLink" href="#return-pretinstall" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the script required before installation. The input value must be a Base64 encoded.</div>
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
                                            <div>Specifies the system disk of the node.</div>
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
                                            <div>Specifies the system disk size, in GB. The value range is 40 to 1024.</div>
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
                                            <div>Specifies the disk type.</div>
                                            <div>SATA is common I/O disk type.</div>
                                            <div>SAS is high I/O disk type.</div>
                                            <div>SSD is ultra-high I/O disk type.</div>
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
                                            <div>Specifies the node status.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#return-subnet_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the subnet to which the NIC belongs.</div>
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
                                            <div>Specifies the tags of the node, key/value pair format.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-taints"></div>
                    <b>taints</b>
                    <a class="ansibleOptionLink" href="#return-taints" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>You can add taints to created nodes to configure anti-affinity.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-taints/effect"></div>
                    <b>effect</b>
                    <a class="ansibleOptionLink" href="#return-taints/effect" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Available options are NoSchedule, PreferNoSchedule, and NoExecute.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-taints/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#return-taints/key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>A key must contain 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed. A DNS subdomain name can be used as the prefix of a key.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-taints/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-taints/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>A value must start with a letter or digit and can contain a maximum of 63 characters, including letters, digits, hyphens (-), underscores (_), and periods (.).</div>
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

