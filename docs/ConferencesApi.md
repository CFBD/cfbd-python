# cfbd.ConferencesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conferences**](ConferencesApi.md#get_conferences) | **GET** /conferences | Get conference list


# **get_conferences**
> list[Conference] get_conferences()

Get conference list

Conferences

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.ConferencesApi()

try:
    # Get conference list
    api_response = api_instance.get_conferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConferencesApi->get_conferences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Conference]**](Conference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

