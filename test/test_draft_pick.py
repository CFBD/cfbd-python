# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.10
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.draft_pick import DraftPick  # noqa: E501

class TestDraftPick(unittest.TestCase):
    """DraftPick unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DraftPick:
        """Test DraftPick
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DraftPick`
        """
        model = DraftPick()  # noqa: E501
        if include_optional:
            return DraftPick(
                college_athlete_id = 56,
                nfl_athlete_id = 56,
                college_id = 56,
                college_team = '',
                college_conference = '',
                nfl_team_id = 56,
                nfl_team = '',
                year = 56,
                overall = 56,
                round = 56,
                pick = 56,
                name = '',
                position = '',
                height = 56,
                weight = 56,
                pre_draft_ranking = 56,
                pre_draft_position_ranking = 56,
                pre_draft_grade = 56,
                hometown_info = cfbd.models.draft_pick_hometown_info.DraftPick_hometownInfo(
                    county_fips = '', 
                    longitude = '', 
                    latitude = '', 
                    country = '', 
                    state = '', 
                    city = '', )
            )
        else:
            return DraftPick(
                college_athlete_id = 56,
                nfl_athlete_id = 56,
                college_id = 56,
                college_team = '',
                college_conference = '',
                nfl_team_id = 56,
                nfl_team = '',
                year = 56,
                overall = 56,
                round = 56,
                pick = 56,
                name = '',
                position = '',
                height = 56,
                weight = 56,
                pre_draft_ranking = 56,
                pre_draft_position_ranking = 56,
                pre_draft_grade = 56,
                hometown_info = cfbd.models.draft_pick_hometown_info.DraftPick_hometownInfo(
                    county_fips = '', 
                    longitude = '', 
                    latitude = '', 
                    country = '', 
                    state = '', 
                    city = '', ),
        )
        """

    def testDraftPick(self):
        """Test DraftPick"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
