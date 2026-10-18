# PlayerPuntingSeason

Null when the player has no punts or returns in that role.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**player_id** | **str** |  | 
**player** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**punting** | [**PlayerPuntingProduction**](PlayerPuntingProduction.md) |  | 
**returning** | [**PlayerPuntReturnProduction**](PlayerPuntReturnProduction.md) |  | 

## Example

```python
from cfbd.models.player_punting_season import PlayerPuntingSeason

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPuntingSeason from a JSON string
player_punting_season_instance = PlayerPuntingSeason.from_json(json)
# print the JSON string representation of the object
print PlayerPuntingSeason.to_json()

# convert the object into a dict
player_punting_season_dict = player_punting_season_instance.to_dict()
# create an instance of PlayerPuntingSeason from a dict
player_punting_season_from_dict = PlayerPuntingSeason.from_dict(player_punting_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


