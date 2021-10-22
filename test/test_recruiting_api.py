# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.2.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.recruiting_api import RecruitingApi  # noqa: E501
from cfbd.rest import ApiException


class TestRecruitingApi(unittest.TestCase):
    """RecruitingApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.recruiting_api.RecruitingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_recruiting_groups(self):
        """Test case for get_recruiting_groups

        Recruit position group ratings  # noqa: E501
        """
        pass

    def test_get_recruiting_players(self):
        """Test case for get_recruiting_players

        Player recruiting ratings and rankings  # noqa: E501
        """
        pass

    def test_get_recruiting_teams(self):
        """Test case for get_recruiting_teams

        Team recruiting rankings and ratings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
