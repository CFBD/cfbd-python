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

from cfbd.models.team_game_predicted_points_added_offense import TeamGamePredictedPointsAddedOffense  # noqa: E501

class TestTeamGamePredictedPointsAddedOffense(unittest.TestCase):
    """TeamGamePredictedPointsAddedOffense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamGamePredictedPointsAddedOffense:
        """Test TeamGamePredictedPointsAddedOffense
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamGamePredictedPointsAddedOffense`
        """
        model = TeamGamePredictedPointsAddedOffense()  # noqa: E501
        if include_optional:
            return TeamGamePredictedPointsAddedOffense(
                third_down = 1.337,
                second_down = 1.337,
                first_down = 1.337,
                rushing = 1.337,
                passing = 1.337,
                overall = 1.337
            )
        else:
            return TeamGamePredictedPointsAddedOffense(
                third_down = 1.337,
                second_down = 1.337,
                first_down = 1.337,
                rushing = 1.337,
                passing = 1.337,
                overall = 1.337,
        )
        """

    def testTeamGamePredictedPointsAddedOffense(self):
        """Test TeamGamePredictedPointsAddedOffense"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
