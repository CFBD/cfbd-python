# ScheduleWindow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**season_type** | **str** |  | 
**week** | **int** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** | Exclusive UTC bound. | 

## Example

```python
from cfbd.models.schedule_window import ScheduleWindow

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleWindow from a JSON string
schedule_window_instance = ScheduleWindow.from_json(json)
# print the JSON string representation of the object
print ScheduleWindow.to_json()

# convert the object into a dict
schedule_window_dict = schedule_window_instance.to_dict()
# create an instance of ScheduleWindow from a dict
schedule_window_from_dict = ScheduleWindow.from_dict(schedule_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


