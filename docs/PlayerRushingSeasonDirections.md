# PlayerRushingSeasonDirections


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown** | [**RushingDirectionProduction**](RushingDirectionProduction.md) |  | 
**right** | [**RushingDirectionProduction**](RushingDirectionProduction.md) |  | 
**middle** | [**RushingDirectionProduction**](RushingDirectionProduction.md) |  | 
**left** | [**RushingDirectionProduction**](RushingDirectionProduction.md) |  | 

## Example

```python
from cfbd.models.player_rushing_season_directions import PlayerRushingSeasonDirections

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRushingSeasonDirections from a JSON string
player_rushing_season_directions_instance = PlayerRushingSeasonDirections.from_json(json)
# print the JSON string representation of the object
print PlayerRushingSeasonDirections.to_json()

# convert the object into a dict
player_rushing_season_directions_dict = player_rushing_season_directions_instance.to_dict()
# create an instance of PlayerRushingSeasonDirections from a dict
player_rushing_season_directions_from_dict = PlayerRushingSeasonDirections.from_dict(player_rushing_season_directions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


