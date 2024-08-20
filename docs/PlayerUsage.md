# PlayerUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**usage** | [**PlayerUsageUsage**](PlayerUsageUsage.md) |  | 

## Example

```python
from cfbd.models.player_usage import PlayerUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerUsage from a JSON string
player_usage_instance = PlayerUsage.from_json(json)
# print the JSON string representation of the object
print PlayerUsage.to_json()

# convert the object into a dict
player_usage_dict = player_usage_instance.to_dict()
# create an instance of PlayerUsage from a dict
player_usage_from_dict = PlayerUsage.from_dict(player_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


