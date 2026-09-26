# PreviewSectionTeamSeasonOverviewAtRatings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 
**assembled_at** | **datetime** |  | 
**source_updated_at** | **datetime** | Snapshot publication time, not a games-through cutoff. | 
**data** | [**PreviewSectionTeamSeasonOverviewAtRatingsData**](PreviewSectionTeamSeasonOverviewAtRatingsData.md) |  | 

## Example

```python
from cfbd.models.preview_section_team_season_overview_at_ratings import PreviewSectionTeamSeasonOverviewAtRatings

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSectionTeamSeasonOverviewAtRatings from a JSON string
preview_section_team_season_overview_at_ratings_instance = PreviewSectionTeamSeasonOverviewAtRatings.from_json(json)
# print the JSON string representation of the object
print PreviewSectionTeamSeasonOverviewAtRatings.to_json()

# convert the object into a dict
preview_section_team_season_overview_at_ratings_dict = preview_section_team_season_overview_at_ratings_instance.to_dict()
# create an instance of PreviewSectionTeamSeasonOverviewAtRatings from a dict
preview_section_team_season_overview_at_ratings_from_dict = PreviewSectionTeamSeasonOverviewAtRatings.from_dict(preview_section_team_season_overview_at_ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


