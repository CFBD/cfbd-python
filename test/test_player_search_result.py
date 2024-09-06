# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.18
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.player_search_result import PlayerSearchResult  # noqa: E501

class TestPlayerSearchResult(unittest.TestCase):
    """PlayerSearchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerSearchResult:
        """Test PlayerSearchResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerSearchResult`
        """
        model = PlayerSearchResult()  # noqa: E501
        if include_optional:
            return PlayerSearchResult(
                id = '',
                team = '',
                name = '',
                first_name = '',
                last_name = '',
                weight = 56,
                height = 56,
                jersey = 56,
                position = '',
                hometown = '',
                team_color = '',
                team_color_secondary = ''
            )
        else:
            return PlayerSearchResult(
                id = '',
                team = '',
                name = '',
                first_name = '',
                last_name = '',
                weight = 56,
                height = 56,
                jersey = 56,
                position = '',
                hometown = '',
                team_color = '',
                team_color_secondary = '',
        )
        """

    def testPlayerSearchResult(self):
        """Test PlayerSearchResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
