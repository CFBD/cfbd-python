# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.8
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.models.scoreboard_game import ScoreboardGame  # noqa: E501
from cfbd.rest import ApiException


class TestScoreboardGame(unittest.TestCase):
    """ScoreboardGame unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScoreboardGame(self):
        """Test ScoreboardGame"""
        # FIXME: construct object with mandatory attributes with example values
        # model = cfbd.models.scoreboard_game.ScoreboardGame()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
