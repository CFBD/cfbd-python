# TeamSPDefense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**havoc** | [**AdvancedSeasonStatOffenseHavoc**](AdvancedSeasonStatOffenseHavoc.md) |  | 
**passing_downs** | **float** |  | 
**standard_downs** | **float** |  | 
**passing** | **float** |  | 
**rushing** | **float** |  | 
**explosiveness** | **float** |  | 
**success** | **float** |  | 
**rating** | **float** |  | 
**ranking** | **int** |  | 

## Example

```python
from cfbd.models.team_sp_defense import TeamSPDefense

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSPDefense from a JSON string
team_sp_defense_instance = TeamSPDefense.from_json(json)
# print the JSON string representation of the object
print TeamSPDefense.to_json()

# convert the object into a dict
team_sp_defense_dict = team_sp_defense_instance.to_dict()
# create an instance of TeamSPDefense from a dict
team_sp_defense_from_dict = TeamSPDefense.from_dict(team_sp_defense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


