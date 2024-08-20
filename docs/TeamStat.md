# TeamStat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**stat_name** | **str** |  | 
**stat_value** | [**TeamStatStatValue**](TeamStatStatValue.md) |  | 

## Example

```python
from cfbd.models.team_stat import TeamStat

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStat from a JSON string
team_stat_instance = TeamStat.from_json(json)
# print the JSON string representation of the object
print TeamStat.to_json()

# convert the object into a dict
team_stat_dict = team_stat_instance.to_dict()
# create an instance of TeamStat from a dict
team_stat_from_dict = TeamStat.from_dict(team_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


