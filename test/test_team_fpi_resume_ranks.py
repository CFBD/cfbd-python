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

from cfbd.models.team_fpi_resume_ranks import TeamFPIResumeRanks  # noqa: E501

class TestTeamFPIResumeRanks(unittest.TestCase):
    """TeamFPIResumeRanks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamFPIResumeRanks:
        """Test TeamFPIResumeRanks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamFPIResumeRanks`
        """
        model = TeamFPIResumeRanks()  # noqa: E501
        if include_optional:
            return TeamFPIResumeRanks(
                game_control = 56,
                remaining_strength_of_schedule = 56,
                strength_of_schedule = 56,
                average_win_probability = 56,
                fpi = 56,
                strength_of_record = 56
            )
        else:
            return TeamFPIResumeRanks(
                game_control = 56,
                remaining_strength_of_schedule = 56,
                strength_of_schedule = 56,
                average_win_probability = 56,
                fpi = 56,
                strength_of_record = 56,
        )
        """

    def testTeamFPIResumeRanks(self):
        """Test TeamFPIResumeRanks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
