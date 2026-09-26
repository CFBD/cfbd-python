# PreviewSectionRecentResultArray


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 
**assembled_at** | **datetime** |  | 
**source_updated_at** | **datetime** | Snapshot publication time, not a games-through cutoff. | 
**data** | [**List[RecentResult]**](RecentResult.md) |  | 

## Example

```python
from cfbd.models.preview_section_recent_result_array import PreviewSectionRecentResultArray

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSectionRecentResultArray from a JSON string
preview_section_recent_result_array_instance = PreviewSectionRecentResultArray.from_json(json)
# print the JSON string representation of the object
print PreviewSectionRecentResultArray.to_json()

# convert the object into a dict
preview_section_recent_result_array_dict = preview_section_recent_result_array_instance.to_dict()
# create an instance of PreviewSectionRecentResultArray from a dict
preview_section_recent_result_array_from_dict = PreviewSectionRecentResultArray.from_dict(preview_section_recent_result_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


