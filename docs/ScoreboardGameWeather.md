# ScoreboardGameWeather


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_direction** | **float** |  | 
**wind_speed** | **float** |  | 
**description** | **str** |  | 
**temperature** | **float** |  | 

## Example

```python
from cfbd.models.scoreboard_game_weather import ScoreboardGameWeather

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreboardGameWeather from a JSON string
scoreboard_game_weather_instance = ScoreboardGameWeather.from_json(json)
# print the JSON string representation of the object
print ScoreboardGameWeather.to_json()

# convert the object into a dict
scoreboard_game_weather_dict = scoreboard_game_weather_instance.to_dict()
# create an instance of ScoreboardGameWeather from a dict
scoreboard_game_weather_from_dict = ScoreboardGameWeather.from_dict(scoreboard_game_weather_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


