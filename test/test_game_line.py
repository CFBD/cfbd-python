# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.18
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.game_line import GameLine  # noqa: E501

class TestGameLine(unittest.TestCase):
    """GameLine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameLine:
        """Test GameLine
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameLine`
        """
        model = GameLine()  # noqa: E501
        if include_optional:
            return GameLine(
                provider = '',
                spread = 1.337,
                formatted_spread = '',
                spread_open = 1.337,
                over_under = 1.337,
                over_under_open = 1.337,
                home_moneyline = 1.337,
                away_moneyline = 1.337
            )
        else:
            return GameLine(
                provider = '',
                spread = 1.337,
                formatted_spread = '',
                spread_open = 1.337,
                over_under = 1.337,
                over_under_open = 1.337,
                home_moneyline = 1.337,
                away_moneyline = 1.337,
        )
        """

    def testGameLine(self):
        """Test GameLine"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
