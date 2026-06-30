# UserUsageTotals


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **float** |  | 
**cfb_requests** | **float** |  | 
**cbb_requests** | **float** |  | 
**unique_endpoints** | **float** |  | 

## Example

```python
from cfbd.models.user_usage_totals import UserUsageTotals

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageTotals from a JSON string
user_usage_totals_instance = UserUsageTotals.from_json(json)
# print the JSON string representation of the object
print UserUsageTotals.to_json()

# convert the object into a dict
user_usage_totals_dict = user_usage_totals_instance.to_dict()
# create an instance of UserUsageTotals from a dict
user_usage_totals_from_dict = UserUsageTotals.from_dict(user_usage_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


