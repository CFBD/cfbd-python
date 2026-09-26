# PreviewSectionTeamSeasonOverviewAtRatingsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sp** | [**TeamSeasonOverviewRatingsSp**](TeamSeasonOverviewRatingsSp.md) |  | 
**srs** | [**TeamSeasonRankedRating**](TeamSeasonRankedRating.md) |  | 
**elo** | **float** | Latest available postgame Elo from a completed game in this season. | 
**core** | [**TeamSeasonOverviewRatingsCore**](TeamSeasonOverviewRatingsCore.md) |  | 
**fpi** | [**TeamSeasonOverviewRatingsFpi**](TeamSeasonOverviewRatingsFpi.md) |  | 

## Example

```python
from cfbd.models.preview_section_team_season_overview_at_ratings_data import PreviewSectionTeamSeasonOverviewAtRatingsData

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSectionTeamSeasonOverviewAtRatingsData from a JSON string
preview_section_team_season_overview_at_ratings_data_instance = PreviewSectionTeamSeasonOverviewAtRatingsData.from_json(json)
# print the JSON string representation of the object
print PreviewSectionTeamSeasonOverviewAtRatingsData.to_json()

# convert the object into a dict
preview_section_team_season_overview_at_ratings_data_dict = preview_section_team_season_overview_at_ratings_data_instance.to_dict()
# create an instance of PreviewSectionTeamSeasonOverviewAtRatingsData from a dict
preview_section_team_season_overview_at_ratings_data_from_dict = PreviewSectionTeamSeasonOverviewAtRatingsData.from_dict(preview_section_team_season_overview_at_ratings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


