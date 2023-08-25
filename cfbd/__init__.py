# coding: utf-8

# flake8: noqa

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.14
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
from cfbd.models.advanced_game_stat_offense import AdvancedGameStatOffense
from cfbd.models.advanced_game_stat_offense_rushing_plays import AdvancedGameStatOffenseRushingPlays
from cfbd.models.advanced_game_stat_offense_standard_downs import AdvancedGameStatOffenseStandardDowns
from cfbd.models.advanced_season_stat import AdvancedSeasonStat
from cfbd.models.advanced_season_stat_offense import AdvancedSeasonStatOffense
from cfbd.models.advanced_season_stat_offense_field_position import AdvancedSeasonStatOffenseFieldPosition
from cfbd.models.advanced_season_stat_offense_rushing_plays import AdvancedSeasonStatOffenseRushingPlays
from cfbd.models.advanced_season_stat_offense_standard_downs import AdvancedSeasonStatOffenseStandardDowns
from cfbd.models.box_score import BoxScore
from cfbd.models.box_score_players import BoxScorePlayers
from cfbd.models.box_score_players_average import BoxScorePlayersAverage
from cfbd.models.box_score_players_ppa import BoxScorePlayersPpa
from cfbd.models.box_score_players_usage import BoxScorePlayersUsage
from cfbd.models.box_score_teams import BoxScoreTeams
from cfbd.models.box_score_teams_explosiveness import BoxScoreTeamsExplosiveness
from cfbd.models.box_score_teams_field_position import BoxScoreTeamsFieldPosition
from cfbd.models.box_score_teams_havoc import BoxScoreTeamsHavoc
from cfbd.models.box_score_teams_overall import BoxScoreTeamsOverall
from cfbd.models.box_score_teams_ppa import BoxScoreTeamsPpa
from cfbd.models.box_score_teams_rushing import BoxScoreTeamsRushing
from cfbd.models.box_score_teams_scoring_opportunities import BoxScoreTeamsScoringOpportunities
from cfbd.models.box_score_teams_success_rates import BoxScoreTeamsSuccessRates
from cfbd.models.coach import Coach
from cfbd.models.coach_seasons import CoachSeasons
from cfbd.models.conference import Conference
from cfbd.models.conference_sp_rating import ConferenceSPRating
from cfbd.models.conference_sp_rating_defense import ConferenceSPRatingDefense
from cfbd.models.conference_sp_rating_offense import ConferenceSPRatingOffense
from cfbd.models.draft_pick import DraftPick
from cfbd.models.draft_pick_hometown_info import DraftPickHometownInfo
from cfbd.models.draft_position import DraftPosition
from cfbd.models.draft_team import DraftTeam
from cfbd.models.drive import Drive
from cfbd.models.drive_start_time import DriveStartTime
from cfbd.models.game import Game
from cfbd.models.game_lines import GameLines
from cfbd.models.game_lines_lines import GameLinesLines
from cfbd.models.game_media import GameMedia
from cfbd.models.game_ppa import GamePPA
from cfbd.models.game_ppa_offense import GamePPAOffense
from cfbd.models.game_weather import GameWeather
from cfbd.models.live_play_by_play import LivePlayByPlay
from cfbd.models.live_play_by_play_drives import LivePlayByPlayDrives
from cfbd.models.live_play_by_play_plays import LivePlayByPlayPlays
from cfbd.models.live_play_by_play_teams import LivePlayByPlayTeams
from cfbd.models.play import Play
from cfbd.models.play_stat import PlayStat
from cfbd.models.play_stat_type import PlayStatType
from cfbd.models.play_type import PlayType
from cfbd.models.play_wp import PlayWP
from cfbd.models.player import Player
from cfbd.models.player_game import PlayerGame
from cfbd.models.player_game_athletes import PlayerGameAthletes
from cfbd.models.player_game_categories import PlayerGameCategories
from cfbd.models.player_game_ppa import PlayerGamePPA
from cfbd.models.player_game_ppa_average_ppa import PlayerGamePPAAveragePPA
from cfbd.models.player_game_teams import PlayerGameTeams
from cfbd.models.player_game_types import PlayerGameTypes
from cfbd.models.player_search_result import PlayerSearchResult
from cfbd.models.player_season_ppa import PlayerSeasonPPA
from cfbd.models.player_season_ppa_average_ppa import PlayerSeasonPPAAveragePPA
from cfbd.models.player_season_stat import PlayerSeasonStat
from cfbd.models.player_usage import PlayerUsage
from cfbd.models.player_usage_usage import PlayerUsageUsage
from cfbd.models.portal_player import PortalPlayer
from cfbd.models.position_group_recruiting_rating import PositionGroupRecruitingRating
from cfbd.models.predicted_points import PredictedPoints
from cfbd.models.pregame_wp import PregameWP
from cfbd.models.ranking_week import RankingWeek
from cfbd.models.ranking_week_polls import RankingWeekPolls
from cfbd.models.ranking_week_ranks import RankingWeekRanks
from cfbd.models.recruit import Recruit
from cfbd.models.recruit_hometown_info import RecruitHometownInfo
from cfbd.models.returning_production import ReturningProduction
from cfbd.models.scoreboard_game import ScoreboardGame
from cfbd.models.scoreboard_game_betting import ScoreboardGameBetting
from cfbd.models.scoreboard_game_home_team import ScoreboardGameHomeTeam
from cfbd.models.scoreboard_game_venue import ScoreboardGameVenue
from cfbd.models.scoreboard_game_weather import ScoreboardGameWeather
from cfbd.models.team import Team
from cfbd.models.team_elo_rating import TeamEloRating
from cfbd.models.team_game import TeamGame
from cfbd.models.team_game_stats import TeamGameStats
from cfbd.models.team_game_teams import TeamGameTeams
from cfbd.models.team_location import TeamLocation
from cfbd.models.team_matchup import TeamMatchup
from cfbd.models.team_matchup_games import TeamMatchupGames
from cfbd.models.team_ppa import TeamPPA
from cfbd.models.team_ppa_offense import TeamPPAOffense
from cfbd.models.team_ppa_offense_cumulative import TeamPPAOffenseCumulative
from cfbd.models.team_record import TeamRecord
from cfbd.models.team_record_total import TeamRecordTotal
from cfbd.models.team_recruiting_rank import TeamRecruitingRank
from cfbd.models.team_sp_rating import TeamSPRating
from cfbd.models.team_sp_rating_defense import TeamSPRatingDefense
from cfbd.models.team_sp_rating_defense_havoc import TeamSPRatingDefenseHavoc
from cfbd.models.team_sp_rating_offense import TeamSPRatingOffense
from cfbd.models.team_sp_rating_special_teams import TeamSPRatingSpecialTeams
from cfbd.models.team_srs_rating import TeamSRSRating
from cfbd.models.team_season import TeamSeason
from cfbd.models.team_season_stat import TeamSeasonStat
from cfbd.models.team_talent import TeamTalent
from cfbd.models.venue import Venue
from cfbd.models.venue_location import VenueLocation
from cfbd.models.week import Week
