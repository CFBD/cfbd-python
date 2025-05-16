# cfbd.RatingsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conference_sp**](RatingsApi.md#get_conference_sp) | **GET** /ratings/sp/conferences | 
[**get_elo**](RatingsApi.md#get_elo) | **GET** /ratings/elo | 
[**get_fpi**](RatingsApi.md#get_fpi) | **GET** /ratings/fpi | 
[**get_sp**](RatingsApi.md#get_sp) | **GET** /ratings/sp | 
[**get_srs**](RatingsApi.md#get_srs) | **GET** /ratings/srs | 


# **get_conference_sp**
> List[ConferenceSP] get_conference_sp(year=year, conference=conference)



Retrieves aggregated historical conference SP+ data

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.conference_sp import ConferenceSP
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
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Optional year filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)

    try:
        api_response = api_instance.get_conference_sp(year=year, conference=conference)
        print("The response of RatingsApi->get_conference_sp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_conference_sp: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Optional year filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 

### Return type

[**List[ConferenceSP]**](ConferenceSP.md)

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

# **get_elo**
> List[TeamElo] get_elo(year=year, week=week, season_type=season_type, team=team, conference=conference)



Retrieves historical Elo ratings

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.season_type import SeasonType
from cfbd.models.team_elo import TeamElo
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
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Optional year filter (optional)
    week = 56 # int | Optional week filter, defaults to last available week in the season (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)

    try:
        api_response = api_instance.get_elo(year=year, week=week, season_type=season_type, team=team, conference=conference)
        print("The response of RatingsApi->get_elo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_elo: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Optional year filter | [optional] 
 **week** | **int**| Optional week filter, defaults to last available week in the season | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 

### Return type

[**List[TeamElo]**](TeamElo.md)

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

# **get_fpi**
> List[TeamFPI] get_fpi(year=year, team=team, conference=conference)



Retrieves historical Football Power Index (FPI) ratings

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_fpi import TeamFPI
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
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | year filter, required if team not specified (optional)
    team = 'team_example' # str | team filter, required if year not specified (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)

    try:
        api_response = api_instance.get_fpi(year=year, team=team, conference=conference)
        print("The response of RatingsApi->get_fpi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_fpi: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| year filter, required if team not specified | [optional] 
 **team** | **str**| team filter, required if year not specified | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 

### Return type

[**List[TeamFPI]**](TeamFPI.md)

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

# **get_sp**
> List[TeamSP] get_sp(year=year, team=team)



Retrieves SP+ ratings for a given year or school

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_sp import TeamSP
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
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Year filter, required if team not specified (optional)
    team = 'team_example' # str | Team filter, required if year not specified (optional)

    try:
        api_response = api_instance.get_sp(year=year, team=team)
        print("The response of RatingsApi->get_sp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_sp: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter, required if team not specified | [optional] 
 **team** | **str**| Team filter, required if year not specified | [optional] 

### Return type

[**List[TeamSP]**](TeamSP.md)

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

# **get_srs**
> List[TeamSRS] get_srs(year=year, team=team, conference=conference)



Retrieves historical SRS for a year or team

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_srs import TeamSRS
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
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Year filter, required if team not specified (optional)
    team = 'team_example' # str | Team filter, required if year not specified (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)

    try:
        api_response = api_instance.get_srs(year=year, team=team, conference=conference)
        print("The response of RatingsApi->get_srs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_srs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter, required if team not specified | [optional] 
 **team** | **str**| Team filter, required if year not specified | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 

### Return type

[**List[TeamSRS]**](TeamSRS.md)

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

