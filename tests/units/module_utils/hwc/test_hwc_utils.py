# -*- coding: utf-8 -*-

from units.compat import unittest
from ansible.module_utils.hwc_utils import (HwcModuleException, navigate_value,
                                            remove_empty_from_dict,
                                            remove_nones_from_dict,
                                            replace_resource_dict)


class HwcUtilsTestCase(unittest.TestCase):
    def test_navigate_value(self):
        value = {
            'foo': {
                'quiet': {
                    'tree': 'test',
                    "trees": [0, 1]
                },
            }
        }

        self.assertEquals(navigate_value(value, ["foo", "quiet", "tree"]),
                          "test")

        self.assertEquals(
            navigate_value(value, ["foo", "quiet", "trees"],
                           {"foo.quiet.trees": 1}),
            1)

        self.assertRaisesRegexp(HwcModuleException,
                                "key(q) is not exist in dict",
                                navigate_value, value, ["foo", "q", "tree"])

        self.assertRaisesRegexp(HwcModuleException, "the index is out of list",
                                navigate_value, value,
                                ["foo", "quiet", "trees"],
                                {"foo.quiet.trees": 2})
