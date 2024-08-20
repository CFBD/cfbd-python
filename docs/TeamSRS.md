# TeamSRS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**division** | **str** |  | 
**rating** | **float** |  | 
**ranking** | **int** |  | 

## Example

```python
from cfbd.models.team_srs import TeamSRS

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSRS from a JSON string
team_srs_instance = TeamSRS.from_json(json)
# print the JSON string representation of the object
print TeamSRS.to_json()

# convert the object into a dict
team_srs_dict = team_srs_instance.to_dict()
# create an instance of TeamSRS from a dict
team_srs_from_dict = TeamSRS.from_dict(team_srs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


