# PlayWinProbability


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**play_id** | **str** |  | 
**play_text** | **str** |  | 
**home_id** | **int** |  | 
**home** | **str** |  | 
**away_id** | **int** |  | 
**away** | **str** |  | 
**spread** | **float** |  | 
**home_ball** | **bool** |  | 
**home_score** | **int** |  | 
**away_score** | **int** |  | 
**yard_line** | **int** |  | 
**down** | **int** |  | 
**distance** | **int** |  | 
**home_win_probability** | **float** |  | 
**play_number** | **int** |  | 

## Example

```python
from cfbd.models.play_win_probability import PlayWinProbability

# TODO update the JSON string below
json = "{}"
# create an instance of PlayWinProbability from a JSON string
play_win_probability_instance = PlayWinProbability.from_json(json)
# print the JSON string representation of the object
print PlayWinProbability.to_json()

# convert the object into a dict
play_win_probability_dict = play_win_probability_instance.to_dict()
# create an instance of PlayWinProbability from a dict
play_win_probability_from_dict = PlayWinProbability.from_dict(play_win_probability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


