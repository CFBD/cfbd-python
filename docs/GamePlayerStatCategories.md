# GamePlayerStatCategories


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**types** | [**List[GamePlayerStatTypes]**](GamePlayerStatTypes.md) |  | 

## Example

```python
from cfbd.models.game_player_stat_categories import GamePlayerStatCategories

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlayerStatCategories from a JSON string
game_player_stat_categories_instance = GamePlayerStatCategories.from_json(json)
# print the JSON string representation of the object
print GamePlayerStatCategories.to_json()

# convert the object into a dict
game_player_stat_categories_dict = game_player_stat_categories_instance.to_dict()
# create an instance of GamePlayerStatCategories from a dict
game_player_stat_categories_from_dict = GamePlayerStatCategories.from_dict(game_player_stat_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


