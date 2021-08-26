.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.hwceco.hwcollection.hwc_vpc_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

hwceco.hwcollection.hwc_vpc -- Creates a Huawei Cloud VPC
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `hwceco.hwcollection collection <https://galaxy.ansible.com/hwceco/hwcollection>`_ (version 1.0.5).

    To install it use: :code:`ansible-galaxy collection install hwceco.hwcollection`.

    To use it in a playbook, specify: :code:`hwceco.hwcollection.hwc_vpc`.

.. version_added

.. versionadded:: 1.0.0 of hwceco.hwcollection

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates and manages a Huawei Cloud VPC.


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
                                            <div>Specifies the range of available subnets in the vpc.</div>
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
                                            <div>Specifies the description of the vpc.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                            <div>Specifies the enterprise project id of the vpc.</div>
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
                                            <div>Specifies the name of vpc.</div>
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
                                                                <td colspan="1">
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
                                            <div>Specifies the key/value pairs to associate with the vpc.</div>
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

    
    - name: create a vpc
      hwc_vpc:
          name: "vpc_1"
          cidr: "192.168.100.0/24"
          state: present




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
                    <div class="ansibleOptionAnchor" id="return-cidr"></div>
                    <b>cidr</b>
                    <a class="ansibleOptionLink" href="#return-cidr" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>the range of available subnets in the vpc.</div>
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
                                            <div>Specifies the description of the vpc.</div>
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
                                            <div>Specifies the enterprise project id of the vpc.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>the id of vpc.</div>
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
                                            <div>the name of vpc.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-routes"></div>
                    <b>routes</b>
                    <a class="ansibleOptionLink" href="#return-routes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>the route information.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-routes/destination"></div>
                    <b>destination</b>
                    <a class="ansibleOptionLink" href="#return-routes/destination" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>the destination network segment of a route.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-routes/next_hop"></div>
                    <b>next_hop</b>
                    <a class="ansibleOptionLink" href="#return-routes/next_hop" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>the next hop of a route.</div>
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
                                            <div>the status of vpc.</div>
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

