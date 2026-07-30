# CoachDraftContext


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**total_picks** | **int** |  | 
**first_round_picks** | **int** |  | 

## Example

```python
from cfbd.models.coach_draft_context import CoachDraftContext

# TODO update the JSON string below
json = "{}"
# create an instance of CoachDraftContext from a JSON string
coach_draft_context_instance = CoachDraftContext.from_json(json)
# print the JSON string representation of the object
print CoachDraftContext.to_json()

# convert the object into a dict
coach_draft_context_dict = coach_draft_context_instance.to_dict()
# create an instance of CoachDraftContext from a dict
coach_draft_context_from_dict = CoachDraftContext.from_dict(coach_draft_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


