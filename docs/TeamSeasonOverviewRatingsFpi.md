# TeamSeasonOverviewRatingsFpi

FPI efficiencies (higher is better for all four), not the FPI points rating.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_teams** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 
**defense** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 
**offense** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 
**overall** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 

## Example

```python
from cfbd.models.team_season_overview_ratings_fpi import TeamSeasonOverviewRatingsFpi

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewRatingsFpi from a JSON string
team_season_overview_ratings_fpi_instance = TeamSeasonOverviewRatingsFpi.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewRatingsFpi.to_json()

# convert the object into a dict
team_season_overview_ratings_fpi_dict = team_season_overview_ratings_fpi_instance.to_dict()
# create an instance of TeamSeasonOverviewRatingsFpi from a dict
team_season_overview_ratings_fpi_from_dict = TeamSeasonOverviewRatingsFpi.from_dict(team_season_overview_ratings_fpi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


