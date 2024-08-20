# PlayerGameUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**quarter1** | **float** |  | 
**quarter2** | **float** |  | 
**quarter3** | **float** |  | 
**quarter4** | **float** |  | 
**rushing** | **float** |  | 
**passing** | **float** |  | 
**player** | **str** |  | 
**team** | **str** |  | 
**position** | **str** |  | 

## Example

```python
from cfbd.models.player_game_usage import PlayerGameUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerGameUsage from a JSON string
player_game_usage_instance = PlayerGameUsage.from_json(json)
# print the JSON string representation of the object
print PlayerGameUsage.to_json()

# convert the object into a dict
player_game_usage_dict = player_game_usage_instance.to_dict()
# create an instance of PlayerGameUsage from a dict
player_game_usage_from_dict = PlayerGameUsage.from_dict(player_game_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


