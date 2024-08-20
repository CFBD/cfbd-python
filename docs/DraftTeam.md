# DraftTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | 
**nickname** | **str** |  | 
**display_name** | **str** |  | 
**logo** | **str** |  | 

## Example

```python
from cfbd.models.draft_team import DraftTeam

# TODO update the JSON string below
json = "{}"
# create an instance of DraftTeam from a JSON string
draft_team_instance = DraftTeam.from_json(json)
# print the JSON string representation of the object
print DraftTeam.to_json()

# convert the object into a dict
draft_team_dict = draft_team_instance.to_dict()
# create an instance of DraftTeam from a dict
draft_team_from_dict = DraftTeam.from_dict(draft_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


