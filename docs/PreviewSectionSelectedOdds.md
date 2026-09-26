# PreviewSectionSelectedOdds


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 
**assembled_at** | **datetime** |  | 
**source_updated_at** | **datetime** | Snapshot publication time, not a games-through cutoff. | 
**data** | [**SelectedOdds**](SelectedOdds.md) |  | 

## Example

```python
from cfbd.models.preview_section_selected_odds import PreviewSectionSelectedOdds

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSectionSelectedOdds from a JSON string
preview_section_selected_odds_instance = PreviewSectionSelectedOdds.from_json(json)
# print the JSON string representation of the object
print PreviewSectionSelectedOdds.to_json()

# convert the object into a dict
preview_section_selected_odds_dict = preview_section_selected_odds_instance.to_dict()
# create an instance of PreviewSectionSelectedOdds from a dict
preview_section_selected_odds_from_dict = PreviewSectionSelectedOdds.from_dict(preview_section_selected_odds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


