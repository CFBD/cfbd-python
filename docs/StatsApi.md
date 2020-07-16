# cfbd.StatsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advanced_team_game_stats**](StatsApi.md#get_advanced_team_game_stats) | **GET** /stats/game/advanced | Advanced team metrics by game
[**get_advanced_team_season_stats**](StatsApi.md#get_advanced_team_season_stats) | **GET** /stats/season/advanced | Advanced team metrics by season
[**get_stat_categories**](StatsApi.md#get_stat_categories) | **GET** /stats/categories | Team stat categories
[**get_team_season_stats**](StatsApi.md#get_team_season_stats) | **GET** /stats/season | Team statistics by season


# **get_advanced_team_game_stats**
> list[AdvancedGameStat] get_advanced_team_game_stats(year=year, week=week, team=team, opponent=opponent, exclude_garbage_time=exclude_garbage_time, season_type=season_type)

Advanced team metrics by game

Advanced team game stats

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.StatsApi()
year = 56 # int | Year filter (required if no team specified) (optional)
week = 56 # int | Week filter (optional)
team = 'team_example' # str | Team filter (required if no year specified) (optional)
opponent = 'opponent_example' # str | Opponent filter (optional)
exclude_garbage_time = true # bool | Filter to remove garbage time plays from calculations (optional)
season_type = 'season_type_example' # str | Season type filter (regular, postseason, or both) (optional)

try:
    # Advanced team metrics by game
    api_response = api_instance.get_advanced_team_game_stats(year=year, week=week, team=team, opponent=opponent, exclude_garbage_time=exclude_garbage_time, season_type=season_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_advanced_team_game_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter (required if no team specified) | [optional] 
 **week** | **int**| Week filter | [optional] 
 **team** | **str**| Team filter (required if no year specified) | [optional] 
 **opponent** | **str**| Opponent filter | [optional] 
 **exclude_garbage_time** | **bool**| Filter to remove garbage time plays from calculations | [optional] 
 **season_type** | **str**| Season type filter (regular, postseason, or both) | [optional] 

### Return type

[**list[AdvancedGameStat]**](AdvancedGameStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advanced_team_season_stats**
> list[AdvancedSeasonStat] get_advanced_team_season_stats(year=year, team=team, exclude_garbage_time=exclude_garbage_time, start_week=start_week, end_week=end_week)

Advanced team metrics by season

Advanced team season stats

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.StatsApi()
year = 56 # int | Year filter (required if no team specified) (optional)
team = 'team_example' # str | Team filter (required if no year specified) (optional)
exclude_garbage_time = true # bool | Filter to remove garbage time plays from calculations (optional)
start_week = 56 # int | Starting week filter (optional)
end_week = 56 # int | Starting week filter (optional)

try:
    # Advanced team metrics by season
    api_response = api_instance.get_advanced_team_season_stats(year=year, team=team, exclude_garbage_time=exclude_garbage_time, start_week=start_week, end_week=end_week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_advanced_team_season_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter (required if no team specified) | [optional] 
 **team** | **str**| Team filter (required if no year specified) | [optional] 
 **exclude_garbage_time** | **bool**| Filter to remove garbage time plays from calculations | [optional] 
 **start_week** | **int**| Starting week filter | [optional] 
 **end_week** | **int**| Starting week filter | [optional] 

### Return type

[**list[AdvancedSeasonStat]**](AdvancedSeasonStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stat_categories**
> list[str] get_stat_categories()

Team stat categories

Stat category list

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.StatsApi()

try:
    # Team stat categories
    api_response = api_instance.get_stat_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_stat_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_season_stats**
> list[TeamSeasonStat] get_team_season_stats(year=year, team=team, conference=conference, start_week=start_week, end_week=end_week)

Team statistics by season

Team season stats

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.StatsApi()
year = 56 # int | Year filter (required if no team specified) (optional)
team = 'team_example' # str | Team filter (required if no year specified) (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)
start_week = 56 # int | Starting week filter (optional)
end_week = 56 # int | Starting week filter (optional)

try:
    # Team statistics by season
    api_response = api_instance.get_team_season_stats(year=year, team=team, conference=conference, start_week=start_week, end_week=end_week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_team_season_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter (required if no team specified) | [optional] 
 **team** | **str**| Team filter (required if no year specified) | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 
 **start_week** | **int**| Starting week filter | [optional] 
 **end_week** | **int**| Starting week filter | [optional] 

### Return type

[**list[TeamSeasonStat]**](TeamSeasonStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

