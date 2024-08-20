# AdvancedBoxScore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_info** | [**AdvancedBoxScoreGameInfo**](AdvancedBoxScoreGameInfo.md) |  | 
**teams** | [**AdvancedBoxScoreTeams**](AdvancedBoxScoreTeams.md) |  | 
**players** | [**AdvancedBoxScorePlayers**](AdvancedBoxScorePlayers.md) |  | 

## Example

```python
from cfbd.models.advanced_box_score import AdvancedBoxScore

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedBoxScore from a JSON string
advanced_box_score_instance = AdvancedBoxScore.from_json(json)
# print the JSON string representation of the object
print AdvancedBoxScore.to_json()

# convert the object into a dict
advanced_box_score_dict = advanced_box_score_instance.to_dict()
# create an instance of AdvancedBoxScore from a dict
advanced_box_score_from_dict = AdvancedBoxScore.from_dict(advanced_box_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


