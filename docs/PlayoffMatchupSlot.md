# PlayoffMatchupSlot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** |  | 
**seed** | **int** |  | 
**participant** | [**PlayoffTeam**](PlayoffTeam.md) |  | 
**source** | [**PlayoffMatchupSlotSource**](PlayoffMatchupSlotSource.md) |  | 

## Example

```python
from cfbd.models.playoff_matchup_slot import PlayoffMatchupSlot

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffMatchupSlot from a JSON string
playoff_matchup_slot_instance = PlayoffMatchupSlot.from_json(json)
# print the JSON string representation of the object
print PlayoffMatchupSlot.to_json()

# convert the object into a dict
playoff_matchup_slot_dict = playoff_matchup_slot_instance.to_dict()
# create an instance of PlayoffMatchupSlot from a dict
playoff_matchup_slot_from_dict = PlayoffMatchupSlot.from_dict(playoff_matchup_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


