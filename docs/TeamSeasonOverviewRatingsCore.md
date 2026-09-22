# TeamSeasonOverviewRatingsCore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defense** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 
**offense** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 
**overall** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 

## Example

```python
from cfbd.models.team_season_overview_ratings_core import TeamSeasonOverviewRatingsCore

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewRatingsCore from a JSON string
team_season_overview_ratings_core_instance = TeamSeasonOverviewRatingsCore.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewRatingsCore.to_json()

# convert the object into a dict
team_season_overview_ratings_core_dict = team_season_overview_ratings_core_instance.to_dict()
# create an instance of TeamSeasonOverviewRatingsCore from a dict
team_season_overview_ratings_core_from_dict = TeamSeasonOverviewRatingsCore.from_dict(team_season_overview_ratings_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


