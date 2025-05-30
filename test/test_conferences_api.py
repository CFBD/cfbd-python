# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.18
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.conferences_api import ConferencesApi  # noqa: E501


class TestConferencesApi(unittest.TestCase):
    """ConferencesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConferencesApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_get_conferences(self) -> None:
        """Test case for get_conferences

        """
        pass


if __name__ == '__main__':
    unittest.main()
