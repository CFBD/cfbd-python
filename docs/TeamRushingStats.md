# TeamRushingStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**power_success** | **float** |  | 
**stuff_rate** | **float** |  | 
**line_yards** | **float** |  | 
**line_yards_average** | **float** |  | 
**second_level_yards** | **float** |  | 
**second_level_yards_average** | **float** |  | 
**open_field_yards** | **float** |  | 
**open_field_yards_average** | **float** |  | 

## Example

```python
from cfbd.models.team_rushing_stats import TeamRushingStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRushingStats from a JSON string
team_rushing_stats_instance = TeamRushingStats.from_json(json)
# print the JSON string representation of the object
print TeamRushingStats.to_json()

# convert the object into a dict
team_rushing_stats_dict = team_rushing_stats_instance.to_dict()
# create an instance of TeamRushingStats from a dict
team_rushing_stats_from_dict = TeamRushingStats.from_dict(team_rushing_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


