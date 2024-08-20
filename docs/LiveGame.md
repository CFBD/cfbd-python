# LiveGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | **str** |  | 
**period** | **int** |  | 
**clock** | **str** |  | 
**possession** | **str** |  | 
**down** | **int** |  | 
**distance** | **int** |  | 
**yards_to_goal** | **int** |  | 
**teams** | [**List[LiveGameTeam]**](LiveGameTeam.md) |  | 
**drives** | [**List[LiveGameDrive]**](LiveGameDrive.md) |  | 

## Example

```python
from cfbd.models.live_game import LiveGame

# TODO update the JSON string below
json = "{}"
# create an instance of LiveGame from a JSON string
live_game_instance = LiveGame.from_json(json)
# print the JSON string representation of the object
print LiveGame.to_json()

# convert the object into a dict
live_game_dict = live_game_instance.to_dict()
# create an instance of LiveGame from a dict
live_game_from_dict = LiveGame.from_dict(live_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


