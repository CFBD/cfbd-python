# PlayerSeasonPredictedPointsAdded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**average_ppa** | [**PlayerSeasonPredictedPointsAddedAveragePPA**](PlayerSeasonPredictedPointsAddedAveragePPA.md) |  | 
**total_ppa** | [**PlayerSeasonPredictedPointsAddedAveragePPA**](PlayerSeasonPredictedPointsAddedAveragePPA.md) |  | 

## Example

```python
from cfbd.models.player_season_predicted_points_added import PlayerSeasonPredictedPointsAdded

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonPredictedPointsAdded from a JSON string
player_season_predicted_points_added_instance = PlayerSeasonPredictedPointsAdded.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonPredictedPointsAdded.to_json()

# convert the object into a dict
player_season_predicted_points_added_dict = player_season_predicted_points_added_instance.to_dict()
# create an instance of PlayerSeasonPredictedPointsAdded from a dict
player_season_predicted_points_added_from_dict = PlayerSeasonPredictedPointsAdded.from_dict(player_season_predicted_points_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


