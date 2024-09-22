# TeamSeasonPredictedPointsAddedOffense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cumulative** | [**AdjustedTeamMetricsEpa**](AdjustedTeamMetricsEpa.md) |  | 
**third_down** | **float** |  | 
**second_down** | **float** |  | 
**first_down** | **float** |  | 
**rushing** | **float** |  | 
**passing** | **float** |  | 
**overall** | **float** |  | 

## Example

```python
from cfbd.models.team_season_predicted_points_added_offense import TeamSeasonPredictedPointsAddedOffense

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonPredictedPointsAddedOffense from a JSON string
team_season_predicted_points_added_offense_instance = TeamSeasonPredictedPointsAddedOffense.from_json(json)
# print the JSON string representation of the object
print TeamSeasonPredictedPointsAddedOffense.to_json()

# convert the object into a dict
team_season_predicted_points_added_offense_dict = team_season_predicted_points_added_offense_instance.to_dict()
# create an instance of TeamSeasonPredictedPointsAddedOffense from a dict
team_season_predicted_points_added_offense_from_dict = TeamSeasonPredictedPointsAddedOffense.from_dict(team_season_predicted_points_added_offense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


