# UserUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window** | [**UserUsageWindow**](UserUsageWindow.md) |  | 
**api** | [**UserUsageApi**](UserUsageApi.md) |  | 
**totals** | [**UserUsageTotals**](UserUsageTotals.md) |  | 
**top_endpoints** | [**List[UserUsageEndpoint]**](UserUsageEndpoint.md) |  | 
**recent_requests** | [**List[UserUsageRecentRequest]**](UserUsageRecentRequest.md) |  | 

## Example

```python
from cfbd.models.user_usage import UserUsage

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsage from a JSON string
user_usage_instance = UserUsage.from_json(json)
# print the JSON string representation of the object
print UserUsage.to_json()

# convert the object into a dict
user_usage_dict = user_usage_instance.to_dict()
# create an instance of UserUsage from a dict
user_usage_from_dict = UserUsage.from_dict(user_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


