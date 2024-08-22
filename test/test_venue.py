# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.11
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.venue import Venue  # noqa: E501

class TestVenue(unittest.TestCase):
    """Venue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Venue:
        """Test Venue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Venue`
        """
        model = Venue()  # noqa: E501
        if include_optional:
            return Venue(
                id = 56,
                name = '',
                city = '',
                state = '',
                zip = '',
                country_code = '',
                timezone = '',
                latitude = 1.337,
                longitude = 1.337,
                elevation = '',
                capacity = 56,
                construction_year = 56,
                grass = True,
                dome = True
            )
        else:
            return Venue(
                id = 56,
                name = '',
                city = '',
                state = '',
                zip = '',
                country_code = '',
                timezone = '',
                latitude = 1.337,
                longitude = 1.337,
                elevation = '',
                capacity = 56,
                construction_year = 56,
        )
        """

    def testVenue(self):
        """Test Venue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
