# cfbd.RatingsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conference_sp_ratings**](RatingsApi.md#get_conference_sp_ratings) | **GET** /ratings/sp/conferences | Historical SP+ ratings by conference
[**get_elo_ratings**](RatingsApi.md#get_elo_ratings) | **GET** /ratings/elo | Historical Elo ratings
[**get_fpi_ratings**](RatingsApi.md#get_fpi_ratings) | **GET** /ratings/fpi | Historical FPI ratings
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

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RatingsApi(cfbd.ApiClient(configuration))
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elo_ratings**
> list[TeamEloRating] get_elo_ratings(year=year, week=week, season_type=season_type, team=team, conference=conference)

Historical Elo ratings

Elo rating data

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RatingsApi(cfbd.ApiClient(configuration))
year = 56 # int | Season filter (optional)
week = 56 # int | Maximum week filter (optional)
season_type = 'season_type_example' # str | Maximum season type to consider (defaults to regular if week is specified else defaults to postseason) (optional)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)

try:
    # Historical Elo ratings
    api_response = api_instance.get_elo_ratings(year=year, week=week, season_type=season_type, team=team, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_elo_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season filter | [optional] 
 **week** | **int**| Maximum week filter | [optional] 
 **season_type** | **str**| Maximum season type to consider (defaults to regular if week is specified else defaults to postseason) | [optional] 
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference filter | [optional] 

### Return type

[**list[TeamEloRating]**](TeamEloRating.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fpi_ratings**
> list[TeamFPIRating] get_fpi_ratings(year=year, team=team, conference=conference)

Historical FPI ratings

FPI rating data

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RatingsApi(cfbd.ApiClient(configuration))
year = 56 # int | Season filter (optional)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)

try:
    # Historical FPI ratings
    api_response = api_instance.get_fpi_ratings(year=year, team=team, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_fpi_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference filter | [optional] 

### Return type

[**list[TeamFPIRating]**](TeamFPIRating.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RatingsApi(cfbd.ApiClient(configuration))
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RatingsApi(cfbd.ApiClient(configuration))
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

