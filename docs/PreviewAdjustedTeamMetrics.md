# PreviewAdjustedTeamMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**is_previous_season** | **bool** |  | 
**metrics** | [**AdjustedTeamMetrics**](AdjustedTeamMetrics.md) |  | 

## Example

```python
from cfbd.models.preview_adjusted_team_metrics import PreviewAdjustedTeamMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewAdjustedTeamMetrics from a JSON string
preview_adjusted_team_metrics_instance = PreviewAdjustedTeamMetrics.from_json(json)
# print the JSON string representation of the object
print PreviewAdjustedTeamMetrics.to_json()

# convert the object into a dict
preview_adjusted_team_metrics_dict = preview_adjusted_team_metrics_instance.to_dict()
# create an instance of PreviewAdjustedTeamMetrics from a dict
preview_adjusted_team_metrics_from_dict = PreviewAdjustedTeamMetrics.from_dict(preview_adjusted_team_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


