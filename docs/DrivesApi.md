# cfbd.DrivesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drives**](DrivesApi.md#get_drives) | **GET** /drives | 


# **get_drives**
> List[Drive] get_drives(year, season_type=season_type, week=week, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference, classification=classification)



Returns historical drive data.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.drive import Drive
from cfbd.models.season_type import SeasonType
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
    api_instance = cfbd.DrivesApi(api_client)
    year = 56 # int | Season year.
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    week = 56 # int | Week number. (optional)
    team = 'team_example' # str | Team name on either side of the drive. (optional)
    offense = 'offense_example' # str | Offensive team name. (optional)
    defense = 'defense_example' # str | Defensive team name. (optional)
    conference = 'conference_example' # str | Conference of either team. (optional)
    offense_conference = 'offense_conference_example' # str | Offensive team conference. (optional)
    defense_conference = 'defense_conference_example' # str | Defensive team conference. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification of either team. (optional)

    try:
        api_response = api_instance.get_drives(year, season_type=season_type, week=week, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference, classification=classification)
        print("The response of DrivesApi->get_drives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrivesApi->get_drives: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **week** | **int**| Week number. | [optional] 
 **team** | **str**| Team name on either side of the drive. | [optional] 
 **offense** | **str**| Offensive team name. | [optional] 
 **defense** | **str**| Defensive team name. | [optional] 
 **conference** | **str**| Conference of either team. | [optional] 
 **offense_conference** | **str**| Offensive team conference. | [optional] 
 **defense_conference** | **str**| Defensive team conference. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification of either team. | [optional] 

### Return type

[**List[Drive]**](Drive.md)

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

