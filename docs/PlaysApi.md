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



Queries live play-by-play data and advanced stats

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
    game_id = 56 # int | Game Id filter

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
 **game_id** | **int**| Game Id filter | 

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



Retrieves available play stat types

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



Retrieve player-play associations (limit 2000)

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
    year = 56 # int | Optional year filter (optional)
    week = 56 # int | Optional week filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    game_id = 56 # int | Optional gameId filter (optional)
    athlete_id = 56 # int | Optional athleteId filter (optional)
    stat_type_id = 56 # int | Optional statTypeId filter (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)

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
 **year** | **int**| Optional year filter | [optional] 
 **week** | **int**| Optional week filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **game_id** | **int**| Optional gameId filter | [optional] 
 **athlete_id** | **int**| Optional athleteId filter | [optional] 
 **stat_type_id** | **int**| Optional statTypeId filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 

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



Retrieves available play types

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



Retrieves historical play data

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
    year = 56 # int | Required year filter
    week = 56 # int | Required week filter
    team = 'team_example' # str | Optional team filter (optional)
    offense = 'offense_example' # str | Optional offensive team filter (optional)
    defense = 'defense_example' # str | Optional defensive team filter (optional)
    offense_conference = 'offense_conference_example' # str | Optional offensive conference filter (optional)
    defense_conference = 'defense_conference_example' # str | Optional defensive conference filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)
    play_type = 'play_type_example' # str | Optoinal play type abbreviation filter (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Optional division classification filter (optional)

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
 **year** | **int**| Required year filter | 
 **week** | **int**| Required week filter | 
 **team** | **str**| Optional team filter | [optional] 
 **offense** | **str**| Optional offensive team filter | [optional] 
 **defense** | **str**| Optional defensive team filter | [optional] 
 **offense_conference** | **str**| Optional offensive conference filter | [optional] 
 **defense_conference** | **str**| Optional defensive conference filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 
 **play_type** | **str**| Optoinal play type abbreviation filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **classification** | [**DivisionClassification**](.md)| Optional division classification filter | [optional] 

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

