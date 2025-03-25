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

from cfbd.models.live_game import LiveGame  # noqa: E501

class TestLiveGame(unittest.TestCase):
    """LiveGame unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LiveGame:
        """Test LiveGame
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LiveGame`
        """
        model = LiveGame()  # noqa: E501
        if include_optional:
            return LiveGame(
                id = 56,
                status = '',
                period = 56,
                clock = '',
                possession = '',
                down = 56,
                distance = 56,
                yards_to_goal = 56,
                teams = [
                    cfbd.models.live_game_team.LiveGameTeam(
                        team_id = 56, 
                        team = '', 
                        home_away = 'home', 
                        line_scores = [
                            56
                            ], 
                        points = 56, 
                        drives = 56, 
                        scoring_opportunities = 56, 
                        points_per_opportunity = 1.337, 
                        plays = 56, 
                        line_yards = 1.337, 
                        line_yards_per_rush = 1.337, 
                        second_level_yards = 1.337, 
                        second_level_yards_per_rush = 1.337, 
                        open_field_yards = 1.337, 
                        open_field_yards_per_rush = 1.337, 
                        epa_per_play = 1.337, 
                        total_epa = 1.337, 
                        passing_epa = 1.337, 
                        epa_per_pass = 1.337, 
                        rushing_epa = 1.337, 
                        epa_per_rush = 1.337, 
                        success_rate = 1.337, 
                        standard_down_success_rate = 1.337, 
                        passing_down_success_rate = 1.337, 
                        explosiveness = 1.337, )
                    ],
                drives = [
                    cfbd.models.live_game_drive.LiveGameDrive(
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
                            ], )
                    ]
            )
        else:
            return LiveGame(
                id = 56,
                status = '',
                period = 56,
                clock = '',
                possession = '',
                down = 56,
                distance = 56,
                yards_to_goal = 56,
                teams = [
                    cfbd.models.live_game_team.LiveGameTeam(
                        team_id = 56, 
                        team = '', 
                        home_away = 'home', 
                        line_scores = [
                            56
                            ], 
                        points = 56, 
                        drives = 56, 
                        scoring_opportunities = 56, 
                        points_per_opportunity = 1.337, 
                        plays = 56, 
                        line_yards = 1.337, 
                        line_yards_per_rush = 1.337, 
                        second_level_yards = 1.337, 
                        second_level_yards_per_rush = 1.337, 
                        open_field_yards = 1.337, 
                        open_field_yards_per_rush = 1.337, 
                        epa_per_play = 1.337, 
                        total_epa = 1.337, 
                        passing_epa = 1.337, 
                        epa_per_pass = 1.337, 
                        rushing_epa = 1.337, 
                        epa_per_rush = 1.337, 
                        success_rate = 1.337, 
                        standard_down_success_rate = 1.337, 
                        passing_down_success_rate = 1.337, 
                        explosiveness = 1.337, )
                    ],
                drives = [
                    cfbd.models.live_game_drive.LiveGameDrive(
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
                            ], )
                    ],
        )
        """

    def testLiveGame(self):
        """Test LiveGame"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
