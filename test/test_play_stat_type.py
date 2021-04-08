# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\").  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.models.play_stat_type import PlayStatType  # noqa: E501
from cfbd.rest import ApiException


class TestPlayStatType(unittest.TestCase):
    """PlayStatType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlayStatType(self):
        """Test PlayStatType"""
        # FIXME: construct object with mandatory attributes with example values
        # model = cfbd.models.play_stat_type.PlayStatType()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
