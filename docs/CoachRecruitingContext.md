# CoachRecruitingContext


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | 
**points** | **float** |  | 
**talent** | **float** |  | 

## Example

```python
from cfbd.models.coach_recruiting_context import CoachRecruitingContext

# TODO update the JSON string below
json = "{}"
# create an instance of CoachRecruitingContext from a JSON string
coach_recruiting_context_instance = CoachRecruitingContext.from_json(json)
# print the JSON string representation of the object
print CoachRecruitingContext.to_json()

# convert the object into a dict
coach_recruiting_context_dict = coach_recruiting_context_instance.to_dict()
# create an instance of CoachRecruitingContext from a dict
coach_recruiting_context_from_dict = CoachRecruitingContext.from_dict(coach_recruiting_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


