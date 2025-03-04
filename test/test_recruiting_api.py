# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.6
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.recruiting_api import RecruitingApi  # noqa: E501


class TestRecruitingApi(unittest.TestCase):
    """RecruitingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RecruitingApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_aggregated_team_recruiting_ratings(self) -> None:
        """Test case for get_aggregated_team_recruiting_ratings

        """
        pass

    def test_get_recruits(self) -> None:
        """Test case for get_recruits

        """
        pass

    def test_get_team_recruiting_rankings(self) -> None:
        """Test case for get_team_recruiting_rankings

        """
        pass


if __name__ == '__main__':
    unittest.main()
