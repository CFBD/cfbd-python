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



Returns a coach profile with canonical identity and career totals.

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
    coach_id = 56 # int | Coach ID.

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
 **coach_id** | **int**| Coach ID. | 

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



Returns coach-season records with attributed results and team context.

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
    coach_id = 56 # int | Coach ID. (optional)
    team = 'team_example' # str | Team name. (optional)
    year = 56 # int | Exact season year. (optional)
    min_year = 56 # int | Earliest season year to include. (optional)
    max_year = 56 # int | Latest season year to include. (optional)

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
 **coach_id** | **int**| Coach ID. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **year** | **int**| Exact season year. | [optional] 
 **min_year** | **int**| Earliest season year to include. | [optional] 
 **max_year** | **int**| Latest season year to include. | [optional] 

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



Returns continuous head-coaching tenures and their attributed records.

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
    coach_id = 56 # int | Coach ID. (optional)
    team = 'team_example' # str | Team name. (optional)
    year = 56 # int | Season year contained within the tenure. (optional)
    active = True # bool | Filters by active status when specified. (optional)

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
 **coach_id** | **int**| Coach ID. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **year** | **int**| Season year contained within the tenure. | [optional] 
 **active** | **bool**| Filters by active status when specified. | [optional] 

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



Returns historical head coach records.

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
    first_name = 'first_name_example' # str | Coach first name. (optional)
    last_name = 'last_name_example' # str | Coach last name. (optional)
    team = 'team_example' # str | Team name. (optional)
    year = 56 # int | Season year. (optional)
    min_year = 56 # int | Earliest season year to include. (optional)
    max_year = 56 # int | Latest season year to include. (optional)

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
 **first_name** | **str**| Coach first name. | [optional] 
 **last_name** | **str**| Coach last name. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **year** | **int**| Season year. | [optional] 
 **min_year** | **int**| Earliest season year to include. | [optional] 
 **max_year** | **int**| Latest season year to include. | [optional] 

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

