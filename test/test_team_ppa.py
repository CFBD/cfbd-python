# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.6
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.team_ppa import TeamPPA  # noqa: E501

class TestTeamPPA(unittest.TestCase):
    """TeamPPA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamPPA:
        """Test TeamPPA
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamPPA`
        """
        model = TeamPPA()  # noqa: E501
        if include_optional:
            return TeamPPA(
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
                rushing = cfbd.models.stats_by_quarter.StatsByQuarter(
                    total = 1.337, 
                    quarter1 = 1.337, 
                    quarter2 = 1.337, 
                    quarter3 = 1.337, 
                    quarter4 = 1.337, )
            )
        else:
            return TeamPPA(
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
                rushing = cfbd.models.stats_by_quarter.StatsByQuarter(
                    total = 1.337, 
                    quarter1 = 1.337, 
                    quarter2 = 1.337, 
                    quarter3 = 1.337, 
                    quarter4 = 1.337, ),
        )
        """

    def testTeamPPA(self):
        """Test TeamPPA"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
