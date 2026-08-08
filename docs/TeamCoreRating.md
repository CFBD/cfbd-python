# TeamCoreRating


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**through_season_type** | [**CoreRatingSeasonType**](CoreRatingSeasonType.md) |  | 
**through_week** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**overall** | **float** | Offense-minus-defense composite; higher is better. | 
**offense** | **float** | Points created above average per 100 qualifying plays; higher is better. | 
**defense** | **float** | Points allowed above average per 100 qualifying plays; lower is better. | 
**offense_plays** | **int** |  | 
**defense_plays** | **int** |  | 
**model_version** | **str** |  | 

## Example

```python
from cfbd.models.team_core_rating import TeamCoreRating

# TODO update the JSON string below
json = "{}"
# create an instance of TeamCoreRating from a JSON string
team_core_rating_instance = TeamCoreRating.from_json(json)
# print the JSON string representation of the object
print TeamCoreRating.to_json()

# convert the object into a dict
team_core_rating_dict = team_core_rating_instance.to_dict()
# create an instance of TeamCoreRating from a dict
team_core_rating_from_dict = TeamCoreRating.from_dict(team_core_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


