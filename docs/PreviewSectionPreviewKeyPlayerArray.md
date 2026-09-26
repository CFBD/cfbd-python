# PreviewSectionPreviewKeyPlayerArray


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 
**assembled_at** | **datetime** |  | 
**source_updated_at** | **datetime** | Snapshot publication time, not a games-through cutoff. | 
**data** | [**List[PreviewKeyPlayer]**](PreviewKeyPlayer.md) |  | 

## Example

```python
from cfbd.models.preview_section_preview_key_player_array import PreviewSectionPreviewKeyPlayerArray

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSectionPreviewKeyPlayerArray from a JSON string
preview_section_preview_key_player_array_instance = PreviewSectionPreviewKeyPlayerArray.from_json(json)
# print the JSON string representation of the object
print PreviewSectionPreviewKeyPlayerArray.to_json()

# convert the object into a dict
preview_section_preview_key_player_array_dict = preview_section_preview_key_player_array_instance.to_dict()
# create an instance of PreviewSectionPreviewKeyPlayerArray from a dict
preview_section_preview_key_player_array_from_dict = PreviewSectionPreviewKeyPlayerArray.from_dict(preview_section_preview_key_player_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


