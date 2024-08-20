# PlayerUsageUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passing_downs** | **float** |  | 
**standard_downs** | **float** |  | 
**third_down** | **float** |  | 
**second_down** | **float** |  | 
**first_down** | **float** |  | 
**rush** | **float** |  | 
**var_pass** | **float** |  | 
**overall** | **float** |  | 

## Example

```python
from cfbd.models.player_usage_usage import PlayerUsageUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerUsageUsage from a JSON string
player_usage_usage_instance = PlayerUsageUsage.from_json(json)
# print the JSON string representation of the object
print PlayerUsageUsage.to_json()

# convert the object into a dict
player_usage_usage_dict = player_usage_usage_instance.to_dict()
# create an instance of PlayerUsageUsage from a dict
player_usage_usage_from_dict = PlayerUsageUsage.from_dict(player_usage_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


