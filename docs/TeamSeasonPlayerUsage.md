# TeamSeasonPlayerUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**usage** | [**TeamSeasonPlayerUsageUsage**](TeamSeasonPlayerUsageUsage.md) |  | 

## Example

```python
from cfbd.models.team_season_player_usage import TeamSeasonPlayerUsage

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonPlayerUsage from a JSON string
team_season_player_usage_instance = TeamSeasonPlayerUsage.from_json(json)
# print the JSON string representation of the object
print TeamSeasonPlayerUsage.to_json()

# convert the object into a dict
team_season_player_usage_dict = team_season_player_usage_instance.to_dict()
# create an instance of TeamSeasonPlayerUsage from a dict
team_season_player_usage_from_dict = TeamSeasonPlayerUsage.from_dict(team_season_player_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


