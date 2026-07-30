# CoachSeasonTeamReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**school** | **str** |  | 
**conference** | **str** |  | 

## Example

```python
from cfbd.models.coach_season_team_reference import CoachSeasonTeamReference

# TODO update the JSON string below
json = "{}"
# create an instance of CoachSeasonTeamReference from a JSON string
coach_season_team_reference_instance = CoachSeasonTeamReference.from_json(json)
# print the JSON string representation of the object
print CoachSeasonTeamReference.to_json()

# convert the object into a dict
coach_season_team_reference_dict = coach_season_team_reference_instance.to_dict()
# create an instance of CoachSeasonTeamReference from a dict
coach_season_team_reference_from_dict = CoachSeasonTeamReference.from_dict(coach_season_team_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


