# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.3.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.models.play_wp import PlayWP  # noqa: E501
from cfbd.rest import ApiException


class TestPlayWP(unittest.TestCase):
    """PlayWP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlayWP(self):
        """Test PlayWP"""
        # FIXME: construct object with mandatory attributes with example values
        # model = cfbd.models.play_wp.PlayWP()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
