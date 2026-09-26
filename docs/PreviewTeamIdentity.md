# PreviewTeamIdentity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**conference** | **str** |  | 
**conference_abbreviation** | **str** |  | 
**classification** | [**DivisionClassification**](DivisionClassification.md) |  | 
**points** | **int** |  | 

## Example

```python
from cfbd.models.preview_team_identity import PreviewTeamIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewTeamIdentity from a JSON string
preview_team_identity_instance = PreviewTeamIdentity.from_json(json)
# print the JSON string representation of the object
print PreviewTeamIdentity.to_json()

# convert the object into a dict
preview_team_identity_dict = preview_team_identity_instance.to_dict()
# create an instance of PreviewTeamIdentity from a dict
preview_team_identity_from_dict = PreviewTeamIdentity.from_dict(preview_team_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


