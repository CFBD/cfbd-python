# coding: utf-8

# flake8: noqa

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.2.3
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from cfbd.api.betting_api import BettingApi
from cfbd.api.coaches_api import CoachesApi
from cfbd.api.conferences_api import ConferencesApi
from cfbd.api.draft_api import DraftApi
from cfbd.api.drives_api import DrivesApi
from cfbd.api.games_api import GamesApi
from cfbd.api.metrics_api import MetricsApi
from cfbd.api.players_api import PlayersApi
from cfbd.api.plays_api import PlaysApi
from cfbd.api.rankings_api import RankingsApi
from cfbd.api.ratings_api import RatingsApi
from cfbd.api.recruiting_api import RecruitingApi
from cfbd.api.stats_api import StatsApi
from cfbd.api.teams_api import TeamsApi
from cfbd.api.venues_api import VenuesApi

# import ApiClient
from cfbd.api_client import ApiClient
from cfbd.configuration import Configuration
# import models into sdk package
from cfbd.models.advanced_game_stat import AdvancedGameStat
from cfbd.models.advanced_season_stat import AdvancedSeasonStat
from cfbd.models.box_score import BoxScore
from cfbd.models.coach import Coach
from cfbd.models.conference import Conference
from cfbd.models.conference_sp_rating import ConferenceSPRating
from cfbd.models.draft_pick import DraftPick
from cfbd.models.draft_position import DraftPosition
from cfbd.models.draft_team import DraftTeam
from cfbd.models.drive import Drive
from cfbd.models.game import Game
from cfbd.models.game_lines import GameLines
from cfbd.models.game_media import GameMedia
from cfbd.models.game_ppa import GamePPA
from cfbd.models.game_weather import GameWeather
from cfbd.models.live_play_by_play import LivePlayByPlay
from cfbd.models.play import Play
from cfbd.models.play_stat import PlayStat
from cfbd.models.play_stat_type import PlayStatType
from cfbd.models.play_type import PlayType
from cfbd.models.play_wp import PlayWP
from cfbd.models.player import Player
from cfbd.models.player_game import PlayerGame
from cfbd.models.player_game_ppa import PlayerGamePPA
from cfbd.models.player_search_result import PlayerSearchResult
from cfbd.models.player_season_ppa import PlayerSeasonPPA
from cfbd.models.player_season_stat import PlayerSeasonStat
from cfbd.models.player_usage import PlayerUsage
from cfbd.models.position_group_recruiting_rating import PositionGroupRecruitingRating
from cfbd.models.predicted_points import PredictedPoints
from cfbd.models.pregame_wp import PregameWP
from cfbd.models.ranking_week import RankingWeek
from cfbd.models.recruit import Recruit
from cfbd.models.returning_production import ReturningProduction
from cfbd.models.scoreboard_game import ScoreboardGame
from cfbd.models.team import Team
from cfbd.models.team_elo_rating import TeamEloRating
from cfbd.models.team_game import TeamGame
from cfbd.models.team_matchup import TeamMatchup
from cfbd.models.team_ppa import TeamPPA
from cfbd.models.team_record import TeamRecord
from cfbd.models.team_recruiting_rank import TeamRecruitingRank
from cfbd.models.team_sp_rating import TeamSPRating
from cfbd.models.team_srs_rating import TeamSRSRating
from cfbd.models.team_season import TeamSeason
from cfbd.models.team_season_stat import TeamSeasonStat
from cfbd.models.team_talent import TeamTalent
from cfbd.models.venue import Venue
from cfbd.models.week import Week
