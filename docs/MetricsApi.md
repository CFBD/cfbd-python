# cfbd.MetricsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_field_goal_expected_points**](MetricsApi.md#get_field_goal_expected_points) | **GET** /metrics/fg/ep | 
[**get_predicted_points**](MetricsApi.md#get_predicted_points) | **GET** /ppa/predicted | 
[**get_predicted_points_added_by_game**](MetricsApi.md#get_predicted_points_added_by_game) | **GET** /ppa/games | 
[**get_predicted_points_added_by_player_game**](MetricsApi.md#get_predicted_points_added_by_player_game) | **GET** /ppa/players/games | 
[**get_predicted_points_added_by_player_season**](MetricsApi.md#get_predicted_points_added_by_player_season) | **GET** /ppa/players/season | 
[**get_predicted_points_added_by_team**](MetricsApi.md#get_predicted_points_added_by_team) | **GET** /ppa/teams | 
[**get_pregame_win_probabilities**](MetricsApi.md#get_pregame_win_probabilities) | **GET** /metrics/wp/pregame | 
[**get_win_probability**](MetricsApi.md#get_win_probability) | **GET** /metrics/wp | 


# **get_field_goal_expected_points**
> List[FieldGoalEP] get_field_goal_expected_points()



Returns expected points values for field goal attempts.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.field_goal_ep import FieldGoalEP
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
    api_instance = cfbd.MetricsApi(api_client)

    try:
        api_response = api_instance.get_field_goal_expected_points()
        print("The response of MetricsApi->get_field_goal_expected_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_field_goal_expected_points: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[FieldGoalEP]**](FieldGoalEP.md)

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

# **get_predicted_points**
> List[PredictedPointsValue] get_predicted_points(down, distance)



Returns predicted points values by down and distance.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.predicted_points_value import PredictedPointsValue
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
    api_instance = cfbd.MetricsApi(api_client)
    down = 56 # int | Down number.
    distance = 56 # int | Distance to gain, in yards.

    try:
        api_response = api_instance.get_predicted_points(down, distance)
        print("The response of MetricsApi->get_predicted_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_predicted_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **down** | **int**| Down number. | 
 **distance** | **int**| Distance to gain, in yards. | 

### Return type

[**List[PredictedPointsValue]**](PredictedPointsValue.md)

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

# **get_predicted_points_added_by_game**
> List[TeamGamePredictedPointsAdded] get_predicted_points_added_by_game(year, week=week, season_type=season_type, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time, classification=classification)



Returns team Predicted Points Added (PPA) metrics by game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.season_type import SeasonType
from cfbd.models.team_game_predicted_points_added import TeamGamePredictedPointsAdded
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
    api_instance = cfbd.MetricsApi(api_client)
    year = 56 # int | Season year.
    week = 56 # int | Week number. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference abbreviation. (optional)
    exclude_garbage_time = True # bool | Excludes garbage-time plays when `true`. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_predicted_points_added_by_game(year, week=week, season_type=season_type, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time, classification=classification)
        print("The response of MetricsApi->get_predicted_points_added_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_predicted_points_added_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 
 **week** | **int**| Week number. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference abbreviation. | [optional] 
 **exclude_garbage_time** | **bool**| Excludes garbage-time plays when &#x60;true&#x60;. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[TeamGamePredictedPointsAdded]**](TeamGamePredictedPointsAdded.md)

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

# **get_predicted_points_added_by_player_game**
> List[PlayerGamePredictedPointsAdded] get_predicted_points_added_by_player_game(year, week=week, season_type=season_type, team=team, position=position, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)



Returns player Predicted Points Added (PPA) metrics by game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_game_predicted_points_added import PlayerGamePredictedPointsAdded
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
    api_instance = cfbd.MetricsApi(api_client)
    year = 56 # int | Season year.
    week = 56 # int | Week number. Required unless `team` is specified. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. Required unless `week` is specified. (optional)
    position = 'position_example' # str | Player position abbreviation. (optional)
    player_id = 'player_id_example' # str | Player ID. (optional)
    threshold = 3.4 # float | Minimum number of plays. (optional)
    exclude_garbage_time = True # bool | Excludes garbage-time plays when `true`. (optional)

    try:
        api_response = api_instance.get_predicted_points_added_by_player_game(year, week=week, season_type=season_type, team=team, position=position, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)
        print("The response of MetricsApi->get_predicted_points_added_by_player_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_predicted_points_added_by_player_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 
 **week** | **int**| Week number. Required unless &#x60;team&#x60; is specified. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;week&#x60; is specified. | [optional] 
 **position** | **str**| Player position abbreviation. | [optional] 
 **player_id** | **str**| Player ID. | [optional] 
 **threshold** | **float**| Minimum number of plays. | [optional] 
 **exclude_garbage_time** | **bool**| Excludes garbage-time plays when &#x60;true&#x60;. | [optional] 

### Return type

[**List[PlayerGamePredictedPointsAdded]**](PlayerGamePredictedPointsAdded.md)

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

# **get_predicted_points_added_by_player_season**
> List[PlayerSeasonPredictedPointsAdded] get_predicted_points_added_by_player_season(year=year, conference=conference, team=team, position=position, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)



Returns player Predicted Points Added (PPA) metrics by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_season_predicted_points_added import PlayerSeasonPredictedPointsAdded
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
    api_instance = cfbd.MetricsApi(api_client)
    year = 56 # int | Season year. Required unless `playerId` is specified. (optional)
    conference = 'conference_example' # str | Conference abbreviation. (optional)
    team = 'team_example' # str | Team name. (optional)
    position = 'position_example' # str | Player position abbreviation. (optional)
    player_id = 'player_id_example' # str | Player ID. Required unless `year` is specified. (optional)
    threshold = 3.4 # float | Minimum number of plays. (optional)
    exclude_garbage_time = True # bool | Excludes garbage-time plays when `true`. (optional)

    try:
        api_response = api_instance.get_predicted_points_added_by_player_season(year=year, conference=conference, team=team, position=position, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)
        print("The response of MetricsApi->get_predicted_points_added_by_player_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_predicted_points_added_by_player_season: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;playerId&#x60; is specified. | [optional] 
 **conference** | **str**| Conference abbreviation. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **position** | **str**| Player position abbreviation. | [optional] 
 **player_id** | **str**| Player ID. Required unless &#x60;year&#x60; is specified. | [optional] 
 **threshold** | **float**| Minimum number of plays. | [optional] 
 **exclude_garbage_time** | **bool**| Excludes garbage-time plays when &#x60;true&#x60;. | [optional] 

### Return type

[**List[PlayerSeasonPredictedPointsAdded]**](PlayerSeasonPredictedPointsAdded.md)

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

# **get_predicted_points_added_by_team**
> List[TeamSeasonPredictedPointsAdded] get_predicted_points_added_by_team(year=year, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time, classification=classification)



Returns team Predicted Points Added (PPA) metrics by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.team_season_predicted_points_added import TeamSeasonPredictedPointsAdded
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
    api_instance = cfbd.MetricsApi(api_client)
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    conference = 'conference_example' # str | Conference abbreviation. (optional)
    exclude_garbage_time = True # bool | Excludes garbage-time plays when `true`. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_predicted_points_added_by_team(year=year, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time, classification=classification)
        print("The response of MetricsApi->get_predicted_points_added_by_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_predicted_points_added_by_team: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **conference** | **str**| Conference abbreviation. | [optional] 
 **exclude_garbage_time** | **bool**| Excludes garbage-time plays when &#x60;true&#x60;. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[TeamSeasonPredictedPointsAdded]**](TeamSeasonPredictedPointsAdded.md)

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

# **get_pregame_win_probabilities**
> List[PregameWinProbability] get_pregame_win_probabilities(year=year, week=week, season_type=season_type, team=team)



Returns pregame win probabilities.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.pregame_win_probability import PregameWinProbability
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
    api_instance = cfbd.MetricsApi(api_client)
    year = 56 # int | Season year. (optional)
    week = 56 # int | Week number. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. (optional)

    try:
        api_response = api_instance.get_pregame_win_probabilities(year=year, week=week, season_type=season_type, team=team)
        print("The response of MetricsApi->get_pregame_win_probabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_pregame_win_probabilities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | [optional] 
 **week** | **int**| Week number. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. | [optional] 

### Return type

[**List[PregameWinProbability]**](PregameWinProbability.md)

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

# **get_win_probability**
> List[PlayWinProbability] get_win_probability(game_id)



Returns play-by-play win probabilities for a game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.play_win_probability import PlayWinProbability
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
    api_instance = cfbd.MetricsApi(api_client)
    game_id = 56 # int | Game ID.

    try:
        api_response = api_instance.get_win_probability(game_id)
        print("The response of MetricsApi->get_win_probability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_win_probability: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| Game ID. | 

### Return type

[**List[PlayWinProbability]**](PlayWinProbability.md)

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

