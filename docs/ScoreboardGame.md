# ScoreboardGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**start_date** | **datetime** |  | 
**start_time_tbd** | **bool** |  | 
**tv** | **str** |  | 
**neutral_site** | **bool** |  | 
**conference_game** | **bool** |  | 
**status** | [**GameStatus**](GameStatus.md) |  | 
**period** | **int** |  | 
**clock** | **str** |  | 
**situation** | **str** |  | 
**possession** | **str** |  | 
**last_play** | **str** |  | 
**venue** | [**ScoreboardGameVenue**](ScoreboardGameVenue.md) |  | 
**home_team** | [**ScoreboardGameHomeTeam**](ScoreboardGameHomeTeam.md) |  | 
**away_team** | [**ScoreboardGameHomeTeam**](ScoreboardGameHomeTeam.md) |  | 
**weather** | [**ScoreboardGameWeather**](ScoreboardGameWeather.md) |  | 
**betting** | [**ScoreboardGameBetting**](ScoreboardGameBetting.md) |  | 

## Example

```python
from cfbd.models.scoreboard_game import ScoreboardGame

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreboardGame from a JSON string
scoreboard_game_instance = ScoreboardGame.from_json(json)
# print the JSON string representation of the object
print ScoreboardGame.to_json()

# convert the object into a dict
scoreboard_game_dict = scoreboard_game_instance.to_dict()
# create an instance of ScoreboardGame from a dict
scoreboard_game_from_dict = ScoreboardGame.from_dict(scoreboard_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


