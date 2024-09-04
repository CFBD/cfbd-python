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

from cfbd.models.advanced_box_score_teams import AdvancedBoxScoreTeams  # noqa: E501

class TestAdvancedBoxScoreTeams(unittest.TestCase):
    """AdvancedBoxScoreTeams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvancedBoxScoreTeams:
        """Test AdvancedBoxScoreTeams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvancedBoxScoreTeams`
        """
        model = AdvancedBoxScoreTeams()  # noqa: E501
        if include_optional:
            return AdvancedBoxScoreTeams(
                field_position = [
                    cfbd.models.team_field_position.TeamFieldPosition(
                        team = '', 
                        average_start = 1.337, 
                        average_starting_predicted_points = 1.337, )
                    ],
                scoring_opportunities = [
                    cfbd.models.team_scoring_opportunities.TeamScoringOpportunities(
                        team = '', 
                        opportunities = 56, 
                        points = 56, 
                        points_per_opportunity = 1.337, )
                    ],
                havoc = [
                    cfbd.models.team_havoc.TeamHavoc(
                        team = '', 
                        total = 1.337, 
                        front_seven = 1.337, 
                        db = 1.337, )
                    ],
                rushing = [
                    cfbd.models.team_rushing_stats.TeamRushingStats(
                        team = '', 
                        power_success = 1.337, 
                        stuff_rate = 1.337, 
                        line_yards = 1.337, 
                        line_yards_average = 1.337, 
                        second_level_yards = 1.337, 
                        second_level_yards_average = 1.337, 
                        open_field_yards = 1.337, 
                        open_field_yards_average = 1.337, )
                    ],
                explosiveness = [
                    cfbd.models.team_explosiveness.TeamExplosiveness(
                        team = '', 
                        overall = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), )
                    ],
                success_rates = [
                    cfbd.models.team_success_rates.TeamSuccessRates(
                        team = '', 
                        overall = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        standard_downs = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        passing_downs = , )
                    ],
                cumulative_ppa = [
                    cfbd.models.team_ppa.TeamPPA(
                        team = '', 
                        plays = 56, 
                        overall = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        passing = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        rushing = , )
                    ],
                ppa = [
                    cfbd.models.team_ppa.TeamPPA(
                        team = '', 
                        plays = 56, 
                        overall = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        passing = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        rushing = , )
                    ]
            )
        else:
            return AdvancedBoxScoreTeams(
                field_position = [
                    cfbd.models.team_field_position.TeamFieldPosition(
                        team = '', 
                        average_start = 1.337, 
                        average_starting_predicted_points = 1.337, )
                    ],
                scoring_opportunities = [
                    cfbd.models.team_scoring_opportunities.TeamScoringOpportunities(
                        team = '', 
                        opportunities = 56, 
                        points = 56, 
                        points_per_opportunity = 1.337, )
                    ],
                havoc = [
                    cfbd.models.team_havoc.TeamHavoc(
                        team = '', 
                        total = 1.337, 
                        front_seven = 1.337, 
                        db = 1.337, )
                    ],
                rushing = [
                    cfbd.models.team_rushing_stats.TeamRushingStats(
                        team = '', 
                        power_success = 1.337, 
                        stuff_rate = 1.337, 
                        line_yards = 1.337, 
                        line_yards_average = 1.337, 
                        second_level_yards = 1.337, 
                        second_level_yards_average = 1.337, 
                        open_field_yards = 1.337, 
                        open_field_yards_average = 1.337, )
                    ],
                explosiveness = [
                    cfbd.models.team_explosiveness.TeamExplosiveness(
                        team = '', 
                        overall = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), )
                    ],
                success_rates = [
                    cfbd.models.team_success_rates.TeamSuccessRates(
                        team = '', 
                        overall = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        standard_downs = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        passing_downs = , )
                    ],
                cumulative_ppa = [
                    cfbd.models.team_ppa.TeamPPA(
                        team = '', 
                        plays = 56, 
                        overall = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        passing = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        rushing = , )
                    ],
                ppa = [
                    cfbd.models.team_ppa.TeamPPA(
                        team = '', 
                        plays = 56, 
                        overall = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        passing = cfbd.models.stats_by_quarter.StatsByQuarter(
                            total = 1.337, 
                            quarter1 = 1.337, 
                            quarter2 = 1.337, 
                            quarter3 = 1.337, 
                            quarter4 = 1.337, ), 
                        rushing = , )
                    ],
        )
        """

    def testAdvancedBoxScoreTeams(self):
        """Test AdvancedBoxScoreTeams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
