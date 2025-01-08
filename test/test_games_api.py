# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.games_api import GamesApi  # noqa: E501


class TestGamesApi(unittest.TestCase):
    """GamesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GamesApi()

    def tearDown(self) -> None:
        pass

    def test_get_advanced_box_score(self) -> None:
        """Test case for get_advanced_box_score

        """
        pass

    def test_get_calendar(self) -> None:
        """Test case for get_calendar

        """
        pass

    def test_get_game_player_stats(self) -> None:
        """Test case for get_game_player_stats

        """
        pass

    def test_get_game_team_stats(self) -> None:
        """Test case for get_game_team_stats

        """
        pass

    def test_get_games(self) -> None:
        """Test case for get_games

        """
        pass

    def test_get_media(self) -> None:
        """Test case for get_media

        """
        pass

    def test_get_records(self) -> None:
        """Test case for get_records

        """
        pass

    def test_get_scoreboard(self) -> None:
        """Test case for get_scoreboard

        """
        pass

    def test_get_weather(self) -> None:
        """Test case for get_weather

        """
        pass


if __name__ == '__main__':
    unittest.main()
