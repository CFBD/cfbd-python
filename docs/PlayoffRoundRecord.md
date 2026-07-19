# PlayoffRoundRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**PlayoffRound**](PlayoffRound.md) |  | 
**name** | **str** |  | 
**order** | **int** |  | 
**matchups** | [**List[PlayoffMatchup]**](PlayoffMatchup.md) |  | 

## Example

```python
from cfbd.models.playoff_round_record import PlayoffRoundRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffRoundRecord from a JSON string
playoff_round_record_instance = PlayoffRoundRecord.from_json(json)
# print the JSON string representation of the object
print PlayoffRoundRecord.to_json()

# convert the object into a dict
playoff_round_record_dict = playoff_round_record_instance.to_dict()
# create an instance of PlayoffRoundRecord from a dict
playoff_round_record_from_dict = PlayoffRoundRecord.from_dict(playoff_round_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


