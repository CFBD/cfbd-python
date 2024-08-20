# GameWeather


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**start_time** | **datetime** |  | 
**game_indoors** | **bool** |  | 
**home_team** | **str** |  | 
**home_conference** | **str** |  | 
**away_team** | **str** |  | 
**away_conference** | **str** |  | 
**venue_id** | **int** |  | 
**venue** | **str** |  | 
**temperature** | **float** |  | 
**dew_point** | **float** |  | 
**humidity** | **float** |  | 
**precipitation** | **float** |  | 
**snowfall** | **float** |  | 
**wind_direction** | **float** |  | 
**wind_speed** | **float** |  | 
**pressure** | **float** |  | 
**weather_condition_code** | **float** |  | 
**weather_condition** | **str** |  | 

## Example

```python
from cfbd.models.game_weather import GameWeather

# TODO update the JSON string below
json = "{}"
# create an instance of GameWeather from a JSON string
game_weather_instance = GameWeather.from_json(json)
# print the JSON string representation of the object
print GameWeather.to_json()

# convert the object into a dict
game_weather_dict = game_weather_instance.to_dict()
# create an instance of GameWeather from a dict
game_weather_from_dict = GameWeather.from_dict(game_weather_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


