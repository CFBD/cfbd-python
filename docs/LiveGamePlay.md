# LiveGamePlay


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**home_score** | **int** |  | 
**away_score** | **int** |  | 
**period** | **int** |  | 
**clock** | **str** |  | 
**wall_clock** | **datetime** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**down** | **int** |  | 
**distance** | **int** |  | 
**yards_to_goal** | **int** |  | 
**yards_gained** | **int** |  | 
**play_type_id** | **int** |  | 
**play_type** | **str** |  | 
**epa** | **float** |  | 
**garbage_time** | **bool** |  | 
**success** | **bool** |  | 
**rush_pash** | **str** |  | 
**down_type** | **str** |  | 
**play_text** | **str** |  | 

## Example

```python
from cfbd.models.live_game_play import LiveGamePlay

# TODO update the JSON string below
json = "{}"
# create an instance of LiveGamePlay from a JSON string
live_game_play_instance = LiveGamePlay.from_json(json)
# print the JSON string representation of the object
print LiveGamePlay.to_json()

# convert the object into a dict
live_game_play_dict = live_game_play_instance.to_dict()
# create an instance of LiveGamePlay from a dict
live_game_play_from_dict = LiveGamePlay.from_dict(live_game_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


