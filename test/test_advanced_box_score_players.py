# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.9
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.advanced_box_score_players import AdvancedBoxScorePlayers  # noqa: E501

class TestAdvancedBoxScorePlayers(unittest.TestCase):
    """AdvancedBoxScorePlayers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvancedBoxScorePlayers:
        """Test AdvancedBoxScorePlayers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvancedBoxScorePlayers`
        """
        model = AdvancedBoxScorePlayers()  # noqa: E501
        if include_optional:
            return AdvancedBoxScorePlayers(
                ppa = [
                    cfbd.models.player_ppa.PlayerPPA(
                        player = '', 
                        team = '', 
                        position = '', 
                        average = cfbd.models.player_stats_by_quarter.PlayerStatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, 
                            rushing = 1.337, 
                            passing = 1.337, ), 
                        cumulative = cfbd.models.player_stats_by_quarter.PlayerStatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, 
                            rushing = 1.337, 
                            passing = 1.337, ), )
                    ],
                usage = [
                    cfbd.models.player_game_usage.PlayerGameUsage(
                        total = 1.337, 
                        quarter1 = 1.337, 
                        quarter2 = 1.337, 
                        quarter3 = 1.337, 
                        quarter4 = 1.337, 
                        rushing = 1.337, 
                        passing = 1.337, 
                        player = '', 
                        team = '', 
                        position = '', )
                    ]
            )
        else:
            return AdvancedBoxScorePlayers(
                ppa = [
                    cfbd.models.player_ppa.PlayerPPA(
                        player = '', 
                        team = '', 
                        position = '', 
                        average = cfbd.models.player_stats_by_quarter.PlayerStatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, 
                            rushing = 1.337, 
                            passing = 1.337, ), 
                        cumulative = cfbd.models.player_stats_by_quarter.PlayerStatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, 
                            rushing = 1.337, 
                            passing = 1.337, ), )
                    ],
                usage = [
                    cfbd.models.player_game_usage.PlayerGameUsage(
                        total = 1.337, 
                        quarter1 = 1.337, 
                        quarter2 = 1.337, 
                        quarter3 = 1.337, 
                        quarter4 = 1.337, 
                        rushing = 1.337, 
                        passing = 1.337, 
                        player = '', 
                        team = '', 
                        position = '', )
                    ],
        )
        """

    def testAdvancedBoxScorePlayers(self):
        """Test AdvancedBoxScorePlayers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
