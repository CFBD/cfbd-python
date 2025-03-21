# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.8
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.coaches_api import CoachesApi  # noqa: E501


class TestCoachesApi(unittest.TestCase):
    """CoachesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CoachesApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_coaches(self) -> None:
        """Test case for get_coaches

        """
        pass


if __name__ == '__main__':
    unittest.main()
