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
import datetime

from cfbd.models.player_game_usage import PlayerGameUsage  # noqa: E501

class TestPlayerGameUsage(unittest.TestCase):
    """PlayerGameUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerGameUsage:
        """Test PlayerGameUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerGameUsage`
        """
        model = PlayerGameUsage()  # noqa: E501
        if include_optional:
            return PlayerGameUsage(
                total = 1.337,
                quarter1 = 1.337,
                quarter2 = 1.337,
                quarter3 = 1.337,
                quarter4 = 1.337,
                rushing = 1.337,
                passing = 1.337,
                player = '',
                team = '',
                position = ''
            )
        else:
            return PlayerGameUsage(
                total = 1.337,
                quarter1 = 1.337,
                quarter2 = 1.337,
                quarter3 = 1.337,
                quarter4 = 1.337,
                rushing = 1.337,
                passing = 1.337,
                player = '',
                team = '',
                position = '',
        )
        """

    def testPlayerGameUsage(self):
        """Test PlayerGameUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
