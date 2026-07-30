# CoachTeamReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**school** | **str** |  | 

## Example

```python
from cfbd.models.coach_team_reference import CoachTeamReference

# TODO update the JSON string below
json = "{}"
# create an instance of CoachTeamReference from a JSON string
coach_team_reference_instance = CoachTeamReference.from_json(json)
# print the JSON string representation of the object
print CoachTeamReference.to_json()

# convert the object into a dict
coach_team_reference_dict = coach_team_reference_instance.to_dict()
# create an instance of CoachTeamReference from a dict
coach_team_reference_from_dict = CoachTeamReference.from_dict(coach_team_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


