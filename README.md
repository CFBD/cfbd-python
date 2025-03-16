# cfbd
This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5.6.7
- Package version: 5.6.7
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

```sh
pip install cfbd
```
(you may need to run `pip` with root permission: `sudo pip install cfbd`)

Then import the package:
```python
import cfbd
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apinext.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://apinext.collegefootballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.AdjustedMetricsApi(api_client)
    year = 56 # int | Optional year filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    position = 'position_example' # str | Optional position abbreviation filter (optional)

    try:
        api_response = api_instance.get_adjusted_player_passing_stats(year=year, team=team, conference=conference, position=position)
        print("The response of AdjustedMetricsApi->get_adjusted_player_passing_stats:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdjustedMetricsApi->get_adjusted_player_passing_stats: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://apinext.collegefootballdata.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdjustedMetricsApi* | [**get_adjusted_player_passing_stats**](docs/AdjustedMetricsApi.md#get_adjusted_player_passing_stats) | **GET** /wepa/players/passing | 
*AdjustedMetricsApi* | [**get_adjusted_player_rushing_stats**](docs/AdjustedMetricsApi.md#get_adjusted_player_rushing_stats) | **GET** /wepa/players/rushing | 
*AdjustedMetricsApi* | [**get_adjusted_team_season_stats**](docs/AdjustedMetricsApi.md#get_adjusted_team_season_stats) | **GET** /wepa/team/season | 
*AdjustedMetricsApi* | [**get_kicker_paar**](docs/AdjustedMetricsApi.md#get_kicker_paar) | **GET** /wepa/players/kicking | 
*BettingApi* | [**get_lines**](docs/BettingApi.md#get_lines) | **GET** /lines | 
*CoachesApi* | [**get_coaches**](docs/CoachesApi.md#get_coaches) | **GET** /coaches | 
*ConferencesApi* | [**get_conferences**](docs/ConferencesApi.md#get_conferences) | **GET** /conferences | 
*DraftApi* | [**get_draft_picks**](docs/DraftApi.md#get_draft_picks) | **GET** /draft/picks | 
*DraftApi* | [**get_draft_positions**](docs/DraftApi.md#get_draft_positions) | **GET** /draft/positions | 
*DraftApi* | [**get_draft_teams**](docs/DraftApi.md#get_draft_teams) | **GET** /draft/teams | 
*DrivesApi* | [**get_drives**](docs/DrivesApi.md#get_drives) | **GET** /drives | 
*GamesApi* | [**get_advanced_box_score**](docs/GamesApi.md#get_advanced_box_score) | **GET** /game/box/advanced | 
*GamesApi* | [**get_calendar**](docs/GamesApi.md#get_calendar) | **GET** /calendar | 
*GamesApi* | [**get_game_player_stats**](docs/GamesApi.md#get_game_player_stats) | **GET** /games/players | 
*GamesApi* | [**get_game_team_stats**](docs/GamesApi.md#get_game_team_stats) | **GET** /games/teams | 
*GamesApi* | [**get_games**](docs/GamesApi.md#get_games) | **GET** /games | 
*GamesApi* | [**get_media**](docs/GamesApi.md#get_media) | **GET** /games/media | 
*GamesApi* | [**get_records**](docs/GamesApi.md#get_records) | **GET** /records | 
*GamesApi* | [**get_scoreboard**](docs/GamesApi.md#get_scoreboard) | **GET** /scoreboard | 
*GamesApi* | [**get_weather**](docs/GamesApi.md#get_weather) | **GET** /games/weather | 
*MetricsApi* | [**get_field_goal_expected_points**](docs/MetricsApi.md#get_field_goal_expected_points) | **GET** /metrics/fg/ep | 
*MetricsApi* | [**get_predicted_points**](docs/MetricsApi.md#get_predicted_points) | **GET** /ppa/predicted | 
*MetricsApi* | [**get_predicted_points_added_by_game**](docs/MetricsApi.md#get_predicted_points_added_by_game) | **GET** /ppa/games | 
*MetricsApi* | [**get_predicted_points_added_by_player_game**](docs/MetricsApi.md#get_predicted_points_added_by_player_game) | **GET** /ppa/players/games | 
*MetricsApi* | [**get_predicted_points_added_by_player_season**](docs/MetricsApi.md#get_predicted_points_added_by_player_season) | **GET** /ppa/players/season | 
*MetricsApi* | [**get_predicted_points_added_by_team**](docs/MetricsApi.md#get_predicted_points_added_by_team) | **GET** /ppa/teams | 
*MetricsApi* | [**get_pregame_win_probabilities**](docs/MetricsApi.md#get_pregame_win_probabilities) | **GET** /metrics/wp/pregame | 
*MetricsApi* | [**get_win_probability**](docs/MetricsApi.md#get_win_probability) | **GET** /metrics/wp | 
*PlayersApi* | [**get_player_usage**](docs/PlayersApi.md#get_player_usage) | **GET** /player/usage | 
*PlayersApi* | [**get_returning_production**](docs/PlayersApi.md#get_returning_production) | **GET** /player/returning | 
*PlayersApi* | [**get_transfer_portal**](docs/PlayersApi.md#get_transfer_portal) | **GET** /player/portal | 
*PlayersApi* | [**search_players**](docs/PlayersApi.md#search_players) | **GET** /player/search | 
*PlaysApi* | [**get_live_plays**](docs/PlaysApi.md#get_live_plays) | **GET** /live/plays | 
*PlaysApi* | [**get_play_stat_types**](docs/PlaysApi.md#get_play_stat_types) | **GET** /plays/stats/types | 
*PlaysApi* | [**get_play_stats**](docs/PlaysApi.md#get_play_stats) | **GET** /plays/stats | 
*PlaysApi* | [**get_play_types**](docs/PlaysApi.md#get_play_types) | **GET** /plays/types | 
*PlaysApi* | [**get_plays**](docs/PlaysApi.md#get_plays) | **GET** /plays | 
*RankingsApi* | [**get_rankings**](docs/RankingsApi.md#get_rankings) | **GET** /rankings | 
*RatingsApi* | [**get_conference_sp**](docs/RatingsApi.md#get_conference_sp) | **GET** /ratings/sp/conferences | 
*RatingsApi* | [**get_elo**](docs/RatingsApi.md#get_elo) | **GET** /ratings/elo | 
*RatingsApi* | [**get_fpi**](docs/RatingsApi.md#get_fpi) | **GET** /ratings/fpi | 
*RatingsApi* | [**get_sp**](docs/RatingsApi.md#get_sp) | **GET** /ratings/sp | 
*RatingsApi* | [**get_srs**](docs/RatingsApi.md#get_srs) | **GET** /ratings/srs | 
*RecruitingApi* | [**get_aggregated_team_recruiting_ratings**](docs/RecruitingApi.md#get_aggregated_team_recruiting_ratings) | **GET** /recruiting/groups | 
*RecruitingApi* | [**get_recruits**](docs/RecruitingApi.md#get_recruits) | **GET** /recruiting/players | 
*RecruitingApi* | [**get_team_recruiting_rankings**](docs/RecruitingApi.md#get_team_recruiting_rankings) | **GET** /recruiting/teams | 
*StatsApi* | [**get_advanced_game_stats**](docs/StatsApi.md#get_advanced_game_stats) | **GET** /stats/game/advanced | 
*StatsApi* | [**get_advanced_season_stats**](docs/StatsApi.md#get_advanced_season_stats) | **GET** /stats/season/advanced | 
*StatsApi* | [**get_categories**](docs/StatsApi.md#get_categories) | **GET** /stats/categories | 
*StatsApi* | [**get_player_season_stats**](docs/StatsApi.md#get_player_season_stats) | **GET** /stats/player/season | 
*StatsApi* | [**get_team_stats**](docs/StatsApi.md#get_team_stats) | **GET** /stats/season | 
*TeamsApi* | [**get_fbs_teams**](docs/TeamsApi.md#get_fbs_teams) | **GET** /teams/fbs | 
*TeamsApi* | [**get_matchup**](docs/TeamsApi.md#get_matchup) | **GET** /teams/matchup | 
*TeamsApi* | [**get_roster**](docs/TeamsApi.md#get_roster) | **GET** /roster | 
*TeamsApi* | [**get_talent**](docs/TeamsApi.md#get_talent) | **GET** /talent | 
*TeamsApi* | [**get_teams**](docs/TeamsApi.md#get_teams) | **GET** /teams | 
*VenuesApi* | [**get_venues**](docs/VenuesApi.md#get_venues) | **GET** /venues | 


## Documentation For Models

 - [AdjustedTeamMetrics](docs/AdjustedTeamMetrics.md)
 - [AdjustedTeamMetricsEpa](docs/AdjustedTeamMetricsEpa.md)
 - [AdjustedTeamMetricsRushing](docs/AdjustedTeamMetricsRushing.md)
 - [AdjustedTeamMetricsSuccessRate](docs/AdjustedTeamMetricsSuccessRate.md)
 - [AdvancedBoxScore](docs/AdvancedBoxScore.md)
 - [AdvancedBoxScoreGameInfo](docs/AdvancedBoxScoreGameInfo.md)
 - [AdvancedBoxScorePlayers](docs/AdvancedBoxScorePlayers.md)
 - [AdvancedBoxScoreTeams](docs/AdvancedBoxScoreTeams.md)
 - [AdvancedGameStat](docs/AdvancedGameStat.md)
 - [AdvancedGameStatOffense](docs/AdvancedGameStatOffense.md)
 - [AdvancedGameStatOffensePassingDowns](docs/AdvancedGameStatOffensePassingDowns.md)
 - [AdvancedGameStatOffensePassingPlays](docs/AdvancedGameStatOffensePassingPlays.md)
 - [AdvancedSeasonStat](docs/AdvancedSeasonStat.md)
 - [AdvancedSeasonStatDefense](docs/AdvancedSeasonStatDefense.md)
 - [AdvancedSeasonStatOffense](docs/AdvancedSeasonStatOffense.md)
 - [AdvancedSeasonStatOffenseFieldPosition](docs/AdvancedSeasonStatOffenseFieldPosition.md)
 - [AdvancedSeasonStatOffenseHavoc](docs/AdvancedSeasonStatOffenseHavoc.md)
 - [AdvancedSeasonStatOffensePassingDowns](docs/AdvancedSeasonStatOffensePassingDowns.md)
 - [AdvancedSeasonStatOffensePassingPlays](docs/AdvancedSeasonStatOffensePassingPlays.md)
 - [AggregatedTeamRecruiting](docs/AggregatedTeamRecruiting.md)
 - [BettingGame](docs/BettingGame.md)
 - [CalendarWeek](docs/CalendarWeek.md)
 - [Coach](docs/Coach.md)
 - [CoachSeason](docs/CoachSeason.md)
 - [Conference](docs/Conference.md)
 - [ConferenceSP](docs/ConferenceSP.md)
 - [ConferenceSPDefense](docs/ConferenceSPDefense.md)
 - [ConferenceSPOffense](docs/ConferenceSPOffense.md)
 - [DivisionClassification](docs/DivisionClassification.md)
 - [DraftPick](docs/DraftPick.md)
 - [DraftPickHometownInfo](docs/DraftPickHometownInfo.md)
 - [DraftPosition](docs/DraftPosition.md)
 - [DraftTeam](docs/DraftTeam.md)
 - [Drive](docs/Drive.md)
 - [FieldGoalEP](docs/FieldGoalEP.md)
 - [Game](docs/Game.md)
 - [GameLine](docs/GameLine.md)
 - [GameMedia](docs/GameMedia.md)
 - [GamePlayerStatCategories](docs/GamePlayerStatCategories.md)
 - [GamePlayerStatPlayer](docs/GamePlayerStatPlayer.md)
 - [GamePlayerStatTypes](docs/GamePlayerStatTypes.md)
 - [GamePlayerStats](docs/GamePlayerStats.md)
 - [GamePlayerStatsTeam](docs/GamePlayerStatsTeam.md)
 - [GameStatus](docs/GameStatus.md)
 - [GameTeamStats](docs/GameTeamStats.md)
 - [GameTeamStatsTeam](docs/GameTeamStatsTeam.md)
 - [GameTeamStatsTeamStat](docs/GameTeamStatsTeamStat.md)
 - [GameWeather](docs/GameWeather.md)
 - [KickerPAAR](docs/KickerPAAR.md)
 - [LiveGame](docs/LiveGame.md)
 - [LiveGameDrive](docs/LiveGameDrive.md)
 - [LiveGamePlay](docs/LiveGamePlay.md)
 - [LiveGameTeam](docs/LiveGameTeam.md)
 - [Matchup](docs/Matchup.md)
 - [MatchupGame](docs/MatchupGame.md)
 - [MediaType](docs/MediaType.md)
 - [Play](docs/Play.md)
 - [PlayClock](docs/PlayClock.md)
 - [PlayStat](docs/PlayStat.md)
 - [PlayStatClock](docs/PlayStatClock.md)
 - [PlayStatType](docs/PlayStatType.md)
 - [PlayType](docs/PlayType.md)
 - [PlayWinProbability](docs/PlayWinProbability.md)
 - [PlayerGamePredictedPointsAdded](docs/PlayerGamePredictedPointsAdded.md)
 - [PlayerGamePredictedPointsAddedAveragePPA](docs/PlayerGamePredictedPointsAddedAveragePPA.md)
 - [PlayerGameUsage](docs/PlayerGameUsage.md)
 - [PlayerPPA](docs/PlayerPPA.md)
 - [PlayerPPAChartItem](docs/PlayerPPAChartItem.md)
 - [PlayerSearchResult](docs/PlayerSearchResult.md)
 - [PlayerSeasonPredictedPointsAdded](docs/PlayerSeasonPredictedPointsAdded.md)
 - [PlayerSeasonPredictedPointsAddedAveragePPA](docs/PlayerSeasonPredictedPointsAddedAveragePPA.md)
 - [PlayerStat](docs/PlayerStat.md)
 - [PlayerStatsByQuarter](docs/PlayerStatsByQuarter.md)
 - [PlayerTransfer](docs/PlayerTransfer.md)
 - [PlayerUsage](docs/PlayerUsage.md)
 - [PlayerUsageUsage](docs/PlayerUsageUsage.md)
 - [PlayerWeightedEPA](docs/PlayerWeightedEPA.md)
 - [Poll](docs/Poll.md)
 - [PollRank](docs/PollRank.md)
 - [PollWeek](docs/PollWeek.md)
 - [PredictedPointsValue](docs/PredictedPointsValue.md)
 - [PregameWinProbability](docs/PregameWinProbability.md)
 - [Recruit](docs/Recruit.md)
 - [RecruitClassification](docs/RecruitClassification.md)
 - [RecruitHometownInfo](docs/RecruitHometownInfo.md)
 - [ReturningProduction](docs/ReturningProduction.md)
 - [RosterPlayer](docs/RosterPlayer.md)
 - [ScoreboardGame](docs/ScoreboardGame.md)
 - [ScoreboardGameBetting](docs/ScoreboardGameBetting.md)
 - [ScoreboardGameHomeTeam](docs/ScoreboardGameHomeTeam.md)
 - [ScoreboardGameVenue](docs/ScoreboardGameVenue.md)
 - [ScoreboardGameWeather](docs/ScoreboardGameWeather.md)
 - [SeasonType](docs/SeasonType.md)
 - [StatsByQuarter](docs/StatsByQuarter.md)
 - [Team](docs/Team.md)
 - [TeamElo](docs/TeamElo.md)
 - [TeamExplosiveness](docs/TeamExplosiveness.md)
 - [TeamFPI](docs/TeamFPI.md)
 - [TeamFPIEfficiencies](docs/TeamFPIEfficiencies.md)
 - [TeamFPIResumeRanks](docs/TeamFPIResumeRanks.md)
 - [TeamFieldPosition](docs/TeamFieldPosition.md)
 - [TeamGamePredictedPointsAdded](docs/TeamGamePredictedPointsAdded.md)
 - [TeamGamePredictedPointsAddedOffense](docs/TeamGamePredictedPointsAddedOffense.md)
 - [TeamHavoc](docs/TeamHavoc.md)
 - [TeamPPA](docs/TeamPPA.md)
 - [TeamRecord](docs/TeamRecord.md)
 - [TeamRecords](docs/TeamRecords.md)
 - [TeamRecruitingRanking](docs/TeamRecruitingRanking.md)
 - [TeamRushingStats](docs/TeamRushingStats.md)
 - [TeamSP](docs/TeamSP.md)
 - [TeamSPDefense](docs/TeamSPDefense.md)
 - [TeamSPOffense](docs/TeamSPOffense.md)
 - [TeamSPSpecialTeams](docs/TeamSPSpecialTeams.md)
 - [TeamSRS](docs/TeamSRS.md)
 - [TeamScoringOpportunities](docs/TeamScoringOpportunities.md)
 - [TeamSeasonPredictedPointsAdded](docs/TeamSeasonPredictedPointsAdded.md)
 - [TeamSeasonPredictedPointsAddedOffense](docs/TeamSeasonPredictedPointsAddedOffense.md)
 - [TeamStat](docs/TeamStat.md)
 - [TeamStatStatValue](docs/TeamStatStatValue.md)
 - [TeamSuccessRates](docs/TeamSuccessRates.md)
 - [TeamTalent](docs/TeamTalent.md)
 - [TransferEligibility](docs/TransferEligibility.md)
 - [Venue](docs/Venue.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="apiKey"></a>
### apiKey

- **Type**: Bearer authentication


## Author

admin@collegefootballdata.com


