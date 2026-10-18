# PlayerPuntingGame

Null when the player has no punts or returns in that role.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**player_id** | **str** |  | 
**player** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**opponent** | **str** |  | 
**punting** | [**PlayerPuntingProduction**](PlayerPuntingProduction.md) |  | 
**returning** | [**PlayerPuntReturnProduction**](PlayerPuntReturnProduction.md) |  | 

## Example

```python
from cfbd.models.player_punting_game import PlayerPuntingGame

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPuntingGame from a JSON string
player_punting_game_instance = PlayerPuntingGame.from_json(json)
# print the JSON string representation of the object
print PlayerPuntingGame.to_json()

# convert the object into a dict
player_punting_game_dict = player_punting_game_instance.to_dict()
# create an instance of PlayerPuntingGame from a dict
player_punting_game_from_dict = PlayerPuntingGame.from_dict(player_punting_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


