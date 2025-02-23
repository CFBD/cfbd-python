# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.aggregated_team_recruiting import AggregatedTeamRecruiting  # noqa: E501

class TestAggregatedTeamRecruiting(unittest.TestCase):
    """AggregatedTeamRecruiting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregatedTeamRecruiting:
        """Test AggregatedTeamRecruiting
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregatedTeamRecruiting`
        """
        model = AggregatedTeamRecruiting()  # noqa: E501
        if include_optional:
            return AggregatedTeamRecruiting(
                team = '',
                conference = '',
                position_group = '',
                average_rating = 1.337,
                total_rating = 1.337,
                commits = 56,
                average_stars = 1.337
            )
        else:
            return AggregatedTeamRecruiting(
                team = '',
                conference = '',
                position_group = '',
                average_rating = 1.337,
                total_rating = 1.337,
                commits = 56,
                average_stars = 1.337,
        )
        """

    def testAggregatedTeamRecruiting(self):
        """Test AggregatedTeamRecruiting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
