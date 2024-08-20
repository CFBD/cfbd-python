# LiveGameTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**team** | **str** |  | 
**home_away** | **str** |  | 
**line_scores** | **List[int]** |  | 
**points** | **int** |  | 
**drives** | **int** |  | 
**scoring_opportunities** | **int** |  | 
**points_per_opportunity** | **float** |  | 
**plays** | **int** |  | 
**line_yards** | **float** |  | 
**line_yards_per_rush** | **float** |  | 
**second_level_yards** | **float** |  | 
**second_level_yards_per_rush** | **float** |  | 
**open_field_yards** | **float** |  | 
**open_field_yards_per_rush** | **float** |  | 
**epa_per_play** | **float** |  | 
**total_epa** | **float** |  | 
**passing_epa** | **float** |  | 
**epa_per_pass** | **float** |  | 
**rushing_epa** | **float** |  | 
**epa_per_rush** | **float** |  | 
**success_rate** | **float** |  | 
**standard_down_success_rate** | **float** |  | 
**passing_down_success_rate** | **float** |  | 
**explosiveness** | **float** |  | 

## Example

```python
from cfbd.models.live_game_team import LiveGameTeam

# TODO update the JSON string below
json = "{}"
# create an instance of LiveGameTeam from a JSON string
live_game_team_instance = LiveGameTeam.from_json(json)
# print the JSON string representation of the object
print LiveGameTeam.to_json()

# convert the object into a dict
live_game_team_dict = live_game_team_instance.to_dict()
# create an instance of LiveGameTeam from a dict
live_game_team_from_dict = LiveGameTeam.from_dict(live_game_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


