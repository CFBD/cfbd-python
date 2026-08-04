# cfbd.GamesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advanced_box_score**](GamesApi.md#get_advanced_box_score) | **GET** /game/box/advanced | 
[**get_calendar**](GamesApi.md#get_calendar) | **GET** /calendar | 
[**get_game_player_stats**](GamesApi.md#get_game_player_stats) | **GET** /games/players | 
[**get_game_team_stats**](GamesApi.md#get_game_team_stats) | **GET** /games/teams | 
[**get_games**](GamesApi.md#get_games) | **GET** /games | 
[**get_media**](GamesApi.md#get_media) | **GET** /games/media | 
[**get_records**](GamesApi.md#get_records) | **GET** /records | 
[**get_scoreboard**](GamesApi.md#get_scoreboard) | **GET** /scoreboard | 
[**get_weather**](GamesApi.md#get_weather) | **GET** /games/weather | 


# **get_advanced_box_score**
> AdvancedBoxScore get_advanced_box_score(id)



Returns an advanced box score for a game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.advanced_box_score import AdvancedBoxScore
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
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
    api_instance = cfbd.GamesApi(api_client)
    id = 56 # int | Game ID.

    try:
        api_response = api_instance.get_advanced_box_score(id)
        print("The response of GamesApi->get_advanced_box_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_advanced_box_score: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Game ID. | 

### Return type

[**AdvancedBoxScore**](AdvancedBoxScore.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calendar**
> List[CalendarWeek] get_calendar(year)



Returns the week-by-week season calendar.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.calendar_week import CalendarWeek
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
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
    api_instance = cfbd.GamesApi(api_client)
    year = 56 # int | Season year.

    try:
        api_response = api_instance.get_calendar(year)
        print("The response of GamesApi->get_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_calendar: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 

### Return type

[**List[CalendarWeek]**](CalendarWeek.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game_player_stats**
> List[GamePlayerStats] get_game_player_stats(year=year, week=week, team=team, conference=conference, classification=classification, season_type=season_type, category=category, id=id)



Returns player box score statistics by game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.game_player_stats import GamePlayerStats
from cfbd.models.season_type import SeasonType
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
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
    api_instance = cfbd.GamesApi(api_client)
    year = 56 # int | Season year. Required unless `id` is specified. (optional)
    week = 56 # int | Week number. One of `week`, `team`, or `conference` is required when filtering by year. (optional)
    team = 'team_example' # str | Team name. One of `week`, `team`, or `conference` is required when filtering by year. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. One of `week`, `team`, or `conference` is required when filtering by year. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    category = 'category_example' # str | Player statistical category. (optional)
    id = 56 # int | Game ID. When specified, returns statistics for that game. (optional)

    try:
        api_response = api_instance.get_game_player_stats(year=year, week=week, team=team, conference=conference, classification=classification, season_type=season_type, category=category, id=id)
        print("The response of GamesApi->get_game_player_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_game_player_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;id&#x60; is specified. | [optional] 
 **week** | **int**| Week number. One of &#x60;week&#x60;, &#x60;team&#x60;, or &#x60;conference&#x60; is required when filtering by year. | [optional] 
 **team** | **str**| Team name. One of &#x60;week&#x60;, &#x60;team&#x60;, or &#x60;conference&#x60; is required when filtering by year. | [optional] 
 **conference** | **str**| Conference name or abbreviation. One of &#x60;week&#x60;, &#x60;team&#x60;, or &#x60;conference&#x60; is required when filtering by year. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **category** | **str**| Player statistical category. | [optional] 
 **id** | **int**| Game ID. When specified, returns statistics for that game. | [optional] 

### Return type

[**List[GamePlayerStats]**](GamePlayerStats.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game_team_stats**
> List[GameTeamStats] get_game_team_stats(year=year, week=week, team=team, conference=conference, classification=classification, season_type=season_type, id=id)



Returns team box score statistics by game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.game_team_stats import GameTeamStats
from cfbd.models.season_type import SeasonType
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
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
    api_instance = cfbd.GamesApi(api_client)
    year = 56 # int | Season year. Required unless `id` is specified. (optional)
    week = 56 # int | Week number. One of `week`, `team`, or `conference` is required when filtering by year. (optional)
    team = 'team_example' # str | Team name. One of `week`, `team`, or `conference` is required when filtering by year. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. One of `week`, `team`, or `conference` is required when filtering by year. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    id = 56 # int | Game ID. When specified, returns statistics for that game. (optional)

    try:
        api_response = api_instance.get_game_team_stats(year=year, week=week, team=team, conference=conference, classification=classification, season_type=season_type, id=id)
        print("The response of GamesApi->get_game_team_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_game_team_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;id&#x60; is specified. | [optional] 
 **week** | **int**| Week number. One of &#x60;week&#x60;, &#x60;team&#x60;, or &#x60;conference&#x60; is required when filtering by year. | [optional] 
 **team** | **str**| Team name. One of &#x60;week&#x60;, &#x60;team&#x60;, or &#x60;conference&#x60; is required when filtering by year. | [optional] 
 **conference** | **str**| Conference name or abbreviation. One of &#x60;week&#x60;, &#x60;team&#x60;, or &#x60;conference&#x60; is required when filtering by year. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **id** | **int**| Game ID. When specified, returns statistics for that game. | [optional] 

### Return type

[**List[GameTeamStats]**](GameTeamStats.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_games**
> List[Game] get_games(year=year, week=week, season_type=season_type, classification=classification, team=team, home=home, away=away, conference=conference, id=id, competition=competition, round=round)



Returns historical game data.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.game import Game
from cfbd.models.playoff_competition import PlayoffCompetition
from cfbd.models.playoff_round import PlayoffRound
from cfbd.models.season_type import SeasonType
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
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
    api_instance = cfbd.GamesApi(api_client)
    year = 56 # int | Season year. Required unless `id` is specified. (optional)
    week = 56 # int | Week number. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. (optional)
    team = 'team_example' # str | Team name on either side of the game. (optional)
    home = 'home_example' # str | Home team name. (optional)
    away = 'away_example' # str | Away team name. (optional)
    conference = 'conference_example' # str | Conference of either team. (optional)
    id = 56 # int | Game ID. When specified, returns data for that game. (optional)
    competition = cfbd.PlayoffCompetition() # PlayoffCompetition | Playoff competition. (optional)
    round = cfbd.PlayoffRound() # PlayoffRound | Playoff round. Requires `competition`. (optional)

    try:
        api_response = api_instance.get_games(year=year, week=week, season_type=season_type, classification=classification, team=team, home=home, away=away, conference=conference, id=id, competition=competition, round=round)
        print("The response of GamesApi->get_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_games: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;id&#x60; is specified. | [optional] 
 **week** | **int**| Week number. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. | [optional] 
 **team** | **str**| Team name on either side of the game. | [optional] 
 **home** | **str**| Home team name. | [optional] 
 **away** | **str**| Away team name. | [optional] 
 **conference** | **str**| Conference of either team. | [optional] 
 **id** | **int**| Game ID. When specified, returns data for that game. | [optional] 
 **competition** | [**PlayoffCompetition**](.md)| Playoff competition. | [optional] 
 **round** | [**PlayoffRound**](.md)| Playoff round. Requires &#x60;competition&#x60;. | [optional] 

### Return type

[**List[Game]**](Game.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> List[GameMedia] get_media(year, season_type=season_type, week=week, team=team, conference=conference, media_type=media_type, classification=classification)



Returns broadcast and media information for games.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.game_media import GameMedia
from cfbd.models.media_type import MediaType
from cfbd.models.season_type import SeasonType
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
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
    api_instance = cfbd.GamesApi(api_client)
    year = 56 # int | Season year.
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    week = 56 # int | Week number. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    media_type = cfbd.MediaType() # MediaType | Media type. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. (optional)

    try:
        api_response = api_instance.get_media(year, season_type=season_type, week=week, team=team, conference=conference, media_type=media_type, classification=classification)
        print("The response of GamesApi->get_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_media: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **week** | **int**| Week number. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **media_type** | [**MediaType**](.md)| Media type. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. | [optional] 

### Return type

[**List[GameMedia]**](GameMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_records**
> List[TeamRecords] get_records(year=year, team=team, conference=conference)



Returns historical team records by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_records import TeamRecords
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
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
    api_instance = cfbd.GamesApi(api_client)
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)

    try:
        api_response = api_instance.get_records(year=year, team=team, conference=conference)
        print("The response of GamesApi->get_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 

### Return type

[**List[TeamRecords]**](TeamRecords.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scoreboard**
> List[ScoreboardGame] get_scoreboard(classification=classification, conference=conference)



Returns current scoreboard data.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.scoreboard_game import ScoreboardGame
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
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
    api_instance = cfbd.GamesApi(api_client)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)

    try:
        api_response = api_instance.get_scoreboard(classification=classification, conference=conference)
        print("The response of GamesApi->get_scoreboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_scoreboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 

### Return type

[**List[ScoreboardGame]**](ScoreboardGame.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weather**
> List[GameWeather] get_weather(year=year, season_type=season_type, week=week, team=team, conference=conference, classification=classification, game_id=game_id)



Returns historical and forecast weather data for games. Requires Patreon.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.game_weather import GameWeather
from cfbd.models.season_type import SeasonType
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
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
    api_instance = cfbd.GamesApi(api_client)
    year = 56 # int | Season year. Required unless `gameId` is specified. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    week = 56 # int | Week number. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. (optional)
    game_id = 56 # int | Game ID. When specified, returns weather for that game. (optional)

    try:
        api_response = api_instance.get_weather(year=year, season_type=season_type, week=week, team=team, conference=conference, classification=classification, game_id=game_id)
        print("The response of GamesApi->get_weather:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_weather: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;gameId&#x60; is specified. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **week** | **int**| Week number. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. | [optional] 
 **game_id** | **int**| Game ID. When specified, returns weather for that game. | [optional] 

### Return type

[**List[GameWeather]**](GameWeather.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

