# CoachRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**ties** | **int** |  | 
**win_percentage** | **float** |  | 

## Example

```python
from cfbd.models.coach_record import CoachRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CoachRecord from a JSON string
coach_record_instance = CoachRecord.from_json(json)
# print the JSON string representation of the object
print CoachRecord.to_json()

# convert the object into a dict
coach_record_dict = coach_record_instance.to_dict()
# create an instance of CoachRecord from a dict
coach_record_from_dict = CoachRecord.from_dict(coach_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


