# Play


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drive_id** | **str** |  | 
**game_id** | **int** |  | 
**drive_number** | **int** |  | 
**play_number** | **int** |  | 
**offense** | **str** |  | 
**offense_conference** | **str** |  | 
**offense_score** | **int** |  | 
**defense** | **str** |  | 
**home** | **str** |  | 
**away** | **str** |  | 
**defense_conference** | **str** |  | 
**defense_score** | **int** |  | 
**period** | **int** |  | 
**clock** | [**PlayClock**](PlayClock.md) |  | 
**offense_timeouts** | **int** |  | 
**defense_timeouts** | **int** |  | 
**yardline** | **int** |  | 
**yards_to_goal** | **int** |  | 
**down** | **int** |  | 
**distance** | **int** |  | 
**yards_gained** | **int** |  | 
**scoring** | **bool** |  | 
**play_type** | **str** |  | 
**play_text** | **str** |  | 
**ppa** | **float** |  | 
**wallclock** | **str** |  | 

## Example

```python
from cfbd.models.play import Play

# TODO update the JSON string below
json = "{}"
# create an instance of Play from a JSON string
play_instance = Play.from_json(json)
# print the JSON string representation of the object
print Play.to_json()

# convert the object into a dict
play_dict = play_instance.to_dict()
# create an instance of Play from a dict
play_from_dict = Play.from_dict(play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


