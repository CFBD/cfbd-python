# TeamTalent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team** | **str** |  | 
**talent** | **float** |  | 

## Example

```python
from cfbd.models.team_talent import TeamTalent

# TODO update the JSON string below
json = "{}"
# create an instance of TeamTalent from a JSON string
team_talent_instance = TeamTalent.from_json(json)
# print the JSON string representation of the object
print TeamTalent.to_json()

# convert the object into a dict
team_talent_dict = team_talent_instance.to_dict()
# create an instance of TeamTalent from a dict
team_talent_from_dict = TeamTalent.from_dict(team_talent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


