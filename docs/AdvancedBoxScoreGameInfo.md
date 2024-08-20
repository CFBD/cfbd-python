# AdvancedBoxScoreGameInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excitement** | **float** |  | 
**home_winner** | **bool** |  | 
**away_win_prob** | **float** |  | 
**away_points** | **int** |  | 
**away_team** | **str** |  | 
**home_win_prob** | **float** |  | 
**home_points** | **int** |  | 
**home_team** | **str** |  | 

## Example

```python
from cfbd.models.advanced_box_score_game_info import AdvancedBoxScoreGameInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedBoxScoreGameInfo from a JSON string
advanced_box_score_game_info_instance = AdvancedBoxScoreGameInfo.from_json(json)
# print the JSON string representation of the object
print AdvancedBoxScoreGameInfo.to_json()

# convert the object into a dict
advanced_box_score_game_info_dict = advanced_box_score_game_info_instance.to_dict()
# create an instance of AdvancedBoxScoreGameInfo from a dict
advanced_box_score_game_info_from_dict = AdvancedBoxScoreGameInfo.from_dict(advanced_box_score_game_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


