# PreviewSectionTeamSeasonOverviewAtRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 
**assembled_at** | **datetime** |  | 
**source_updated_at** | **datetime** | Snapshot publication time, not a games-through cutoff. | 
**data** | [**PreviewSectionTeamSeasonOverviewAtRecordData**](PreviewSectionTeamSeasonOverviewAtRecordData.md) |  | 

## Example

```python
from cfbd.models.preview_section_team_season_overview_at_record import PreviewSectionTeamSeasonOverviewAtRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSectionTeamSeasonOverviewAtRecord from a JSON string
preview_section_team_season_overview_at_record_instance = PreviewSectionTeamSeasonOverviewAtRecord.from_json(json)
# print the JSON string representation of the object
print PreviewSectionTeamSeasonOverviewAtRecord.to_json()

# convert the object into a dict
preview_section_team_season_overview_at_record_dict = preview_section_team_season_overview_at_record_instance.to_dict()
# create an instance of PreviewSectionTeamSeasonOverviewAtRecord from a dict
preview_section_team_season_overview_at_record_from_dict = PreviewSectionTeamSeasonOverviewAtRecord.from_dict(preview_section_team_season_overview_at_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


