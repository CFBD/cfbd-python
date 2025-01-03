# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.team_fpi_efficiencies import TeamFPIEfficiencies  # noqa: E501

class TestTeamFPIEfficiencies(unittest.TestCase):
    """TeamFPIEfficiencies unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamFPIEfficiencies:
        """Test TeamFPIEfficiencies
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamFPIEfficiencies`
        """
        model = TeamFPIEfficiencies()  # noqa: E501
        if include_optional:
            return TeamFPIEfficiencies(
                special_teams = 1.337,
                defense = 1.337,
                offense = 1.337,
                overall = 1.337
            )
        else:
            return TeamFPIEfficiencies(
                special_teams = 1.337,
                defense = 1.337,
                offense = 1.337,
                overall = 1.337,
        )
        """

    def testTeamFPIEfficiencies(self):
        """Test TeamFPIEfficiencies"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
