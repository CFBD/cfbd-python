# cfbd.CoachesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coach_profile**](CoachesApi.md#get_coach_profile) | **GET** /coaches/profile | 
[**get_coach_seasons**](CoachesApi.md#get_coach_seasons) | **GET** /coaches/seasons | 
[**get_coach_tenures**](CoachesApi.md#get_coach_tenures) | **GET** /coaches/tenures | 
[**get_coaches**](CoachesApi.md#get_coaches) | **GET** /coaches | 


# **get_coach_profile**
> CoachProfile get_coach_profile(coach_id)



Retrieves canonical coach identity and complete career totals

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.coach_profile import CoachProfile
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
    api_instance = cfbd.CoachesApi(api_client)
    coach_id = 56 # int | Required coach ID

    try:
        api_response = api_instance.get_coach_profile(coach_id)
        print("The response of CoachesApi->get_coach_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoachesApi->get_coach_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coach_id** | **int**| Required coach ID | 

### Return type

[**CoachProfile**](CoachProfile.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Validation error |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coach_seasons**
> List[DetailedCoachSeason] get_coach_seasons(coach_id=coach_id, team=team, year=year, min_year=min_year, max_year=max_year)



Retrieves detailed coach-season records with attributed results and
whole-team season context

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.detailed_coach_season import DetailedCoachSeason
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
    api_instance = cfbd.CoachesApi(api_client)
    coach_id = 56 # int | Optional coach ID (optional)
    team = 'team_example' # str | Optional team filter (optional)
    year = 56 # int | Optional exact season year (optional)
    min_year = 56 # int | Optional start year range filter (optional)
    max_year = 56 # int | Optional end year range filter (optional)

    try:
        api_response = api_instance.get_coach_seasons(coach_id=coach_id, team=team, year=year, min_year=min_year, max_year=max_year)
        print("The response of CoachesApi->get_coach_seasons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoachesApi->get_coach_seasons: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coach_id** | **int**| Optional coach ID | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **year** | **int**| Optional exact season year | [optional] 
 **min_year** | **int**| Optional start year range filter | [optional] 
 **max_year** | **int**| Optional end year range filter | [optional] 

### Return type

[**List[DetailedCoachSeason]**](DetailedCoachSeason.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coach_tenures**
> List[CoachTenure] get_coach_tenures(coach_id=coach_id, team=team, year=year, active=active)



Retrieves continuous head-coaching stints and attributed records

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.coach_tenure import CoachTenure
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
    api_instance = cfbd.CoachesApi(api_client)
    coach_id = 56 # int | Optional coach ID (optional)
    team = 'team_example' # str | Optional team filter (optional)
    year = 56 # int | Optional season year contained by the tenure (optional)
    active = True # bool | Optional active-tenure filter (optional)

    try:
        api_response = api_instance.get_coach_tenures(coach_id=coach_id, team=team, year=year, active=active)
        print("The response of CoachesApi->get_coach_tenures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoachesApi->get_coach_tenures: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coach_id** | **int**| Optional coach ID | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **year** | **int**| Optional season year contained by the tenure | [optional] 
 **active** | **bool**| Optional active-tenure filter | [optional] 

### Return type

[**List[CoachTenure]**](CoachTenure.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coaches**
> List[Coach] get_coaches(first_name=first_name, last_name=last_name, team=team, year=year, min_year=min_year, max_year=max_year)



Retrieves historical head coach information and records

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.coach import Coach
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
    api_instance = cfbd.CoachesApi(api_client)
    first_name = 'first_name_example' # str | Optional first name filter (optional)
    last_name = 'last_name_example' # str | Optional last name filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    year = 56 # int | Optional year filter (optional)
    min_year = 56 # int | Optional start year range filter (optional)
    max_year = 56 # int | Optional end year range filter (optional)

    try:
        api_response = api_instance.get_coaches(first_name=first_name, last_name=last_name, team=team, year=year, min_year=min_year, max_year=max_year)
        print("The response of CoachesApi->get_coaches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoachesApi->get_coaches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| Optional first name filter | [optional] 
 **last_name** | **str**| Optional last name filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **year** | **int**| Optional year filter | [optional] 
 **min_year** | **int**| Optional start year range filter | [optional] 
 **max_year** | **int**| Optional end year range filter | [optional] 

### Return type

[**List[Coach]**](Coach.md)

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

