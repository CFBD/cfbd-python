# PlayerSeasonPredictedPointsAddedAveragePPA


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passing_downs** | **float** |  | [optional] 
**standard_downs** | **float** |  | [optional] 
**third_down** | **float** |  | [optional] 
**second_down** | **float** |  | [optional] 
**first_down** | **float** |  | [optional] 
**rush** | **float** |  | [optional] 
**var_pass** | **float** |  | [optional] 
**all** | **float** |  | 

## Example

```python
from cfbd.models.player_season_predicted_points_added_average_ppa import PlayerSeasonPredictedPointsAddedAveragePPA

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonPredictedPointsAddedAveragePPA from a JSON string
player_season_predicted_points_added_average_ppa_instance = PlayerSeasonPredictedPointsAddedAveragePPA.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonPredictedPointsAddedAveragePPA.to_json()

# convert the object into a dict
player_season_predicted_points_added_average_ppa_dict = player_season_predicted_points_added_average_ppa_instance.to_dict()
# create an instance of PlayerSeasonPredictedPointsAddedAveragePPA from a dict
player_season_predicted_points_added_average_ppa_from_dict = PlayerSeasonPredictedPointsAddedAveragePPA.from_dict(player_season_predicted_points_added_average_ppa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


