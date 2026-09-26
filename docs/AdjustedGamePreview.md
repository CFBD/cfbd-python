# AdjustedGamePreview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembled_at** | **datetime** |  | 
**game** | [**GamePreviewMetadata**](GamePreviewMetadata.md) |  | 
**availability** | **str** |  | 
**reason** | [**PreviewReason**](PreviewReason.md) |  | 
**analysis** | [**AdjustedPreviewAnalysis**](AdjustedPreviewAnalysis.md) |  | 

## Example

```python
from cfbd.models.adjusted_game_preview import AdjustedGamePreview

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedGamePreview from a JSON string
adjusted_game_preview_instance = AdjustedGamePreview.from_json(json)
# print the JSON string representation of the object
print AdjustedGamePreview.to_json()

# convert the object into a dict
adjusted_game_preview_dict = adjusted_game_preview_instance.to_dict()
# create an instance of AdjustedGamePreview from a dict
adjusted_game_preview_from_dict = AdjustedGamePreview.from_dict(adjusted_game_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


