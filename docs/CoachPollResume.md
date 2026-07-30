# CoachPollResume


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preseason_rank** | **int** |  | 
**postseason_rank** | **int** |  | 
**best_rank** | **int** |  | 
**weeks_ranked** | **int** |  | 
**weeks_top_ten** | **int** |  | 

## Example

```python
from cfbd.models.coach_poll_resume import CoachPollResume

# TODO update the JSON string below
json = "{}"
# create an instance of CoachPollResume from a JSON string
coach_poll_resume_instance = CoachPollResume.from_json(json)
# print the JSON string representation of the object
print CoachPollResume.to_json()

# convert the object into a dict
coach_poll_resume_dict = coach_poll_resume_instance.to_dict()
# create an instance of CoachPollResume from a dict
coach_poll_resume_from_dict = CoachPollResume.from_dict(coach_poll_resume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


