# cfbd.BettingApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lines**](BettingApi.md#get_lines) | **GET** /lines | 


# **get_lines**
> List[BettingGame] get_lines(game_id=game_id, year=year, season_type=season_type, week=week, team=team, home=home, away=away, conference=conference, provider=provider)



Retrieves historical betting data

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.betting_game import BettingGame
from cfbd.models.season_type import SeasonType
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
    api_instance = cfbd.BettingApi(api_client)
    game_id = 56 # int | Optional gameId filter (optional)
    year = 56 # int | Year filter, required if game id not specified (optional)
    season_type = cfbd.SeasonType() # SeasonType | Optional season type filter (optional)
    week = 56 # int | Optional week filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    home = 'home_example' # str | Optional home team filter (optional)
    away = 'away_example' # str | Optional away team filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)
    provider = 'provider_example' # str | Optional provider name filter (optional)

    try:
        api_response = api_instance.get_lines(game_id=game_id, year=year, season_type=season_type, week=week, team=team, home=home, away=away, conference=conference, provider=provider)
        print("The response of BettingApi->get_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BettingApi->get_lines: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| Optional gameId filter | [optional] 
 **year** | **int**| Year filter, required if game id not specified | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **week** | **int**| Optional week filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **home** | **str**| Optional home team filter | [optional] 
 **away** | **str**| Optional away team filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 
 **provider** | **str**| Optional provider name filter | [optional] 

### Return type

[**List[BettingGame]**](BettingGame.md)

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

