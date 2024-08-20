# GameTeamStatsTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**home_away** | **str** |  | 
**points** | **int** |  | 
**stats** | [**List[GameTeamStatsTeamStat]**](GameTeamStatsTeamStat.md) |  | 

## Example

```python
from cfbd.models.game_team_stats_team import GameTeamStatsTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GameTeamStatsTeam from a JSON string
game_team_stats_team_instance = GameTeamStatsTeam.from_json(json)
# print the JSON string representation of the object
print GameTeamStatsTeam.to_json()

# convert the object into a dict
game_team_stats_team_dict = game_team_stats_team_instance.to_dict()
# create an instance of GameTeamStatsTeam from a dict
game_team_stats_team_from_dict = GameTeamStatsTeam.from_dict(game_team_stats_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


