# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.10
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.adjusted_metrics_api import AdjustedMetricsApi  # noqa: E501


class TestAdjustedMetricsApi(unittest.TestCase):
    """AdjustedMetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdjustedMetricsApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_adjusted_player_passing_stats(self) -> None:
        """Test case for get_adjusted_player_passing_stats

        """
        pass

    def test_get_adjusted_player_rushing_stats(self) -> None:
        """Test case for get_adjusted_player_rushing_stats

        """
        pass

    def test_get_adjusted_team_season_stats(self) -> None:
        """Test case for get_adjusted_team_season_stats

        """
        pass

    def test_get_kicker_paar(self) -> None:
        """Test case for get_kicker_paar

        """
        pass


if __name__ == '__main__':
    unittest.main()
