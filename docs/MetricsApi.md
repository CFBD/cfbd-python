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



Queries field goal expected points values

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



Query Predicted Points values by down and distance

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
    down = 56 # int | Down value
    distance = 56 # int | Distance value

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
 **down** | **int**| Down value | 
 **distance** | **int**| Distance value | 

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
> List[TeamGamePredictedPointsAdded] get_predicted_points_added_by_game(year, week=week, season_type=season_type, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time)



Retrieves historical team PPA metrics by game

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
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
    year = 56 # int | Required year filter
    week = 56 # int | Optional week filter (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    exclude_garbage_time = True # bool | Optional flag to exclude garbage time plays (optional)

    try:
        api_response = api_instance.get_predicted_points_added_by_game(year, week=week, season_type=season_type, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time)
        print("The response of MetricsApi->get_predicted_points_added_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_predicted_points_added_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Required year filter | 
 **week** | **int**| Optional week filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **exclude_garbage_time** | **bool**| Optional flag to exclude garbage time plays | [optional] 

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



Queries player PPA statistics by game

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
    year = 56 # int | Required year filter
    week = 56 # int | Week filter, required if team not specified (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    team = 'team_example' # str | Team filter, required if week not specified (optional)
    position = 'position_example' # str | Optional player position abbreviation filter (optional)
    player_id = 'player_id_example' # str | Optional player ID filter (optional)
    threshold = 3.4 # float | Threshold value for minimum number of plays (optional)
    exclude_garbage_time = True # bool | Optional flag to exclude garbage time plays (optional)

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
 **year** | **int**| Required year filter | 
 **week** | **int**| Week filter, required if team not specified | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **team** | **str**| Team filter, required if week not specified | [optional] 
 **position** | **str**| Optional player position abbreviation filter | [optional] 
 **player_id** | **str**| Optional player ID filter | [optional] 
 **threshold** | **float**| Threshold value for minimum number of plays | [optional] 
 **exclude_garbage_time** | **bool**| Optional flag to exclude garbage time plays | [optional] 

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



Queries player PPA statistics by season

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
    year = 56 # int | Year filter, required if playerId not specified (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    position = 'position_example' # str | Optional position abbreviation filter (optional)
    player_id = 'player_id_example' # str | Player ID filter, required if year not specified (optional)
    threshold = 3.4 # float | Threshold value for minimum number of plays (optional)
    exclude_garbage_time = True # bool | Optional flag to exclude garbage time plays (optional)

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
 **year** | **int**| Year filter, required if playerId not specified | [optional] 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **position** | **str**| Optional position abbreviation filter | [optional] 
 **player_id** | **str**| Player ID filter, required if year not specified | [optional] 
 **threshold** | **float**| Threshold value for minimum number of plays | [optional] 
 **exclude_garbage_time** | **bool**| Optional flag to exclude garbage time plays | [optional] 

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
> List[TeamSeasonPredictedPointsAdded] get_predicted_points_added_by_team(year=year, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time)



Retrieves historical team PPA metrics by season

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
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
    year = 56 # int | Year filter, required if team not specified (optional)
    team = 'team_example' # str | Team filter, required if year not specified (optional)
    conference = 'conference_example' # str | Conference abbreviation filter (optional)
    exclude_garbage_time = True # bool | Exclude garbage time plays (optional)

    try:
        api_response = api_instance.get_predicted_points_added_by_team(year=year, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time)
        print("The response of MetricsApi->get_predicted_points_added_by_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_predicted_points_added_by_team: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter, required if team not specified | [optional] 
 **team** | **str**| Team filter, required if year not specified | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 
 **exclude_garbage_time** | **bool**| Exclude garbage time plays | [optional] 

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



Queries pregame win probabilities

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
    year = 56 # int | Optional year filter (optional)
    week = 56 # int | Optional week filter (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    team = 'team_example' # str | Optional team filter (optional)

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
 **year** | **int**| Optional year filter | [optional] 
 **week** | **int**| Optional week filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 

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



Query play win probabilities by game

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
    game_id = 56 # int | Required game ID filter

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
 **game_id** | **int**| Required game ID filter | 

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

