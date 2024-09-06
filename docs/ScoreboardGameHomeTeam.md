# ScoreboardGameHomeTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_scores** | **List[int]** |  | 
**points** | **int** |  | 
**classification** | [**DivisionClassification**](DivisionClassification.md) |  | 
**conference** | **str** |  | 
**name** | **str** |  | 
**id** | **int** |  | 

## Example

```python
from cfbd.models.scoreboard_game_home_team import ScoreboardGameHomeTeam

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreboardGameHomeTeam from a JSON string
scoreboard_game_home_team_instance = ScoreboardGameHomeTeam.from_json(json)
# print the JSON string representation of the object
print ScoreboardGameHomeTeam.to_json()

# convert the object into a dict
scoreboard_game_home_team_dict = scoreboard_game_home_team_instance.to_dict()
# create an instance of ScoreboardGameHomeTeam from a dict
scoreboard_game_home_team_from_dict = ScoreboardGameHomeTeam.from_dict(scoreboard_game_home_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


