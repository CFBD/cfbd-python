# GamePreview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembled_at** | **datetime** |  | 
**game** | [**GamePreviewMetadata**](GamePreviewMetadata.md) |  | 
**availability** | **str** |  | 
**reason** | [**PreviewReason**](PreviewReason.md) |  | 
**analysis** | [**FreePreviewAnalysis**](FreePreviewAnalysis.md) |  | 

## Example

```python
from cfbd.models.game_preview import GamePreview

# TODO update the JSON string below
json = "{}"
# create an instance of GamePreview from a JSON string
game_preview_instance = GamePreview.from_json(json)
# print the JSON string representation of the object
print GamePreview.to_json()

# convert the object into a dict
game_preview_dict = game_preview_instance.to_dict()
# create an instance of GamePreview from a dict
game_preview_from_dict = GamePreview.from_dict(game_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


