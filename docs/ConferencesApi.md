# cfbd.ConferencesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conferences**](ConferencesApi.md#get_conferences) | **GET** /conferences | 


# **get_conferences**
> List[Conference] get_conferences()



Retrieves list of conferences

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.conference import Conference
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
    api_instance = cfbd.ConferencesApi(api_client)

    try:
        api_response = api_instance.get_conferences()
        print("The response of ConferencesApi->get_conferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->get_conferences: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Conference]**](Conference.md)

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

