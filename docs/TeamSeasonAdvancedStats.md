# TeamSeasonAdvancedStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**offense** | [**TeamSeasonAdvancedStatsOffense**](TeamSeasonAdvancedStatsOffense.md) |  | 
**defense** | [**TeamSeasonAdvancedStatsDefense**](TeamSeasonAdvancedStatsDefense.md) |  | 

## Example

```python
from cfbd.models.team_season_advanced_stats import TeamSeasonAdvancedStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonAdvancedStats from a JSON string
team_season_advanced_stats_instance = TeamSeasonAdvancedStats.from_json(json)
# print the JSON string representation of the object
print TeamSeasonAdvancedStats.to_json()

# convert the object into a dict
team_season_advanced_stats_dict = team_season_advanced_stats_instance.to_dict()
# create an instance of TeamSeasonAdvancedStats from a dict
team_season_advanced_stats_from_dict = TeamSeasonAdvancedStats.from_dict(team_season_advanced_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


