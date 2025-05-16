# cfbd.StatsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advanced_game_stats**](StatsApi.md#get_advanced_game_stats) | **GET** /stats/game/advanced | 
[**get_advanced_season_stats**](StatsApi.md#get_advanced_season_stats) | **GET** /stats/season/advanced | 
[**get_categories**](StatsApi.md#get_categories) | **GET** /stats/categories | 
[**get_player_season_stats**](StatsApi.md#get_player_season_stats) | **GET** /stats/player/season | 
[**get_team_stats**](StatsApi.md#get_team_stats) | **GET** /stats/season | 


# **get_advanced_game_stats**
> List[AdvancedGameStat] get_advanced_game_stats(year=year, team=team, week=week, opponent=opponent, exclude_garbage_time=exclude_garbage_time, season_type=season_type)



Retrieves advanced statistics aggregated by game

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.advanced_game_stat import AdvancedGameStat
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
    api_instance = cfbd.StatsApi(api_client)
    year = 56 # int | Year filter, required if team not specified (optional)
    team = 'team_example' # str | Team filter, required if year not specified (optional)
    week = 3.4 # float | Optional week filter (optional)
    opponent = 'opponent_example' # str | Optional opponent filter (optional)
    exclude_garbage_time = True # bool | Garbage time exclusion filter, defaults to false (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)

    try:
        api_response = api_instance.get_advanced_game_stats(year=year, team=team, week=week, opponent=opponent, exclude_garbage_time=exclude_garbage_time, season_type=season_type)
        print("The response of StatsApi->get_advanced_game_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_advanced_game_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter, required if team not specified | [optional] 
 **team** | **str**| Team filter, required if year not specified | [optional] 
 **week** | **float**| Optional week filter | [optional] 
 **opponent** | **str**| Optional opponent filter | [optional] 
 **exclude_garbage_time** | **bool**| Garbage time exclusion filter, defaults to false | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 

### Return type

[**List[AdvancedGameStat]**](AdvancedGameStat.md)

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

# **get_advanced_season_stats**
> List[AdvancedSeasonStat] get_advanced_season_stats(year=year, team=team, exclude_garbage_time=exclude_garbage_time, start_week=start_week, end_week=end_week)



Retrieves advanced season statistics for teams

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.advanced_season_stat import AdvancedSeasonStat
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
    api_instance = cfbd.StatsApi(api_client)
    year = 56 # int | Year filter, required if team not specified (optional)
    team = 'team_example' # str | Team filter, required if year not specified (optional)
    exclude_garbage_time = True # bool | Garbage time exclusion filter, defaults to false (optional)
    start_week = 56 # int | Optional start week range filter (optional)
    end_week = 56 # int | Optional end week range filter (optional)

    try:
        api_response = api_instance.get_advanced_season_stats(year=year, team=team, exclude_garbage_time=exclude_garbage_time, start_week=start_week, end_week=end_week)
        print("The response of StatsApi->get_advanced_season_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_advanced_season_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter, required if team not specified | [optional] 
 **team** | **str**| Team filter, required if year not specified | [optional] 
 **exclude_garbage_time** | **bool**| Garbage time exclusion filter, defaults to false | [optional] 
 **start_week** | **int**| Optional start week range filter | [optional] 
 **end_week** | **int**| Optional end week range filter | [optional] 

### Return type

[**List[AdvancedSeasonStat]**](AdvancedSeasonStat.md)

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

# **get_categories**
> List[str] get_categories()



Gets team statistical categories

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
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
    api_instance = cfbd.StatsApi(api_client)

    try:
        api_response = api_instance.get_categories()
        print("The response of StatsApi->get_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_categories: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **get_player_season_stats**
> List[PlayerStat] get_player_season_stats(year, conference=conference, team=team, start_week=start_week, end_week=end_week, season_type=season_type, category=category)



Retrieves aggregated player statistics for a given season

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_stat import PlayerStat
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
    api_instance = cfbd.StatsApi(api_client)
    year = 56 # int | Required year filter
    conference = 'conference_example' # str | Optional conference filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    start_week = 56 # int | Optional starting week range (optional)
    end_week = 56 # int | Optional ending week range (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    category = 'category_example' # str | Optional category filter (optional)

    try:
        api_response = api_instance.get_player_season_stats(year, conference=conference, team=team, start_week=start_week, end_week=end_week, season_type=season_type, category=category)
        print("The response of StatsApi->get_player_season_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_player_season_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Required year filter | 
 **conference** | **str**| Optional conference filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **start_week** | **int**| Optional starting week range | [optional] 
 **end_week** | **int**| Optional ending week range | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **category** | **str**| Optional category filter | [optional] 

### Return type

[**List[PlayerStat]**](PlayerStat.md)

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

# **get_team_stats**
> List[TeamStat] get_team_stats(year=year, team=team, conference=conference, start_week=start_week, end_week=end_week)



Retrieves aggregated team season statistics

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_stat import TeamStat
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
    api_instance = cfbd.StatsApi(api_client)
    year = 56 # int | Year filter, required if team not specified (optional)
    team = 'team_example' # str | Team filter, required if year not specified (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)
    start_week = 56 # int | Optional week start range filter (optional)
    end_week = 56 # int | Optional week end range filter (optional)

    try:
        api_response = api_instance.get_team_stats(year=year, team=team, conference=conference, start_week=start_week, end_week=end_week)
        print("The response of StatsApi->get_team_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_team_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter, required if team not specified | [optional] 
 **team** | **str**| Team filter, required if year not specified | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 
 **start_week** | **int**| Optional week start range filter | [optional] 
 **end_week** | **int**| Optional week end range filter | [optional] 

### Return type

[**List[TeamStat]**](TeamStat.md)

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

