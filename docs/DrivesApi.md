# cfbd.DrivesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drives**](DrivesApi.md#get_drives) | **GET** /drives | Drive data and results


# **get_drives**
> list[Drive] get_drives(year, season_type=season_type, week=week, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference, classification=classification)

Drive data and results

Get game drives

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
api_instance = cfbd.DrivesApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter
season_type = 'regular' # str | Season type filter (optional) (default to regular)
week = 56 # int | Week filter (optional)
team = 'team_example' # str | Team filter (optional)
offense = 'offense_example' # str | Offensive team filter (optional)
defense = 'defense_example' # str | Defensive team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)
offense_conference = 'offense_conference_example' # str | Offensive conference filter (optional)
defense_conference = 'defense_conference_example' # str | Defensive conference filter (optional)
classification = 'classification_example' # str | Division classification filter (fbs/fcs/ii/iii) (optional)

try:
    # Drive data and results
    api_response = api_instance.get_drives(year, season_type=season_type, week=week, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference, classification=classification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DrivesApi->get_drives: %s\n" % e)
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
 **classification** | **str**| Division classification filter (fbs/fcs/ii/iii) | [optional] 

### Return type

[**list[Drive]**](Drive.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

