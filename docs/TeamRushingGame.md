# TeamRushingGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**opponent** | **str** |  | 
**offense** | [**TeamRushingProduction**](TeamRushingProduction.md) |  | 
**defense** | [**TeamRushingProduction**](TeamRushingProduction.md) |  | 

## Example

```python
from cfbd.models.team_rushing_game import TeamRushingGame

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRushingGame from a JSON string
team_rushing_game_instance = TeamRushingGame.from_json(json)
# print the JSON string representation of the object
print TeamRushingGame.to_json()

# convert the object into a dict
team_rushing_game_dict = team_rushing_game_instance.to_dict()
# create an instance of TeamRushingGame from a dict
team_rushing_game_from_dict = TeamRushingGame.from_dict(team_rushing_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


