# Game


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**start_date** | **datetime** |  | 
**start_time_tbd** | **bool** |  | 
**completed** | **bool** |  | 
**neutral_site** | **bool** |  | 
**conference_game** | **bool** |  | 
**attendance** | **int** |  | 
**venue_id** | **int** |  | 
**venue** | **str** |  | 
**home_id** | **int** |  | 
**home_team** | **str** |  | 
**home_conference** | **str** |  | 
**home_classification** | [**DivisionClassification**](DivisionClassification.md) |  | 
**home_points** | **int** |  | 
**home_line_scores** | **List[float]** |  | 
**home_postgame_win_probability** | **float** |  | 
**home_pregame_elo** | **int** |  | 
**home_postgame_elo** | **int** |  | 
**away_id** | **int** |  | 
**away_team** | **str** |  | 
**away_conference** | **str** |  | 
**away_classification** | [**DivisionClassification**](DivisionClassification.md) |  | 
**away_points** | **int** |  | 
**away_line_scores** | **List[float]** |  | 
**away_postgame_win_probability** | **float** |  | 
**away_pregame_elo** | **int** |  | 
**away_postgame_elo** | **int** |  | 
**excitement_index** | **float** |  | 
**highlights** | **str** |  | 
**notes** | **str** |  | 

## Example

```python
from cfbd.models.game import Game

# TODO update the JSON string below
json = "{}"
# create an instance of Game from a JSON string
game_instance = Game.from_json(json)
# print the JSON string representation of the object
print Game.to_json()

# convert the object into a dict
game_dict = game_instance.to_dict()
# create an instance of Game from a dict
game_from_dict = Game.from_dict(game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


