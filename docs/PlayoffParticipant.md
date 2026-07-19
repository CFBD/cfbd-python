# PlayoffParticipant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**PlayoffTeam**](PlayoffTeam.md) |  | 
**committee_rank** | **int** |  | 
**seed** | **int** |  | 
**bid_type** | [**PlayoffBidType**](PlayoffBidType.md) |  | 
**qualification_reason** | **str** |  | 
**conference_champion** | **bool** |  | 
**qualifying_conference** | **str** |  | 
**first_round_bye** | **bool** |  | 
**outcome** | [**PlayoffOutcome**](PlayoffOutcome.md) |  | 
**eliminated_round** | [**PlayoffRound**](PlayoffRound.md) |  | 

## Example

```python
from cfbd.models.playoff_participant import PlayoffParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffParticipant from a JSON string
playoff_participant_instance = PlayoffParticipant.from_json(json)
# print the JSON string representation of the object
print PlayoffParticipant.to_json()

# convert the object into a dict
playoff_participant_dict = playoff_participant_instance.to_dict()
# create an instance of PlayoffParticipant from a dict
playoff_participant_from_dict = PlayoffParticipant.from_dict(playoff_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


