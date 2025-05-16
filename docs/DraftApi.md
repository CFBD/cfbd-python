# cfbd.DraftApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_draft_picks**](DraftApi.md#get_draft_picks) | **GET** /draft/picks | 
[**get_draft_positions**](DraftApi.md#get_draft_positions) | **GET** /draft/positions | 
[**get_draft_teams**](DraftApi.md#get_draft_teams) | **GET** /draft/teams | 


# **get_draft_picks**
> List[DraftPick] get_draft_picks(year=year, team=team, school=school, conference=conference, position=position)



Retrieve historical NFL draft data

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.draft_pick import DraftPick
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
    api_instance = cfbd.DraftApi(api_client)
    year = 56 # int | Optional year filter (optional)
    team = 'team_example' # str | Optional NFL team filter (optional)
    school = 'school_example' # str | Optional college team filter (optional)
    conference = 'conference_example' # str | Optional college conference filter (optional)
    position = 'position_example' # str | Optional position classification filter (optional)

    try:
        api_response = api_instance.get_draft_picks(year=year, team=team, school=school, conference=conference, position=position)
        print("The response of DraftApi->get_draft_picks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft_picks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Optional year filter | [optional] 
 **team** | **str**| Optional NFL team filter | [optional] 
 **school** | **str**| Optional college team filter | [optional] 
 **conference** | **str**| Optional college conference filter | [optional] 
 **position** | **str**| Optional position classification filter | [optional] 

### Return type

[**List[DraftPick]**](DraftPick.md)

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

# **get_draft_positions**
> List[DraftPosition] get_draft_positions()



Retrieves list of player position categories for the NFL Draft

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.draft_position import DraftPosition
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
    api_instance = cfbd.DraftApi(api_client)

    try:
        api_response = api_instance.get_draft_positions()
        print("The response of DraftApi->get_draft_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft_positions: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DraftPosition]**](DraftPosition.md)

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

# **get_draft_teams**
> List[DraftTeam] get_draft_teams()



Retrieves list of NFL teams

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.draft_team import DraftTeam
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
    api_instance = cfbd.DraftApi(api_client)

    try:
        api_response = api_instance.get_draft_teams()
        print("The response of DraftApi->get_draft_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft_teams: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DraftTeam]**](DraftTeam.md)

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

