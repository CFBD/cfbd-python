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

from cfbd.models.advanced_season_stat_offense import AdvancedSeasonStatOffense  # noqa: E501

class TestAdvancedSeasonStatOffense(unittest.TestCase):
    """AdvancedSeasonStatOffense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvancedSeasonStatOffense:
        """Test AdvancedSeasonStatOffense
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvancedSeasonStatOffense`
        """
        model = AdvancedSeasonStatOffense()  # noqa: E501
        if include_optional:
            return AdvancedSeasonStatOffense(
                passing_plays = cfbd.models.advanced_season_stat_offense_passing_plays.AdvancedSeasonStat_offense_passingPlays(
                    explosiveness = 1.337, 
                    success_rate = 1.337, 
                    total_ppa = 1.337, 
                    ppa = 1.337, 
                    rate = 1.337, ),
                rushing_plays = cfbd.models.advanced_season_stat_offense_passing_plays.AdvancedSeasonStat_offense_passingPlays(
                    explosiveness = 1.337, 
                    success_rate = 1.337, 
                    total_ppa = 1.337, 
                    ppa = 1.337, 
                    rate = 1.337, ),
                passing_downs = cfbd.models.advanced_season_stat_offense_passing_downs.AdvancedSeasonStat_offense_passingDowns(
                    explosiveness = 1.337, 
                    success_rate = 1.337, 
                    ppa = 1.337, 
                    rate = 1.337, ),
                standard_downs = cfbd.models.advanced_season_stat_offense_passing_downs.AdvancedSeasonStat_offense_passingDowns(
                    explosiveness = 1.337, 
                    success_rate = 1.337, 
                    ppa = 1.337, 
                    rate = 1.337, ),
                havoc = cfbd.models.advanced_season_stat_offense_havoc.AdvancedSeasonStat_offense_havoc(
                    db = 1.337, 
                    front_seven = 1.337, 
                    total = 1.337, ),
                field_position = cfbd.models.advanced_season_stat_offense_field_position.AdvancedSeasonStat_offense_fieldPosition(
                    average_predicted_points = 1.337, 
                    average_start = 1.337, ),
                points_per_opportunity = 1.337,
                total_opportunies = 56,
                open_field_yards_total = 56,
                open_field_yards = 1.337,
                second_level_yards_total = 56,
                second_level_yards = 1.337,
                line_yards_total = 56,
                line_yards = 1.337,
                stuff_rate = 1.337,
                power_success = 1.337,
                explosiveness = 1.337,
                success_rate = 1.337,
                total_ppa = 1.337,
                ppa = 1.337,
                drives = 56,
                plays = 56
            )
        else:
            return AdvancedSeasonStatOffense(
                passing_plays = cfbd.models.advanced_season_stat_offense_passing_plays.AdvancedSeasonStat_offense_passingPlays(
                    explosiveness = 1.337, 
                    success_rate = 1.337, 
                    total_ppa = 1.337, 
                    ppa = 1.337, 
                    rate = 1.337, ),
                rushing_plays = cfbd.models.advanced_season_stat_offense_passing_plays.AdvancedSeasonStat_offense_passingPlays(
                    explosiveness = 1.337, 
                    success_rate = 1.337, 
                    total_ppa = 1.337, 
                    ppa = 1.337, 
                    rate = 1.337, ),
                passing_downs = cfbd.models.advanced_season_stat_offense_passing_downs.AdvancedSeasonStat_offense_passingDowns(
                    explosiveness = 1.337, 
                    success_rate = 1.337, 
                    ppa = 1.337, 
                    rate = 1.337, ),
                standard_downs = cfbd.models.advanced_season_stat_offense_passing_downs.AdvancedSeasonStat_offense_passingDowns(
                    explosiveness = 1.337, 
                    success_rate = 1.337, 
                    ppa = 1.337, 
                    rate = 1.337, ),
                havoc = cfbd.models.advanced_season_stat_offense_havoc.AdvancedSeasonStat_offense_havoc(
                    db = 1.337, 
                    front_seven = 1.337, 
                    total = 1.337, ),
                field_position = cfbd.models.advanced_season_stat_offense_field_position.AdvancedSeasonStat_offense_fieldPosition(
                    average_predicted_points = 1.337, 
                    average_start = 1.337, ),
                points_per_opportunity = 1.337,
                total_opportunies = 56,
                open_field_yards_total = 56,
                open_field_yards = 1.337,
                second_level_yards_total = 56,
                second_level_yards = 1.337,
                line_yards_total = 56,
                line_yards = 1.337,
                stuff_rate = 1.337,
                power_success = 1.337,
                explosiveness = 1.337,
                success_rate = 1.337,
                total_ppa = 1.337,
                ppa = 1.337,
                drives = 56,
                plays = 56,
        )
        """

    def testAdvancedSeasonStatOffense(self):
        """Test AdvancedSeasonStatOffense"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
