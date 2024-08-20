# LiveGameDrive


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**offense_id** | **int** |  | 
**offense** | **str** |  | 
**defense_id** | **int** |  | 
**defense** | **str** |  | 
**play_count** | **int** |  | 
**yards** | **int** |  | 
**start_period** | **int** |  | 
**start_clock** | **str** |  | 
**start_yards_to_goal** | **int** |  | 
**end_period** | **int** |  | 
**end_clock** | **str** |  | 
**end_yards_to_goal** | **int** |  | 
**duration** | **str** |  | 
**scoring_opportunity** | **bool** |  | 
**result** | **str** |  | 
**points_gained** | **int** |  | 
**plays** | [**List[LiveGamePlay]**](LiveGamePlay.md) |  | 

## Example

```python
from cfbd.models.live_game_drive import LiveGameDrive

# TODO update the JSON string below
json = "{}"
# create an instance of LiveGameDrive from a JSON string
live_game_drive_instance = LiveGameDrive.from_json(json)
# print the JSON string representation of the object
print LiveGameDrive.to_json()

# convert the object into a dict
live_game_drive_dict = live_game_drive_instance.to_dict()
# create an instance of LiveGameDrive from a dict
live_game_drive_from_dict = LiveGameDrive.from_dict(live_game_drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


