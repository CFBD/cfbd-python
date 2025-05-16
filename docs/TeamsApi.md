# cfbd.TeamsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fbs_teams**](TeamsApi.md#get_fbs_teams) | **GET** /teams/fbs | 
[**get_matchup**](TeamsApi.md#get_matchup) | **GET** /teams/matchup | 
[**get_roster**](TeamsApi.md#get_roster) | **GET** /roster | 
[**get_talent**](TeamsApi.md#get_talent) | **GET** /talent | 
[**get_teams**](TeamsApi.md#get_teams) | **GET** /teams | 


# **get_fbs_teams**
> List[Team] get_fbs_teams(year=year)



Retrieves information on teams playing in the highest division of CFB

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team import Team
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
    api_instance = cfbd.TeamsApi(api_client)
    year = 56 # int | Year or season (optional)

    try:
        api_response = api_instance.get_fbs_teams(year=year)
        print("The response of TeamsApi->get_fbs_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_fbs_teams: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year or season | [optional] 

### Return type

[**List[Team]**](Team.md)

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

# **get_matchup**
> Matchup get_matchup(team1, team2, min_year=min_year, max_year=max_year)



Retrieves historical matchup details for two given teams

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.matchup import Matchup
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
    api_instance = cfbd.TeamsApi(api_client)
    team1 = 'team1_example' # str | First team to compare
    team2 = 'team2_example' # str | Second team to compare
    min_year = 56 # int | Optional starting year (optional)
    max_year = 56 # int | Optional ending year (optional)

    try:
        api_response = api_instance.get_matchup(team1, team2, min_year=min_year, max_year=max_year)
        print("The response of TeamsApi->get_matchup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_matchup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team1** | **str**| First team to compare | 
 **team2** | **str**| Second team to compare | 
 **min_year** | **int**| Optional starting year | [optional] 
 **max_year** | **int**| Optional ending year | [optional] 

### Return type

[**Matchup**](Matchup.md)

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

# **get_roster**
> List[RosterPlayer] get_roster(team=team, year=year)



Retrieves historical roster data

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.roster_player import RosterPlayer
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
    api_instance = cfbd.TeamsApi(api_client)
    team = 'team_example' # str | Optional team filter (optional)
    year = 56 # int | Optional year filter, defaults to 2023 (optional)

    try:
        api_response = api_instance.get_roster(team=team, year=year)
        print("The response of TeamsApi->get_roster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_roster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | **str**| Optional team filter | [optional] 
 **year** | **int**| Optional year filter, defaults to 2023 | [optional] 

### Return type

[**List[RosterPlayer]**](RosterPlayer.md)

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

# **get_talent**
> List[TeamTalent] get_talent(year)



Retrieve 247 Team Talent Composite for a given year

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_talent import TeamTalent
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
    api_instance = cfbd.TeamsApi(api_client)
    year = 56 # int | Year filter

    try:
        api_response = api_instance.get_talent(year)
        print("The response of TeamsApi->get_talent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_talent: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | 

### Return type

[**List[TeamTalent]**](TeamTalent.md)

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

# **get_teams**
> List[Team] get_teams(conference=conference, year=year)



Retrieves team information

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team import Team
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
    api_instance = cfbd.TeamsApi(api_client)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    year = 56 # int | Optional year filter to get historical conference affiliations (optional)

    try:
        api_response = api_instance.get_teams(conference=conference, year=year)
        print("The response of TeamsApi->get_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_teams: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **year** | **int**| Optional year filter to get historical conference affiliations | [optional] 

### Return type

[**List[Team]**](Team.md)

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

