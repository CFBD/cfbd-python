# TeamSeasonPredictedPointsAdded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**conference** | **str** |  | 
**team** | **str** |  | 
**offense** | [**TeamSeasonPredictedPointsAddedOffense**](TeamSeasonPredictedPointsAddedOffense.md) |  | 
**defense** | [**TeamSeasonPredictedPointsAddedOffense**](TeamSeasonPredictedPointsAddedOffense.md) |  | 

## Example

```python
from cfbd.models.team_season_predicted_points_added import TeamSeasonPredictedPointsAdded

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonPredictedPointsAdded from a JSON string
team_season_predicted_points_added_instance = TeamSeasonPredictedPointsAdded.from_json(json)
# print the JSON string representation of the object
print TeamSeasonPredictedPointsAdded.to_json()

# convert the object into a dict
team_season_predicted_points_added_dict = team_season_predicted_points_added_instance.to_dict()
# create an instance of TeamSeasonPredictedPointsAdded from a dict
team_season_predicted_points_added_from_dict = TeamSeasonPredictedPointsAdded.from_dict(team_season_predicted_points_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


