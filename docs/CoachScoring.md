# CoachScoring


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points_for** | **int** |  | 
**points_against** | **int** |  | 
**average_point_differential** | **float** |  | 

## Example

```python
from cfbd.models.coach_scoring import CoachScoring

# TODO update the JSON string below
json = "{}"
# create an instance of CoachScoring from a JSON string
coach_scoring_instance = CoachScoring.from_json(json)
# print the JSON string representation of the object
print CoachScoring.to_json()

# convert the object into a dict
coach_scoring_dict = coach_scoring_instance.to_dict()
# create an instance of CoachScoring from a dict
coach_scoring_from_dict = CoachScoring.from_dict(coach_scoring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


