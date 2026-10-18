# PlayerPuntingProduction

Production on punts kicked by a player.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**punts** | **int** |  | 
**punt_yards_available** | **int** | Punts with known gross yards. | 
**punt_yards** | **int** |  | 
**yards_per_punt** | **float** |  | 
**longest_punt** | **int** |  | 
**punts50_plus** | **int** |  | 
**net_punt_yards_available** | **int** | Punts with known net yards. | 
**net_punt_yards** | **int** |  | 
**net_yards_per_punt** | **float** |  | 
**touchbacks** | **int** |  | 
**fair_catches** | **int** |  | 
**out_of_bounds** | **int** |  | 
**downed** | **int** |  | 
**inside20** | **int** | Punts after which the receiving team took possession inside its own 20, excluding touchbacks. | 
**blocked** | **int** |  | 

## Example

```python
from cfbd.models.player_punting_production import PlayerPuntingProduction

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPuntingProduction from a JSON string
player_punting_production_instance = PlayerPuntingProduction.from_json(json)
# print the JSON string representation of the object
print PlayerPuntingProduction.to_json()

# convert the object into a dict
player_punting_production_dict = player_punting_production_instance.to_dict()
# create an instance of PlayerPuntingProduction from a dict
player_punting_production_from_dict = PlayerPuntingProduction.from_dict(player_punting_production_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


