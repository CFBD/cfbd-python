# FreePreviewTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**season** | **int** |  | 
**record** | [**PreviewSectionTeamSeasonOverviewAtRecord**](PreviewSectionTeamSeasonOverviewAtRecord.md) |  | 
**ratings** | [**PreviewSectionTeamSeasonOverviewAtRatings**](PreviewSectionTeamSeasonOverviewAtRatings.md) |  | 
**statistics** | [**PreviewSectionPreviewTeamStatistics**](PreviewSectionPreviewTeamStatistics.md) |  | 
**key_players** | [**PreviewKeyPlayers**](PreviewKeyPlayers.md) |  | 
**recent_results** | [**PreviewSectionRecentResultArray**](PreviewSectionRecentResultArray.md) |  | 

## Example

```python
from cfbd.models.free_preview_team import FreePreviewTeam

# TODO update the JSON string below
json = "{}"
# create an instance of FreePreviewTeam from a JSON string
free_preview_team_instance = FreePreviewTeam.from_json(json)
# print the JSON string representation of the object
print FreePreviewTeam.to_json()

# convert the object into a dict
free_preview_team_dict = free_preview_team_instance.to_dict()
# create an instance of FreePreviewTeam from a dict
free_preview_team_from_dict = FreePreviewTeam.from_dict(free_preview_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


