# cfbd.RecruitingApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recruiting_groups**](RecruitingApi.md#get_recruiting_groups) | **GET** /recruiting/groups | Recruit position group ratings
[**get_recruiting_players**](RecruitingApi.md#get_recruiting_players) | **GET** /recruiting/players | Player recruiting ratings and rankings
[**get_recruiting_teams**](RecruitingApi.md#get_recruiting_teams) | **GET** /recruiting/teams | Team recruiting rankings and ratings


# **get_recruiting_groups**
> list[PositionGroupRecruitingRating] get_recruiting_groups(start_year=start_year, end_year=end_year, team=team, conference=conference)

Recruit position group ratings

Gets a list of aggregated statistics by team and position grouping

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RecruitingApi(cfbd.ApiClient(configuration))
start_year = 56 # int | Starting year (optional)
end_year = 56 # int | Ending year (optional)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | conference filter (optional)

try:
    # Recruit position group ratings
    api_response = api_instance.get_recruiting_groups(start_year=start_year, end_year=end_year, team=team, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecruitingApi->get_recruiting_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_year** | **int**| Starting year | [optional] 
 **end_year** | **int**| Ending year | [optional] 
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| conference filter | [optional] 

### Return type

[**list[PositionGroupRecruitingRating]**](PositionGroupRecruitingRating.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recruiting_players**
> list[Recruit] get_recruiting_players(year=year, classification=classification, position=position, state=state, team=team)

Player recruiting ratings and rankings

Get player recruiting rankings and data. Requires either a year or team to be specified.

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RecruitingApi(cfbd.ApiClient(configuration))
year = 56 # int | Recruiting class year (required if team no specified) (optional)
classification = 'HighSchool' # str | Type of recruit (HighSchool, JUCO, PrepSchool) (optional) (default to HighSchool)
position = 'position_example' # str | Position abbreviation filter (optional)
state = 'state_example' # str | State or province abbreviation filter (optional)
team = 'team_example' # str | Committed team filter (required if year not specified) (optional)

try:
    # Player recruiting ratings and rankings
    api_response = api_instance.get_recruiting_players(year=year, classification=classification, position=position, state=state, team=team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecruitingApi->get_recruiting_players: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Recruiting class year (required if team no specified) | [optional] 
 **classification** | **str**| Type of recruit (HighSchool, JUCO, PrepSchool) | [optional] [default to HighSchool]
 **position** | **str**| Position abbreviation filter | [optional] 
 **state** | **str**| State or province abbreviation filter | [optional] 
 **team** | **str**| Committed team filter (required if year not specified) | [optional] 

### Return type

[**list[Recruit]**](Recruit.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recruiting_teams**
> list[TeamRecruitingRank] get_recruiting_teams(year=year, team=team)

Team recruiting rankings and ratings

Team recruiting rankings

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RecruitingApi(cfbd.ApiClient(configuration))
year = 56 # int | Recruiting class year (optional)
team = 'team_example' # str | Team filter (optional)

try:
    # Team recruiting rankings and ratings
    api_response = api_instance.get_recruiting_teams(year=year, team=team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecruitingApi->get_recruiting_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Recruiting class year | [optional] 
 **team** | **str**| Team filter | [optional] 

### Return type

[**list[TeamRecruitingRank]**](TeamRecruitingRank.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

