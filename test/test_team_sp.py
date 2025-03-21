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

from cfbd.models.team_sp import TeamSP  # noqa: E501

class TestTeamSP(unittest.TestCase):
    """TeamSP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamSP:
        """Test TeamSP
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamSP`
        """
        model = TeamSP()  # noqa: E501
        if include_optional:
            return TeamSP(
                year = 56,
                team = '',
                conference = '',
                rating = 1.337,
                ranking = 56,
                second_order_wins = 1.337,
                sos = 1.337,
                offense = cfbd.models.team_sp_offense.TeamSP_offense(
                    pace = 1.337, 
                    run_rate = 1.337, 
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    passing = 1.337, 
                    rushing = 1.337, 
                    explosiveness = 1.337, 
                    success = 1.337, 
                    rating = 1.337, 
                    ranking = 56, ),
                defense = cfbd.models.team_sp_defense.TeamSP_defense(
                    havoc = cfbd.models.advanced_season_stat_offense_havoc.AdvancedSeasonStat_offense_havoc(
                        db = 1.337, 
                        front_seven = 1.337, 
                        total = 1.337, ), 
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    passing = 1.337, 
                    rushing = 1.337, 
                    explosiveness = 1.337, 
                    success = 1.337, 
                    rating = 1.337, 
                    ranking = 56, ),
                special_teams = cfbd.models.team_sp_special_teams.TeamSP_specialTeams(
                    rating = 1.337, )
            )
        else:
            return TeamSP(
                year = 56,
                team = '',
                conference = '',
                rating = 1.337,
                ranking = 56,
                second_order_wins = 1.337,
                sos = 1.337,
                offense = cfbd.models.team_sp_offense.TeamSP_offense(
                    pace = 1.337, 
                    run_rate = 1.337, 
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    passing = 1.337, 
                    rushing = 1.337, 
                    explosiveness = 1.337, 
                    success = 1.337, 
                    rating = 1.337, 
                    ranking = 56, ),
                defense = cfbd.models.team_sp_defense.TeamSP_defense(
                    havoc = cfbd.models.advanced_season_stat_offense_havoc.AdvancedSeasonStat_offense_havoc(
                        db = 1.337, 
                        front_seven = 1.337, 
                        total = 1.337, ), 
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    passing = 1.337, 
                    rushing = 1.337, 
                    explosiveness = 1.337, 
                    success = 1.337, 
                    rating = 1.337, 
                    ranking = 56, ),
                special_teams = cfbd.models.team_sp_special_teams.TeamSP_specialTeams(
                    rating = 1.337, ),
        )
        """

    def testTeamSP(self):
        """Test TeamSP"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
