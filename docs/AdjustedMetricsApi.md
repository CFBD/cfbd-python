# cfbd.AdjustedMetricsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_adjusted_player_passing_stats**](AdjustedMetricsApi.md#get_adjusted_player_passing_stats) | **GET** /wepa/players/passing | 
[**get_adjusted_player_rushing_stats**](AdjustedMetricsApi.md#get_adjusted_player_rushing_stats) | **GET** /wepa/players/rushing | 
[**get_adjusted_team_season_stats**](AdjustedMetricsApi.md#get_adjusted_team_season_stats) | **GET** /wepa/team/season | 
[**get_kicker_paar**](AdjustedMetricsApi.md#get_kicker_paar) | **GET** /wepa/players/kicking | 


# **get_adjusted_player_passing_stats**
> List[PlayerWeightedEPA] get_adjusted_player_passing_stats(year=year, team=team, conference=conference, position=position)



Returns opponent-adjusted player passing metrics.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_weighted_epa import PlayerWeightedEPA
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
    api_instance = cfbd.AdjustedMetricsApi(api_client)
    year = 56 # int | Season year. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference abbreviation. (optional)
    position = 'position_example' # str | Player position abbreviation. (optional)

    try:
        api_response = api_instance.get_adjusted_player_passing_stats(year=year, team=team, conference=conference, position=position)
        print("The response of AdjustedMetricsApi->get_adjusted_player_passing_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustedMetricsApi->get_adjusted_player_passing_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference abbreviation. | [optional] 
 **position** | **str**| Player position abbreviation. | [optional] 

### Return type

[**List[PlayerWeightedEPA]**](PlayerWeightedEPA.md)

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

# **get_adjusted_player_rushing_stats**
> List[PlayerWeightedEPA] get_adjusted_player_rushing_stats(year=year, team=team, conference=conference, position=position)



Returns opponent-adjusted player rushing metrics.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.player_weighted_epa import PlayerWeightedEPA
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
    api_instance = cfbd.AdjustedMetricsApi(api_client)
    year = 56 # int | Season year. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference abbreviation. (optional)
    position = 'position_example' # str | Player position abbreviation. (optional)

    try:
        api_response = api_instance.get_adjusted_player_rushing_stats(year=year, team=team, conference=conference, position=position)
        print("The response of AdjustedMetricsApi->get_adjusted_player_rushing_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustedMetricsApi->get_adjusted_player_rushing_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference abbreviation. | [optional] 
 **position** | **str**| Player position abbreviation. | [optional] 

### Return type

[**List[PlayerWeightedEPA]**](PlayerWeightedEPA.md)

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

# **get_adjusted_team_season_stats**
> List[AdjustedTeamMetrics] get_adjusted_team_season_stats(year=year, team=team, conference=conference)



Returns opponent-adjusted team statistics by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.adjusted_team_metrics import AdjustedTeamMetrics
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
    api_instance = cfbd.AdjustedMetricsApi(api_client)
    year = 56 # int | Season year. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)

    try:
        api_response = api_instance.get_adjusted_team_season_stats(year=year, team=team, conference=conference)
        print("The response of AdjustedMetricsApi->get_adjusted_team_season_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustedMetricsApi->get_adjusted_team_season_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 

### Return type

[**List[AdjustedTeamMetrics]**](AdjustedTeamMetrics.md)

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

# **get_kicker_paar**
> List[KickerPAAR] get_kicker_paar(year=year, team=team, conference=conference)



Returns Points Added Above Replacement (PAAR) ratings for kickers.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.kicker_paar import KickerPAAR
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
    api_instance = cfbd.AdjustedMetricsApi(api_client)
    year = 56 # int | Season year. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference abbreviation. (optional)

    try:
        api_response = api_instance.get_kicker_paar(year=year, team=team, conference=conference)
        print("The response of AdjustedMetricsApi->get_kicker_paar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustedMetricsApi->get_kicker_paar: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference abbreviation. | [optional] 

### Return type

[**List[KickerPAAR]**](KickerPAAR.md)

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

