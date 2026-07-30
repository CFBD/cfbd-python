# CoachReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 

## Example

```python
from cfbd.models.coach_reference import CoachReference

# TODO update the JSON string below
json = "{}"
# create an instance of CoachReference from a JSON string
coach_reference_instance = CoachReference.from_json(json)
# print the JSON string representation of the object
print CoachReference.to_json()

# convert the object into a dict
coach_reference_dict = coach_reference_instance.to_dict()
# create an instance of CoachReference from a dict
coach_reference_from_dict = CoachReference.from_dict(coach_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


