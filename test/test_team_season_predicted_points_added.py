# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.team_season_predicted_points_added import TeamSeasonPredictedPointsAdded  # noqa: E501

class TestTeamSeasonPredictedPointsAdded(unittest.TestCase):
    """TeamSeasonPredictedPointsAdded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamSeasonPredictedPointsAdded:
        """Test TeamSeasonPredictedPointsAdded
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamSeasonPredictedPointsAdded`
        """
        model = TeamSeasonPredictedPointsAdded()  # noqa: E501
        if include_optional:
            return TeamSeasonPredictedPointsAdded(
                season = 56,
                conference = '',
                team = '',
                offense = cfbd.models.team_season_predicted_points_added_offense.TeamSeasonPredictedPointsAdded_offense(
                    cumulative = cfbd.models.adjusted_team_metrics_epa.AdjustedTeamMetrics_epa(
                        rushing = 1.337, 
                        passing = 1.337, 
                        total = 1.337, ), 
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rushing = 1.337, 
                    passing = 1.337, 
                    overall = 1.337, ),
                defense = cfbd.models.team_season_predicted_points_added_offense.TeamSeasonPredictedPointsAdded_offense(
                    cumulative = cfbd.models.adjusted_team_metrics_epa.AdjustedTeamMetrics_epa(
                        rushing = 1.337, 
                        passing = 1.337, 
                        total = 1.337, ), 
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rushing = 1.337, 
                    passing = 1.337, 
                    overall = 1.337, )
            )
        else:
            return TeamSeasonPredictedPointsAdded(
                season = 56,
                conference = '',
                team = '',
                offense = cfbd.models.team_season_predicted_points_added_offense.TeamSeasonPredictedPointsAdded_offense(
                    cumulative = cfbd.models.adjusted_team_metrics_epa.AdjustedTeamMetrics_epa(
                        rushing = 1.337, 
                        passing = 1.337, 
                        total = 1.337, ), 
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rushing = 1.337, 
                    passing = 1.337, 
                    overall = 1.337, ),
                defense = cfbd.models.team_season_predicted_points_added_offense.TeamSeasonPredictedPointsAdded_offense(
                    cumulative = cfbd.models.adjusted_team_metrics_epa.AdjustedTeamMetrics_epa(
                        rushing = 1.337, 
                        passing = 1.337, 
                        total = 1.337, ), 
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rushing = 1.337, 
                    passing = 1.337, 
                    overall = 1.337, ),
        )
        """

    def testTeamSeasonPredictedPointsAdded(self):
        """Test TeamSeasonPredictedPointsAdded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
