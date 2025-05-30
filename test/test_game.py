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

from cfbd.models.game import Game  # noqa: E501

class TestGame(unittest.TestCase):
    """Game unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Game:
        """Test Game
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Game`
        """
        model = Game()  # noqa: E501
        if include_optional:
            return Game(
                id = 56,
                season = 56,
                week = 56,
                season_type = 'regular',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time_tbd = True,
                completed = True,
                neutral_site = True,
                conference_game = True,
                attendance = 56,
                venue_id = 56,
                venue = '',
                home_id = 56,
                home_team = '',
                home_conference = '',
                home_classification = 'fbs',
                home_points = 56,
                home_line_scores = [
                    1.337
                    ],
                home_postgame_win_probability = 1.337,
                home_pregame_elo = 56,
                home_postgame_elo = 56,
                away_id = 56,
                away_team = '',
                away_conference = '',
                away_classification = 'fbs',
                away_points = 56,
                away_line_scores = [
                    1.337
                    ],
                away_postgame_win_probability = 1.337,
                away_pregame_elo = 56,
                away_postgame_elo = 56,
                excitement_index = 1.337,
                highlights = '',
                notes = ''
            )
        else:
            return Game(
                id = 56,
                season = 56,
                week = 56,
                season_type = 'regular',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time_tbd = True,
                completed = True,
                neutral_site = True,
                conference_game = True,
                attendance = 56,
                venue_id = 56,
                venue = '',
                home_id = 56,
                home_team = '',
                home_conference = '',
                home_classification = 'fbs',
                home_points = 56,
                home_line_scores = [
                    1.337
                    ],
                home_postgame_win_probability = 1.337,
                home_pregame_elo = 56,
                home_postgame_elo = 56,
                away_id = 56,
                away_team = '',
                away_conference = '',
                away_classification = 'fbs',
                away_points = 56,
                away_line_scores = [
                    1.337
                    ],
                away_postgame_win_probability = 1.337,
                away_pregame_elo = 56,
                away_postgame_elo = 56,
                excitement_index = 1.337,
                highlights = '',
                notes = '',
        )
        """

    def testGame(self):
        """Test Game"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
