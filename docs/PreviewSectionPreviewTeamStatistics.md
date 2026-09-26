# PreviewSectionPreviewTeamStatistics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 
**assembled_at** | **datetime** |  | 
**source_updated_at** | **datetime** | Snapshot publication time, not a games-through cutoff. | 
**data** | [**PreviewTeamStatistics**](PreviewTeamStatistics.md) |  | 

## Example

```python
from cfbd.models.preview_section_preview_team_statistics import PreviewSectionPreviewTeamStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSectionPreviewTeamStatistics from a JSON string
preview_section_preview_team_statistics_instance = PreviewSectionPreviewTeamStatistics.from_json(json)
# print the JSON string representation of the object
print PreviewSectionPreviewTeamStatistics.to_json()

# convert the object into a dict
preview_section_preview_team_statistics_dict = preview_section_preview_team_statistics_instance.to_dict()
# create an instance of PreviewSectionPreviewTeamStatistics from a dict
preview_section_preview_team_statistics_from_dict = PreviewSectionPreviewTeamStatistics.from_dict(preview_section_preview_team_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


