# cfbd.PlayersApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_season_stats**](PlayersApi.md#get_player_season_stats) | **GET** /stats/player/season | Player stats by season
[**get_player_usage**](PlayersApi.md#get_player_usage) | **GET** /player/usage | Player usage metrics broken down by season
[**get_returning_production**](PlayersApi.md#get_returning_production) | **GET** /player/returning | Team returning production metrics
[**get_transfer_portal**](PlayersApi.md#get_transfer_portal) | **GET** /player/portal | Transfer portal by season
[**player_search**](PlayersApi.md#player_search) | **GET** /player/search | Search for player information


# **get_player_season_stats**
> list[PlayerSeasonStat] get_player_season_stats(year, team=team, conference=conference, start_week=start_week, end_week=end_week, season_type=season_type, category=category)

Player stats by season

Season player stats

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
api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)
start_week = 56 # int | Start week filter (optional)
end_week = 56 # int | Start week filter (optional)
season_type = 'season_type_example' # str | Season type filter (regular, postseason, or both) (optional)
category = 'category_example' # str | Stat category filter (e.g. passing) (optional)

try:
    # Player stats by season
    api_response = api_instance.get_player_season_stats(year, team=team, conference=conference, start_week=start_week, end_week=end_week, season_type=season_type, category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_season_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | 
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 
 **start_week** | **int**| Start week filter | [optional] 
 **end_week** | **int**| Start week filter | [optional] 
 **season_type** | **str**| Season type filter (regular, postseason, or both) | [optional] 
 **category** | **str**| Stat category filter (e.g. passing) | [optional] 

### Return type

[**list[PlayerSeasonStat]**](PlayerSeasonStat.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_usage**
> list[PlayerUsage] get_player_usage(year, team=team, conference=conference, position=position, player_id=player_id, exclude_garbage_time=exclude_garbage_time)

Player usage metrics broken down by season

Player usage metrics by season

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
api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
year = 2022 # int | Year filter (default to 2022)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)
position = 'position_example' # str | Position abbreviation filter (optional)
player_id = 56 # int | Player id filter (optional)
exclude_garbage_time = true # bool | Filter to remove garbage time plays from calculations (optional)

try:
    # Player usage metrics broken down by season
    api_response = api_instance.get_player_usage(year, team=team, conference=conference, position=position, player_id=player_id, exclude_garbage_time=exclude_garbage_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [default to 2022]
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 
 **position** | **str**| Position abbreviation filter | [optional] 
 **player_id** | **int**| Player id filter | [optional] 
 **exclude_garbage_time** | **bool**| Filter to remove garbage time plays from calculations | [optional] 

### Return type

[**list[PlayerUsage]**](PlayerUsage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_returning_production**
> list[ReturningProduction] get_returning_production(year=year, team=team, conference=conference)

Team returning production metrics

Returning production metrics

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
api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter (optional)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)

try:
    # Team returning production metrics
    api_response = api_instance.get_returning_production(year=year, team=team, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_returning_production: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 

### Return type

[**list[ReturningProduction]**](ReturningProduction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_portal**
> list[PortalPlayer] get_transfer_portal(year)

Transfer portal by season

Transfer portal by season

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
api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter

try:
    # Transfer portal by season
    api_response = api_instance.get_transfer_portal(year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_transfer_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | 

### Return type

[**list[PortalPlayer]**](PortalPlayer.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_search**
> list[PlayerSearchResult] player_search(search_term, position=position, team=team, year=year)

Search for player information

Search for players

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
api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
search_term = 'search_term_example' # str | Term to search on
position = 'position_example' # str | Position abbreviation filter (optional)
team = 'team_example' # str | Team filter (optional)
year = 56 # int | Year filter (optional)

try:
    # Search for player information
    api_response = api_instance.player_search(search_term, position=position, team=team, year=year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->player_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Term to search on | 
 **position** | **str**| Position abbreviation filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **year** | **int**| Year filter | [optional] 

### Return type

[**list[PlayerSearchResult]**](PlayerSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

