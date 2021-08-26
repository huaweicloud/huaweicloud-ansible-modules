.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.hwceco.hwcollection.hwc_vpc_security_group_rule_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

hwceco.hwcollection.hwc_vpc_security_group_rule -- Creates a resource of Vpc/SecurityGroupRule in Huawei Cloud
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `hwceco.hwcollection collection <https://galaxy.ansible.com/hwceco/hwcollection>`_ (version 1.0.5).

    To install it use: :code:`ansible-galaxy collection install hwceco.hwcollection`.

    To use it in a playbook, specify: :code:`hwceco.hwcollection.hwc_vpc_security_group_rule`.

.. version_added

.. versionadded:: 1.0.0 of hwceco.hwcollection

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates and manages a resource of Vpc/SecurityGroupRule in Huawei Cloud.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- huaweicloudsdkcore >= 3.0.47
- huaweicloudsdkvpc >= 3.0.47


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                            <div>Provides supplementary information about the security group rule. The value is a string of no more than 255 characters that can contain letters and digits.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-direction"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-direction" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the direction of access control. The value can be egress or ingress.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ethertype"></div>
                    <b>ethertype</b>
                    <a class="ansibleOptionLink" href="#parameter-ethertype" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the IP protocol version. The value can be IPv4 or IPv6. If you do not set this parameter, IPv4 is used by default.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-port_range_max"></div>
                    <b>port_range_max</b>
                    <a class="ansibleOptionLink" href="#parameter-port_range_max" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the end port number. The value ranges from 1 to 65535. If the protocol is not icmp, the value cannot be smaller than the port_range_min value. An empty value indicates all ports.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-port_range_min"></div>
                    <b>port_range_min</b>
                    <a class="ansibleOptionLink" href="#parameter-port_range_min" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the start port number. The value ranges from 1 to 65535. The value cannot be greater than the port_range_max value. An empty value indicates all ports.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the protocol type. The value can be icmp, tcp, or udp. If the parameter is left blank, the security group supports all protocols.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-remote_group_id"></div>
                    <b>remote_group_id</b>
                    <a class="ansibleOptionLink" href="#parameter-remote_group_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the ID of the peer security group. The value is exclusive with parameter remote_ip_prefix.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-remote_ip_prefix"></div>
                    <b>remote_ip_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-remote_ip_prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the remote IP address. If the access control direction is set to egress, the parameter specifies the source IP address. If the access control direction is set to ingress, the parameter specifies the destination IP address. The value can be in the CIDR format or IP addresses. The parameter is exclusive with parameter remote_group_id.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_group_id"></div>
                    <b>security_group_id</b>
                    <a class="ansibleOptionLink" href="#parameter-security_group_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the security group rule ID, which uniquely identifies the security group rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Provides supplementary information about the security group rule. The value is a string of no more than 255 characters that can contain letters and digits.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-direction"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#return-direction" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the direction of access control. The value can be egress or ingress.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ethertype"></div>
                    <b>ethertype</b>
                    <a class="ansibleOptionLink" href="#return-ethertype" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the IP protocol version. The value can be IPv4 or IPv6. If you do not set this parameter, IPv4 is used by default.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-port_range_max"></div>
                    <b>port_range_max</b>
                    <a class="ansibleOptionLink" href="#return-port_range_max" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the end port number. The value ranges from 1 to 65535. If the protocol is not icmp, the value cannot be smaller than the port_range_min value. An empty value indicates all ports.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-port_range_min"></div>
                    <b>port_range_min</b>
                    <a class="ansibleOptionLink" href="#return-port_range_min" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the start port number. The value ranges from 1 to 65535. The value cannot be greater than the port_range_max value. An empty value indicates all ports.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the protocol type. The value can be icmp, tcp, or udp. If the parameter is left blank, the security group supports all protocols.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-remote_group_id"></div>
                    <b>remote_group_id</b>
                    <a class="ansibleOptionLink" href="#return-remote_group_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the peer security group. The value is exclusive with parameter remote_ip_prefix.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-remote_ip_prefix"></div>
                    <b>remote_ip_prefix</b>
                    <a class="ansibleOptionLink" href="#return-remote_ip_prefix" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the remote IP address. If the access control direction is set to egress, the parameter specifies the source IP address. If the access control direction is set to ingress, the parameter specifies the destination IP address. The value can be in the CIDR format or IP addresses. The parameter is exclusive with parameter remote_group_id.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-security_group_id"></div>
                    <b>security_group_id</b>
                    <a class="ansibleOptionLink" href="#return-security_group_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the security group rule ID, which uniquely identifies the security group rule.</div>
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

