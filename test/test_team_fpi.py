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

from cfbd.models.team_fpi import TeamFPI  # noqa: E501

class TestTeamFPI(unittest.TestCase):
    """TeamFPI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamFPI:
        """Test TeamFPI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamFPI`
        """
        model = TeamFPI()  # noqa: E501
        if include_optional:
            return TeamFPI(
                year = 56,
                team = '',
                conference = '',
                fpi = 1.337,
                resume_ranks = cfbd.models.team_fpi_resume_ranks.TeamFPI_resumeRanks(
                    game_control = 56, 
                    remaining_strength_of_schedule = 56, 
                    strength_of_schedule = 56, 
                    average_win_probability = 56, 
                    fpi = 56, 
                    strength_of_record = 56, ),
                efficiencies = cfbd.models.team_fpi_efficiencies.TeamFPI_efficiencies(
                    special_teams = 1.337, 
                    defense = 1.337, 
                    offense = 1.337, 
                    overall = 1.337, )
            )
        else:
            return TeamFPI(
                year = 56,
                team = '',
                conference = '',
                fpi = 1.337,
                resume_ranks = cfbd.models.team_fpi_resume_ranks.TeamFPI_resumeRanks(
                    game_control = 56, 
                    remaining_strength_of_schedule = 56, 
                    strength_of_schedule = 56, 
                    average_win_probability = 56, 
                    fpi = 56, 
                    strength_of_record = 56, ),
                efficiencies = cfbd.models.team_fpi_efficiencies.TeamFPI_efficiencies(
                    special_teams = 1.337, 
                    defense = 1.337, 
                    offense = 1.337, 
                    overall = 1.337, ),
        )
        """

    def testTeamFPI(self):
        """Test TeamFPI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
