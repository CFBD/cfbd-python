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

from cfbd.models.player_transfer import PlayerTransfer  # noqa: E501

class TestPlayerTransfer(unittest.TestCase):
    """PlayerTransfer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerTransfer:
        """Test PlayerTransfer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerTransfer`
        """
        model = PlayerTransfer()  # noqa: E501
        if include_optional:
            return PlayerTransfer(
                season = 56,
                first_name = '',
                last_name = '',
                position = '',
                origin = '',
                destination = '',
                transfer_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                rating = 1.337,
                stars = 56,
                eligibility = 'Withdrawn'
            )
        else:
            return PlayerTransfer(
                season = 56,
                first_name = '',
                last_name = '',
                position = '',
                origin = '',
                destination = '',
                transfer_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                rating = 1.337,
                stars = 56,
                eligibility = 'Withdrawn',
        )
        """

    def testPlayerTransfer(self):
        """Test PlayerTransfer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
