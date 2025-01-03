# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.recruit_hometown_info import RecruitHometownInfo  # noqa: E501

class TestRecruitHometownInfo(unittest.TestCase):
    """RecruitHometownInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecruitHometownInfo:
        """Test RecruitHometownInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecruitHometownInfo`
        """
        model = RecruitHometownInfo()  # noqa: E501
        if include_optional:
            return RecruitHometownInfo(
                fips_code = '',
                longitude = 1.337,
                latitude = 1.337
            )
        else:
            return RecruitHometownInfo(
                fips_code = '',
                longitude = 1.337,
                latitude = 1.337,
        )
        """

    def testRecruitHometownInfo(self):
        """Test RecruitHometownInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
