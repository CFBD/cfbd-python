# AdvancedGameStat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**team** | **str** |  | 
**opponent** | **str** |  | 
**offense** | [**AdvancedGameStatOffense**](AdvancedGameStatOffense.md) |  | 
**defense** | [**AdvancedGameStatDefense**](AdvancedGameStatDefense.md) |  | 

## Example

```python
from cfbd.models.advanced_game_stat import AdvancedGameStat

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedGameStat from a JSON string
advanced_game_stat_instance = AdvancedGameStat.from_json(json)
# print the JSON string representation of the object
print AdvancedGameStat.to_json()

# convert the object into a dict
advanced_game_stat_dict = advanced_game_stat_instance.to_dict()
# create an instance of AdvancedGameStat from a dict
advanced_game_stat_from_dict = AdvancedGameStat.from_dict(advanced_game_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


