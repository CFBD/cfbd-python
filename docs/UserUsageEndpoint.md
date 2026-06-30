# UserUsageEndpoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | [**UserUsageApi**](UserUsageApi.md) |  | 
**endpoint** | **str** |  | 
**requests** | **float** |  | 
**last_used_at** | **str** |  | 

## Example

```python
from cfbd.models.user_usage_endpoint import UserUsageEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageEndpoint from a JSON string
user_usage_endpoint_instance = UserUsageEndpoint.from_json(json)
# print the JSON string representation of the object
print UserUsageEndpoint.to_json()

# convert the object into a dict
user_usage_endpoint_dict = user_usage_endpoint_instance.to_dict()
# create an instance of UserUsageEndpoint from a dict
user_usage_endpoint_from_dict = UserUsageEndpoint.from_dict(user_usage_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


