# TeamSeasonAdvancedStatsDefense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passing_plays** | [**TeamSeasonAdvancedStatsOffensePassingPlays**](TeamSeasonAdvancedStatsOffensePassingPlays.md) |  | 
**rushing_plays** | [**TeamSeasonAdvancedStatsOffensePassingPlays**](TeamSeasonAdvancedStatsOffensePassingPlays.md) |  | 
**passing_downs** | [**TeamSeasonAdvancedStatsOffensePassingPlays**](TeamSeasonAdvancedStatsOffensePassingPlays.md) |  | 
**standard_downs** | [**TeamSeasonAdvancedStatsOffensePassingDowns**](TeamSeasonAdvancedStatsOffensePassingDowns.md) |  | 
**havoc** | [**TeamSeasonAdvancedStatsOffenseHavoc**](TeamSeasonAdvancedStatsOffenseHavoc.md) |  | 
**field_position** | [**TeamSeasonAdvancedStatsOffenseFieldPosition**](TeamSeasonAdvancedStatsOffenseFieldPosition.md) |  | 
**points_per_opportunity** | **float** |  | 
**total_opportunies** | **int** |  | 
**open_field_yards_total** | **int** |  | 
**open_field_yards** | **float** |  | 
**second_level_yards_total** | **int** |  | 
**second_level_yards** | **float** |  | 
**line_yards_total** | **int** |  | 
**line_yards** | **float** |  | 
**stuff_rate** | **float** |  | 
**power_success** | **float** |  | 
**explosiveness** | **float** |  | 
**success_rate** | **float** |  | 
**total_ppa** | **float** |  | 
**ppa** | **float** |  | 
**drives** | **int** |  | 
**plays** | **int** |  | 

## Example

```python
from cfbd.models.team_season_advanced_stats_defense import TeamSeasonAdvancedStatsDefense

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonAdvancedStatsDefense from a JSON string
team_season_advanced_stats_defense_instance = TeamSeasonAdvancedStatsDefense.from_json(json)
# print the JSON string representation of the object
print TeamSeasonAdvancedStatsDefense.to_json()

# convert the object into a dict
team_season_advanced_stats_defense_dict = team_season_advanced_stats_defense_instance.to_dict()
# create an instance of TeamSeasonAdvancedStatsDefense from a dict
team_season_advanced_stats_defense_from_dict = TeamSeasonAdvancedStatsDefense.from_dict(team_season_advanced_stats_defense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


