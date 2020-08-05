# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.9
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.games_api import GamesApi  # noqa: E501
from cfbd.rest import ApiException


class TestGamesApi(unittest.TestCase):
    """GamesApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.games_api.GamesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_advanced_box_score(self):
        """Test case for get_advanced_box_score

        Advanced box scores  # noqa: E501
        """
        pass

    def test_get_game_media(self):
        """Test case for get_game_media

        Game media information and schedules  # noqa: E501
        """
        pass

    def test_get_games(self):
        """Test case for get_games

        Games and results  # noqa: E501
        """
        pass

    def test_get_player_game_stats(self):
        """Test case for get_player_game_stats

        Player game stats  # noqa: E501
        """
        pass

    def test_get_team_game_stats(self):
        """Test case for get_team_game_stats

        Team game stats  # noqa: E501
        """
        pass

    def test_get_team_records(self):
        """Test case for get_team_records

        Team records  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
