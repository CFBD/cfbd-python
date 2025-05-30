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

from cfbd.models.team_game_predicted_points_added import TeamGamePredictedPointsAdded  # noqa: E501

class TestTeamGamePredictedPointsAdded(unittest.TestCase):
    """TeamGamePredictedPointsAdded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamGamePredictedPointsAdded:
        """Test TeamGamePredictedPointsAdded
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamGamePredictedPointsAdded`
        """
        model = TeamGamePredictedPointsAdded()  # noqa: E501
        if include_optional:
            return TeamGamePredictedPointsAdded(
                game_id = 56,
                season = 56,
                week = 56,
                season_type = 'regular',
                team = '',
                conference = '',
                opponent = '',
                offense = cfbd.models.team_game_predicted_points_added_offense.TeamGamePredictedPointsAdded_offense(
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rushing = 1.337, 
                    passing = 1.337, 
                    overall = 1.337, ),
                defense = cfbd.models.team_game_predicted_points_added_offense.TeamGamePredictedPointsAdded_offense(
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rushing = 1.337, 
                    passing = 1.337, 
                    overall = 1.337, )
            )
        else:
            return TeamGamePredictedPointsAdded(
                game_id = 56,
                season = 56,
                week = 56,
                season_type = 'regular',
                team = '',
                conference = '',
                opponent = '',
                offense = cfbd.models.team_game_predicted_points_added_offense.TeamGamePredictedPointsAdded_offense(
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rushing = 1.337, 
                    passing = 1.337, 
                    overall = 1.337, ),
                defense = cfbd.models.team_game_predicted_points_added_offense.TeamGamePredictedPointsAdded_offense(
                    third_down = 1.337, 
                    second_down = 1.337, 
                    first_down = 1.337, 
                    rushing = 1.337, 
                    passing = 1.337, 
                    overall = 1.337, ),
        )
        """

    def testTeamGamePredictedPointsAdded(self):
        """Test TeamGamePredictedPointsAdded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
