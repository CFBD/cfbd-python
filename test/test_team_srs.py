# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.5.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.team_srs import TeamSRS  # noqa: E501

class TestTeamSRS(unittest.TestCase):
    """TeamSRS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamSRS:
        """Test TeamSRS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamSRS`
        """
        model = TeamSRS()  # noqa: E501
        if include_optional:
            return TeamSRS(
                year = 56,
                team = '',
                conference = '',
                division = '',
                rating = 1.337,
                ranking = 56
            )
        else:
            return TeamSRS(
                year = 56,
                team = '',
                conference = '',
                division = '',
                rating = 1.337,
                ranking = 56,
        )
        """

    def testTeamSRS(self):
        """Test TeamSRS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
