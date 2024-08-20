# GamePlayerStatsTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**conference** | **str** |  | 
**home_away** | **str** |  | 
**points** | **int** |  | 
**categories** | [**List[GamePlayerStatCategories]**](GamePlayerStatCategories.md) |  | 

## Example

```python
from cfbd.models.game_player_stats_team import GamePlayerStatsTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlayerStatsTeam from a JSON string
game_player_stats_team_instance = GamePlayerStatsTeam.from_json(json)
# print the JSON string representation of the object
print GamePlayerStatsTeam.to_json()

# convert the object into a dict
game_player_stats_team_dict = game_player_stats_team_instance.to_dict()
# create an instance of GamePlayerStatsTeam from a dict
game_player_stats_team_from_dict = GamePlayerStatsTeam.from_dict(game_player_stats_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


