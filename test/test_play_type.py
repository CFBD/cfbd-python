# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.7
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.play_type import PlayType  # noqa: E501

class TestPlayType(unittest.TestCase):
    """PlayType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayType:
        """Test PlayType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayType`
        """
        model = PlayType()  # noqa: E501
        if include_optional:
            return PlayType(
                id = 56,
                text = '',
                abbreviation = ''
            )
        else:
            return PlayType(
                id = 56,
                text = '',
                abbreviation = '',
        )
        """

    def testPlayType(self):
        """Test PlayType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
