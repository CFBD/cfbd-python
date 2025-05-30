# coding: utf-8

# flake8: noqa
"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.18
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from cfbd.models.adjusted_team_metrics import AdjustedTeamMetrics
from cfbd.models.adjusted_team_metrics_epa import AdjustedTeamMetricsEpa
from cfbd.models.adjusted_team_metrics_rushing import AdjustedTeamMetricsRushing
from cfbd.models.adjusted_team_metrics_success_rate import AdjustedTeamMetricsSuccessRate
from cfbd.models.advanced_box_score import AdvancedBoxScore
from cfbd.models.advanced_box_score_game_info import AdvancedBoxScoreGameInfo
from cfbd.models.advanced_box_score_players import AdvancedBoxScorePlayers
from cfbd.models.advanced_box_score_teams import AdvancedBoxScoreTeams
from cfbd.models.advanced_game_stat import AdvancedGameStat
from cfbd.models.advanced_game_stat_defense import AdvancedGameStatDefense
from cfbd.models.advanced_game_stat_offense import AdvancedGameStatOffense
from cfbd.models.advanced_game_stat_offense_passing_downs import AdvancedGameStatOffensePassingDowns
from cfbd.models.advanced_game_stat_offense_passing_plays import AdvancedGameStatOffensePassingPlays
from cfbd.models.advanced_season_stat import AdvancedSeasonStat
from cfbd.models.advanced_season_stat_defense import AdvancedSeasonStatDefense
from cfbd.models.advanced_season_stat_offense import AdvancedSeasonStatOffense
from cfbd.models.advanced_season_stat_offense_field_position import AdvancedSeasonStatOffenseFieldPosition
from cfbd.models.advanced_season_stat_offense_havoc import AdvancedSeasonStatOffenseHavoc
from cfbd.models.advanced_season_stat_offense_passing_downs import AdvancedSeasonStatOffensePassingDowns
from cfbd.models.advanced_season_stat_offense_passing_plays import AdvancedSeasonStatOffensePassingPlays
from cfbd.models.aggregated_team_recruiting import AggregatedTeamRecruiting
from cfbd.models.betting_game import BettingGame
from cfbd.models.calendar_week import CalendarWeek
from cfbd.models.coach import Coach
from cfbd.models.coach_season import CoachSeason
from cfbd.models.conference import Conference
from cfbd.models.conference_sp import ConferenceSP
from cfbd.models.conference_sp_defense import ConferenceSPDefense
from cfbd.models.conference_sp_offense import ConferenceSPOffense
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.draft_pick import DraftPick
from cfbd.models.draft_pick_hometown_info import DraftPickHometownInfo
from cfbd.models.draft_position import DraftPosition
from cfbd.models.draft_team import DraftTeam
from cfbd.models.drive import Drive
from cfbd.models.field_goal_ep import FieldGoalEP
from cfbd.models.game import Game
from cfbd.models.game_line import GameLine
from cfbd.models.game_media import GameMedia
from cfbd.models.game_player_stat_categories import GamePlayerStatCategories
from cfbd.models.game_player_stat_player import GamePlayerStatPlayer
from cfbd.models.game_player_stat_types import GamePlayerStatTypes
from cfbd.models.game_player_stats import GamePlayerStats
from cfbd.models.game_player_stats_team import GamePlayerStatsTeam
from cfbd.models.game_status import GameStatus
from cfbd.models.game_team_stats import GameTeamStats
from cfbd.models.game_team_stats_team import GameTeamStatsTeam
from cfbd.models.game_team_stats_team_stat import GameTeamStatsTeamStat
from cfbd.models.game_weather import GameWeather
from cfbd.models.kicker_paar import KickerPAAR
from cfbd.models.live_game import LiveGame
from cfbd.models.live_game_drive import LiveGameDrive
from cfbd.models.live_game_play import LiveGamePlay
from cfbd.models.live_game_team import LiveGameTeam
from cfbd.models.matchup import Matchup
from cfbd.models.matchup_game import MatchupGame
from cfbd.models.media_type import MediaType
from cfbd.models.play import Play
from cfbd.models.play_clock import PlayClock
from cfbd.models.play_stat import PlayStat
from cfbd.models.play_stat_clock import PlayStatClock
from cfbd.models.play_stat_type import PlayStatType
from cfbd.models.play_type import PlayType
from cfbd.models.play_win_probability import PlayWinProbability
from cfbd.models.player_game_predicted_points_added import PlayerGamePredictedPointsAdded
from cfbd.models.player_game_predicted_points_added_average_ppa import PlayerGamePredictedPointsAddedAveragePPA
from cfbd.models.player_game_usage import PlayerGameUsage
from cfbd.models.player_ppa import PlayerPPA
from cfbd.models.player_ppa_chart_item import PlayerPPAChartItem
from cfbd.models.player_search_result import PlayerSearchResult
from cfbd.models.player_season_predicted_points_added import PlayerSeasonPredictedPointsAdded
from cfbd.models.player_season_predicted_points_added_average_ppa import PlayerSeasonPredictedPointsAddedAveragePPA
from cfbd.models.player_stat import PlayerStat
from cfbd.models.player_stats_by_quarter import PlayerStatsByQuarter
from cfbd.models.player_transfer import PlayerTransfer
from cfbd.models.player_usage import PlayerUsage
from cfbd.models.player_usage_usage import PlayerUsageUsage
from cfbd.models.player_weighted_epa import PlayerWeightedEPA
from cfbd.models.poll import Poll
from cfbd.models.poll_rank import PollRank
from cfbd.models.poll_week import PollWeek
from cfbd.models.predicted_points_value import PredictedPointsValue
from cfbd.models.pregame_win_probability import PregameWinProbability
from cfbd.models.recruit import Recruit
from cfbd.models.recruit_classification import RecruitClassification
from cfbd.models.recruit_hometown_info import RecruitHometownInfo
from cfbd.models.returning_production import ReturningProduction
from cfbd.models.roster_player import RosterPlayer
from cfbd.models.scoreboard_game import ScoreboardGame
from cfbd.models.scoreboard_game_betting import ScoreboardGameBetting
from cfbd.models.scoreboard_game_home_team import ScoreboardGameHomeTeam
from cfbd.models.scoreboard_game_venue import ScoreboardGameVenue
from cfbd.models.scoreboard_game_weather import ScoreboardGameWeather
from cfbd.models.season_type import SeasonType
from cfbd.models.stats_by_quarter import StatsByQuarter
from cfbd.models.team import Team
from cfbd.models.team_elo import TeamElo
from cfbd.models.team_explosiveness import TeamExplosiveness
from cfbd.models.team_fpi import TeamFPI
from cfbd.models.team_fpi_efficiencies import TeamFPIEfficiencies
from cfbd.models.team_fpi_resume_ranks import TeamFPIResumeRanks
from cfbd.models.team_field_position import TeamFieldPosition
from cfbd.models.team_game_predicted_points_added import TeamGamePredictedPointsAdded
from cfbd.models.team_game_predicted_points_added_offense import TeamGamePredictedPointsAddedOffense
from cfbd.models.team_havoc import TeamHavoc
from cfbd.models.team_ppa import TeamPPA
from cfbd.models.team_record import TeamRecord
from cfbd.models.team_records import TeamRecords
from cfbd.models.team_recruiting_ranking import TeamRecruitingRanking
from cfbd.models.team_rushing_stats import TeamRushingStats
from cfbd.models.team_sp import TeamSP
from cfbd.models.team_sp_defense import TeamSPDefense
from cfbd.models.team_sp_offense import TeamSPOffense
from cfbd.models.team_sp_special_teams import TeamSPSpecialTeams
from cfbd.models.team_srs import TeamSRS
from cfbd.models.team_scoring_opportunities import TeamScoringOpportunities
from cfbd.models.team_season_predicted_points_added import TeamSeasonPredictedPointsAdded
from cfbd.models.team_season_predicted_points_added_offense import TeamSeasonPredictedPointsAddedOffense
from cfbd.models.team_stat import TeamStat
from cfbd.models.team_stat_stat_value import TeamStatStatValue
from cfbd.models.team_success_rates import TeamSuccessRates
from cfbd.models.team_talent import TeamTalent
from cfbd.models.transfer_eligibility import TransferEligibility
from cfbd.models.venue import Venue
