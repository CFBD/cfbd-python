# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.3.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.team import Team  # noqa: E501

class TestTeam(unittest.TestCase):
    """Team unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Team:
        """Test Team
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Team`
        """
        model = Team()  # noqa: E501
        if include_optional:
            return Team(
                id = 56,
                school = '',
                mascot = '',
                abbreviation = '',
                alternate_names = [
                    ''
                    ],
                conference = '',
                division = '',
                classification = '',
                color = '',
                alternate_color = '',
                logos = [
                    ''
                    ],
                twitter = '',
                location = cfbd.models.venue.Venue(
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
                    dome = True, )
            )
        else:
            return Team(
                id = 56,
                school = '',
                mascot = '',
                abbreviation = '',
                alternate_names = [
                    ''
                    ],
                conference = '',
                division = '',
                classification = '',
                color = '',
                alternate_color = '',
                logos = [
                    ''
                    ],
                twitter = '',
                location = cfbd.models.venue.Venue(
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
                    dome = True, ),
        )
        """

    def testTeam(self):
        """Test Team"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
