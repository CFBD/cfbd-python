# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.5.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.field_goal_ep import FieldGoalEP  # noqa: E501

class TestFieldGoalEP(unittest.TestCase):
    """FieldGoalEP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FieldGoalEP:
        """Test FieldGoalEP
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FieldGoalEP`
        """
        model = FieldGoalEP()  # noqa: E501
        if include_optional:
            return FieldGoalEP(
                yards_to_goal = 56,
                distance = 56,
                expected_points = 1.337
            )
        else:
            return FieldGoalEP(
                yards_to_goal = 56,
                distance = 56,
                expected_points = 1.337,
        )
        """

    def testFieldGoalEP(self):
        """Test FieldGoalEP"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
