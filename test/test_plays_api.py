# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.plays_api import PlaysApi  # noqa: E501


class TestPlaysApi(unittest.TestCase):
    """PlaysApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlaysApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_live_plays(self) -> None:
        """Test case for get_live_plays

        """
        pass

    def test_get_play_stat_types(self) -> None:
        """Test case for get_play_stat_types

        """
        pass

    def test_get_play_stats(self) -> None:
        """Test case for get_play_stats

        """
        pass

    def test_get_play_types(self) -> None:
        """Test case for get_play_types

        """
        pass

    def test_get_plays(self) -> None:
        """Test case for get_plays

        """
        pass


if __name__ == '__main__':
    unittest.main()
