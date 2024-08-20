# GamePlayerStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**teams** | [**List[GamePlayerStatsTeam]**](GamePlayerStatsTeam.md) |  | 

## Example

```python
from cfbd.models.game_player_stats import GamePlayerStats

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlayerStats from a JSON string
game_player_stats_instance = GamePlayerStats.from_json(json)
# print the JSON string representation of the object
print GamePlayerStats.to_json()

# convert the object into a dict
game_player_stats_dict = game_player_stats_instance.to_dict()
# create an instance of GamePlayerStats from a dict
game_player_stats_from_dict = GamePlayerStats.from_dict(game_player_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


