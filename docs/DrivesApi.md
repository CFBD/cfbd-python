# cfbd.DrivesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drives**](DrivesApi.md#get_drives) | **GET** /drives | 


# **get_drives**
> List[Drive] get_drives(year, season_type=season_type, week=week, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference, classification=classification)



Retrieves historical drive data

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
    year = 56 # int | Required year filter
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    week = 56 # int | Optional week filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    offense = 'offense_example' # str | Optional offensive team filter (optional)
    defense = 'defense_example' # str | Optional defensive team filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)
    offense_conference = 'offense_conference_example' # str | Optional offensive team conference filter (optional)
    defense_conference = 'defense_conference_example' # str | Optional defensive team conference filter (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Optional division classification filter (optional)

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
 **year** | **int**| Required year filter | 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **week** | **int**| Optional week filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **offense** | **str**| Optional offensive team filter | [optional] 
 **defense** | **str**| Optional defensive team filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 
 **offense_conference** | **str**| Optional offensive team conference filter | [optional] 
 **defense_conference** | **str**| Optional defensive team conference filter | [optional] 
 **classification** | [**DivisionClassification**](.md)| Optional division classification filter | [optional] 

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

