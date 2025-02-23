# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.scoreboard_game import ScoreboardGame  # noqa: E501

class TestScoreboardGame(unittest.TestCase):
    """ScoreboardGame unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScoreboardGame:
        """Test ScoreboardGame
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScoreboardGame`
        """
        model = ScoreboardGame()  # noqa: E501
        if include_optional:
            return ScoreboardGame(
                id = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time_tbd = True,
                tv = '',
                neutral_site = True,
                conference_game = True,
                status = 'scheduled',
                period = 56,
                clock = '',
                situation = '',
                possession = '',
                last_play = '',
                venue = cfbd.models.scoreboard_game_venue.ScoreboardGame_venue(
                    state = '', 
                    city = '', 
                    name = '', ),
                home_team = cfbd.models.scoreboard_game_home_team.ScoreboardGame_homeTeam(
                    line_scores = [
                        56
                        ], 
                    points = 56, 
                    classification = null, 
                    conference = '', 
                    name = '', 
                    id = 56, ),
                away_team = cfbd.models.scoreboard_game_home_team.ScoreboardGame_homeTeam(
                    line_scores = [
                        56
                        ], 
                    points = 56, 
                    classification = null, 
                    conference = '', 
                    name = '', 
                    id = 56, ),
                weather = cfbd.models.scoreboard_game_weather.ScoreboardGame_weather(
                    wind_direction = 1.337, 
                    wind_speed = 1.337, 
                    description = '', 
                    temperature = 1.337, ),
                betting = cfbd.models.scoreboard_game_betting.ScoreboardGame_betting(
                    away_moneyline = 1.337, 
                    home_moneyline = 1.337, 
                    over_under = 1.337, 
                    spread = 1.337, )
            )
        else:
            return ScoreboardGame(
                id = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time_tbd = True,
                tv = '',
                neutral_site = True,
                conference_game = True,
                status = 'scheduled',
                period = 56,
                clock = '',
                situation = '',
                possession = '',
                last_play = '',
                venue = cfbd.models.scoreboard_game_venue.ScoreboardGame_venue(
                    state = '', 
                    city = '', 
                    name = '', ),
                home_team = cfbd.models.scoreboard_game_home_team.ScoreboardGame_homeTeam(
                    line_scores = [
                        56
                        ], 
                    points = 56, 
                    classification = null, 
                    conference = '', 
                    name = '', 
                    id = 56, ),
                away_team = cfbd.models.scoreboard_game_home_team.ScoreboardGame_homeTeam(
                    line_scores = [
                        56
                        ], 
                    points = 56, 
                    classification = null, 
                    conference = '', 
                    name = '', 
                    id = 56, ),
                weather = cfbd.models.scoreboard_game_weather.ScoreboardGame_weather(
                    wind_direction = 1.337, 
                    wind_speed = 1.337, 
                    description = '', 
                    temperature = 1.337, ),
                betting = cfbd.models.scoreboard_game_betting.ScoreboardGame_betting(
                    away_moneyline = 1.337, 
                    home_moneyline = 1.337, 
                    over_under = 1.337, 
                    spread = 1.337, ),
        )
        """

    def testScoreboardGame(self):
        """Test ScoreboardGame"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
