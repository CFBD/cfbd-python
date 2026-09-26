# GameSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembled_at** | **datetime** |  | 
**selection** | **str** |  | 
**filters** | [**GameScheduleFilters**](GameScheduleFilters.md) |  | 
**window** | [**ScheduleWindow**](ScheduleWindow.md) |  | 
**following_window** | [**ScheduleWindow**](ScheduleWindow.md) |  | 
**games** | [**List[ScheduleGame]**](ScheduleGame.md) |  | 

## Example

```python
from cfbd.models.game_schedule import GameSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of GameSchedule from a JSON string
game_schedule_instance = GameSchedule.from_json(json)
# print the JSON string representation of the object
print GameSchedule.to_json()

# convert the object into a dict
game_schedule_dict = game_schedule_instance.to_dict()
# create an instance of GameSchedule from a dict
game_schedule_from_dict = GameSchedule.from_dict(game_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


