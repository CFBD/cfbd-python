# cfbd.RecruitingApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregated_team_recruiting_ratings**](RecruitingApi.md#get_aggregated_team_recruiting_ratings) | **GET** /recruiting/groups | 
[**get_recruits**](RecruitingApi.md#get_recruits) | **GET** /recruiting/players | 
[**get_team_recruiting_rankings**](RecruitingApi.md#get_team_recruiting_rankings) | **GET** /recruiting/teams | 


# **get_aggregated_team_recruiting_ratings**
> List[AggregatedTeamRecruiting] get_aggregated_team_recruiting_ratings(team=team, conference=conference, recruit_type=recruit_type, start_year=start_year, end_year=end_year)



Retrieves aggregated recruiting statistics by team and position grouping

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.aggregated_team_recruiting import AggregatedTeamRecruiting
from cfbd.models.recruit_classification import RecruitClassification
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
    api_instance = cfbd.RecruitingApi(api_client)
    team = 'team_example' # str | Optional team filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)
    recruit_type = cfbd.RecruitClassification() # RecruitClassification | Optional recruit type filter, defaults to HighSchool (optional)
    start_year = 56 # int | Optional start year range, defaults to 2000 (optional)
    end_year = 56 # int | Optional end year range, defaults to current year (optional)

    try:
        api_response = api_instance.get_aggregated_team_recruiting_ratings(team=team, conference=conference, recruit_type=recruit_type, start_year=start_year, end_year=end_year)
        print("The response of RecruitingApi->get_aggregated_team_recruiting_ratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecruitingApi->get_aggregated_team_recruiting_ratings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | **str**| Optional team filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 
 **recruit_type** | [**RecruitClassification**](.md)| Optional recruit type filter, defaults to HighSchool | [optional] 
 **start_year** | **int**| Optional start year range, defaults to 2000 | [optional] 
 **end_year** | **int**| Optional end year range, defaults to current year | [optional] 

### Return type

[**List[AggregatedTeamRecruiting]**](AggregatedTeamRecruiting.md)

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

# **get_recruits**
> List[Recruit] get_recruits(year=year, team=team, position=position, state=state, classification=classification)



Retrieves player recruiting rankings

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.recruit import Recruit
from cfbd.models.recruit_classification import RecruitClassification
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
    api_instance = cfbd.RecruitingApi(api_client)
    year = 56 # int | Year filter, required when no team specified (optional)
    team = 'team_example' # str | Team filter, required when no team specified (optional)
    position = 'position_example' # str | Optional position categorization filter (optional)
    state = 'state_example' # str | Optional state/province filter (optional)
    classification = cfbd.RecruitClassification() # RecruitClassification | Optional recruit type classification filter, defaults to HighSchool (optional)

    try:
        api_response = api_instance.get_recruits(year=year, team=team, position=position, state=state, classification=classification)
        print("The response of RecruitingApi->get_recruits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecruitingApi->get_recruits: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter, required when no team specified | [optional] 
 **team** | **str**| Team filter, required when no team specified | [optional] 
 **position** | **str**| Optional position categorization filter | [optional] 
 **state** | **str**| Optional state/province filter | [optional] 
 **classification** | [**RecruitClassification**](.md)| Optional recruit type classification filter, defaults to HighSchool | [optional] 

### Return type

[**List[Recruit]**](Recruit.md)

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

# **get_team_recruiting_rankings**
> List[TeamRecruitingRanking] get_team_recruiting_rankings(year=year, team=team)



Retrieves team recruiting rankings

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_recruiting_ranking import TeamRecruitingRanking
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
    api_instance = cfbd.RecruitingApi(api_client)
    year = 56 # int | Optional year filter (optional)
    team = 'team_example' # str | Optional team filter (optional)

    try:
        api_response = api_instance.get_team_recruiting_rankings(year=year, team=team)
        print("The response of RecruitingApi->get_team_recruiting_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecruitingApi->get_team_recruiting_rankings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Optional year filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 

### Return type

[**List[TeamRecruitingRanking]**](TeamRecruitingRanking.md)

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

