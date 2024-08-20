# GameTeamStatsTeamStat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | 
**stat** | **str** |  | 

## Example

```python
from cfbd.models.game_team_stats_team_stat import GameTeamStatsTeamStat

# TODO update the JSON string below
json = "{}"
# create an instance of GameTeamStatsTeamStat from a JSON string
game_team_stats_team_stat_instance = GameTeamStatsTeamStat.from_json(json)
# print the JSON string representation of the object
print GameTeamStatsTeamStat.to_json()

# convert the object into a dict
game_team_stats_team_stat_dict = game_team_stats_team_stat_instance.to_dict()
# create an instance of GameTeamStatsTeamStat from a dict
game_team_stats_team_stat_from_dict = GameTeamStatsTeamStat.from_dict(game_team_stats_team_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


