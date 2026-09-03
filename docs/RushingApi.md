# cfbd.RushingApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_rushing_by_game**](RushingApi.md#get_player_rushing_by_game) | **GET** /rushing/players/games | 
[**get_player_rushing_by_season**](RushingApi.md#get_player_rushing_by_season) | **GET** /rushing/players/season | 
[**get_rushing_plays**](RushingApi.md#get_rushing_plays) | **GET** /rushing/plays | 
[**get_team_rushing_by_game**](RushingApi.md#get_team_rushing_by_game) | **GET** /rushing/teams/games | 
[**get_team_rushing_by_season**](RushingApi.md#get_team_rushing_by_season) | **GET** /rushing/teams/season | 


# **get_player_rushing_by_game**
> List[PlayerRushingGame] get_player_rushing_by_game(year=year, week=week, season_type=season_type, team=team, conference=conference, rusher_id=rusher_id, classification=classification)



Returns individually attributed rusher production by game.

Player totals include only guarded rusher attribution, including
individually attributed sacks. They do not include team-only or unresolved
attempts and therefore are not expected to sum to team totals.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.player_rushing_game import PlayerRushingGame
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
    api_instance = cfbd.RushingApi(api_client)
    year = 56 # int | Season year. Requires team or week; optional when rusherId is specified alone. (optional)
    week = 56 # int | Week number. Requires year; either team or week is required with year. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name; either team or week is required with year. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    rusher_id = 'rusher_id_example' # str | Rusher athlete ID. Required unless year is specified. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_player_rushing_by_game(year=year, week=week, season_type=season_type, team=team, conference=conference, rusher_id=rusher_id, classification=classification)
        print("The response of RushingApi->get_player_rushing_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RushingApi->get_player_rushing_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Requires team or week; optional when rusherId is specified alone. | [optional] 
 **week** | **int**| Week number. Requires year; either team or week is required with year. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name; either team or week is required with year. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **rusher_id** | **str**| Rusher athlete ID. Required unless year is specified. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[PlayerRushingGame]**](PlayerRushingGame.md)

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

# **get_player_rushing_by_season**
> List[PlayerRushingSeason] get_player_rushing_by_season(year=year, season_type=season_type, team=team, conference=conference, rusher_id=rusher_id, classification=classification)



Returns individually attributed rusher production by season.

Player totals include only guarded rusher attribution, including
individually attributed sacks. They do not include team-only or unresolved
attempts and therefore are not expected to sum to team totals.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.player_rushing_season import PlayerRushingSeason
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
    api_instance = cfbd.RushingApi(api_client)
    year = 56 # int | Season year. Required unless rusherId is specified. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    rusher_id = 'rusher_id_example' # str | Rusher athlete ID. Required unless year is specified. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_player_rushing_by_season(year=year, season_type=season_type, team=team, conference=conference, rusher_id=rusher_id, classification=classification)
        print("The response of RushingApi->get_player_rushing_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RushingApi->get_player_rushing_by_season: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless rusherId is specified. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **rusher_id** | **str**| Rusher athlete ID. Required unless year is specified. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[PlayerRushingSeason]**](PlayerRushingSeason.md)

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

# **get_rushing_plays**
> List[RushingPlay] get_rushing_plays(game_id=game_id, year=year, week=week, season_type=season_type, team=team, offense=offense, defense=defense, conference=conference, rusher_id=rusher_id, rush_direction=rush_direction, direction_analysis_eligible=direction_analysis_eligible, attribution_status=attribution_status, is_rushing_touchdown=is_rushing_touchdown, is_sack=is_sack, is_kneel=is_kneel, is_team_rush=is_team_rush, classification=classification)



Returns enriched rushing attempts.

Team results include sacks, kneels, team-only attempts, and unresolved
attribution. Direction eligibility identifies the ordinary-rush analysis
population; eligible attempts can still have an unknown direction.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.rush_attribution_status import RushAttributionStatus
from cfbd.models.rush_direction import RushDirection
from cfbd.models.rushing_play import RushingPlay
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
    api_instance = cfbd.RushingApi(api_client)
    game_id = 56 # int | Game ID. (optional)
    year = 56 # int | Season year. Requires team or week. (optional)
    week = 56 # int | Week number. Requires year; either team or week is required with year. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name on either side of the rush; either team or week is required with year. (optional)
    offense = 'offense_example' # str | Rushing offense team name. (optional)
    defense = 'defense_example' # str | Defending team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation on either side of the rush. (optional)
    rusher_id = 'rusher_id_example' # str | Rusher athlete ID. (optional)
    rush_direction = cfbd.RushDirection() # RushDirection | Rushing direction. (optional)
    direction_analysis_eligible = True # bool | Filters attempts by ordinary direction-analysis eligibility. (optional)
    attribution_status = cfbd.RushAttributionStatus() # RushAttributionStatus | Rusher attribution status. (optional)
    is_rushing_touchdown = True # bool | Filters known rushing touchdown results. (optional)
    is_sack = True # bool | Filters sack attempts. (optional)
    is_kneel = True # bool | Filters kneel attempts. (optional)
    is_team_rush = True # bool | Filters team-only rushing attempts. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_rushing_plays(game_id=game_id, year=year, week=week, season_type=season_type, team=team, offense=offense, defense=defense, conference=conference, rusher_id=rusher_id, rush_direction=rush_direction, direction_analysis_eligible=direction_analysis_eligible, attribution_status=attribution_status, is_rushing_touchdown=is_rushing_touchdown, is_sack=is_sack, is_kneel=is_kneel, is_team_rush=is_team_rush, classification=classification)
        print("The response of RushingApi->get_rushing_plays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RushingApi->get_rushing_plays: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| Game ID. | [optional] 
 **year** | **int**| Season year. Requires team or week. | [optional] 
 **week** | **int**| Week number. Requires year; either team or week is required with year. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name on either side of the rush; either team or week is required with year. | [optional] 
 **offense** | **str**| Rushing offense team name. | [optional] 
 **defense** | **str**| Defending team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation on either side of the rush. | [optional] 
 **rusher_id** | **str**| Rusher athlete ID. | [optional] 
 **rush_direction** | [**RushDirection**](.md)| Rushing direction. | [optional] 
 **direction_analysis_eligible** | **bool**| Filters attempts by ordinary direction-analysis eligibility. | [optional] 
 **attribution_status** | [**RushAttributionStatus**](.md)| Rusher attribution status. | [optional] 
 **is_rushing_touchdown** | **bool**| Filters known rushing touchdown results. | [optional] 
 **is_sack** | **bool**| Filters sack attempts. | [optional] 
 **is_kneel** | **bool**| Filters kneel attempts. | [optional] 
 **is_team_rush** | **bool**| Filters team-only rushing attempts. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[RushingPlay]**](RushingPlay.md)

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

# **get_team_rushing_by_game**
> List[TeamRushingGame] get_team_rushing_by_game(year, week=week, season_type=season_type, team=team, conference=conference, classification=classification)



Returns team rushing production by game.

Team totals include sacks, kneels, team-only attempts, and unresolved
attribution. Defense contains rushing production allowed.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.season_type import SeasonType
from cfbd.models.team_rushing_game import TeamRushingGame
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
    api_instance = cfbd.RushingApi(api_client)
    year = 56 # int | Season year. Required.
    week = 56 # int | Week number. Either team or week is required. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. Either team or week is required. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_team_rushing_by_game(year, week=week, season_type=season_type, team=team, conference=conference, classification=classification)
        print("The response of RushingApi->get_team_rushing_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RushingApi->get_team_rushing_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required. | 
 **week** | **int**| Week number. Either team or week is required. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. Either team or week is required. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[TeamRushingGame]**](TeamRushingGame.md)

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

# **get_team_rushing_by_season**
> List[TeamRushingSeason] get_team_rushing_by_season(year=year, season_type=season_type, team=team, conference=conference, classification=classification)



Returns team rushing production by season.

Team totals include sacks, kneels, team-only attempts, and unresolved
attribution. Defense contains rushing production allowed.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.season_type import SeasonType
from cfbd.models.team_rushing_season import TeamRushingSeason
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
    api_instance = cfbd.RushingApi(api_client)
    year = 56 # int | Season year. Required unless team is specified. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. Required unless year is specified. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_team_rushing_by_season(year=year, season_type=season_type, team=team, conference=conference, classification=classification)
        print("The response of RushingApi->get_team_rushing_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RushingApi->get_team_rushing_by_season: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless team is specified. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. Required unless year is specified. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[TeamRushingSeason]**](TeamRushingSeason.md)

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

