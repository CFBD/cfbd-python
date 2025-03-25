# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.9
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.live_game_drive import LiveGameDrive  # noqa: E501

class TestLiveGameDrive(unittest.TestCase):
    """LiveGameDrive unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LiveGameDrive:
        """Test LiveGameDrive
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LiveGameDrive`
        """
        model = LiveGameDrive()  # noqa: E501
        if include_optional:
            return LiveGameDrive(
                id = '',
                offense_id = 56,
                offense = '',
                defense_id = 56,
                defense = '',
                play_count = 56,
                yards = 56,
                start_period = 56,
                start_clock = '',
                start_yards_to_goal = 56,
                end_period = 56,
                end_clock = '',
                end_yards_to_goal = 56,
                duration = '',
                scoring_opportunity = True,
                result = '',
                points_gained = 56,
                plays = [
                    cfbd.models.live_game_play.LiveGamePlay(
                        id = '', 
                        home_score = 56, 
                        away_score = 56, 
                        period = 56, 
                        clock = '', 
                        wall_clock = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        team_id = 56, 
                        team = '', 
                        down = 56, 
                        distance = 56, 
                        yards_to_goal = 56, 
                        yards_gained = 56, 
                        play_type_id = 56, 
                        play_type = '', 
                        epa = 1.337, 
                        garbage_time = True, 
                        success = True, 
                        rush_pash = 'rush', 
                        down_type = 'passing', 
                        play_text = '', )
                    ]
            )
        else:
            return LiveGameDrive(
                id = '',
                offense_id = 56,
                offense = '',
                defense_id = 56,
                defense = '',
                play_count = 56,
                yards = 56,
                start_period = 56,
                start_clock = '',
                start_yards_to_goal = 56,
                end_period = 56,
                end_clock = '',
                end_yards_to_goal = 56,
                duration = '',
                scoring_opportunity = True,
                result = '',
                points_gained = 56,
                plays = [
                    cfbd.models.live_game_play.LiveGamePlay(
                        id = '', 
                        home_score = 56, 
                        away_score = 56, 
                        period = 56, 
                        clock = '', 
                        wall_clock = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        team_id = 56, 
                        team = '', 
                        down = 56, 
                        distance = 56, 
                        yards_to_goal = 56, 
                        yards_gained = 56, 
                        play_type_id = 56, 
                        play_type = '', 
                        epa = 1.337, 
                        garbage_time = True, 
                        success = True, 
                        rush_pash = 'rush', 
                        down_type = 'passing', 
                        play_text = '', )
                    ],
        )
        """

    def testLiveGameDrive(self):
        """Test LiveGameDrive"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
