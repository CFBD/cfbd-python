# TeamSP


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**rating** | **float** |  | 
**ranking** | **int** |  | 
**second_order_wins** | **float** |  | 
**sos** | **float** |  | 
**offense** | [**TeamSPOffense**](TeamSPOffense.md) |  | 
**defense** | [**TeamSPDefense**](TeamSPDefense.md) |  | 
**special_teams** | [**TeamSPSpecialTeams**](TeamSPSpecialTeams.md) |  | 

## Example

```python
from cfbd.models.team_sp import TeamSP

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSP from a JSON string
team_sp_instance = TeamSP.from_json(json)
# print the JSON string representation of the object
print TeamSP.to_json()

# convert the object into a dict
team_sp_dict = team_sp_instance.to_dict()
# create an instance of TeamSP from a dict
team_sp_from_dict = TeamSP.from_dict(team_sp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


