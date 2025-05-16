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



Retrieves an advanced box score for a game

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
    id = 56 # int | Required game id filter

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
 **id** | **int**| Required game id filter | 

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



Retrieves calendar information

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
    year = 56 # int | Required year filter

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
 **year** | **int**| Required year filter | 

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



Retrieves player box score statistics

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
    year = 56 # int | Required year filter (along with one of week, team, or conference), unless id is specified (optional)
    week = 56 # int | Optional week filter, required if team and conference not specified (optional)
    team = 'team_example' # str | Optional team filter, required if week and conference not specified (optional)
    conference = 'conference_example' # str | Optional conference filter, required if week and team not specified (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Optional division classification filter (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    category = 'category_example' # str | Optional player statistical category filter (optional)
    id = 56 # int | Optional id filter to retrieve a single game (optional)

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
 **year** | **int**| Required year filter (along with one of week, team, or conference), unless id is specified | [optional] 
 **week** | **int**| Optional week filter, required if team and conference not specified | [optional] 
 **team** | **str**| Optional team filter, required if week and conference not specified | [optional] 
 **conference** | **str**| Optional conference filter, required if week and team not specified | [optional] 
 **classification** | [**DivisionClassification**](.md)| Optional division classification filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **category** | **str**| Optional player statistical category filter | [optional] 
 **id** | **int**| Optional id filter to retrieve a single game | [optional] 

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



Retrieves team box score statistics

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
    year = 56 # int | Required year filter (along with one of week, team, or conference), unless id is specified (optional)
    week = 56 # int | Optional week filter, required if team and conference not specified (optional)
    team = 'team_example' # str | Optional team filter, required if week and conference not specified (optional)
    conference = 'conference_example' # str | Optional conference filter, required if week and team not specified (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Optional division classification filter (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    id = 56 # int | Optional id filter to retrieve a single game (optional)

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
 **year** | **int**| Required year filter (along with one of week, team, or conference), unless id is specified | [optional] 
 **week** | **int**| Optional week filter, required if team and conference not specified | [optional] 
 **team** | **str**| Optional team filter, required if week and conference not specified | [optional] 
 **conference** | **str**| Optional conference filter, required if week and team not specified | [optional] 
 **classification** | [**DivisionClassification**](.md)| Optional division classification filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **id** | **int**| Optional id filter to retrieve a single game | [optional] 

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
> List[Game] get_games(year=year, week=week, season_type=season_type, classification=classification, team=team, home=home, away=away, conference=conference, id=id)



Retrieves historical game data

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.game import Game
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
    year = 56 # int | Required year filter (except when id is specified) (optional)
    week = 56 # int | Optional week filter (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Optional division classification filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    home = 'home_example' # str | Optional home team filter (optional)
    away = 'away_example' # str | Optional away team filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)
    id = 56 # int | Game id filter to retrieve a single game (optional)

    try:
        api_response = api_instance.get_games(year=year, week=week, season_type=season_type, classification=classification, team=team, home=home, away=away, conference=conference, id=id)
        print("The response of GamesApi->get_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_games: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Required year filter (except when id is specified) | [optional] 
 **week** | **int**| Optional week filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **classification** | [**DivisionClassification**](.md)| Optional division classification filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **home** | **str**| Optional home team filter | [optional] 
 **away** | **str**| Optional away team filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 
 **id** | **int**| Game id filter to retrieve a single game | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> List[GameMedia] get_media(year, season_type=season_type, week=week, team=team, conference=conference, media_type=media_type, classification=classification)



Retrieves media information for games

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
    year = 56 # int | Required year filter
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    week = 56 # int | Optional week filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)
    media_type = cfbd.MediaType() # MediaType | Optional media type filter (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Optional division classification filter (optional)

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
 **year** | **int**| Required year filter | 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **week** | **int**| Optional week filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 
 **media_type** | [**MediaType**](.md)| Optional media type filter | [optional] 
 **classification** | [**DivisionClassification**](.md)| Optional division classification filter | [optional] 

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



Retrieves historical team records

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
    year = 56 # int | Year filter, required if team not specified (optional)
    team = 'team_example' # str | Team filter, required if year not specified (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)

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
 **year** | **int**| Year filter, required if team not specified | [optional] 
 **team** | **str**| Team filter, required if year not specified | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 

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



Retrieves live scoreboard data

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
    classification = cfbd.DivisionClassification() # DivisionClassification | Optional division classification filter, defaults to fbs (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)

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
 **classification** | [**DivisionClassification**](.md)| Optional division classification filter, defaults to fbs | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 

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



Retrieve historical and future weather data (Patreon only)

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
    year = 56 # int | Year filter, required if game id not specified (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    week = 56 # int | Optional week filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Optional division classification filter (optional)
    game_id = 56 # int | Filter for retrieving a single game (optional)

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
 **year** | **int**| Year filter, required if game id not specified | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **week** | **int**| Optional week filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 
 **classification** | [**DivisionClassification**](.md)| Optional division classification filter | [optional] 
 **game_id** | **int**| Filter for retrieving a single game | [optional] 

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

