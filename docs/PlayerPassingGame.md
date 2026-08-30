# PlayerPassingGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int** |  | 
**completions** | **int** |  | 
**incompletions** | **int** |  | 
**interceptions** | **int** |  | 
**completion_rate** | **float** |  | 
**air_yards_attempts_available** | **int** | Number of attempts with non-null air yards, including zero-yard values. | 
**total_air_yards** | **int** |  | 
**average_depth_of_target** | **float** |  | 
**total_yards_attempts_available** | **int** | Number of attempts with non-null total yards, including zero-yard incompletions and interceptions. | 
**total_yards** | **int** |  | 
**yards_after_catch_attempts_available** | **int** | Number of completed attempts with valid total yards and air yards to calculate yards after catch, including zero-yard values. | 
**total_yards_after_catch** | **int** |  | 
**average_yards_after_catch** | **float** |  | 
**game_id** | **int** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**player_id** | **str** |  | 
**player** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**opponent** | **str** |  | 

## Example

```python
from cfbd.models.player_passing_game import PlayerPassingGame

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPassingGame from a JSON string
player_passing_game_instance = PlayerPassingGame.from_json(json)
# print the JSON string representation of the object
print PlayerPassingGame.to_json()

# convert the object into a dict
player_passing_game_dict = player_passing_game_instance.to_dict()
# create an instance of PlayerPassingGame from a dict
player_passing_game_from_dict = PlayerPassingGame.from_dict(player_passing_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


