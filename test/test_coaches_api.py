# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.15
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.coaches_api import CoachesApi  # noqa: E501
from cfbd.rest import ApiException


class TestCoachesApi(unittest.TestCase):
    """CoachesApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.coaches_api.CoachesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_coaches(self):
        """Test case for get_coaches

        Coaching records and history  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
