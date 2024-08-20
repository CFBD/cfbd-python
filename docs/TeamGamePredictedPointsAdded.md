# TeamGamePredictedPointsAdded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**opponent** | **str** |  | 
**offense** | [**TeamGamePredictedPointsAddedOffense**](TeamGamePredictedPointsAddedOffense.md) |  | 
**defense** | [**TeamGamePredictedPointsAddedOffense**](TeamGamePredictedPointsAddedOffense.md) |  | 

## Example

```python
from cfbd.models.team_game_predicted_points_added import TeamGamePredictedPointsAdded

# TODO update the JSON string below
json = "{}"
# create an instance of TeamGamePredictedPointsAdded from a JSON string
team_game_predicted_points_added_instance = TeamGamePredictedPointsAdded.from_json(json)
# print the JSON string representation of the object
print TeamGamePredictedPointsAdded.to_json()

# convert the object into a dict
team_game_predicted_points_added_dict = team_game_predicted_points_added_instance.to_dict()
# create an instance of TeamGamePredictedPointsAdded from a dict
team_game_predicted_points_added_from_dict = TeamGamePredictedPointsAdded.from_dict(team_game_predicted_points_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


