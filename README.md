# cfbd
This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.2.14
- Package version: 2.2.14
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

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

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cfbd
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.BettingApi(cfbd.ApiClient(configuration))
game_id = 56 # int | Game id filter (optional)
year = 56 # int | Year/season filter for games (optional)
week = 56 # int | Week filter (optional)
season_type = 'regular' # str | Season type filter (regular or postseason) (optional) (default to regular)
team = 'team_example' # str | Team (optional)
home = 'home_example' # str | Home team filter (optional)
away = 'away_example' # str | Away team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)

try:
    # Betting lines
    api_response = api_instance.get_lines(game_id=game_id, year=year, week=week, season_type=season_type, team=team, home=home, away=away, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BettingApi->get_lines: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.collegefootballdata.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BettingApi* | [**get_lines**](docs/BettingApi.md#get_lines) | **GET** /lines | Betting lines
*CoachesApi* | [**get_coaches**](docs/CoachesApi.md#get_coaches) | **GET** /coaches | Coaching records and history
*ConferencesApi* | [**get_conferences**](docs/ConferencesApi.md#get_conferences) | **GET** /conferences | Conferences
*DrivesApi* | [**get_drives**](docs/DrivesApi.md#get_drvies) | **GET** /drives | Drive data and results
*GamesApi* | [**get_advanced_box_score**](docs/GamesApi.md#get_advanced_box_score) | **GET** /game/box/advanced | Advanced box scores
*GamesApi* | [**get_game_media**](docs/GamesApi.md#get_game_media) | **GET** /games/media | Game media information and schedules
*GamesApi* | [**get_games**](docs/GamesApi.md#get_games) | **GET** /games | Games and results
*GamesApi* | [**get_player_game_stats**](docs/GamesApi.md#get_player_game_stats) | **GET** /games/players | Player game stats
*GamesApi* | [**get_team_game_stats**](docs/GamesApi.md#get_team_game_stats) | **GET** /games/teams | Team game stats
*GamesApi* | [**get_team_records**](docs/GamesApi.md#get_team_records) | **GET** /records | Team records
*MetricsApi* | [**get_game_ppa**](docs/MetricsApi.md#get_game_ppa) | **GET** /ppa/games | Team Predicated Points Added (PPA/EPA) by game
*MetricsApi* | [**get_player_game_ppa**](docs/MetricsApi.md#get_player_game_ppa) | **GET** /ppa/players/games | Player Predicated Points Added (PPA/EPA) broken down by game
*MetricsApi* | [**get_player_season_ppa**](docs/MetricsApi.md#get_player_season_ppa) | **GET** /ppa/players/season | Player Predicated Points Added (PPA/EPA) broken down by season
*MetricsApi* | [**get_predicted_points**](docs/MetricsApi.md#get_predicted_points) | **GET** /ppa/predicted | Predicted Points (i.e. Expected Points or EP)
*MetricsApi* | [**get_pregame_win_probabilities**](docs/MetricsApi.md#get_pregame_win_probabilities) | **GET** /metrics/wp/pregame | Pregame win probability data
*MetricsApi* | [**get_team_ppa**](docs/MetricsApi.md#get_team_ppa) | **GET** /ppa/teams | Predicted Points Added (PPA/EPA) data by team
*MetricsApi* | [**get_win_probability_data**](docs/MetricsApi.md#get_win_probability_data) | **GET** /metrics/wp | Win probability chart data
*PlayersApi* | [**get_player_season_stats**](docs/PlayersApi.md#get_player_season_stats) | **GET** /stats/player/season | Player stats by season
*PlayersApi* | [**get_player_usage**](docs/PlayersApi.md#get_player_usage) | **GET** /player/usage | Player usage metrics broken down by season
*PlayersApi* | [**get_returning_production**](docs/PlayersApi.md#get_returning_production) | **GET** /player/returning | Team returning production metrics
*PlayersApi* | [**player_search**](docs/PlayersApi.md#player_search) | **GET** /player/search | Search for player information
*PlaysApi* | [**get_play_stat_types**](docs/PlaysApi.md#get_play_stat_types) | **GET** /play/stat/types | Types of player play stats
*PlaysApi* | [**get_play_stats**](docs/PlaysApi.md#get_play_stats) | **GET** /play/stats | Play stats by play
*PlaysApi* | [**get_play_types**](docs/PlaysApi.md#get_play_types) | **GET** /play/types | Play types
*PlaysApi* | [**get_plays**](docs/PlaysApi.md#get_plays) | **GET** /plays | Play by play data
*RankingsApi* | [**get_rankings**](docs/RankingsApi.md#get_rankings) | **GET** /rankings | Historical polls and rankings
*RatingsApi* | [**get_conference_sp_ratings**](docs/RatingsApi.md#get_conference_sp_ratings) | **GET** /ratings/sp/conferences | Historical SP+ ratings by conference
*RatingsApi* | [**get_sp_ratings**](docs/RatingsApi.md#get_sp_ratings) | **GET** /ratings/sp | Historical SP+ ratings
*RatingsApi* | [**get_srs_ratings**](docs/RatingsApi.md#get_srs_ratings) | **GET** /ratings/srs | Historical SRS ratings
*RecruitingApi* | [**get_recruiting_groups**](docs/RecruitingApi.md#get_recruiting_groups) | **GET** /recruiting/groups | Recruit position group ratings
*RecruitingApi* | [**get_recruiting_players**](docs/RecruitingApi.md#get_recruiting_players) | **GET** /recruiting/players | Player recruiting ratings and rankings
*RecruitingApi* | [**get_recruiting_teams**](docs/RecruitingApi.md#get_recruiting_teams) | **GET** /recruiting/teams | Team recruiting rankings and ratings
*StatsApi* | [**get_advanced_team_game_stats**](docs/StatsApi.md#get_advanced_team_game_stats) | **GET** /stats/game/advanced | Advanced team metrics by game
*StatsApi* | [**get_advanced_team_season_stats**](docs/StatsApi.md#get_advanced_team_season_stats) | **GET** /stats/season/advanced | Advanced team metrics by season
*StatsApi* | [**get_stat_categories**](docs/StatsApi.md#get_stat_categories) | **GET** /stats/categories | Team stat categories
*StatsApi* | [**get_team_season_stats**](docs/StatsApi.md#get_team_season_stats) | **GET** /stats/season | Team statistics by season
*TeamsApi* | [**get_fbs_teams**](docs/TeamsApi.md#get_fbs_teams) | **GET** /teams/fbs | FBS team list
*TeamsApi* | [**get_roster**](docs/TeamsApi.md#get_roster) | **GET** /roster | Team rosters
*TeamsApi* | [**get_talent**](docs/TeamsApi.md#get_talent) | **GET** /talent | Team talent composite rankings
*TeamsApi* | [**get_team_matchup**](docs/TeamsApi.md#get_team_matchup) | **GET** /teams/matchup | Team matchup history
*TeamsApi* | [**get_teams**](docs/TeamsApi.md#get_teams) | **GET** /teams | Team information
*VenuesApi* | [**get_venues**](docs/VenuesApi.md#get_venues) | **GET** /venues | Arena and venue information


## Documentation For Models

 - [AdvancedGameStat](docs/AdvancedGameStat.md)
 - [AdvancedGameStatOffense](docs/AdvancedGameStatOffense.md)
 - [AdvancedGameStatOffenseRushingPlays](docs/AdvancedGameStatOffenseRushingPlays.md)
 - [AdvancedGameStatOffenseStandardDowns](docs/AdvancedGameStatOffenseStandardDowns.md)
 - [AdvancedSeasonStat](docs/AdvancedSeasonStat.md)
 - [AdvancedSeasonStatOffense](docs/AdvancedSeasonStatOffense.md)
 - [AdvancedSeasonStatOffenseFieldPosition](docs/AdvancedSeasonStatOffenseFieldPosition.md)
 - [AdvancedSeasonStatOffenseRushingPlays](docs/AdvancedSeasonStatOffenseRushingPlays.md)
 - [AdvancedSeasonStatOffenseStandardDowns](docs/AdvancedSeasonStatOffenseStandardDowns.md)
 - [BoxScore](docs/BoxScore.md)
 - [BoxScorePlayers](docs/BoxScorePlayers.md)
 - [BoxScorePlayersAverage](docs/BoxScorePlayersAverage.md)
 - [BoxScorePlayersPpa](docs/BoxScorePlayersPpa.md)
 - [BoxScorePlayersUsage](docs/BoxScorePlayersUsage.md)
 - [BoxScoreTeams](docs/BoxScoreTeams.md)
 - [BoxScoreTeamsExplosiveness](docs/BoxScoreTeamsExplosiveness.md)
 - [BoxScoreTeamsFieldPosition](docs/BoxScoreTeamsFieldPosition.md)
 - [BoxScoreTeamsHavoc](docs/BoxScoreTeamsHavoc.md)
 - [BoxScoreTeamsOverall](docs/BoxScoreTeamsOverall.md)
 - [BoxScoreTeamsPpa](docs/BoxScoreTeamsPpa.md)
 - [BoxScoreTeamsRushing](docs/BoxScoreTeamsRushing.md)
 - [BoxScoreTeamsScoringOpportunities](docs/BoxScoreTeamsScoringOpportunities.md)
 - [BoxScoreTeamsSuccessRates](docs/BoxScoreTeamsSuccessRates.md)
 - [Conference](docs/Conference.md)
 - [ConferenceSPRating](docs/ConferenceSPRating.md)
 - [Drive](docs/Drive.md)
 - [DriveStartTime](docs/DriveStartTime.md)
 - [Game](docs/Game.md)
 - [GameLines](docs/GameLines.md)
 - [GameLinesLines](docs/GameLinesLines.md)
 - [GameMedia](docs/GameMedia.md)
 - [GamePPA](docs/GamePPA.md)
 - [GamePPAOffense](docs/GamePPAOffense.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Play](docs/Play.md)
 - [PlayStat](docs/PlayStat.md)
 - [PlayStatType](docs/PlayStatType.md)
 - [PlayType](docs/PlayType.md)
 - [PlayWP](docs/PlayWP.md)
 - [Player](docs/Player.md)
 - [PlayerGame](docs/PlayerGame.md)
 - [PlayerGameAthletes](docs/PlayerGameAthletes.md)
 - [PlayerGameCategories](docs/PlayerGameCategories.md)
 - [PlayerGamePPA](docs/PlayerGamePPA.md)
 - [PlayerGamePPAAveragePPA](docs/PlayerGamePPAAveragePPA.md)
 - [PlayerGameSchool](docs/PlayerGameSchool.md)
 - [PlayerGameTeams](docs/PlayerGameTeams.md)
 - [PlayerGameTypes](docs/PlayerGameTypes.md)
 - [PlayerSearchResult](docs/PlayerSearchResult.md)
 - [PlayerSeasonPPA](docs/PlayerSeasonPPA.md)
 - [PlayerSeasonPPAAveragePPA](docs/PlayerSeasonPPAAveragePPA.md)
 - [PlayerSeasonStat](docs/PlayerSeasonStat.md)
 - [PlayerUsage](docs/PlayerUsage.md)
 - [PlayerUsageUsage](docs/PlayerUsageUsage.md)
 - [PositionGroupRecruitingRating](docs/PositionGroupRecruitingRating.md)
 - [PredictedPoints](docs/PredictedPoints.md)
 - [PregameWP](docs/PregameWP.md)
 - [RankingWeek](docs/RankingWeek.md)
 - [RankingWeekPolls](docs/RankingWeekPolls.md)
 - [RankingWeekRanks](docs/RankingWeekRanks.md)
 - [Recruit](docs/Recruit.md)
 - [ReturningProduction](docs/ReturningProduction.md)
 - [Team](docs/Team.md)
 - [TeamGame](docs/TeamGame.md)
 - [TeamGameStats](docs/TeamGameStats.md)
 - [TeamGameTeams](docs/TeamGameTeams.md)
 - [TeamMatchup](docs/TeamMatchup.md)
 - [TeamMatchupGames](docs/TeamMatchupGames.md)
 - [TeamPPA](docs/TeamPPA.md)
 - [TeamPPAOffense](docs/TeamPPAOffense.md)
 - [TeamPPAOffenseCumulative](docs/TeamPPAOffenseCumulative.md)
 - [TeamRecord](docs/TeamRecord.md)
 - [TeamRecordTotal](docs/TeamRecordTotal.md)
 - [TeamRecruitingRank](docs/TeamRecruitingRank.md)
 - [TeamSPRating](docs/TeamSPRating.md)
 - [TeamSPRatingDefense](docs/TeamSPRatingDefense.md)
 - [TeamSPRatingDefenseHavoc](docs/TeamSPRatingDefenseHavoc.md)
 - [TeamSPRatingOffense](docs/TeamSPRatingOffense.md)
 - [TeamSPRatingSpecialTeams](docs/TeamSPRatingSpecialTeams.md)
 - [TeamSRSRating](docs/TeamSRSRating.md)
 - [TeamSeason](docs/TeamSeason.md)
 - [TeamSeasonStat](docs/TeamSeasonStat.md)
 - [TeamTalent](docs/TeamTalent.md)
 - [Venue](docs/Venue.md)
 - [VenueLocation](docs/VenueLocation.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

admin@collegefootballdata.com

