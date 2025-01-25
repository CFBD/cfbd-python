# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.8
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.ratings_api import RatingsApi  # noqa: E501


class TestRatingsApi(unittest.TestCase):
    """RatingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RatingsApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_conference_sp(self) -> None:
        """Test case for get_conference_sp

        """
        pass

    def test_get_elo(self) -> None:
        """Test case for get_elo

        """
        pass

    def test_get_fpi(self) -> None:
        """Test case for get_fpi

        """
        pass

    def test_get_sp(self) -> None:
        """Test case for get_sp

        """
        pass

    def test_get_srs(self) -> None:
        """Test case for get_srs

        """
        pass


if __name__ == '__main__':
    unittest.main()
