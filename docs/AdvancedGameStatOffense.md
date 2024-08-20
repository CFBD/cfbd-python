# AdvancedGameStatOffense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passing_plays** | [**AdvancedGameStatOffensePassingPlays**](AdvancedGameStatOffensePassingPlays.md) |  | 
**rushing_plays** | [**AdvancedGameStatOffensePassingPlays**](AdvancedGameStatOffensePassingPlays.md) |  | 
**passing_downs** | [**AdvancedGameStatOffensePassingDowns**](AdvancedGameStatOffensePassingDowns.md) |  | 
**standard_downs** | [**AdvancedGameStatOffensePassingDowns**](AdvancedGameStatOffensePassingDowns.md) |  | 
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
from cfbd.models.advanced_game_stat_offense import AdvancedGameStatOffense

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedGameStatOffense from a JSON string
advanced_game_stat_offense_instance = AdvancedGameStatOffense.from_json(json)
# print the JSON string representation of the object
print AdvancedGameStatOffense.to_json()

# convert the object into a dict
advanced_game_stat_offense_dict = advanced_game_stat_offense_instance.to_dict()
# create an instance of AdvancedGameStatOffense from a dict
advanced_game_stat_offense_from_dict = AdvancedGameStatOffense.from_dict(advanced_game_stat_offense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


