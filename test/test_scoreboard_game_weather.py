# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.18
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.scoreboard_game_weather import ScoreboardGameWeather  # noqa: E501

class TestScoreboardGameWeather(unittest.TestCase):
    """ScoreboardGameWeather unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScoreboardGameWeather:
        """Test ScoreboardGameWeather
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScoreboardGameWeather`
        """
        model = ScoreboardGameWeather()  # noqa: E501
        if include_optional:
            return ScoreboardGameWeather(
                wind_direction = 1.337,
                wind_speed = 1.337,
                description = '',
                temperature = 1.337
            )
        else:
            return ScoreboardGameWeather(
                wind_direction = 1.337,
                wind_speed = 1.337,
                description = '',
                temperature = 1.337,
        )
        """

    def testScoreboardGameWeather(self):
        """Test ScoreboardGameWeather"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
