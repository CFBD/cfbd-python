# GamePlayoff


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competition** | [**PlayoffCompetition**](PlayoffCompetition.md) |  | 
**format** | **str** |  | 
**round** | [**PlayoffRound**](PlayoffRound.md) |  | 
**round_name** | **str** |  | 
**bracket_slot** | **str** |  | 
**home_seed** | **int** |  | 
**away_seed** | **int** |  | 
**bowl_name** | **str** |  | 

## Example

```python
from cfbd.models.game_playoff import GamePlayoff

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlayoff from a JSON string
game_playoff_instance = GamePlayoff.from_json(json)
# print the JSON string representation of the object
print GamePlayoff.to_json()

# convert the object into a dict
game_playoff_dict = game_playoff_instance.to_dict()
# create an instance of GamePlayoff from a dict
game_playoff_from_dict = GamePlayoff.from_dict(game_playoff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


