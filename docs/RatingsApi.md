# cfbd.RatingsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conference_sp_ratings**](RatingsApi.md#get_conference_sp_ratings) | **GET** /ratings/sp/conferences | Historical SP+ ratings by conference
[**get_sp_ratings**](RatingsApi.md#get_sp_ratings) | **GET** /ratings/sp | Historical SP+ ratings
[**get_srs_ratings**](RatingsApi.md#get_srs_ratings) | **GET** /ratings/srs | Historical SRS ratings


# **get_conference_sp_ratings**
> list[ConferenceSPRating] get_conference_sp_ratings(year=year, conference=conference)

Historical SP+ ratings by conference

Get average SP+ historical rating data by conference

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.RatingsApi()
year = 56 # int | Season filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)

try:
    # Historical SP+ ratings by conference
    api_response = api_instance.get_conference_sp_ratings(year=year, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_conference_sp_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season filter | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 

### Return type

[**list[ConferenceSPRating]**](ConferenceSPRating.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_ratings**
> list[TeamSPRating] get_sp_ratings(year=year, team=team)

Historical SP+ ratings

SP+ rating data

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.RatingsApi()
year = 56 # int | Season filter (required if team not specified) (optional)
team = 'team_example' # str | Team filter (required if year not specified) (optional)

try:
    # Historical SP+ ratings
    api_response = api_instance.get_sp_ratings(year=year, team=team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_sp_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season filter (required if team not specified) | [optional] 
 **team** | **str**| Team filter (required if year not specified) | [optional] 

### Return type

[**list[TeamSPRating]**](TeamSPRating.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_srs_ratings**
> list[TeamSRSRating] get_srs_ratings(year=year, team=team, conference=conference)

Historical SRS ratings

SRS rating data (requires either a year or team specified)

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.RatingsApi()
year = 56 # int | Season filter (required if team not specified) (optional)
team = 'team_example' # str | Team filter (required if year not specified) (optional)
conference = 'conference_example' # str | Conference filter (optional)

try:
    # Historical SRS ratings
    api_response = api_instance.get_srs_ratings(year=year, team=team, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_srs_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season filter (required if team not specified) | [optional] 
 **team** | **str**| Team filter (required if year not specified) | [optional] 
 **conference** | **str**| Conference filter | [optional] 

### Return type

[**list[TeamSRSRating]**](TeamSRSRating.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

