# PreviewSectionPreviewAdjustedTeamMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 
**assembled_at** | **datetime** |  | 
**source_updated_at** | **datetime** | Snapshot publication time, not a games-through cutoff. | 
**data** | [**PreviewAdjustedTeamMetrics**](PreviewAdjustedTeamMetrics.md) |  | 

## Example

```python
from cfbd.models.preview_section_preview_adjusted_team_metrics import PreviewSectionPreviewAdjustedTeamMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSectionPreviewAdjustedTeamMetrics from a JSON string
preview_section_preview_adjusted_team_metrics_instance = PreviewSectionPreviewAdjustedTeamMetrics.from_json(json)
# print the JSON string representation of the object
print PreviewSectionPreviewAdjustedTeamMetrics.to_json()

# convert the object into a dict
preview_section_preview_adjusted_team_metrics_dict = preview_section_preview_adjusted_team_metrics_instance.to_dict()
# create an instance of PreviewSectionPreviewAdjustedTeamMetrics from a dict
preview_section_preview_adjusted_team_metrics_from_dict = PreviewSectionPreviewAdjustedTeamMetrics.from_dict(preview_section_preview_adjusted_team_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


