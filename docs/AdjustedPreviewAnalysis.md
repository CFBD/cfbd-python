# AdjustedPreviewAnalysis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**AdjustedPreviewTeam**](AdjustedPreviewTeam.md) |  | 
**away** | [**AdjustedPreviewTeam**](AdjustedPreviewTeam.md) |  | 

## Example

```python
from cfbd.models.adjusted_preview_analysis import AdjustedPreviewAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedPreviewAnalysis from a JSON string
adjusted_preview_analysis_instance = AdjustedPreviewAnalysis.from_json(json)
# print the JSON string representation of the object
print AdjustedPreviewAnalysis.to_json()

# convert the object into a dict
adjusted_preview_analysis_dict = adjusted_preview_analysis_instance.to_dict()
# create an instance of AdjustedPreviewAnalysis from a dict
adjusted_preview_analysis_from_dict = AdjustedPreviewAnalysis.from_dict(adjusted_preview_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


