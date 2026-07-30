# CoachRecordSplits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | [**CoachRecord**](CoachRecord.md) |  | 
**postseason** | [**CoachRecord**](CoachRecord.md) |  | 
**home** | [**CoachRecord**](CoachRecord.md) |  | 
**away** | [**CoachRecord**](CoachRecord.md) |  | 
**neutral** | [**CoachRecord**](CoachRecord.md) |  | 

## Example

```python
from cfbd.models.coach_record_splits import CoachRecordSplits

# TODO update the JSON string below
json = "{}"
# create an instance of CoachRecordSplits from a JSON string
coach_record_splits_instance = CoachRecordSplits.from_json(json)
# print the JSON string representation of the object
print CoachRecordSplits.to_json()

# convert the object into a dict
coach_record_splits_dict = coach_record_splits_instance.to_dict()
# create an instance of CoachRecordSplits from a dict
coach_record_splits_from_dict = CoachRecordSplits.from_dict(coach_record_splits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


