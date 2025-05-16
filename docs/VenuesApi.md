# cfbd.VenuesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_venues**](VenuesApi.md#get_venues) | **GET** /venues | 


# **get_venues**
> List[Venue] get_venues()



Retrieve list of venues

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.venue import Venue
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
    api_instance = cfbd.VenuesApi(api_client)

    try:
        api_response = api_instance.get_venues()
        print("The response of VenuesApi->get_venues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VenuesApi->get_venues: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Venue]**](Venue.md)

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

