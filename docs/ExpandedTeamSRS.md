# ExpandedTeamSRS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**division** | **str** |  | 
**rating** | **float** |  | 
**ranking** | **int** |  | 
**classification** | [**DivisionClassification**](DivisionClassification.md) |  | 

## Example

```python
from cfbd.models.expanded_team_srs import ExpandedTeamSRS

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedTeamSRS from a JSON string
expanded_team_srs_instance = ExpandedTeamSRS.from_json(json)
# print the JSON string representation of the object
print ExpandedTeamSRS.to_json()

# convert the object into a dict
expanded_team_srs_dict = expanded_team_srs_instance.to_dict()
# create an instance of ExpandedTeamSRS from a dict
expanded_team_srs_from_dict = ExpandedTeamSRS.from_dict(expanded_team_srs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


