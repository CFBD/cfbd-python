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

from cfbd.models.advanced_box_score_game_info import AdvancedBoxScoreGameInfo  # noqa: E501

class TestAdvancedBoxScoreGameInfo(unittest.TestCase):
    """AdvancedBoxScoreGameInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvancedBoxScoreGameInfo:
        """Test AdvancedBoxScoreGameInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvancedBoxScoreGameInfo`
        """
        model = AdvancedBoxScoreGameInfo()  # noqa: E501
        if include_optional:
            return AdvancedBoxScoreGameInfo(
                excitement = 1.337,
                home_winner = True,
                away_win_prob = 1.337,
                away_points = 56,
                away_team = '',
                home_win_prob = 1.337,
                home_points = 56,
                home_team = ''
            )
        else:
            return AdvancedBoxScoreGameInfo(
                excitement = 1.337,
                home_winner = True,
                away_win_prob = 1.337,
                away_points = 56,
                away_team = '',
                home_win_prob = 1.337,
                home_points = 56,
                home_team = '',
        )
        """

    def testAdvancedBoxScoreGameInfo(self):
        """Test AdvancedBoxScoreGameInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
