# PlayoffLinkedGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**start_date** | **datetime** |  | 
**completed** | **bool** |  | 
**home_team** | [**PlayoffTeam**](PlayoffTeam.md) |  | 
**home_points** | **int** |  | 
**away_team** | [**PlayoffTeam**](PlayoffTeam.md) |  | 
**away_points** | **int** |  | 
**venue_id** | **int** |  | 
**venue** | **str** |  | 

## Example

```python
from cfbd.models.playoff_linked_game import PlayoffLinkedGame

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffLinkedGame from a JSON string
playoff_linked_game_instance = PlayoffLinkedGame.from_json(json)
# print the JSON string representation of the object
print PlayoffLinkedGame.to_json()

# convert the object into a dict
playoff_linked_game_dict = playoff_linked_game_instance.to_dict()
# create an instance of PlayoffLinkedGame from a dict
playoff_linked_game_from_dict = PlayoffLinkedGame.from_dict(playoff_linked_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


