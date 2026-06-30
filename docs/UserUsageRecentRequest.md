# UserUsageRecentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | [**UserUsageApi**](UserUsageApi.md) |  | 
**endpoint** | **str** |  | 
**requested_at** | **str** |  | 

## Example

```python
from cfbd.models.user_usage_recent_request import UserUsageRecentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageRecentRequest from a JSON string
user_usage_recent_request_instance = UserUsageRecentRequest.from_json(json)
# print the JSON string representation of the object
print UserUsageRecentRequest.to_json()

# convert the object into a dict
user_usage_recent_request_dict = user_usage_recent_request_instance.to_dict()
# create an instance of UserUsageRecentRequest from a dict
user_usage_recent_request_from_dict = UserUsageRecentRequest.from_dict(user_usage_recent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


