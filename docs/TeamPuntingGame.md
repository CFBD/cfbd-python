# TeamPuntingGame


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
**punting** | [**TeamPuntingProduction**](TeamPuntingProduction.md) |  | 
**returning** | [**TeamPuntingProduction**](TeamPuntingProduction.md) |  | 

## Example

```python
from cfbd.models.team_punting_game import TeamPuntingGame

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPuntingGame from a JSON string
team_punting_game_instance = TeamPuntingGame.from_json(json)
# print the JSON string representation of the object
print TeamPuntingGame.to_json()

# convert the object into a dict
team_punting_game_dict = team_punting_game_instance.to_dict()
# create an instance of TeamPuntingGame from a dict
team_punting_game_from_dict = TeamPuntingGame.from_dict(team_punting_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


