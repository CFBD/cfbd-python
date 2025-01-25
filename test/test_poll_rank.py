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
import datetime

from cfbd.models.poll_rank import PollRank  # noqa: E501

class TestPollRank(unittest.TestCase):
    """PollRank unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PollRank:
        """Test PollRank
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PollRank`
        """
        model = PollRank()  # noqa: E501
        if include_optional:
            return PollRank(
                rank = 56,
                school = '',
                conference = '',
                first_place_votes = 56,
                points = 56
            )
        else:
            return PollRank(
                rank = 56,
                school = '',
                conference = '',
                first_place_votes = 56,
                points = 56,
        )
        """

    def testPollRank(self):
        """Test PollRank"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
