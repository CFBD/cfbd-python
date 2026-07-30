# CoachCfpContext


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appeared** | **bool** |  | 
**seed** | **int** |  | 
**outcome** | [**CfpCoachSeasonOutcome**](CfpCoachSeasonOutcome.md) |  | 

## Example

```python
from cfbd.models.coach_cfp_context import CoachCfpContext

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCfpContext from a JSON string
coach_cfp_context_instance = CoachCfpContext.from_json(json)
# print the JSON string representation of the object
print CoachCfpContext.to_json()

# convert the object into a dict
coach_cfp_context_dict = coach_cfp_context_instance.to_dict()
# create an instance of CoachCfpContext from a dict
coach_cfp_context_from_dict = CoachCfpContext.from_dict(coach_cfp_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


