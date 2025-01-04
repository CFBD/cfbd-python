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

from cfbd.models.stats_by_quarter import StatsByQuarter  # noqa: E501

class TestStatsByQuarter(unittest.TestCase):
    """StatsByQuarter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatsByQuarter:
        """Test StatsByQuarter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatsByQuarter`
        """
        model = StatsByQuarter()  # noqa: E501
        if include_optional:
            return StatsByQuarter(
                total = 1.337,
                quarter1 = 1.337,
                quarter2 = 1.337,
                quarter3 = 1.337,
                quarter4 = 1.337
            )
        else:
            return StatsByQuarter(
                total = 1.337,
                quarter1 = 1.337,
                quarter2 = 1.337,
                quarter3 = 1.337,
                quarter4 = 1.337,
        )
        """

    def testStatsByQuarter(self):
        """Test StatsByQuarter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
