# GetCoachTenures400Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**Dict[str, FieldErrorsValue]**](FieldErrorsValue.md) |  | 
**message** | **str** |  | 

## Example

```python
from cfbd.models.get_coach_tenures400_response import GetCoachTenures400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCoachTenures400Response from a JSON string
get_coach_tenures400_response_instance = GetCoachTenures400Response.from_json(json)
# print the JSON string representation of the object
print GetCoachTenures400Response.to_json()

# convert the object into a dict
get_coach_tenures400_response_dict = get_coach_tenures400_response_instance.to_dict()
# create an instance of GetCoachTenures400Response from a dict
get_coach_tenures400_response_from_dict = GetCoachTenures400Response.from_dict(get_coach_tenures400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


