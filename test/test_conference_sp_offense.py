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

from cfbd.models.conference_sp_offense import ConferenceSPOffense  # noqa: E501

class TestConferenceSPOffense(unittest.TestCase):
    """ConferenceSPOffense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConferenceSPOffense:
        """Test ConferenceSPOffense
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConferenceSPOffense`
        """
        model = ConferenceSPOffense()  # noqa: E501
        if include_optional:
            return ConferenceSPOffense(
                pace = 1.337,
                run_rate = 1.337,
                passing_downs = 1.337,
                standard_downs = 1.337,
                passing = 1.337,
                rushing = 1.337,
                explosiveness = 1.337,
                success = 1.337,
                rating = 1.337
            )
        else:
            return ConferenceSPOffense(
                pace = 1.337,
                run_rate = 1.337,
                passing_downs = 1.337,
                standard_downs = 1.337,
                passing = 1.337,
                rushing = 1.337,
                explosiveness = 1.337,
                success = 1.337,
                rating = 1.337,
        )
        """

    def testConferenceSPOffense(self):
        """Test ConferenceSPOffense"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
