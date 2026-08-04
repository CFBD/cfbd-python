# cfbd.PlayersApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_season_overview**](PlayersApi.md#get_player_season_overview) | **GET** /player/season/overview | 
[**get_player_usage**](PlayersApi.md#get_player_usage) | **GET** /player/usage | 
[**get_returning_production**](PlayersApi.md#get_returning_production) | **GET** /player/returning | 
[**get_transfer_portal**](PlayersApi.md#get_transfer_portal) | **GET** /player/portal | 
[**search_players**](PlayersApi.md#search_players) | **GET** /player/search | 


# **get_player_season_overview**
> PlayerSeasonOverview get_player_season_overview(year, player_id)



Returns a player season overview with box score, usage, and Predicted
Points Added (PPA) data.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_season_overview import PlayerSeasonOverview
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
    api_instance = cfbd.PlayersApi(api_client)
    year = 56 # int | Season year.
    player_id = 56 # int | Player ID.

    try:
        api_response = api_instance.get_player_season_overview(year, player_id)
        print("The response of PlayersApi->get_player_season_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player_season_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 
 **player_id** | **int**| Player ID. | 

### Return type

[**PlayerSeasonOverview**](PlayerSeasonOverview.md)

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

# **get_player_usage**
> List[PlayerUsage] get_player_usage(year, conference=conference, position=position, team=team, player_id=player_id, exclude_garbage_time=exclude_garbage_time)



Returns player usage metrics for a season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_usage import PlayerUsage
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
    api_instance = cfbd.PlayersApi(api_client)
    year = 56 # int | Season year.
    conference = 'conference_example' # str | Conference abbreviation. (optional)
    position = 'position_example' # str | Player position abbreviation. (optional)
    team = 'team_example' # str | Team name. (optional)
    player_id = 56 # int | Player ID. (optional)
    exclude_garbage_time = True # bool | Excludes garbage-time plays when `true`. Defaults to `false`. (optional)

    try:
        api_response = api_instance.get_player_usage(year, conference=conference, position=position, team=team, player_id=player_id, exclude_garbage_time=exclude_garbage_time)
        print("The response of PlayersApi->get_player_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 
 **conference** | **str**| Conference abbreviation. | [optional] 
 **position** | **str**| Player position abbreviation. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **player_id** | **int**| Player ID. | [optional] 
 **exclude_garbage_time** | **bool**| Excludes garbage-time plays when &#x60;true&#x60;. Defaults to &#x60;false&#x60;. | [optional] 

### Return type

[**List[PlayerUsage]**](PlayerUsage.md)

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

# **get_returning_production**
> List[ReturningProduction] get_returning_production(year=year, team=team, conference=conference)



Returns returning production metrics by team and season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.returning_production import ReturningProduction
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
    api_instance = cfbd.PlayersApi(api_client)
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)

    try:
        api_response = api_instance.get_returning_production(year=year, team=team, conference=conference)
        print("The response of PlayersApi->get_returning_production:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_returning_production: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 

### Return type

[**List[ReturningProduction]**](ReturningProduction.md)

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

# **get_transfer_portal**
> List[PlayerTransfer] get_transfer_portal(year)



Returns transfer portal entries for a season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_transfer import PlayerTransfer
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
    api_instance = cfbd.PlayersApi(api_client)
    year = 56 # int | Season year.

    try:
        api_response = api_instance.get_transfer_portal(year)
        print("The response of PlayersApi->get_transfer_portal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_transfer_portal: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 

### Return type

[**List[PlayerTransfer]**](PlayerTransfer.md)

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

# **search_players**
> List[PlayerSearchResult] search_players(search_term, year=year, team=team, position=position)



Returns up to 100 players whose names match the search term.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_search_result import PlayerSearchResult
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
    api_instance = cfbd.PlayersApi(api_client)
    search_term = 'search_term_example' # str | Full or partial player name.
    year = 56 # int | Season year. (optional)
    team = 'team_example' # str | Team name. (optional)
    position = 'position_example' # str | Player position abbreviation. (optional)

    try:
        api_response = api_instance.search_players(search_term, year=year, team=team, position=position)
        print("The response of PlayersApi->search_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->search_players: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Full or partial player name. | 
 **year** | **int**| Season year. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **position** | **str**| Player position abbreviation. | [optional] 

### Return type

[**List[PlayerSearchResult]**](PlayerSearchResult.md)

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

