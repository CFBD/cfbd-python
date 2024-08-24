# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.14
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.plays_api import PlaysApi  # noqa: E501


class TestPlaysApi(unittest.TestCase):
    """PlaysApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlaysApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

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
