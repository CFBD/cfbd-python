# GameHavocStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**season_type** | [**SeasonTypeDB**](SeasonTypeDB.md) |  | 
**week** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**opponent** | **str** |  | 
**opponent_conference** | **str** |  | 
**offense** | [**GameHavocStatsOffense**](GameHavocStatsOffense.md) |  | 
**defense** | [**GameHavocStatsOffense**](GameHavocStatsOffense.md) |  | 

## Example

```python
from cfbd.models.game_havoc_stats import GameHavocStats

# TODO update the JSON string below
json = "{}"
# create an instance of GameHavocStats from a JSON string
game_havoc_stats_instance = GameHavocStats.from_json(json)
# print the JSON string representation of the object
print GameHavocStats.to_json()

# convert the object into a dict
game_havoc_stats_dict = game_havoc_stats_instance.to_dict()
# create an instance of GameHavocStats from a dict
game_havoc_stats_from_dict = GameHavocStats.from_dict(game_havoc_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


