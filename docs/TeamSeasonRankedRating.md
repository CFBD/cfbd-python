# TeamSeasonRankedRating


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **float** | Rating/efficiency rounded to two decimal places. | 
**rank** | **int** | Competition rank within the requested season and division, using unrounded values. | 

## Example

```python
from cfbd.models.team_season_ranked_rating import TeamSeasonRankedRating

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonRankedRating from a JSON string
team_season_ranked_rating_instance = TeamSeasonRankedRating.from_json(json)
# print the JSON string representation of the object
print TeamSeasonRankedRating.to_json()

# convert the object into a dict
team_season_ranked_rating_dict = team_season_ranked_rating_instance.to_dict()
# create an instance of TeamSeasonRankedRating from a dict
team_season_ranked_rating_from_dict = TeamSeasonRankedRating.from_dict(team_season_ranked_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


