# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.8
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.game_team_stats import GameTeamStats  # noqa: E501

class TestGameTeamStats(unittest.TestCase):
    """GameTeamStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameTeamStats:
        """Test GameTeamStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameTeamStats`
        """
        model = GameTeamStats()  # noqa: E501
        if include_optional:
            return GameTeamStats(
                id = 56,
                teams = [
                    cfbd.models.game_team_stats_team.GameTeamStatsTeam(
                        team_id = 56, 
                        team = '', 
                        conference = '', 
                        home_away = 'home', 
                        points = 56, 
                        stats = [
                            cfbd.models.game_team_stats_team_stat.GameTeamStatsTeamStat(
                                category = '', 
                                stat = '', )
                            ], )
                    ]
            )
        else:
            return GameTeamStats(
                id = 56,
                teams = [
                    cfbd.models.game_team_stats_team.GameTeamStatsTeam(
                        team_id = 56, 
                        team = '', 
                        conference = '', 
                        home_away = 'home', 
                        points = 56, 
                        stats = [
                            cfbd.models.game_team_stats_team_stat.GameTeamStatsTeamStat(
                                category = '', 
                                stat = '', )
                            ], )
                    ],
        )
        """

    def testGameTeamStats(self):
        """Test GameTeamStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
