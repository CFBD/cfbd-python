# PreviewSectionSeriesHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 
**assembled_at** | **datetime** |  | 
**source_updated_at** | **datetime** | Snapshot publication time, not a games-through cutoff. | 
**data** | [**SeriesHistory**](SeriesHistory.md) |  | 

## Example

```python
from cfbd.models.preview_section_series_history import PreviewSectionSeriesHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSectionSeriesHistory from a JSON string
preview_section_series_history_instance = PreviewSectionSeriesHistory.from_json(json)
# print the JSON string representation of the object
print PreviewSectionSeriesHistory.to_json()

# convert the object into a dict
preview_section_series_history_dict = preview_section_series_history_instance.to_dict()
# create an instance of PreviewSectionSeriesHistory from a dict
preview_section_series_history_from_dict = PreviewSectionSeriesHistory.from_dict(preview_section_series_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


