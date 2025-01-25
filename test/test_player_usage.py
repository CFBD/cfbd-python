# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.8
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.player_usage import PlayerUsage  # noqa: E501

class TestPlayerUsage(unittest.TestCase):
    """PlayerUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerUsage:
        """Test PlayerUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerUsage`
        """
        model = PlayerUsage()  # noqa: E501
        if include_optional:
            return PlayerUsage(
                season = 56,
                id = '',
                name = '',
                position = '',
                team = '',
                conference = '',
                usage = cfbd.models.player_usage_usage.PlayerUsage_usage(
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rush = 1.337, 
                    pass = 1.337, 
                    overall = 1.337, )
            )
        else:
            return PlayerUsage(
                season = 56,
                id = '',
                name = '',
                position = '',
                team = '',
                conference = '',
                usage = cfbd.models.player_usage_usage.PlayerUsage_usage(
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rush = 1.337, 
                    pass = 1.337, 
                    overall = 1.337, ),
        )
        """

    def testPlayerUsage(self):
        """Test PlayerUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
