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
import datetime

from cfbd.models.poll import Poll  # noqa: E501

class TestPoll(unittest.TestCase):
    """Poll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Poll:
        """Test Poll
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Poll`
        """
        model = Poll()  # noqa: E501
        if include_optional:
            return Poll(
                poll = '',
                ranks = [
                    cfbd.models.poll_rank.PollRank(
                        rank = 56, 
                        school = '', 
                        conference = '', 
                        first_place_votes = 56, 
                        points = 56, )
                    ]
            )
        else:
            return Poll(
                poll = '',
                ranks = [
                    cfbd.models.poll_rank.PollRank(
                        rank = 56, 
                        school = '', 
                        conference = '', 
                        first_place_votes = 56, 
                        points = 56, )
                    ],
        )
        """

    def testPoll(self):
        """Test Poll"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
