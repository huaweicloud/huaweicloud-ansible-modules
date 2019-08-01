# Copyright (c), Google Inc, 2017
# Simplified BSD License (see licenses/simplified_bsd.txt or
# https://opensource.org/licenses/BSD-2-Clause)

import re
import time
import traceback

THIRD_LIBRARIES_IMP_ERR = None
try:
    from keystoneauth1.adapter import Adapter
    from keystoneauth1.identity import v3
    from keystoneauth1 import session
    HAS_THIRD_LIBRARIES = True
except ImportError:
    THIRD_LIBRARIES_IMP_ERR = traceback.format_exc()
    HAS_THIRD_LIBRARIES = False

from ansible.module_utils.basic import (AnsibleModule, env_fallback,
                                        missing_required_lib)
from ansible.module_utils._text import to_text


class HwcModuleException(Exception):
    def __init__(self, message):
        super(HwcModuleException, self).__init__()

        self._message = message

    def __str__(self):
        return "[HwcClientException] message=%s" % self._message


class HwcClientException(Exception):
    def __init__(self, code, message):
        super(HwcClientException, self).__init__()

        self._code = code
        self._message = message

    def __str__(self):
        msg = " code=%s," % str(self._code) if self._code != 0 else ""
        return "[HwcClientException]%s message=%s" % (
            msg, self._message)


class HwcClientException404(HwcClientException):
    def __init__(self, message):
        super(HwcClientException404, self).__init__(404, message)

    def __str__(self):
        return "[HwcClientException404] message=%s" % self._message


def session_method_wrapper(f):
    def _wrap(self, url, *args, **kwargs):
        try:
            url = self.endpoint + url
            r = f(self, url, *args, **kwargs)
        except Exception as ex:
            raise HwcClientException(
                0, "Sending request failed, error=%s" % ex)

        result = None
        if r.content:
            try:
                result = r.json()
            except Exception as ex:
                raise HwcCl
