# cfbd.PuntingApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_punting_by_game**](PuntingApi.md#get_player_punting_by_game) | **GET** /punting/players/games | 
[**get_player_punting_by_season**](PuntingApi.md#get_player_punting_by_season) | **GET** /punting/players/season | 
[**get_punting_plays**](PuntingApi.md#get_punting_plays) | **GET** /punting/plays | 
[**get_team_punting_by_game**](PuntingApi.md#get_team_punting_by_game) | **GET** /punting/teams/games | 
[**get_team_punting_by_season**](PuntingApi.md#get_team_punting_by_season) | **GET** /punting/teams/season | 


# **get_player_punting_by_game**
> List[PlayerPuntingGame] get_player_punting_by_game(year, week=week, season_type=season_type, team=team, conference=conference, player_id=player_id, classification=classification)



Returns player punting and punt return statistics by game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.player_punting_game import PlayerPuntingGame
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
    api_instance = cfbd.PuntingApi(api_client)
    year = 56 # int | Season year. Required.
    week = 56 # int | Week number. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    player_id = 'player_id_example' # str | Player athlete ID. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_player_punting_by_game(year, week=week, season_type=season_type, team=team, conference=conference, player_id=player_id, classification=classification)
        print("The response of PuntingApi->get_player_punting_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PuntingApi->get_player_punting_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required. | 
 **week** | **int**| Week number. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **player_id** | **str**| Player athlete ID. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[PlayerPuntingGame]**](PlayerPuntingGame.md)

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

# **get_player_punting_by_season**
> List[PlayerPuntingSeason] get_player_punting_by_season(year, season_type=season_type, team=team, conference=conference, player_id=player_id, classification=classification)



Returns player punting and punt return statistics by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.player_punting_season import PlayerPuntingSeason
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
    api_instance = cfbd.PuntingApi(api_client)
    year = 56 # int | Season year. Required.
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    player_id = 'player_id_example' # str | Player athlete ID. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_player_punting_by_season(year, season_type=season_type, team=team, conference=conference, player_id=player_id, classification=classification)
        print("The response of PuntingApi->get_player_punting_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PuntingApi->get_player_punting_by_season: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required. | 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **player_id** | **str**| Player athlete ID. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[PlayerPuntingSeason]**](PlayerPuntingSeason.md)

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

# **get_punting_plays**
> List[PuntingPlay] get_punting_plays(game_id=game_id, year=year, week=week, season_type=season_type, team=team, punting_team=punting_team, receiving_team=receiving_team, conference=conference, punter_id=punter_id, returner_id=returner_id, classification=classification)



Returns enriched punt plays with yardage, field position, and outcomes.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.punting_play import PuntingPlay
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
    api_instance = cfbd.PuntingApi(api_client)
    game_id = 56 # int | Game ID. (optional)
    year = 56 # int | Season year. Required unless gameId is specified. (optional)
    week = 56 # int | Week number. Either week, a team filter, punterId, or returnerId is required with year. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name on either side of the punt. (optional)
    punting_team = 'punting_team_example' # str | Punting team name. (optional)
    receiving_team = 'receiving_team_example' # str | Receiving team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation on either side of the punt. (optional)
    punter_id = 'punter_id_example' # str | Punter athlete ID. (optional)
    returner_id = 'returner_id_example' # str | Returner athlete ID. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_punting_plays(game_id=game_id, year=year, week=week, season_type=season_type, team=team, punting_team=punting_team, receiving_team=receiving_team, conference=conference, punter_id=punter_id, returner_id=returner_id, classification=classification)
        print("The response of PuntingApi->get_punting_plays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PuntingApi->get_punting_plays: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| Game ID. | [optional] 
 **year** | **int**| Season year. Required unless gameId is specified. | [optional] 
 **week** | **int**| Week number. Either week, a team filter, punterId, or returnerId is required with year. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name on either side of the punt. | [optional] 
 **punting_team** | **str**| Punting team name. | [optional] 
 **receiving_team** | **str**| Receiving team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation on either side of the punt. | [optional] 
 **punter_id** | **str**| Punter athlete ID. | [optional] 
 **returner_id** | **str**| Returner athlete ID. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[PuntingPlay]**](PuntingPlay.md)

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

# **get_team_punting_by_game**
> List[TeamPuntingGame] get_team_punting_by_game(year, week=week, season_type=season_type, team=team, conference=conference, classification=classification)



Returns team punting and punt return statistics by game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.season_type import SeasonType
from cfbd.models.team_punting_game import TeamPuntingGame
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
    api_instance = cfbd.PuntingApi(api_client)
    year = 56 # int | Season year. Required.
    week = 56 # int | Week number. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_team_punting_by_game(year, week=week, season_type=season_type, team=team, conference=conference, classification=classification)
        print("The response of PuntingApi->get_team_punting_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PuntingApi->get_team_punting_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required. | 
 **week** | **int**| Week number. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[TeamPuntingGame]**](TeamPuntingGame.md)

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

# **get_team_punting_by_season**
> List[TeamPuntingSeason] get_team_punting_by_season(year, season_type=season_type, team=team, conference=conference, classification=classification)



Returns team punting and punt return statistics by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.season_type import SeasonType
from cfbd.models.team_punting_season import TeamPuntingSeason
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
    api_instance = cfbd.PuntingApi(api_client)
    year = 56 # int | Season year. Required.
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_team_punting_by_season(year, season_type=season_type, team=team, conference=conference, classification=classification)
        print("The response of PuntingApi->get_team_punting_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PuntingApi->get_team_punting_by_season: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required. | 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[TeamPuntingSeason]**](TeamPuntingSeason.md)

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

