# PlayerPuntReturnProduction

Production on punts fielded, returned, or blocked by a player.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**returns** | **int** |  | 
**return_yards_available** | **int** | Returns with known yards. | 
**return_yards** | **int** |  | 
**yards_per_return** | **float** |  | 
**longest_return** | **int** |  | 
**returns20_plus** | **int** |  | 
**return_touchdowns** | **int** |  | 
**fair_catches** | **int** |  | 
**muffs** | **int** |  | 
**blocks** | **int** |  | 

## Example

```python
from cfbd.models.player_punt_return_production import PlayerPuntReturnProduction

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPuntReturnProduction from a JSON string
player_punt_return_production_instance = PlayerPuntReturnProduction.from_json(json)
# print the JSON string representation of the object
print PlayerPuntReturnProduction.to_json()

# convert the object into a dict
player_punt_return_production_dict = player_punt_return_production_instance.to_dict()
# create an instance of PlayerPuntReturnProduction from a dict
player_punt_return_production_from_dict = PlayerPuntReturnProduction.from_dict(player_punt_return_production_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


