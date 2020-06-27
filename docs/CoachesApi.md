# cfbd.CoachesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coaches**](CoachesApi.md#get_coaches) | **GET** /coaches | Get coach records and school history


# **get_coaches**
> InlineResponse200 get_coaches(first_name=first_name, last_name=last_name, team=team, year=year, min_year=min_year, max_year=max_year)

Get coach records and school history

Coaching history

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.CoachesApi()
first_name = 'first_name_example' # str | First name filter (optional)
last_name = 'last_name_example' # str | Last name filter (optional)
team = 'team_example' # str | Team name filter (optional)
year = 56 # int | Year filter (optional)
min_year = 56 # int | Minimum year filter (inclusive) (optional)
max_year = 56 # int | Maximum year filter (inclusive) (optional)

try:
    # Get coach records and school history
    api_response = api_instance.get_coaches(first_name=first_name, last_name=last_name, team=team, year=year, min_year=min_year, max_year=max_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoachesApi->get_coaches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| First name filter | [optional] 
 **last_name** | **str**| Last name filter | [optional] 
 **team** | **str**| Team name filter | [optional] 
 **year** | **int**| Year filter | [optional] 
 **min_year** | **int**| Minimum year filter (inclusive) | [optional] 
 **max_year** | **int**| Maximum year filter (inclusive) | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

