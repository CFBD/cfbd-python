# FieldErrorsValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | [optional] 
**message** | **str** |  | 

## Example

```python
from cfbd.models.field_errors_value import FieldErrorsValue

# TODO update the JSON string below
json = "{}"
# create an instance of FieldErrorsValue from a JSON string
field_errors_value_instance = FieldErrorsValue.from_json(json)
# print the JSON string representation of the object
print FieldErrorsValue.to_json()

# convert the object into a dict
field_errors_value_dict = field_errors_value_instance.to_dict()
# create an instance of FieldErrorsValue from a dict
field_errors_value_from_dict = FieldErrorsValue.from_dict(field_errors_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


