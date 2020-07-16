# cfbd.DrivesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drvies**](DrivesApi.md#get_drvies) | **GET** /drives | Drive data and results


# **get_drvies**
> list[Drive] get_drvies(year, season_type=season_type, week=week, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference)

Drive data and results

Get game drives

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.DrivesApi()
year = 56 # int | Year filter
season_type = 'regular' # str | Season type filter (optional) (default to regular)
week = 56 # int | Week filter (optional)
team = 'team_example' # str | Team filter (optional)
offense = 'offense_example' # str | Offensive team filter (optional)
defense = 'defense_example' # str | Defensive team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)
offense_conference = 'offense_conference_example' # str | Offensive conference filter (optional)
defense_conference = 'defense_conference_example' # str | Defensive conference filter (optional)

try:
    # Drive data and results
    api_response = api_instance.get_drvies(year, season_type=season_type, week=week, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DrivesApi->get_drvies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | 
 **season_type** | **str**| Season type filter | [optional] [default to regular]
 **week** | **int**| Week filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **offense** | **str**| Offensive team filter | [optional] 
 **defense** | **str**| Defensive team filter | [optional] 
 **conference** | **str**| Conference filter | [optional] 
 **offense_conference** | **str**| Offensive conference filter | [optional] 
 **defense_conference** | **str**| Defensive conference filter | [optional] 

### Return type

[**list[Drive]**](Drive.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

