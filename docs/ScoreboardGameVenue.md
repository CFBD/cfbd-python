# ScoreboardGameVenue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**city** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from cfbd.models.scoreboard_game_venue import ScoreboardGameVenue

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreboardGameVenue from a JSON string
scoreboard_game_venue_instance = ScoreboardGameVenue.from_json(json)
# print the JSON string representation of the object
print ScoreboardGameVenue.to_json()

# convert the object into a dict
scoreboard_game_venue_dict = scoreboard_game_venue_instance.to_dict()
# create an instance of ScoreboardGameVenue from a dict
scoreboard_game_venue_from_dict = ScoreboardGameVenue.from_dict(scoreboard_game_venue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


