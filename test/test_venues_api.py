# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.2.3
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.venues_api import VenuesApi  # noqa: E501
from cfbd.rest import ApiException


class TestVenuesApi(unittest.TestCase):
    """VenuesApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.venues_api.VenuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_venues(self):
        """Test case for get_venues

        Arena and venue information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
