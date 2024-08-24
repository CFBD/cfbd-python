# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.14
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.team_records import TeamRecords  # noqa: E501

class TestTeamRecords(unittest.TestCase):
    """TeamRecords unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamRecords:
        """Test TeamRecords
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamRecords`
        """
        model = TeamRecords()  # noqa: E501
        if include_optional:
            return TeamRecords(
                year = 56,
                team_id = 56,
                team = '',
                classification = 'fbs',
                conference = '',
                division = '',
                expected_wins = 1.337,
                total = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, ),
                conference_games = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, ),
                home_games = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, ),
                away_games = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, ),
                neutral_site_games = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, )
            )
        else:
            return TeamRecords(
                year = 56,
                team_id = 56,
                team = '',
                classification = 'fbs',
                conference = '',
                division = '',
                expected_wins = 1.337,
                total = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, ),
                conference_games = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, ),
                home_games = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, ),
                away_games = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, ),
                neutral_site_games = cfbd.models.team_record.TeamRecord(
                    games = 56, 
                    wins = 56, 
                    losses = 56, 
                    ties = 56, ),
        )
        """

    def testTeamRecords(self):
        """Test TeamRecords"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
