# PlayerGamePredictedPointsAdded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**opponent** | **str** |  | 
**average_ppa** | [**PlayerGamePredictedPointsAddedAveragePPA**](PlayerGamePredictedPointsAddedAveragePPA.md) |  | 

## Example

```python
from cfbd.models.player_game_predicted_points_added import PlayerGamePredictedPointsAdded

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerGamePredictedPointsAdded from a JSON string
player_game_predicted_points_added_instance = PlayerGamePredictedPointsAdded.from_json(json)
# print the JSON string representation of the object
print PlayerGamePredictedPointsAdded.to_json()

# convert the object into a dict
player_game_predicted_points_added_dict = player_game_predicted_points_added_instance.to_dict()
# create an instance of PlayerGamePredictedPointsAdded from a dict
player_game_predicted_points_added_from_dict = PlayerGamePredictedPointsAdded.from_dict(player_game_predicted_points_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


