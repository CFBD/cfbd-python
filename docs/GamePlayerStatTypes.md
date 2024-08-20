# GamePlayerStatTypes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**athletes** | [**List[GamePlayerStatPlayer]**](GamePlayerStatPlayer.md) |  | 

## Example

```python
from cfbd.models.game_player_stat_types import GamePlayerStatTypes

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlayerStatTypes from a JSON string
game_player_stat_types_instance = GamePlayerStatTypes.from_json(json)
# print the JSON string representation of the object
print GamePlayerStatTypes.to_json()

# convert the object into a dict
game_player_stat_types_dict = game_player_stat_types_instance.to_dict()
# create an instance of GamePlayerStatTypes from a dict
game_player_stat_types_from_dict = GamePlayerStatTypes.from_dict(game_player_stat_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


