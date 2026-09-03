# PlayerRushingGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int** |  | 
**rushing_yards_available** | **int** |  | 
**total_rushing_yards** | **int** |  | 
**yards_per_carry** | **float** |  | 
**individual_attempts** | **int** |  | 
**unattributed_attempts** | **int** |  | 
**sacks** | **int** |  | 
**kneels** | **int** |  | 
**team_rushes** | **int** |  | 
**multi_carrier_attempts** | **int** |  | 
**direction_eligible_attempts** | **int** |  | 
**direction_available_attempts** | **int** |  | 
**success_rate** | **float** |  | 
**ppa** | **float** |  | 
**total_ppa** | **float** |  | 
**line_yards** | **float** |  | 
**line_yards_total** | **float** |  | 
**second_level_yards** | **float** |  | 
**second_level_yards_total** | **float** |  | 
**open_field_yards** | **float** |  | 
**open_field_yards_total** | **float** |  | 
**stuff_rate** | **float** |  | 
**power_success** | **float** |  | 
**explosiveness** | **float** |  | 
**directions** | [**PlayerRushingSeasonDirections**](PlayerRushingSeasonDirections.md) |  | 
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
from cfbd.models.player_rushing_game import PlayerRushingGame

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRushingGame from a JSON string
player_rushing_game_instance = PlayerRushingGame.from_json(json)
# print the JSON string representation of the object
print PlayerRushingGame.to_json()

# convert the object into a dict
player_rushing_game_dict = player_rushing_game_instance.to_dict()
# create an instance of PlayerRushingGame from a dict
player_rushing_game_from_dict = PlayerRushingGame.from_dict(player_rushing_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


