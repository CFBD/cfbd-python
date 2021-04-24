# cfbd.DraftApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_draft_picks**](DraftApi.md#get_draft_picks) | **GET** /draft/picks | List of NFL Draft picks
[**get_nfl_positions**](DraftApi.md#get_nfl_positions) | **GET** /draft/positions | List of NFL positions
[**get_nfl_teams**](DraftApi.md#get_nfl_teams) | **GET** /draft/teams | List of NFL teams


# **get_draft_picks**
> list[DraftPick] get_draft_picks(year=year, nfl_team=nfl_team, college=college, conference=conference, position=position)

List of NFL Draft picks

List of NFL Draft picks

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
api_instance = cfbd.DraftApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter (optional)
nfl_team = 'nfl_team_example' # str | NFL team filter (optional)
college = 'college_example' # str | Player college filter (optional)
conference = 'conference_example' # str | College confrence abbreviation filter (optional)
position = 'position_example' # str | NFL position filter (optional)

try:
    # List of NFL Draft picks
    api_response = api_instance.get_draft_picks(year=year, nfl_team=nfl_team, college=college, conference=conference, position=position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->get_draft_picks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [optional] 
 **nfl_team** | **str**| NFL team filter | [optional] 
 **college** | **str**| Player college filter | [optional] 
 **conference** | **str**| College confrence abbreviation filter | [optional] 
 **position** | **str**| NFL position filter | [optional] 

### Return type

[**list[DraftPick]**](DraftPick.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfl_positions**
> list[DraftPosition] get_nfl_positions()

List of NFL positions

List of NFL positions

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
api_instance = cfbd.DraftApi(cfbd.ApiClient(configuration))

try:
    # List of NFL positions
    api_response = api_instance.get_nfl_positions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->get_nfl_positions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DraftPosition]**](DraftPosition.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfl_teams**
> list[DraftTeam] get_nfl_teams()

List of NFL teams

List of NFL teams

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
api_instance = cfbd.DraftApi(cfbd.ApiClient(configuration))

try:
    # List of NFL teams
    api_response = api_instance.get_nfl_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftApi->get_nfl_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DraftTeam]**](DraftTeam.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

