# FreePreviewAnalysis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broadcasts** | [**PreviewSectionPreviewBroadcastArray**](PreviewSectionPreviewBroadcastArray.md) |  | 
**odds** | [**PreviewSectionSelectedOdds**](PreviewSectionSelectedOdds.md) |  | 
**home** | [**FreePreviewTeam**](FreePreviewTeam.md) |  | 
**away** | [**FreePreviewTeam**](FreePreviewTeam.md) |  | 
**series** | [**PreviewSectionSeriesHistory**](PreviewSectionSeriesHistory.md) |  | 

## Example

```python
from cfbd.models.free_preview_analysis import FreePreviewAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of FreePreviewAnalysis from a JSON string
free_preview_analysis_instance = FreePreviewAnalysis.from_json(json)
# print the JSON string representation of the object
print FreePreviewAnalysis.to_json()

# convert the object into a dict
free_preview_analysis_dict = free_preview_analysis_instance.to_dict()
# create an instance of FreePreviewAnalysis from a dict
free_preview_analysis_from_dict = FreePreviewAnalysis.from_dict(free_preview_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


