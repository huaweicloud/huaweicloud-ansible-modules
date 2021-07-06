# Ansible Collection for Huaweicloud

This collection includes a series of Ansible modules for interacting with Huaweicloud.

Prerequisite
------------

The usage of this collection assumes that you've already setup an Ansible environment for HuaweiCloud.

[Installed the ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) in your environment.

Installation
------------

Install dependencies.

  ```bash
  pip install -r requirements.txt
  ```

Install the collection.

  ``` bash
  $ ansible-galaxy collection install hwceco.hwcollection
  ```

Upgrade to the lastet version of the collection.

  ``` bash
  $ ansible-galaxy collection install hwceco.hwcollection --force
  ```

Example Playbook
----------------

    $ cat test.yml
    - hosts: localhost
      collections:
        - hwceco.hwcollection
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
