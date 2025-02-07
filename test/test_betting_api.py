# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.5.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.betting_api import BettingApi  # noqa: E501


class TestBettingApi(unittest.TestCase):
    """BettingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BettingApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_lines(self) -> None:
        """Test case for get_lines

        """
        pass


if __name__ == '__main__':
    unittest.main()
