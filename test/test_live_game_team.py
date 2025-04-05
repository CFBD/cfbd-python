# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.11
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.live_game_team import LiveGameTeam  # noqa: E501

class TestLiveGameTeam(unittest.TestCase):
    """LiveGameTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LiveGameTeam:
        """Test LiveGameTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LiveGameTeam`
        """
        model = LiveGameTeam()  # noqa: E501
        if include_optional:
            return LiveGameTeam(
                team_id = 56,
                team = '',
                home_away = 'home',
                line_scores = [
                    56
                    ],
                points = 56,
                drives = 56,
                scoring_opportunities = 56,
                points_per_opportunity = 1.337,
                plays = 56,
                line_yards = 1.337,
                line_yards_per_rush = 1.337,
                second_level_yards = 1.337,
                second_level_yards_per_rush = 1.337,
                open_field_yards = 1.337,
                open_field_yards_per_rush = 1.337,
                epa_per_play = 1.337,
                total_epa = 1.337,
                passing_epa = 1.337,
                epa_per_pass = 1.337,
                rushing_epa = 1.337,
                epa_per_rush = 1.337,
                success_rate = 1.337,
                standard_down_success_rate = 1.337,
                passing_down_success_rate = 1.337,
                explosiveness = 1.337
            )
        else:
            return LiveGameTeam(
                team_id = 56,
                team = '',
                home_away = 'home',
                line_scores = [
                    56
                    ],
                points = 56,
                drives = 56,
                scoring_opportunities = 56,
                points_per_opportunity = 1.337,
                plays = 56,
                line_yards = 1.337,
                line_yards_per_rush = 1.337,
                second_level_yards = 1.337,
                second_level_yards_per_rush = 1.337,
                open_field_yards = 1.337,
                open_field_yards_per_rush = 1.337,
                epa_per_play = 1.337,
                total_epa = 1.337,
                passing_epa = 1.337,
                epa_per_pass = 1.337,
                rushing_epa = 1.337,
                epa_per_rush = 1.337,
                success_rate = 1.337,
                standard_down_success_rate = 1.337,
                passing_down_success_rate = 1.337,
                explosiveness = 1.337,
        )
        """

    def testLiveGameTeam(self):
        """Test LiveGameTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
