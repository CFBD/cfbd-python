# cfbd.StatsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advanced_game_stats**](StatsApi.md#get_advanced_game_stats) | **GET** /stats/game/advanced | 
[**get_advanced_season_stats**](StatsApi.md#get_advanced_season_stats) | **GET** /stats/season/advanced | 
[**get_categories**](StatsApi.md#get_categories) | **GET** /stats/categories | 
[**get_game_havoc_stats**](StatsApi.md#get_game_havoc_stats) | **GET** /stats/game/havoc | 
[**get_player_game_success_rates**](StatsApi.md#get_player_game_success_rates) | **GET** /stats/player/success/game | 
[**get_player_season_stats**](StatsApi.md#get_player_season_stats) | **GET** /stats/player/season | 
[**get_player_season_success_rates**](StatsApi.md#get_player_season_success_rates) | **GET** /stats/player/success | 
[**get_team_stats**](StatsApi.md#get_team_stats) | **GET** /stats/season | 


# **get_advanced_game_stats**
> List[AdvancedGameStat] get_advanced_game_stats(year=year, team=team, week=week, opponent=opponent, exclude_garbage_time=exclude_garbage_time, season_type=season_type)



Returns advanced team statistics aggregated by game.

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
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    week = 3.4 # float | Week number. (optional)
    opponent = 'opponent_example' # str | Opponent team name. (optional)
    exclude_garbage_time = True # bool | Excludes garbage-time plays when `true`. Defaults to `false`. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)

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
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **week** | **float**| Week number. | [optional] 
 **opponent** | **str**| Opponent team name. | [optional] 
 **exclude_garbage_time** | **bool**| Excludes garbage-time plays when &#x60;true&#x60;. Defaults to &#x60;false&#x60;. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 

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
> List[AdvancedSeasonStat] get_advanced_season_stats(year=year, team=team, exclude_garbage_time=exclude_garbage_time, start_week=start_week, end_week=end_week, classification=classification)



Returns advanced team statistics aggregated by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.advanced_season_stat import AdvancedSeasonStat
from cfbd.models.division_classification import DivisionClassification
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
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    exclude_garbage_time = True # bool | Excludes garbage-time plays when `true`. Defaults to `false`. (optional)
    start_week = 56 # int | Earliest week to include. (optional)
    end_week = 56 # int | Latest week to include. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_advanced_season_stats(year=year, team=team, exclude_garbage_time=exclude_garbage_time, start_week=start_week, end_week=end_week, classification=classification)
        print("The response of StatsApi->get_advanced_season_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_advanced_season_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **exclude_garbage_time** | **bool**| Excludes garbage-time plays when &#x60;true&#x60;. Defaults to &#x60;false&#x60;. | [optional] 
 **start_week** | **int**| Earliest week to include. | [optional] 
 **end_week** | **int**| Latest week to include. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

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



Returns the available team statistical categories.

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

# **get_game_havoc_stats**
> List[GameHavocStats] get_game_havoc_stats(year=year, team=team, week=week, opponent=opponent, season_type=season_type)



Returns team havoc statistics aggregated by game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.game_havoc_stats import GameHavocStats
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
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    week = 3.4 # float | Week number. (optional)
    opponent = 'opponent_example' # str | Opponent team name. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)

    try:
        api_response = api_instance.get_game_havoc_stats(year=year, team=team, week=week, opponent=opponent, season_type=season_type)
        print("The response of StatsApi->get_game_havoc_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_game_havoc_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **week** | **float**| Week number. | [optional] 
 **opponent** | **str**| Opponent team name. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 

### Return type

[**List[GameHavocStats]**](GameHavocStats.md)

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

# **get_player_game_success_rates**
> List[PlayerGameSuccessRate] get_player_game_success_rates(year, week=week, season_type=season_type, conference=conference, team=team, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)



Returns player passing and rushing success rates by game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_game_success_rate import PlayerGameSuccessRate
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
    year = 56 # int | Season year.
    week = 56 # int | Week number. Required unless `team` or `playerId` is specified. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    conference = 'conference_example' # str | Conference abbreviation. (optional)
    team = 'team_example' # str | Team name. (optional)
    player_id = 56 # int | Player ID. (optional)
    threshold = 56 # int | Minimum credited passing and rushing plays. (optional)
    exclude_garbage_time = True # bool | Excludes garbage-time plays when `true`. (optional)

    try:
        api_response = api_instance.get_player_game_success_rates(year, week=week, season_type=season_type, conference=conference, team=team, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)
        print("The response of StatsApi->get_player_game_success_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_player_game_success_rates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 
 **week** | **int**| Week number. Required unless &#x60;team&#x60; or &#x60;playerId&#x60; is specified. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **conference** | **str**| Conference abbreviation. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **player_id** | **int**| Player ID. | [optional] 
 **threshold** | **int**| Minimum credited passing and rushing plays. | [optional] 
 **exclude_garbage_time** | **bool**| Excludes garbage-time plays when &#x60;true&#x60;. | [optional] 

### Return type

[**List[PlayerGameSuccessRate]**](PlayerGameSuccessRate.md)

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



Returns player statistics aggregated by season.

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
    year = 56 # int | Season year.
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    team = 'team_example' # str | Team name. (optional)
    start_week = 56 # int | Earliest week to include. (optional)
    end_week = 56 # int | Latest week to include. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    category = 'category_example' # str | Statistical category. (optional)

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
 **year** | **int**| Season year. | 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **start_week** | **int**| Earliest week to include. | [optional] 
 **end_week** | **int**| Latest week to include. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **category** | **str**| Statistical category. | [optional] 

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

# **get_player_season_success_rates**
> List[PlayerSeasonSuccessRate] get_player_season_success_rates(year=year, conference=conference, team=team, player_id=player_id, season_type=season_type, start_week=start_week, end_week=end_week, threshold=threshold, exclude_garbage_time=exclude_garbage_time)



Returns player passing and rushing success rates by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_season_success_rate import PlayerSeasonSuccessRate
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
    year = 56 # int | Season year. Required unless `playerId` is specified. (optional)
    conference = 'conference_example' # str | Conference abbreviation. (optional)
    team = 'team_example' # str | Team name. (optional)
    player_id = 56 # int | Player ID. Required unless `year` is specified. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    start_week = 56 # int | Earliest week to include. (optional)
    end_week = 56 # int | Latest week to include. (optional)
    threshold = 56 # int | Minimum credited passing and rushing plays. (optional)
    exclude_garbage_time = True # bool | Excludes garbage-time plays when `true`. (optional)

    try:
        api_response = api_instance.get_player_season_success_rates(year=year, conference=conference, team=team, player_id=player_id, season_type=season_type, start_week=start_week, end_week=end_week, threshold=threshold, exclude_garbage_time=exclude_garbage_time)
        print("The response of StatsApi->get_player_season_success_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_player_season_success_rates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;playerId&#x60; is specified. | [optional] 
 **conference** | **str**| Conference abbreviation. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **player_id** | **int**| Player ID. Required unless &#x60;year&#x60; is specified. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **start_week** | **int**| Earliest week to include. | [optional] 
 **end_week** | **int**| Latest week to include. | [optional] 
 **threshold** | **int**| Minimum credited passing and rushing plays. | [optional] 
 **exclude_garbage_time** | **bool**| Excludes garbage-time plays when &#x60;true&#x60;. | [optional] 

### Return type

[**List[PlayerSeasonSuccessRate]**](PlayerSeasonSuccessRate.md)

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
> List[TeamStat] get_team_stats(year=year, team=team, conference=conference, start_week=start_week, end_week=end_week, classification=classification)



Returns team statistics aggregated by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
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
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    start_week = 56 # int | Earliest week to include. (optional)
    end_week = 56 # int | Latest week to include. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_team_stats(year=year, team=team, conference=conference, start_week=start_week, end_week=end_week, classification=classification)
        print("The response of StatsApi->get_team_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_team_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **start_week** | **int**| Earliest week to include. | [optional] 
 **end_week** | **int**| Latest week to include. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

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

