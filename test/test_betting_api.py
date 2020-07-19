# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.5
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.betting_api import BettingApi  # noqa: E501
from cfbd.rest import ApiException


class TestBettingApi(unittest.TestCase):
    """BettingApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.betting_api.BettingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_lines(self):
        """Test case for get_lines

        Betting lines  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
