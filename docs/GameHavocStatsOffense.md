# GameHavocStatsOffense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_havoc_rate** | **float** |  | 
**front_seven_havoc_rate** | **float** |  | 
**havoc_rate** | **float** |  | 
**db_havoc_events** | **float** |  | 
**front_seven_havoc_events** | **float** |  | 
**total_havoc_events** | **float** |  | 
**total_plays** | **float** |  | 

## Example

```python
from cfbd.models.game_havoc_stats_offense import GameHavocStatsOffense

# TODO update the JSON string below
json = "{}"
# create an instance of GameHavocStatsOffense from a JSON string
game_havoc_stats_offense_instance = GameHavocStatsOffense.from_json(json)
# print the JSON string representation of the object
print GameHavocStatsOffense.to_json()

# convert the object into a dict
game_havoc_stats_offense_dict = game_havoc_stats_offense_instance.to_dict()
# create an instance of GameHavocStatsOffense from a dict
game_havoc_stats_offense_from_dict = GameHavocStatsOffense.from_dict(game_havoc_stats_offense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


