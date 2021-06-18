# Copyright (c), Google Inc, 2017
# Simplified BSD License (see licenses/simplified_bsd.txt or
# https://opensource.org/licenses/BSD-2-Clause)

import json
import time

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.http.http_config import HttpConfig

from huaweicloudsdkvpc.v2 import VpcClient
from huaweicloudsdkecs.v2 import EcsClient
from huaweicloudsdkevs.v2 import EvsClient
from huaweicloudsdkcce.v3 import CceClient

from ansible.module_utils.basic import (AnsibleModule, env_fallback,)
from ansible.module_utils._text import to_text
class HwcModuleBase(object):
    def __init__(self, derived_arg_spec, no_log=False, supports_check_mode=False, skip_exec=False):
        merged_arg_spec = dict()

        merged_arg_spec.update(
            dict(
                region=dict(
                    required=True, type='str',
                    fallback=(env_fallback, ['ANSIBLE_HWC_REGION']),
                ),
                access_key=dict(
                    required=True, type='str',
                    fallback=(env_fallback, ['ANSIBLE_HWC_ACCESS_KEY']),
                ),
                secret_key=dict(
                    required=True, type='str', no_log=True,
                    fallback=(env_fallback, ['ANSIBLE_HWC_SECRET_KEY']),
                ),
                project_id=dict(
                    type='str',
                    fallback=(env_fallback, ['ANSIBLE_HWC_PROJECT_ID']),
                ),
                identity_endpoint=dict(
                    type='str',
                    fallback=(env_fallback, ['ANSIBLE_HWC_IDENTITY_ENDPOINT']),
                ),
                cloud=dict(
                    default='myhuaweicloud.com',
                    type='str',
                    fallback=(env_fallback, ['ANSIBLE_HWC_CLOUD']),
                ),
                id=dict(type='str')
            )
        )

        if derived_arg_spec:
            merged_arg_spec.update(derived_arg_spec)

        self.module = AnsibleModule(argument_spec=merged_arg_spec,
                                    no_log=no_log,
                                    supports_check_mode=supports_check_mode,)

        self.check_mode = self.module.check_mode
        self._vpc_client = None
        self._ecs_client = None
        self._evs_client = None
        self._cce_client = None

        if not skip_exec:
            res = self.exec_module(**self.module.params)
            self.module.exit_json(**res)


    def exec_module(self, **kwargs):
        self.fail("Error: {0} failed to implement exec_module method.".format(self.__class__.__name__))

    def fail(self, msg, **kwargs):
        '''
        Shortcut for calling module.fail()
        :param msg: Error message text.
        :param kwargs: Any key=value pairs
        :return: None
        '''
        self.module.fail_json(msg=msg, **kwargs)

    def deprecate(self, msg, version=None):
        self.module.deprecate(msg, version)

    def log(self, msg, pretty_print=False):
        # Use only during module development
        
        log_file = open('hwc_module.log', 'a')
        if pretty_print:
            log_file.write(json.dumps(msg, indent=4, sort_keys=True))
        else:
            log_file.write(msg + u'\n')

    @property
    def vpc_client(self):
        self.log('Geting VPC client')
        if not self._vpc_client:
            config = HttpConfig.get_default_config()
            config.ignore_ssl_verification = True
            if self.module.params["project_id"]:
                credentials = BasicCredentials(self.module.params["access_key"], self.module.params["secret_key"], self.module.params["project_id"])

                if self.module.params["identity_endpoint"]:
                    credentials.iam_endpoint = self.module.params["identity_endpoint"]

                endpoint = 'https://vpc.{}.{}'.format(self.module.params["region"], self.module.params["cloud"])
                self._vpc_client = VpcClient.new_builder() \
                .with_http_config(config) \
                .with_credentials(credentials) \
                .with_endpoint(endpoint) \
                .build()
            else:
                raise HwcModuleException(
                        'Getting VPC client failed: "project_id" is required for VPC client')

        return self._vpc_client

    @property
    def ecs_client(self):
        self.log('Geting ECS client')
        if not self._ecs_client:
            config = HttpConfig.get_default_config()
            config.ignore_ssl_verification = True
            if self.module.params["project_id"]:
                credentials = BasicCredentials(self.module.params["access_key"], self.module.params["secret_key"], self.module.params["project_id"])

                if self.module.params["identity_endpoint"]:
                    credentials.iam_endpoint = self.module.params["identity_endpoint"]

                endpoint = 'https://ecs.{}.{}'.format(self.module.params["region"], self.module.params["cloud"])
                self._ecs_client = EcsClient.new_builder() \
                .with_http_config(config) \
                .with_credentials(credentials) \
                .with_endpoint(endpoint) \
                .build()
            else:
                raise HwcModuleException(
                        'Getting ECS client failed: "project_id" is required for ECS client')

        return self._ecs_client

    @property
    def evs_client(self):
        self.log('Geting EVS client')
        if not self._evs_client:
            config = HttpConfig.get_default_config()
            config.ignore_ssl_verification = True
            if self.module.params["project_id"]:
                credentials = BasicCredentials(self.module.params["access_key"], self.module.params["secret_key"], self.module.params["project_id"])

                if self.module.params["identity_endpoint"]:
                    credentials.iam_endpoint = self.module.params["identity_endpoint"]

                endpoint = 'https://evs.{}.{}'.format(self.module.params["region"], self.module.params["cloud"])
                self._evs_client = EvsClient.new_builder() \
                .with_http_config(config) \
                .with_credentials(credentials) \
                .with_endpoint(endpoint) \
                .build()
            else:
                raise HwcModuleException(
                        'Getting EVS client failed: "project_id" is required for EVS client')

        return self._evs_client


    @property
    def cce_client(self):
        self.log('Geting CCE client')
        if not self._cce_client:
            config = HttpConfig.get_default_config()
            config.ignore_ssl_verification = True
            if self.module.params["project_id"]:
                credentials = BasicCredentials(self.module.params["access_key"], self.module.params["secret_key"], self.module.params["project_id"])

                if self.module.params["identity_endpoint"]:
                    credentials.iam_endpoint = self.module.params["identity_endpoint"]

                endpoint = 'https://cce.{}.{}'.format(self.module.params["region"], self.module.params["cloud"])
                self._cce_client = CceClient.new_builder() \
                .with_http_config(config) \
                .with_credentials(credentials) \
                .with_endpoint(endpoint) \
                .build()
            else:
                raise HwcModuleException(
                        'Getting CCE client failed: "project_id" is required for CCE client')

        return self._cce_client
    

class HwcModuleException(Exception):
    def __init__(self, message):
        super(HwcModuleException, self).__init__()

        self._message = message

    def __str__(self):
        return "[HwcClientException] message=%s" % self._message

class _DictComparison(object):
    ''' This class takes in two dictionaries `a` and `b`.
        These are dictionaries of arbitrary depth, but made up of standard
        Python types only.
        This differ will compare all values in `a` to those in `b`.
        If value in `a` is None, always returns True, indicating
        this value is no need to compare.
        Note: On all lists, order does matter.
    '''

    def __init__(self, request):
        self.request = request

    def __eq__(self, other):
        return self._compare_dicts(self.request, other.request)

    def __ne__(self, other):
        return not self.__eq__(other)

    def _compare_dicts(self, dict1, dict2):
        if dict1 is None:
            return True

        if set(dict1.keys()) != set(dict2.keys()):
            return False

        for k in dict1:
            if not self._compare_value(dict1.get(k), dict2.get(k)):
                return False

        return True

    def _compare_lists(self, list1, list2):
        """Takes in two lists and compares them."""
        if list1 is None:
            return True

        if len(list1) != len(list2):
            return False

        for i in range(len(list1)):
            if not self._compare_value(list1[i], list2[i]):
                return False

        return True

    def _compare_value(self, value1, value2):
        """
        return: True: value1 is same as value2, otherwise False.
        """
        if value1 is None:
            return True

        if not (value1 and value2):
            return (not value1) and (not value2)

        # Can assume non-None types at this point.
        if isinstance(value1, list) and isinstance(value2, list):
            return self._compare_lists(value1, value2)

        elif isinstance(value1, dict) and isinstance(value2, dict):
            return self._compare_dicts(value1, value2)

        # Always use to_text values to avoid unicode issues.
        return (to_text(value1, errors='surrogate_or_strict') == to_text(
            value2, errors='surrogate_or_strict'))


def wait_to_finish(target, pending, refresh, timeout, min_interval=1, delay=3):
    is_last_time = False
    not_found_times = 0
    wait = 0

    time.sleep(delay)

    end = time.time() + timeout
    while not is_last_time:
        if time.time() > end:
            is_last_time = True

        obj, status = refresh()

        if obj is None:
            not_found_times += 1

            if not_found_times > 10:
                raise HwcModuleException(
                    "not found the object for %d times" % not_found_times)
        else:
            not_found_times = 0

            if status in target:
                return obj

            if pending and status not in pending:
                raise HwcModuleException(
                    "unexpect status(%s) occured" % status)

        if not is_last_time:
            wait *= 2
            if wait < min_interval:
                wait = min_interval
            elif wait > 10:
                wait = 10

            time.sleep(wait)

    raise HwcModuleException("asycn wait timeout after %d seconds" % timeout)


def navigate_value(data, index, array_index=None):
    if array_index and (not isinstance(array_index, dict)):
        raise HwcModuleException("array_index must be dict")

    d = data
    for n in range(len(index)):
        if d is None:
            return None

        if not isinstance(d, dict):
            raise HwcModuleException(
                "can't navigate value from a non-dict object")

        i = index[n]
        if i not in d:
            raise HwcModuleException(
                "navigate value failed: key(%s) is not exist in dict" % i)
        d = d[i]

        if not array_index:
            continue

        k = ".".join(index[: (n + 1)])
        if k not in array_index:
            continue

        if d is None:
            return None

        if not isinstance(d, list):
            raise HwcModuleException(
                "can't navigate value from a non-list object")

        j = array_index.get(k)
        if j >= len(d):
            raise HwcModuleException(
                "navigate value failed: the index is out of list")
        d = d[j]

    return d

def build_tags_parameters(opts, action):
    params = dict()
    params['action'] = action
    tags_raw = navigate_value(opts, ['tags'], None)
    tags = []
    for k, v in tags_raw.items():
        tag = {
            "key": k,
            "value": v
        }
        tags.append(tag)

    params['tags'] = tags

    return params

def tags_to_dict(tags_raw):
    tags = {}
    for tag_raw in tags_raw:
        tags[tag_raw['key']] = tag_raw['value']
    return tags


def is_empty_value(v):
    return (not v)


def are_different_dicts(dict1, dict2):
    return _DictComparison(dict1) != _DictComparison(dict2)
