# PlayerRushingSeason


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
**season** | **int** |  | 
**player_id** | **str** |  | 
**player** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 

## Example

```python
from cfbd.models.player_rushing_season import PlayerRushingSeason

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRushingSeason from a JSON string
player_rushing_season_instance = PlayerRushingSeason.from_json(json)
# print the JSON string representation of the object
print PlayerRushingSeason.to_json()

# convert the object into a dict
player_rushing_season_dict = player_rushing_season_instance.to_dict()
# create an instance of PlayerRushingSeason from a dict
player_rushing_season_from_dict = PlayerRushingSeason.from_dict(player_rushing_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


