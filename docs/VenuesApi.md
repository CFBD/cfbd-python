# cfbd.VenuesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_venues**](VenuesApi.md#get_venues) | **GET** /venues | Arena and venue information


# **get_venues**
> list[Venue] get_venues()

Arena and venue information

Venues

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.VenuesApi()

try:
    # Arena and venue information
    api_response = api_instance.get_venues()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VenuesApi->get_venues: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Venue]**](Venue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

