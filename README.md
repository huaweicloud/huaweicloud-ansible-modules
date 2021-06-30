huaweicloud.huaweicloud_ansible_modules
=========

This role includes the latest changes and bug fixes for HuaweiCloud modules from the `devel` branch of [Ansible repository](https://github.com/ansible/ansible). If you cannot wait for Ansible's next release, installing this role is a good choice. 

Prerequisite
------------

The usage of this playbook role assumes that you've already setup an Ansible environment for HuaweiCloud.

[Installed the ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) in your environment.

Installation
------------

Install the role.

  ``` bash
  $ ansible-galaxy install huaweicloud.huaweicloud_ansible_modules
  ```

Example Playbook
----------------

    $ cat test.yml
    - hosts: localhost
      roles:
        - { role: huaweicloud.huaweicloud_ansible_modules }
      tasks:
		- name: create a new vpc
		  hwc_vpc:
			identity_endpoint: "https://iam.cn-north-1.myhwclouds.com/v3"
			cloud: "myhwclouds.com"
			access_key: "{{ access_key }}"
			secret_key: "{{ secret_key }}"
			project_id: "{{ project_id }}"
			region: "{{ region }}"

			name: "{{ vpc_name }}"
			cidr: "192.168.100.0/24"
			state: present
		  register: vpc 
		- name: dump the output
		  debug:
			msg: '{{ vpc }}'

Run ansible
-----------
```
$ ansible-playbook test.yml
```

License
-------
Apache 2.0
