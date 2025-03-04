# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.4
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.game_media import GameMedia  # noqa: E501

class TestGameMedia(unittest.TestCase):
    """GameMedia unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameMedia:
        """Test GameMedia
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameMedia`
        """
        model = GameMedia()  # noqa: E501
        if include_optional:
            return GameMedia(
                id = 56,
                season = 56,
                week = 56,
                season_type = 'regular',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_start_time_tbd = True,
                home_team = '',
                home_conference = '',
                away_team = '',
                away_conference = '',
                media_type = 'tv',
                outlet = ''
            )
        else:
            return GameMedia(
                id = 56,
                season = 56,
                week = 56,
                season_type = 'regular',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_start_time_tbd = True,
                home_team = '',
                home_conference = '',
                away_team = '',
                away_conference = '',
                media_type = 'tv',
                outlet = '',
        )
        """

    def testGameMedia(self):
        """Test GameMedia"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
