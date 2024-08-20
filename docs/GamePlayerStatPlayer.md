# GamePlayerStatPlayer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**stat** | **str** |  | 

## Example

```python
from cfbd.models.game_player_stat_player import GamePlayerStatPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlayerStatPlayer from a JSON string
game_player_stat_player_instance = GamePlayerStatPlayer.from_json(json)
# print the JSON string representation of the object
print GamePlayerStatPlayer.to_json()

# convert the object into a dict
game_player_stat_player_dict = game_player_stat_player_instance.to_dict()
# create an instance of GamePlayerStatPlayer from a dict
game_player_stat_player_from_dict = GamePlayerStatPlayer.from_dict(game_player_stat_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


