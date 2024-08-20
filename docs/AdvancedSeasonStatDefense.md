# AdvancedSeasonStatDefense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passing_plays** | [**AdvancedSeasonStatOffensePassingPlays**](AdvancedSeasonStatOffensePassingPlays.md) |  | 
**rushing_plays** | [**AdvancedSeasonStatOffensePassingPlays**](AdvancedSeasonStatOffensePassingPlays.md) |  | 
**passing_downs** | [**AdvancedSeasonStatOffensePassingPlays**](AdvancedSeasonStatOffensePassingPlays.md) |  | 
**standard_downs** | [**AdvancedSeasonStatOffensePassingDowns**](AdvancedSeasonStatOffensePassingDowns.md) |  | 
**havoc** | [**AdvancedSeasonStatOffenseHavoc**](AdvancedSeasonStatOffenseHavoc.md) |  | 
**field_position** | [**AdvancedSeasonStatOffenseFieldPosition**](AdvancedSeasonStatOffenseFieldPosition.md) |  | 
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
from cfbd.models.advanced_season_stat_defense import AdvancedSeasonStatDefense

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedSeasonStatDefense from a JSON string
advanced_season_stat_defense_instance = AdvancedSeasonStatDefense.from_json(json)
# print the JSON string representation of the object
print AdvancedSeasonStatDefense.to_json()

# convert the object into a dict
advanced_season_stat_defense_dict = advanced_season_stat_defense_instance.to_dict()
# create an instance of AdvancedSeasonStatDefense from a dict
advanced_season_stat_defense_from_dict = AdvancedSeasonStatDefense.from_dict(advanced_season_stat_defense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


