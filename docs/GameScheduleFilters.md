# GameScheduleFilters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | **str** |  | 
**classification** | **str** |  | 

## Example

```python
from cfbd.models.game_schedule_filters import GameScheduleFilters

# TODO update the JSON string below
json = "{}"
# create an instance of GameScheduleFilters from a JSON string
game_schedule_filters_instance = GameScheduleFilters.from_json(json)
# print the JSON string representation of the object
print GameScheduleFilters.to_json()

# convert the object into a dict
game_schedule_filters_dict = game_schedule_filters_instance.to_dict()
# create an instance of GameScheduleFilters from a dict
game_schedule_filters_from_dict = GameScheduleFilters.from_dict(game_schedule_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


