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
from cfbd.models.team_matchup import TeamMatchup  # noqa: E501
from cfbd.rest import ApiException


class TestTeamMatchup(unittest.TestCase):
    """TeamMatchup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTeamMatchup(self):
        """Test TeamMatchup"""
        # FIXME: construct object with mandatory attributes with example values
        # model = cfbd.models.team_matchup.TeamMatchup()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
