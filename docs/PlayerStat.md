# PlayerStat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**player_id** | **str** |  | 
**player** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**category** | **str** |  | 
**stat_type** | **str** |  | 
**stat** | **str** |  | 

## Example

```python
from cfbd.models.player_stat import PlayerStat

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStat from a JSON string
player_stat_instance = PlayerStat.from_json(json)
# print the JSON string representation of the object
print PlayerStat.to_json()

# convert the object into a dict
player_stat_dict = player_stat_instance.to_dict()
# create an instance of PlayerStat from a dict
player_stat_from_dict = PlayerStat.from_dict(player_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


