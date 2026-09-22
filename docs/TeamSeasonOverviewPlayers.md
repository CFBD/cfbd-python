# TeamSeasonOverviewPlayers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | [**List[TeamSeasonPlayerUsage]**](TeamSeasonPlayerUsage.md) |  | 
**ppa** | [**List[TeamSeasonPlayerPpa]**](TeamSeasonPlayerPpa.md) |  | 

## Example

```python
from cfbd.models.team_season_overview_players import TeamSeasonOverviewPlayers

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewPlayers from a JSON string
team_season_overview_players_instance = TeamSeasonOverviewPlayers.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewPlayers.to_json()

# convert the object into a dict
team_season_overview_players_dict = team_season_overview_players_instance.to_dict()
# create an instance of TeamSeasonOverviewPlayers from a dict
team_season_overview_players_from_dict = TeamSeasonOverviewPlayers.from_dict(team_season_overview_players_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


