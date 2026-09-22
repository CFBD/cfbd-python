# TeamSeasonPlayerUsageUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passing_downs** | **float** |  | 
**standard_downs** | **float** |  | 
**third_down** | **float** |  | 
**second_down** | **float** |  | 
**first_down** | **float** |  | 
**rush** | **float** |  | 
**var_pass** | **float** |  | 
**overall** | **float** |  | 

## Example

```python
from cfbd.models.team_season_player_usage_usage import TeamSeasonPlayerUsageUsage

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonPlayerUsageUsage from a JSON string
team_season_player_usage_usage_instance = TeamSeasonPlayerUsageUsage.from_json(json)
# print the JSON string representation of the object
print TeamSeasonPlayerUsageUsage.to_json()

# convert the object into a dict
team_season_player_usage_usage_dict = team_season_player_usage_usage_instance.to_dict()
# create an instance of TeamSeasonPlayerUsageUsage from a dict
team_season_player_usage_usage_from_dict = TeamSeasonPlayerUsageUsage.from_dict(team_season_player_usage_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


