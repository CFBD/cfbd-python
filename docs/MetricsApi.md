# cfbd.MetricsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_game_ppa**](MetricsApi.md#get_game_ppa) | **GET** /ppa/games | Team Predicated Points Added (PPA/EPA) by game
[**get_player_game_ppa**](MetricsApi.md#get_player_game_ppa) | **GET** /ppa/players/games | Player Predicated Points Added (PPA/EPA) broken down by game
[**get_player_season_ppa**](MetricsApi.md#get_player_season_ppa) | **GET** /ppa/players/season | Player Predicated Points Added (PPA/EPA) broken down by season
[**get_predicted_points**](MetricsApi.md#get_predicted_points) | **GET** /ppa/predicted | Predicted Points (i.e. Expected Points or EP)
[**get_pregame_win_probabilities**](MetricsApi.md#get_pregame_win_probabilities) | **GET** /metrics/wp/pregame | Pregame win probability data
[**get_team_ppa**](MetricsApi.md#get_team_ppa) | **GET** /ppa/teams | Predicted Points Added (PPA/EPA) data by team
[**get_win_probability_data**](MetricsApi.md#get_win_probability_data) | **GET** /metrics/wp | Win probability chart data


# **get_game_ppa**
> list[GamePPA] get_game_ppa(year, week=week, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time)

Team Predicated Points Added (PPA/EPA) by game

Predicted Points Added (PPA) by game

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.MetricsApi()
year = 56 # int | Year filter
week = 56 # int | Week filter (optional)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)
exclude_garbage_time = true # bool | Filter to remove garbage time plays from calculations (optional)

try:
    # Team Predicated Points Added (PPA/EPA) by game
    api_response = api_instance.get_game_ppa(year, week=week, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_game_ppa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | 
 **week** | **int**| Week filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference filter | [optional] 
 **exclude_garbage_time** | **bool**| Filter to remove garbage time plays from calculations | [optional] 

### Return type

[**list[GamePPA]**](GamePPA.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_game_ppa**
> list[PlayerGamePPA] get_player_game_ppa(year=year, week=week, team=team, position=position, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)

Player Predicated Points Added (PPA/EPA) broken down by game

Predicted Points Added (PPA) by player game

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.MetricsApi()
year = 56 # int | Year filter (optional)
week = 56 # int | Week filter (optional)
team = 'team_example' # str | Team filter (optional)
position = 'position_example' # str | Position abbreviation filter (optional)
player_id = 56 # int | Player id filter (optional)
threshold = 'threshold_example' # str | Minimum play threshold filter (optional)
exclude_garbage_time = true # bool | Filter to remove garbage time plays from calculations (optional)

try:
    # Player Predicated Points Added (PPA/EPA) broken down by game
    api_response = api_instance.get_player_game_ppa(year=year, week=week, team=team, position=position, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_player_game_ppa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [optional] 
 **week** | **int**| Week filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **position** | **str**| Position abbreviation filter | [optional] 
 **player_id** | **int**| Player id filter | [optional] 
 **threshold** | **str**| Minimum play threshold filter | [optional] 
 **exclude_garbage_time** | **bool**| Filter to remove garbage time plays from calculations | [optional] 

### Return type

[**list[PlayerGamePPA]**](PlayerGamePPA.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_season_ppa**
> list[PlayerSeasonPPA] get_player_season_ppa(year=year, team=team, conference=conference, position=position, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)

Player Predicated Points Added (PPA/EPA) broken down by season

Predicted Points Added (PPA) by player season

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.MetricsApi()
year = 56 # int | Year filter (optional)
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)
position = 'position_example' # str | Position abbreviation filter (optional)
player_id = 56 # int | Player id filter (optional)
threshold = 'threshold_example' # str | Minimum play threshold filter (optional)
exclude_garbage_time = true # bool | Filter to remove garbage time plays from calculations (optional)

try:
    # Player Predicated Points Added (PPA/EPA) broken down by season
    api_response = api_instance.get_player_season_ppa(year=year, team=team, conference=conference, position=position, player_id=player_id, threshold=threshold, exclude_garbage_time=exclude_garbage_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_player_season_ppa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **conference** | **str**| Conference abbreviation filter | [optional] 
 **position** | **str**| Position abbreviation filter | [optional] 
 **player_id** | **int**| Player id filter | [optional] 
 **threshold** | **str**| Minimum play threshold filter | [optional] 
 **exclude_garbage_time** | **bool**| Filter to remove garbage time plays from calculations | [optional] 

### Return type

[**list[PlayerSeasonPPA]**](PlayerSeasonPPA.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_predicted_points**
> list[PredictedPoints] get_predicted_points(down, distance)

Predicted Points (i.e. Expected Points or EP)

Predicted Points

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.MetricsApi()
down = 56 # int | Down filter
distance = 56 # int | Distance filter

try:
    # Predicted Points (i.e. Expected Points or EP)
    api_response = api_instance.get_predicted_points(down, distance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_predicted_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **down** | **int**| Down filter | 
 **distance** | **int**| Distance filter | 

### Return type

[**list[PredictedPoints]**](PredictedPoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pregame_win_probabilities**
> list[PregameWP] get_pregame_win_probabilities(year=year, week=week, team=team, season_type=season_type)

Pregame win probability data

Pregame win probabilities

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.MetricsApi()
year = 56 # int | Year filter (optional)
week = 56 # int | Week filter (optional)
team = 'team_example' # str | Team filter (optional)
season_type = 'season_type_example' # str | regular or postseason (optional)

try:
    # Pregame win probability data
    api_response = api_instance.get_pregame_win_probabilities(year=year, week=week, team=team, season_type=season_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_pregame_win_probabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [optional] 
 **week** | **int**| Week filter | [optional] 
 **team** | **str**| Team filter | [optional] 
 **season_type** | **str**| regular or postseason | [optional] 

### Return type

[**list[PregameWP]**](PregameWP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_ppa**
> list[TeamPPA] get_team_ppa(year=year, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time)

Predicted Points Added (PPA/EPA) data by team

Predicted Points Added (PPA)

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.MetricsApi()
year = 56 # int | Year filter (required if team not specified) (optional)
team = 'team_example' # str | Team filter (required if year not specified) (optional)
conference = 'conference_example' # str | Conference filter (optional)
exclude_garbage_time = true # bool | Filter to remove garbage time plays from calculations (optional)

try:
    # Predicted Points Added (PPA/EPA) data by team
    api_response = api_instance.get_team_ppa(year=year, team=team, conference=conference, exclude_garbage_time=exclude_garbage_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_team_ppa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter (required if team not specified) | [optional] 
 **team** | **str**| Team filter (required if year not specified) | [optional] 
 **conference** | **str**| Conference filter | [optional] 
 **exclude_garbage_time** | **bool**| Filter to remove garbage time plays from calculations | [optional] 

### Return type

[**list[TeamPPA]**](TeamPPA.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_win_probability_data**
> list[PlayWP] get_win_probability_data(game_id, adjust_for_spread=adjust_for_spread)

Win probability chart data

Win probability data

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cfbd.MetricsApi()
game_id = 56 # int | Game id filter
adjust_for_spread = true # bool | Toggles pregame spread adjustments (optional) (default to true)

try:
    # Win probability chart data
    api_response = api_instance.get_win_probability_data(game_id, adjust_for_spread=adjust_for_spread)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_win_probability_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| Game id filter | 
 **adjust_for_spread** | **bool**| Toggles pregame spread adjustments | [optional] [default to true]

### Return type

[**list[PlayWP]**](PlayWP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

