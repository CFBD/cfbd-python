# cfbd.PlayersApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_usage**](PlayersApi.md#get_player_usage) | **GET** /player/usage | 
[**get_returning_production**](PlayersApi.md#get_returning_production) | **GET** /player/returning | 
[**get_transfer_portal**](PlayersApi.md#get_transfer_portal) | **GET** /player/portal | 
[**search_players**](PlayersApi.md#search_players) | **GET** /player/search | 


# **get_player_usage**
> List[PlayerUsage] get_player_usage(year, conference=conference, position=position, team=team, player_id=player_id, exclude_garbage_time=exclude_garbage_time)



Retrieves player usage data for a given season

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
    year = 56 # int | Required year filter
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    position = 'position_example' # str | Optional position abbreivation filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    player_id = 56 # int | Optional player id filter (optional)
    exclude_garbage_time = True # bool | Optional exclude garbage time flag, defaults to false (optional)

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
 **year** | **int**| Required year filter | 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **position** | **str**| Optional position abbreivation filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **player_id** | **int**| Optional player id filter | [optional] 
 **exclude_garbage_time** | **bool**| Optional exclude garbage time flag, defaults to false | [optional] 

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



Retrieves returning production data. Either a year or team filter must be specified.

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
    year = 56 # int | Year filter, required if team not specified (optional)
    team = 'team_example' # str | Team filter, required if year not specified (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)

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
 **year** | **int**| Year filter, required if team not specified | [optional] 
 **team** | **str**| Team filter, required if year not specified | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 

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



Retrieves transfer portal data for a given year

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
    year = 56 # int | Required year filter

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
 **year** | **int**| Required year filter | 

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



Search for players (lists top 100 results)

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
    search_term = 'search_term_example' # str | Search term for matching player name
    year = 56 # int | Optional year filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    position = 'position_example' # str | Optional position abbreviation filter (optional)

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
 **search_term** | **str**| Search term for matching player name | 
 **year** | **int**| Optional year filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **position** | **str**| Optional position abbreviation filter | [optional] 

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

