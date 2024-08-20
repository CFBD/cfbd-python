# PregameWinProbability


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**week** | **int** |  | 
**game_id** | **int** |  | 
**home_team** | **str** |  | 
**away_team** | **str** |  | 
**spread** | **float** |  | 
**home_win_probability** | **float** |  | 

## Example

```python
from cfbd.models.pregame_win_probability import PregameWinProbability

# TODO update the JSON string below
json = "{}"
# create an instance of PregameWinProbability from a JSON string
pregame_win_probability_instance = PregameWinProbability.from_json(json)
# print the JSON string representation of the object
print PregameWinProbability.to_json()

# convert the object into a dict
pregame_win_probability_dict = pregame_win_probability_instance.to_dict()
# create an instance of PregameWinProbability from a dict
pregame_win_probability_from_dict = PregameWinProbability.from_dict(pregame_win_probability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


