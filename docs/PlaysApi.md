# cfbd.PlaysApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_play_stat_types**](PlaysApi.md#get_play_stat_types) | **GET** /play/stat/types | Get play stat type lists
[**get_play_stats**](PlaysApi.md#get_play_stats) | **GET** /play/stats | Get play statistics
[**get_play_types**](PlaysApi.md#get_play_types) | **GET** /play/types | Get play type list
[**get_plays**](PlaysApi.md#get_plays) | **GET** /plays | Get play information. Requires either a week or team to be specified.


# **get_play_stat_types**
> list[PlayStatType] get_play_stat_types()

Get play stat type lists

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
    # Get play stat type lists
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
> list[PlayStat] get_play_stats(year=year, week=week, team=team, game_id=game_id, athlete_id=athlete_id, stat_type_id=stat_type_id, season_type=season_type)

Get play statistics

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

try:
    # Get play statistics
    api_response = api_instance.get_play_stats(year=year, week=week, team=team, game_id=game_id, athlete_id=athlete_id, stat_type_id=stat_type_id, season_type=season_type)
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

Get play type list

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
    # Get play type list
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
> list[Play] get_plays(year, season_type=season_type, week=week, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference, play_type=play_type)

Get play information. Requires either a week or team to be specified.

Play results

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
season_type = 'regular' # str | Season type filter (optional) (default to regular)
week = 56 # int | Week filter (required if team, offense, or defense, not specified) (optional)
team = 'team_example' # str | Team filter (optional)
offense = 'offense_example' # str | Offensive team filter (optional)
defense = 'defense_example' # str | Defensive team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)
offense_conference = 'offense_conference_example' # str | Offensive conference filter (optional)
defense_conference = 'defense_conference_example' # str | Defensive conference filter (optional)
play_type = 56 # int | Play type filter (optional)

try:
    # Get play information. Requires either a week or team to be specified.
    api_response = api_instance.get_plays(year, season_type=season_type, week=week, team=team, offense=offense, defense=defense, conference=conference, offense_conference=offense_conference, defense_conference=defense_conference, play_type=play_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaysApi->get_plays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | 
 **season_type** | **str**| Season type filter | [optional] [default to regular]
 **week** | **int**| Week filter (required if team, offense, or defense, not specified) | [optional] 
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

