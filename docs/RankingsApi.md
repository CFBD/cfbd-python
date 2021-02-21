# cfbd.RankingsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rankings**](RankingsApi.md#get_rankings) | **GET** /rankings | Historical polls and rankings


# **get_rankings**
> list[RankingWeek] get_rankings(year, week=week, season_type=season_type)

Historical polls and rankings

Poll rankings

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RankingsApi(cfbd.ApiClient(configuration))
year = 56 # int | Year/season filter for games
week = 56 # int | Week filter (optional)
season_type = 'regular' # str | Season type filter (regular or postseason) (optional) (default to regular)

try:
    # Historical polls and rankings
    api_response = api_instance.get_rankings(year, week=week, season_type=season_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankingsApi->get_rankings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year/season filter for games | 
 **week** | **int**| Week filter | [optional] 
 **season_type** | **str**| Season type filter (regular or postseason) | [optional] [default to regular]

### Return type

[**list[RankingWeek]**](RankingWeek.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

