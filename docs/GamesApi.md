# cfbd.GamesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advanced_box_score**](GamesApi.md#get_advanced_box_score) | **GET** /game/box/advanced | Advanced box scores
[**get_calendar**](GamesApi.md#get_calendar) | **GET** /calendar | Season calendar
[**get_game_media**](GamesApi.md#get_game_media) | **GET** /games/media | Game media information and schedules
[**get_games**](GamesApi.md#get_games) | **GET** /games | Games and results
[**get_player_game_stats**](GamesApi.md#get_player_game_stats) | **GET** /games/players | Player game stats
[**get_team_game_stats**](GamesApi.md#get_team_game_stats) | **GET** /games/teams | Team game stats
[**get_team_records**](GamesApi.md#get_team_records) | **GET** /records | Team records


# **get_advanced_box_score**
> BoxScore get_advanced_box_score(game_id)

Advanced box scores

Get advanced box score data

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
game_id = 56 # int | Game id parameters

try:
    # Advanced box scores
    api_response = api_instance.get_advanced_box_score(game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_advanced_box_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| Game id parameters | 

### Return type

[**BoxScore**](BoxScore.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calendar**
> list[Week] get_calendar(year)

Season calendar

Get calendar of weeks by season

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter

try:
    # Season calendar
    api_response = api_instance.get_calendar(year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | 

### Return type

[**list[Week]**](Week.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game_media**
> list[GameMedia] get_game_media(year, week=week, season_type=season_type, team=team, conference=conference, media_type=media_type)

Game media information and schedules

Game media information (TV, radio, etc)

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter
week = 56 # int | Week filter (optional)
season_type = 'season_type_example' # str | Season type filter (regular, postseason, or both) (optional)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)
media_type = 'media_type_example' # str | Media type filter (tv, radio, web, ppv, or mobile) (optional)

try:
    # Game media information and schedules
    api_response = api_instance.get_game_media(year, week=week, season_type=season_type, team=team, conference=conference, media_type=media_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_game_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | 
 **week** | **int**| Week filter | [optional] 
 **season_type** | **str**| Season type filter (regular, postseason, or both) | [optional] 
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference filter | [optional] 
 **media_type** | **str**| Media type filter (tv, radio, web, ppv, or mobile) | [optional] 

### Return type

[**list[GameMedia]**](GameMedia.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_games**
> list[Game] get_games(year, week=week, season_type=season_type, team=team, home=home, away=away, conference=conference, id=id)

Games and results

Get game results

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
year = 56 # int | Year/season filter for games
week = 56 # int | Week filter (optional)
season_type = 'regular' # str | Season type filter (regular or postseason) (optional) (default to regular)
team = 'team_example' # str | Team (optional)
home = 'home_example' # str | Home team filter (optional)
away = 'away_example' # str | Away team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)
id = 56 # int | id filter for querying a single game (optional)

try:
    # Games and results
    api_response = api_instance.get_games(year, week=week, season_type=season_type, team=team, home=home, away=away, conference=conference, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_games: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year/season filter for games | 
 **week** | **int**| Week filter | [optional] 
 **season_type** | **str**| Season type filter (regular or postseason) | [optional] [default to regular]
 **team** | **str**| Team | [optional] 
 **home** | **str**| Home team filter | [optional] 
 **away** | **str**| Away team filter | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 
 **id** | **int**| id filter for querying a single game | [optional] 

### Return type

[**list[Game]**](Game.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_game_stats**
> list[PlayerGame] get_player_game_stats(year, week=week, season_type=season_type, team=team, conference=conference, category=category, game_id=game_id)

Player game stats

Player stats broken down by game

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
year = 56 # int | Year/season filter for games
week = 56 # int | Week filter (optional)
season_type = 'regular' # str | Season type filter (regular or postseason) (optional) (default to regular)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)
category = 'category_example' # str | Category filter (e.g defensive) (optional)
game_id = 56 # int | Game id filter (optional)

try:
    # Player game stats
    api_response = api_instance.get_player_game_stats(year, week=week, season_type=season_type, team=team, conference=conference, category=category, game_id=game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_player_game_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year/season filter for games | 
 **week** | **int**| Week filter | [optional] 
 **season_type** | **str**| Season type filter (regular or postseason) | [optional] [default to regular]
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 
 **category** | **str**| Category filter (e.g defensive) | [optional] 
 **game_id** | **int**| Game id filter | [optional] 

### Return type

[**list[PlayerGame]**](PlayerGame.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_game_stats**
> list[TeamGame] get_team_game_stats(year, week=week, season_type=season_type, team=team, conference=conference, game_id=game_id)

Team game stats

Team stats broken down by game

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
year = 56 # int | Year/season filter for games
week = 56 # int | Week filter (optional)
season_type = 'regular' # str | Season type filter (regular or postseason) (optional) (default to regular)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)
game_id = 56 # int | Game id filter (optional)

try:
    # Team game stats
    api_response = api_instance.get_team_game_stats(year, week=week, season_type=season_type, team=team, conference=conference, game_id=game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_team_game_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year/season filter for games | 
 **week** | **int**| Week filter | [optional] 
 **season_type** | **str**| Season type filter (regular or postseason) | [optional] [default to regular]
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 
 **game_id** | **int**| Game id filter | [optional] 

### Return type

[**list[TeamGame]**](TeamGame.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_records**
> list[TeamRecord] get_team_records(year=year, team=team, conference=conference)

Team records

Get team records by year

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter (optional)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)

try:
    # Team records
    api_response = api_instance.get_team_records(year=year, team=team, conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_team_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference filter | [optional] 

### Return type

[**list[TeamRecord]**](TeamRecord.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

