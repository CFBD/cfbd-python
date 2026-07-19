# PlayoffMatchup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**bracket_slot** | **str** |  | 
**round** | [**PlayoffRound**](PlayoffRound.md) |  | 
**round_name** | **str** |  | 
**round_order** | **int** |  | 
**matchup_order** | **int** |  | 
**start_date** | **datetime** |  | 
**bowl_name** | **str** |  | 
**slots** | [**List[PlayoffMatchupSlot]**](PlayoffMatchupSlot.md) |  | 
**game** | [**PlayoffLinkedGame**](PlayoffLinkedGame.md) |  | 
**advances_to** | [**PlayoffAdvancement**](PlayoffAdvancement.md) |  | 

## Example

```python
from cfbd.models.playoff_matchup import PlayoffMatchup

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffMatchup from a JSON string
playoff_matchup_instance = PlayoffMatchup.from_json(json)
# print the JSON string representation of the object
print PlayoffMatchup.to_json()

# convert the object into a dict
playoff_matchup_dict = playoff_matchup_instance.to_dict()
# create an instance of PlayoffMatchup from a dict
playoff_matchup_from_dict = PlayoffMatchup.from_dict(playoff_matchup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


