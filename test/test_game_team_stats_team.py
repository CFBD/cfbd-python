# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.16
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.game_team_stats_team import GameTeamStatsTeam  # noqa: E501

class TestGameTeamStatsTeam(unittest.TestCase):
    """GameTeamStatsTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameTeamStatsTeam:
        """Test GameTeamStatsTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameTeamStatsTeam`
        """
        model = GameTeamStatsTeam()  # noqa: E501
        if include_optional:
            return GameTeamStatsTeam(
                team_id = 56,
                team = '',
                conference = '',
                home_away = 'home',
                points = 56,
                stats = [
                    cfbd.models.game_team_stats_team_stat.GameTeamStatsTeamStat(
                        category = '', 
                        stat = '', )
                    ]
            )
        else:
            return GameTeamStatsTeam(
                team_id = 56,
                team = '',
                conference = '',
                home_away = 'home',
                points = 56,
                stats = [
                    cfbd.models.game_team_stats_team_stat.GameTeamStatsTeamStat(
                        category = '', 
                        stat = '', )
                    ],
        )
        """

    def testGameTeamStatsTeam(self):
        """Test GameTeamStatsTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
