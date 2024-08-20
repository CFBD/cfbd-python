# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.10
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.play_win_probability import PlayWinProbability  # noqa: E501

class TestPlayWinProbability(unittest.TestCase):
    """PlayWinProbability unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayWinProbability:
        """Test PlayWinProbability
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayWinProbability`
        """
        model = PlayWinProbability()  # noqa: E501
        if include_optional:
            return PlayWinProbability(
                game_id = 56,
                play_id = '',
                play_text = '',
                home_id = 56,
                home = '',
                away_id = 56,
                away = '',
                spread = 1.337,
                home_ball = True,
                home_score = 56,
                away_score = 56,
                yard_line = 56,
                down = 56,
                distance = 56,
                home_win_probability = 1.337,
                play_number = 56
            )
        else:
            return PlayWinProbability(
                game_id = 56,
                play_id = '',
                play_text = '',
                home_id = 56,
                home = '',
                away_id = 56,
                away = '',
                spread = 1.337,
                home_ball = True,
                home_score = 56,
                away_score = 56,
                yard_line = 56,
                down = 56,
                distance = 56,
                home_win_probability = 1.337,
                play_number = 56,
        )
        """

    def testPlayWinProbability(self):
        """Test PlayWinProbability"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()