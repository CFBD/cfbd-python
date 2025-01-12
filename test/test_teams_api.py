# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.5
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.teams_api import TeamsApi  # noqa: E501


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TeamsApi()

    def tearDown(self) -> None:
        pass

    def test_get_fbs_teams(self) -> None:
        """Test case for get_fbs_teams

        """
        pass

    def test_get_matchup(self) -> None:
        """Test case for get_matchup

        """
        pass

    def test_get_roster(self) -> None:
        """Test case for get_roster

        """
        pass

    def test_get_talent(self) -> None:
        """Test case for get_talent

        """
        pass

    def test_get_teams(self) -> None:
        """Test case for get_teams

        """
        pass


if __name__ == '__main__':
    unittest.main()
