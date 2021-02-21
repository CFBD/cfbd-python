# cfbd.ConferencesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conferences**](ConferencesApi.md#get_conferences) | **GET** /conferences | Conferences


# **get_conferences**
> list[Conference] get_conferences()

Conferences

Get conference list

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
api_instance = cfbd.ConferencesApi(cfbd.ApiClient(configuration))

try:
    # Conferences
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

