# cfbd.PlaysApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_live_plays**](PlaysApi.md#get_live_plays) | **GET** /live/plays | 
[**get_play_stat_types**](PlaysApi.md#get_play_stat_types) | **GET** /plays/stats/types | 
[**get_play_stats**](PlaysApi.md#get_play_stats) | **GET** /plays/stats | 
[**get_play_types**](PlaysApi.md#get_play_types) | **GET** /plays/types | 
[**get_plays**](PlaysApi.md#get_plays) | **GET** /plays | 


# **get_live_plays**
> LiveGame get_live_plays(game_id)



Returns live play-by-play data and advanced metrics for a game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.live_game import LiveGame
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
    api_instance = cfbd.PlaysApi(api_client)
    game_id = 56 # int | Game ID.

    try:
        api_response = api_instance.get_live_plays(game_id)
        print("The response of PlaysApi->get_live_plays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_live_plays: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| Game ID. | 

### Return type

[**LiveGame**](LiveGame.md)

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

# **get_play_stat_types**
> List[PlayStatType] get_play_stat_types()



Returns the available play stat types.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.play_stat_type import PlayStatType
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
    api_instance = cfbd.PlaysApi(api_client)

    try:
        api_response = api_instance.get_play_stat_types()
        print("The response of PlaysApi->get_play_stat_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_play_stat_types: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[PlayStatType]**](PlayStatType.md)

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

# **get_play_stats**
> List[PlayStat] get_play_stats(year=year, week=week, team=team, game_id=game_id, athlete_id=athlete_id, stat_type_id=stat_type_id, season_type=season_type, conference=conference)



Returns player and play-stat associations, limited to 2,000 records.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.play_stat import PlayStat
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
    api_instance = cfbd.PlaysApi(api_client)
    year = 56 # int | Season year. (optional)
    week = 56 # int | Week number. (optional)
    team = 'team_example' # str | Team name. (optional)
    game_id = 56 # int | Game ID. (optional)
    athlete_id = 56 # int | Athlete ID. (optional)
    stat_type_id = 56 # int | Play stat type ID. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)

    try:
        api_response = api_instance.get_play_stats(year=year, week=week, team=team, game_id=game_id, athlete_id=athlete_id, stat_type_id=stat_type_id, season_type=season_type, conference=conference)
        print("The response of PlaysApi->get_play_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_play_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | [optional] 
 **week** | **int**| Week number. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **game_id** | **int**| Game ID. | [optional] 
 **athlete_id** | **int**| Athlete ID. | [optional] 
 **stat_type_id** | **int**| Play stat type ID. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 

### Return type

[**List[PlayStat]**](PlayStat.md)

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

# **get_play_types**
> List[PlayType] get_play_types()



Returns the available play types.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.play_type import PlayType
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
    api_instance = cfbd.PlaysApi(api_client)

    try:
        api_response = api_instance.get_play_types()
        print("The response of PlaysApi->get_play_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_play_types: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[PlayType]**](PlayType.md)

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

# **get_plays**
> List[Play] get_plays(year, week, team=team, offense=offense, defense=defense, offense_conference=offense_conference, defense_conference=defense_conference, conference=conference, play_type=play_type, season_type=season_type, classification=classification)



Returns historical play-by-play data.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.play import Play
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
    api_instance = cfbd.PlaysApi(api_client)
    year = 56 # int | Season year.
    week = 56 # int | Week number.
    team = 'team_example' # str | Team name on either side of the play. (optional)
    offense = 'offense_example' # str | Offensive team name. (optional)
    defense = 'defense_example' # str | Defensive team name. (optional)
    offense_conference = 'offense_conference_example' # str | Offensive team conference. (optional)
    defense_conference = 'defense_conference_example' # str | Defensive team conference. (optional)
    conference = 'conference_example' # str | Conference of either team. (optional)
    play_type = 'play_type_example' # str | Play type abbreviation. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification of either team. (optional)

    try:
        api_response = api_instance.get_plays(year, week, team=team, offense=offense, defense=defense, offense_conference=offense_conference, defense_conference=defense_conference, conference=conference, play_type=play_type, season_type=season_type, classification=classification)
        print("The response of PlaysApi->get_plays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_plays: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 
 **week** | **int**| Week number. | 
 **team** | **str**| Team name on either side of the play. | [optional] 
 **offense** | **str**| Offensive team name. | [optional] 
 **defense** | **str**| Defensive team name. | [optional] 
 **offense_conference** | **str**| Offensive team conference. | [optional] 
 **defense_conference** | **str**| Defensive team conference. | [optional] 
 **conference** | **str**| Conference of either team. | [optional] 
 **play_type** | **str**| Play type abbreviation. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification of either team. | [optional] 

### Return type

[**List[Play]**](Play.md)

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

