# GameTeamStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**teams** | [**List[GameTeamStatsTeam]**](GameTeamStatsTeam.md) |  | 

## Example

```python
from cfbd.models.game_team_stats import GameTeamStats

# TODO update the JSON string below
json = "{}"
# create an instance of GameTeamStats from a JSON string
game_team_stats_instance = GameTeamStats.from_json(json)
# print the JSON string representation of the object
print GameTeamStats.to_json()

# convert the object into a dict
game_team_stats_dict = game_team_stats_instance.to_dict()
# create an instance of GameTeamStats from a dict
game_team_stats_from_dict = GameTeamStats.from_dict(game_team_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


