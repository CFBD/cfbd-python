# CoachTenure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**coach** | [**CoachReference**](CoachReference.md) |  | 
**team** | [**CoachTeamReference**](CoachTeamReference.md) |  | 
**hire_date** | **str** |  | 
**start_year** | **int** |  | 
**end_year** | **int** |  | 
**effective_start** | **datetime** |  | 
**effective_end** | **datetime** |  | 
**is_interim** | **bool** |  | 
**active** | **bool** |  | 
**seasons** | **int** |  | 
**record** | [**CoachRecord**](CoachRecord.md) |  | 
**attribution_complete** | **bool** |  | 

## Example

```python
from cfbd.models.coach_tenure import CoachTenure

# TODO update the JSON string below
json = "{}"
# create an instance of CoachTenure from a JSON string
coach_tenure_instance = CoachTenure.from_json(json)
# print the JSON string representation of the object
print CoachTenure.to_json()

# convert the object into a dict
coach_tenure_dict = coach_tenure_instance.to_dict()
# create an instance of CoachTenure from a dict
coach_tenure_from_dict = CoachTenure.from_dict(coach_tenure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


