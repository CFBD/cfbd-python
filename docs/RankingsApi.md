# cfbd.RankingsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rankings**](RankingsApi.md#get_rankings) | **GET** /rankings | 


# **get_rankings**
> List[PollWeek] get_rankings(year, season_type=season_type, week=week)



Retrieves historical poll data

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.poll_week import PollWeek
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
    api_instance = cfbd.RankingsApi(api_client)
    year = 56 # int | Required year filter
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    week = 3.4 # float | Optional week filter (optional)

    try:
        api_response = api_instance.get_rankings(year, season_type=season_type, week=week)
        print("The response of RankingsApi->get_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankingsApi->get_rankings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Required year filter | 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **week** | **float**| Optional week filter | [optional] 

### Return type

[**List[PollWeek]**](PollWeek.md)

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

