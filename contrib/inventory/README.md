# Inventory for Huaweicloud

Installation
------------

Download `hwc_ecs.ini`, `hwc_ecs.py` and `requirements-inventory.txt` to your local directory.

Install dependencies

  ```bash
  pip install -r requirements-inventory.txt
  ```

Add executable permission

  ``` bash
  $ chmod +x hwc_ecs.py
  ```

Config your credentials in `hwc_ecs.ini`

Test the inventory

  ``` bash
  $ ./hwc_ecs.py --list
  ```

Use the inventory with ansible

  ```bash
  $ ansible -i hwc_ecs.py huaweicloud -m ping
  ```
