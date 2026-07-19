# PlayoffMatchupSlotSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchup_id** | **int** |  | 
**bracket_slot** | **str** |  | 
**outcome** | **str** |  | 

## Example

```python
from cfbd.models.playoff_matchup_slot_source import PlayoffMatchupSlotSource

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffMatchupSlotSource from a JSON string
playoff_matchup_slot_source_instance = PlayoffMatchupSlotSource.from_json(json)
# print the JSON string representation of the object
print PlayoffMatchupSlotSource.to_json()

# convert the object into a dict
playoff_matchup_slot_source_dict = playoff_matchup_slot_source_instance.to_dict()
# create an instance of PlayoffMatchupSlotSource from a dict
playoff_matchup_slot_source_from_dict = PlayoffMatchupSlotSource.from_dict(playoff_matchup_slot_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


