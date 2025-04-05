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

from cfbd.models.game_player_stats_team import GamePlayerStatsTeam  # noqa: E501

class TestGamePlayerStatsTeam(unittest.TestCase):
    """GamePlayerStatsTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GamePlayerStatsTeam:
        """Test GamePlayerStatsTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GamePlayerStatsTeam`
        """
        model = GamePlayerStatsTeam()  # noqa: E501
        if include_optional:
            return GamePlayerStatsTeam(
                team = '',
                conference = '',
                home_away = 'home',
                points = 56,
                categories = [
                    cfbd.models.game_player_stat_categories.GamePlayerStatCategories(
                        name = '', 
                        types = [
                            cfbd.models.game_player_stat_types.GamePlayerStatTypes(
                                name = '', 
                                athletes = [
                                    cfbd.models.game_player_stat_player.GamePlayerStatPlayer(
                                        id = '', 
                                        name = '', 
                                        stat = '', )
                                    ], )
                            ], )
                    ]
            )
        else:
            return GamePlayerStatsTeam(
                team = '',
                conference = '',
                home_away = 'home',
                points = 56,
                categories = [
                    cfbd.models.game_player_stat_categories.GamePlayerStatCategories(
                        name = '', 
                        types = [
                            cfbd.models.game_player_stat_types.GamePlayerStatTypes(
                                name = '', 
                                athletes = [
                                    cfbd.models.game_player_stat_player.GamePlayerStatPlayer(
                                        id = '', 
                                        name = '', 
                                        stat = '', )
                                    ], )
                            ], )
                    ],
        )
        """

    def testGamePlayerStatsTeam(self):
        """Test GamePlayerStatsTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
