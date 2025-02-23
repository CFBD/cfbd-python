# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.returning_production import ReturningProduction  # noqa: E501

class TestReturningProduction(unittest.TestCase):
    """ReturningProduction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturningProduction:
        """Test ReturningProduction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturningProduction`
        """
        model = ReturningProduction()  # noqa: E501
        if include_optional:
            return ReturningProduction(
                season = 56,
                team = '',
                conference = '',
                total_ppa = 1.337,
                total_passing_ppa = 1.337,
                total_receiving_ppa = 1.337,
                total_rushing_ppa = 1.337,
                percent_ppa = 1.337,
                percent_passing_ppa = 1.337,
                percent_receiving_ppa = 1.337,
                percent_rushing_ppa = 1.337,
                usage = 1.337,
                passing_usage = 1.337,
                receiving_usage = 1.337,
                rushing_usage = 1.337
            )
        else:
            return ReturningProduction(
                season = 56,
                team = '',
                conference = '',
                total_ppa = 1.337,
                total_passing_ppa = 1.337,
                total_receiving_ppa = 1.337,
                total_rushing_ppa = 1.337,
                percent_ppa = 1.337,
                percent_passing_ppa = 1.337,
                percent_receiving_ppa = 1.337,
                percent_rushing_ppa = 1.337,
                usage = 1.337,
                passing_usage = 1.337,
                receiving_usage = 1.337,
                rushing_usage = 1.337,
        )
        """

    def testReturningProduction(self):
        """Test ReturningProduction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
