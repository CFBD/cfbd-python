# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.6
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.models.live_play_by_play_plays import LivePlayByPlayPlays  # noqa: E501
from cfbd.rest import ApiException


class TestLivePlayByPlayPlays(unittest.TestCase):
    """LivePlayByPlayPlays unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLivePlayByPlayPlays(self):
        """Test LivePlayByPlayPlays"""
        # FIXME: construct object with mandatory attributes with example values
        # model = cfbd.models.live_play_by_play_plays.LivePlayByPlayPlays()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
