# AdvancedBoxScorePlayers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ppa** | [**List[PlayerPPA]**](PlayerPPA.md) |  | 
**usage** | [**List[PlayerGameUsage]**](PlayerGameUsage.md) |  | 

## Example

```python
from cfbd.models.advanced_box_score_players import AdvancedBoxScorePlayers

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedBoxScorePlayers from a JSON string
advanced_box_score_players_instance = AdvancedBoxScorePlayers.from_json(json)
# print the JSON string representation of the object
print AdvancedBoxScorePlayers.to_json()

# convert the object into a dict
advanced_box_score_players_dict = advanced_box_score_players_instance.to_dict()
# create an instance of AdvancedBoxScorePlayers from a dict
advanced_box_score_players_from_dict = AdvancedBoxScorePlayers.from_dict(advanced_box_score_players_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


