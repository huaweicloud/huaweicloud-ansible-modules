.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.hwceco.hwcollection.hwc_vpc_subnet_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

hwceco.hwcollection.hwc_vpc_subnet -- Creates a resource of Vpc/Subnet in Huawei Cloud
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `hwceco.hwcollection collection <https://galaxy.ansible.com/hwceco/hwcollection>`_ (version 1.0.5).

    To install it use: :code:`ansible-galaxy collection install hwceco.hwcollection`.

    To use it in a playbook, specify: :code:`hwceco.hwcollection.hwc_vpc_subnet`.

.. version_added

.. versionadded:: 1.0.0 of hwceco.hwcollection

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates and manages a resource of Vpc/Subnet in Huawei Cloud.


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
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the AZ to which the subnet belongs.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-cidr"></div>
                    <b>cidr</b>
                    <a class="ansibleOptionLink" href="#parameter-cidr" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the subnet CIDR block. The value must be within the VPC CIDR block and be in CIDR format. The subnet mask cannot be greater than 28.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-dhcp_enable"></div>
                    <b>dhcp_enable</b>
                    <a class="ansibleOptionLink" href="#parameter-dhcp_enable" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether DHCP is enabled for the subnet.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-dns_address"></div>
                    <b>dns_address</b>
                    <a class="ansibleOptionLink" href="#parameter-dns_address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the DNS server addresses for subnet. The address in the head will be used first.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-gateway_ip"></div>
                    <b>gateway_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-gateway_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the gateway of the subnet. The value must be an IP address in the subnet.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ipv6_enable"></div>
                    <b>ipv6_enable</b>
                    <a class="ansibleOptionLink" href="#parameter-ipv6_enable" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies whether the IPv6 function is enabled for the subnet.</div>
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
                                            <div>Specifies the subnet name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores <code>_</code>, hyphens (-), and periods (.).</div>
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
                                            <div>Specifies the key/value pairs to associate with the subnet.</div>
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
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"15m"</div>
                                    </td>
                                                                <td>
                                            <div>The timeouts for create operation.</div>
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
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"15m"</div>
                                    </td>
                                                                <td>
                                            <div>The timeouts for update operation.</div>
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
                                            <div>Specifies the ID of the VPC to which the subnet belongs.</div>
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

    
    # create subnet
    - name: create vpc
      hwc_vpc:
          cidr: "192.168.100.0/24"
          name: "ansible_network_vpc_test"
      register: vpc
    - name: create subnet
      hwc_vpc_subnet:
          filters:
              - "name"
          vpc_id: "{{ vpc.state.id }}"
          cidr: "192.168.100.0/26"
          gateway_ip: "192.168.100.32"
          name: "ansible_network_subnet_test"
          dhcp_enable: True




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
                    <div class="ansibleOptionAnchor" id="return-availability_zone"></div>
                    <b>availability_zone</b>
                    <a class="ansibleOptionLink" href="#return-availability_zone" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the AZ to which the subnet belongs.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-cidr"></div>
                    <b>cidr</b>
                    <a class="ansibleOptionLink" href="#return-cidr" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the subnet CIDR block. The value must be within the VPC CIDR block and be in CIDR format. The subnet mask cannot be greater than 28.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-dhcp_enable"></div>
                    <b>dhcp_enable</b>
                    <a class="ansibleOptionLink" href="#return-dhcp_enable" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies whether DHCP is enabled for the subnet.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-dns_address"></div>
                    <b>dns_address</b>
                    <a class="ansibleOptionLink" href="#return-dns_address" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the DNS server addresses for subnet. Note that the address in the head will be used first.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-gateway_ip"></div>
                    <b>gateway_ip</b>
                    <a class="ansibleOptionLink" href="#return-gateway_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the gateway of the subnet. The value must be an IP address in the subnet.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ipv6_enable"></div>
                    <b>ipv6_enable</b>
                    <a class="ansibleOptionLink" href="#return-ipv6_enable" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies whether the IPv6 function is enabled for the subnet.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the subnet name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores <code>_</code>, hyphens (-), and periods (.).</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-tags"></div>
                    <b>tags</b>
                    <a class="ansibleOptionLink" href="#return-tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the key/value pairs to associate with the subnet.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-vpc_id"></div>
                    <b>vpc_id</b>
                    <a class="ansibleOptionLink" href="#return-vpc_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specifies the ID of the VPC to which the subnet belongs.</div>
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

