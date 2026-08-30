# TeamPassingGame


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
**offense** | [**PassingProduction**](PassingProduction.md) |  | 
**defense** | [**PassingProduction**](PassingProduction.md) |  | 

## Example

```python
from cfbd.models.team_passing_game import TeamPassingGame

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPassingGame from a JSON string
team_passing_game_instance = TeamPassingGame.from_json(json)
# print the JSON string representation of the object
print TeamPassingGame.to_json()

# convert the object into a dict
team_passing_game_dict = team_passing_game_instance.to_dict()
# create an instance of TeamPassingGame from a dict
team_passing_game_from_dict = TeamPassingGame.from_dict(team_passing_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


