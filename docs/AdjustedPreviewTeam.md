# AdjustedPreviewTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**season** | **int** |  | 
**team_metrics** | [**PreviewSectionPreviewAdjustedTeamMetrics**](PreviewSectionPreviewAdjustedTeamMetrics.md) |  | 
**passing** | [**PreviewSectionPreviewPlayerWepaArray**](PreviewSectionPreviewPlayerWepaArray.md) |  | 
**rushing** | [**PreviewSectionPreviewPlayerWepaArray**](PreviewSectionPreviewPlayerWepaArray.md) |  | 
**kicking** | [**PreviewSectionPreviewKickerPaarArray**](PreviewSectionPreviewKickerPaarArray.md) |  | 

## Example

```python
from cfbd.models.adjusted_preview_team import AdjustedPreviewTeam

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedPreviewTeam from a JSON string
adjusted_preview_team_instance = AdjustedPreviewTeam.from_json(json)
# print the JSON string representation of the object
print AdjustedPreviewTeam.to_json()

# convert the object into a dict
adjusted_preview_team_dict = adjusted_preview_team_instance.to_dict()
# create an instance of AdjustedPreviewTeam from a dict
adjusted_preview_team_from_dict = AdjustedPreviewTeam.from_dict(adjusted_preview_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


