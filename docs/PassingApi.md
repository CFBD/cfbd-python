# cfbd.PassingApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_passing_plays**](PassingApi.md#get_passing_plays) | **GET** /passing/plays | 
[**get_player_passing_by_game**](PassingApi.md#get_player_passing_by_game) | **GET** /passing/players/games | 
[**get_player_passing_by_season**](PassingApi.md#get_player_passing_by_season) | **GET** /passing/players/season | 
[**get_team_passing_by_game**](PassingApi.md#get_team_passing_by_game) | **GET** /passing/teams/games | 
[**get_team_passing_by_season**](PassingApi.md#get_team_passing_by_season) | **GET** /passing/teams/season | 


# **get_passing_plays**
> List[PassingPlay] get_passing_plays(year, team=team, week=week, game_id=game_id, season_type=season_type, offense=offense, defense=defense, conference=conference, passer_id=passer_id, target_id=target_id, outcome=outcome, classification=classification)



Returns enriched pass attempts with stored PPA, success, and location-analysis eligibility.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.pass_outcome import PassOutcome
from cfbd.models.passing_play import PassingPlay
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
    api_instance = cfbd.PassingApi(api_client)
    year = 56 # int | Season year.
    team = 'team_example' # str | Team name on either side of the pass. Either team or week is required. (optional)
    week = 56 # int | Week number. Either team or week is required. (optional)
    game_id = 56 # int | Game ID. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    offense = 'offense_example' # str | Offensive team name. (optional)
    defense = 'defense_example' # str | Defensive team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation on either side of the pass. (optional)
    passer_id = 'passer_id_example' # str | Passer athlete ID. (optional)
    target_id = 'target_id_example' # str | Intended target athlete ID. (optional)
    outcome = cfbd.PassOutcome() # PassOutcome | Pass outcome. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_passing_plays(year, team=team, week=week, game_id=game_id, season_type=season_type, offense=offense, defense=defense, conference=conference, passer_id=passer_id, target_id=target_id, outcome=outcome, classification=classification)
        print("The response of PassingApi->get_passing_plays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PassingApi->get_passing_plays: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 
 **team** | **str**| Team name on either side of the pass. Either team or week is required. | [optional] 
 **week** | **int**| Week number. Either team or week is required. | [optional] 
 **game_id** | **int**| Game ID. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **offense** | **str**| Offensive team name. | [optional] 
 **defense** | **str**| Defensive team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation on either side of the pass. | [optional] 
 **passer_id** | **str**| Passer athlete ID. | [optional] 
 **target_id** | **str**| Intended target athlete ID. | [optional] 
 **outcome** | [**PassOutcome**](.md)| Pass outcome. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[PassingPlay]**](PassingPlay.md)

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

# **get_player_passing_by_game**
> List[PlayerPassingGame] get_player_passing_by_game(year, week=week, season_type=season_type, team=team, conference=conference, passer_id=passer_id, classification=classification)



Returns passer production, advanced metrics, and pass-location breakdowns by game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.player_passing_game import PlayerPassingGame
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
    api_instance = cfbd.PassingApi(api_client)
    year = 56 # int | Season year. Required.
    week = 56 # int | Week number. Either passerId, team, or week is required. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. Either passerId, team, or week is required. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    passer_id = 'passer_id_example' # str | Passer athlete ID. Either passerId, team, or week is required. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_player_passing_by_game(year, week=week, season_type=season_type, team=team, conference=conference, passer_id=passer_id, classification=classification)
        print("The response of PassingApi->get_player_passing_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PassingApi->get_player_passing_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required. | 
 **week** | **int**| Week number. Either passerId, team, or week is required. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. Either passerId, team, or week is required. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **passer_id** | **str**| Passer athlete ID. Either passerId, team, or week is required. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[PlayerPassingGame]**](PlayerPassingGame.md)

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

# **get_player_passing_by_season**
> List[PlayerPassingSeason] get_player_passing_by_season(year=year, season_type=season_type, team=team, conference=conference, passer_id=passer_id, classification=classification)



Returns passer production, advanced metrics, and pass-location breakdowns by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.player_passing_season import PlayerPassingSeason
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
    api_instance = cfbd.PassingApi(api_client)
    year = 56 # int | Season year. Required unless passerId is specified. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    passer_id = 'passer_id_example' # str | Passer athlete ID. Required unless year is specified. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_player_passing_by_season(year=year, season_type=season_type, team=team, conference=conference, passer_id=passer_id, classification=classification)
        print("The response of PassingApi->get_player_passing_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PassingApi->get_player_passing_by_season: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless passerId is specified. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **passer_id** | **str**| Passer athlete ID. Required unless year is specified. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[PlayerPassingSeason]**](PlayerPassingSeason.md)

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

# **get_team_passing_by_game**
> List[TeamPassingGame] get_team_passing_by_game(year, week=week, season_type=season_type, team=team, conference=conference, classification=classification)



Returns team passing production, advanced metrics, and pass-location
breakdowns by game for offense and defense.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.season_type import SeasonType
from cfbd.models.team_passing_game import TeamPassingGame
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
    api_instance = cfbd.PassingApi(api_client)
    year = 56 # int | Season year. Required.
    week = 56 # int | Week number. Either team or week is required. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. Either team or week is required. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_team_passing_by_game(year, week=week, season_type=season_type, team=team, conference=conference, classification=classification)
        print("The response of PassingApi->get_team_passing_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PassingApi->get_team_passing_by_game: %s\n" % e)
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

[**List[TeamPassingGame]**](TeamPassingGame.md)

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

# **get_team_passing_by_season**
> List[TeamPassingSeason] get_team_passing_by_season(year=year, season_type=season_type, team=team, conference=conference, classification=classification)



Returns team passing production, advanced metrics, and pass-location
breakdowns by season for offense and defense.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.season_type import SeasonType
from cfbd.models.team_passing_season import TeamPassingSeason
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
    api_instance = cfbd.PassingApi(api_client)
    year = 56 # int | Season year. Required unless team is specified. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. Required unless year is specified. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_team_passing_by_season(year=year, season_type=season_type, team=team, conference=conference, classification=classification)
        print("The response of PassingApi->get_team_passing_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PassingApi->get_team_passing_by_season: %s\n" % e)
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

[**List[TeamPassingSeason]**](TeamPassingSeason.md)

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

