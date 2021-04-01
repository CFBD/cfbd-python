# cfbd.BettingApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lines**](BettingApi.md#get_lines) | **GET** /lines | Betting lines


# **get_lines**
> list[GameLines] get_lines(game_id=game_id, year=year, week=week, season_type=season_type, team=team, home=home, away=away, conference=conference)

Betting lines

Closing betting lines

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
api_instance = cfbd.BettingApi(cfbd.ApiClient(configuration))
game_id = 56 # int | Game id filter (optional)
year = 56 # int | Year/season filter for games (optional)
week = 56 # int | Week filter (optional)
season_type = 'regular' # str | Season type filter (regular or postseason) (optional) (default to regular)
team = 'team_example' # str | Team (optional)
home = 'home_example' # str | Home team filter (optional)
away = 'away_example' # str | Away team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)

try:
    # Betting lines
    api_response = api_instance.get_lines(game_id=game_id, year=year, week=week, season_type=season_type, team=team, home=home, away=away, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BettingApi->get_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| Game id filter | [optional] 
 **year** | **int**| Year/season filter for games | [optional] 
 **week** | **int**| Week filter | [optional] 
 **season_type** | **str**| Season type filter (regular or postseason) | [optional] [default to regular]
 **team** | **str**| Team | [optional] 
 **home** | **str**| Home team filter | [optional] 
 **away** | **str**| Away team filter | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 

### Return type

[**list[GameLines]**](GameLines.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

