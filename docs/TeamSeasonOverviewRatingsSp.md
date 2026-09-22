# TeamSeasonOverviewRatingsSp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_teams** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 
**defense** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 
**offense** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 
**overall** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 

## Example

```python
from cfbd.models.team_season_overview_ratings_sp import TeamSeasonOverviewRatingsSp

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewRatingsSp from a JSON string
team_season_overview_ratings_sp_instance = TeamSeasonOverviewRatingsSp.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewRatingsSp.to_json()

# convert the object into a dict
team_season_overview_ratings_sp_dict = team_season_overview_ratings_sp_instance.to_dict()
# create an instance of TeamSeasonOverviewRatingsSp from a dict
team_season_overview_ratings_sp_from_dict = TeamSeasonOverviewRatingsSp.from_dict(team_season_overview_ratings_sp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


