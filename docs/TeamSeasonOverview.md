# TeamSeasonOverview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced** | [**TeamSeasonAdvancedStats**](TeamSeasonAdvancedStats.md) |  | 
**players** | [**TeamSeasonOverviewPlayers**](TeamSeasonOverviewPlayers.md) |  | 
**passing** | [**TeamPassingSeason**](TeamPassingSeason.md) |  | 
**rushing** | [**TeamRushingSeason**](TeamRushingSeason.md) |  | 
**record** | [**TeamSeasonOverviewRecord**](TeamSeasonOverviewRecord.md) |  | 
**ratings** | [**TeamSeasonOverviewRatings**](TeamSeasonOverviewRatings.md) |  | 
**season** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 

## Example

```python
from cfbd.models.team_season_overview import TeamSeasonOverview

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverview from a JSON string
team_season_overview_instance = TeamSeasonOverview.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverview.to_json()

# convert the object into a dict
team_season_overview_dict = team_season_overview_instance.to_dict()
# create an instance of TeamSeasonOverview from a dict
team_season_overview_from_dict = TeamSeasonOverview.from_dict(team_season_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


