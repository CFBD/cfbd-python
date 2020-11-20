# cfbd.PlaysApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_play_stat_types**](PlaysApi.md#get_play_stat_types) | **GET** /play/stat/types | Types of player play stats
[**get_play_stats**](PlaysApi.md#get_play_stats) | **GET** /play/stats | Play stats by play
[**get_play_types**](PlaysApi.md#get_play_types) | **GET** /play/types | Play types
[**get_plays**](PlaysApi.md#get_plays) | **GET** /plays | Play by play data


# **get_play_stat_types**
> list[PlayStatType] get_play_stat_types()

Types of player play stats

Type of play stats

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.PlaysApi()

try:
    # Types of player play stats
    api_response = api_instance.get_play_stat_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaysApi->get_play_stat_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PlayStatType]**](PlayStatType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_play_stats**
> list[PlayStat] get_play_stats(year=year, week=week, team=team, game_id=game_id, athlete_id=athlete_id, stat_type_id=stat_type_id, season_type=season_type, conference=conference)

Play stats by play

Gets player stats associated by play (limit 1000)

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.PlaysApi()
year = 56 # int | Year filter (optional)
week = 56 # int | Week filter (optional)
team = 'team_example' # str | Team filter (optional)
game_id = 56 # int | gameId filter (from /games endpoint) (optional)
athlete_id = 56 # int | athleteId filter (from /roster endpoint) (optional)
stat_type_id = 56 # int | statTypeId filter (from /play/stat/types endpoint) (optional)
season_type = 'season_type_example' # str | regular, postseason, or both (optional)
conference = 'conference_example' # str | conference abbreviation filter (optional)

try:
    # Play stats by play
    api_response = api_instance.get_play_stats(year=year, week=week, team=team, game_id=game_id, athlete_id=athlete_id, stat_type_id=stat_type_id, season_type=season_type, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaysApi->get_play_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [optional] 
 **week** | **int**| Week filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **game_id** | **int**| gameId filter (from /games endpoint) | [optional] 
 **athlete_id** | **int**| athleteId filter (from /roster endpoint) | [optional] 
 **stat_type_id** | **int**| statTypeId filter (from /play/stat/types endpoint) | [optional] 
 **season_type** | **str**| regular, postseason, or both | [optional] 
 **conference** | **str**| conference abbreviation filter | [optional] 

### Return type

[**list[PlayStat]**](PlayStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_play_types**
> list[PlayType] get_play_types()

Play types

Types of plays

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.PlaysApi()

try:
    # Play types
    api_response = api_instance.get_play_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaysApi->get_play_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PlayType]**](PlayType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plays**
> list[Play] get_plays(year, week, season_type=season_type, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference, play_type=play_type)

Play by play data

Get play data and results. Requires either a week or team to be specified.

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.PlaysApi()
year = 56 # int | Year filter
week = 56 # int | Week filter (required if team, offense, or defense, not specified)
season_type = 'regular' # str | Season type filter (optional) (default to regular)
team = 'team_example' # str | Team filter (optional)
offense = 'offense_example' # str | Offensive team filter (optional)
defense = 'defense_example' # str | Defensive team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)
offense_conference = 'offense_conference_example' # str | Offensive conference filter (optional)
defense_conference = 'defense_conference_example' # str | Defensive conference filter (optional)
play_type = 56 # int | Play type filter (optional)

try:
    # Play by play data
    api_response = api_instance.get_plays(year, week, season_type=season_type, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference, play_type=play_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaysApi->get_plays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | 
 **week** | **int**| Week filter (required if team, offense, or defense, not specified) | 
 **season_type** | **str**| Season type filter | [optional] [default to regular]
 **team** | **str**| Team filter | [optional] 
 **offense** | **str**| Offensive team filter | [optional] 
 **defense** | **str**| Defensive team filter | [optional] 
 **conference** | **str**| Conference filter | [optional] 
 **offense_conference** | **str**| Offensive conference filter | [optional] 
 **defense_conference** | **str**| Defensive conference filter | [optional] 
 **play_type** | **int**| Play type filter | [optional] 

### Return type

[**list[Play]**](Play.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

