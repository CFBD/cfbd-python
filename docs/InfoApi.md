# cfbd.InfoApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage**](InfoApi.md#get_usage) | **GET** /info/usage | 
[**get_user_info**](InfoApi.md#get_user_info) | **GET** /info | 


# **get_usage**
> UserUsage get_usage(days=days, limit=limit, api=api)



Retrieves bounded API usage for the authenticated user's shared CFB/CBB call pool.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.user_usage import UserUsage
from cfbd.models.user_usage_api import UserUsageApi
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
    api_instance = cfbd.InfoApi(api_client)
    days = 56 # int | Number of trailing days to include, defaults to 7 and is capped at 31 (optional)
    limit = 56 # int | Number of endpoint and recent request rows to return, defaults to 10 and is capped at 50 (optional)
    api = cfbd.UserUsageApi() # UserUsageApi | Optional API filter: all, cfb, or cbb (optional)

    try:
        api_response = api_instance.get_usage(days=days, limit=limit, api=api)
        print("The response of InfoApi->get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->get_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of trailing days to include, defaults to 7 and is capped at 31 | [optional] 
 **limit** | **int**| Number of endpoint and recent request rows to return, defaults to 10 and is capped at 50 | [optional] 
 **api** | [**UserUsageApi**](.md)| Optional API filter: all, cfb, or cbb | [optional] 

### Return type

[**UserUsage**](UserUsage.md)

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

# **get_user_info**
> UserInfo get_user_info()



Retrieves information about the user, including their Patreon level and remaining API calls.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.user_info import UserInfo
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
    api_instance = cfbd.InfoApi(api_client)

    try:
        api_response = api_instance.get_user_info()
        print("The response of InfoApi->get_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->get_user_info: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserInfo object containing patron level and remaining calls, or null if not authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

