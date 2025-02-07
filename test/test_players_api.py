# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.10
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.players_api import PlayersApi  # noqa: E501


class TestPlayersApi(unittest.TestCase):
    """PlayersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlayersApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_player_usage(self) -> None:
        """Test case for get_player_usage

        """
        pass

    def test_get_returning_production(self) -> None:
        """Test case for get_returning_production

        """
        pass

    def test_get_transfer_portal(self) -> None:
        """Test case for get_transfer_portal

        """
        pass

    def test_search_players(self) -> None:
        """Test case for search_players

        """
        pass


if __name__ == '__main__':
    unittest.main()
