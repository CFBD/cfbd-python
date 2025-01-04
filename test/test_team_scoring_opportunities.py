# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.team_scoring_opportunities import TeamScoringOpportunities  # noqa: E501

class TestTeamScoringOpportunities(unittest.TestCase):
    """TeamScoringOpportunities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamScoringOpportunities:
        """Test TeamScoringOpportunities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamScoringOpportunities`
        """
        model = TeamScoringOpportunities()  # noqa: E501
        if include_optional:
            return TeamScoringOpportunities(
                team = '',
                opportunities = 56,
                points = 56,
                points_per_opportunity = 1.337
            )
        else:
            return TeamScoringOpportunities(
                team = '',
                opportunities = 56,
                points = 56,
                points_per_opportunity = 1.337,
        )
        """

    def testTeamScoringOpportunities(self):
        """Test TeamScoringOpportunities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
