# CalendarWeek


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**first_game_start** | **datetime** |  | 
**last_game_start** | **datetime** |  | 

## Example

```python
from cfbd.models.calendar_week import CalendarWeek

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarWeek from a JSON string
calendar_week_instance = CalendarWeek.from_json(json)
# print the JSON string representation of the object
print CalendarWeek.to_json()

# convert the object into a dict
calendar_week_dict = calendar_week_instance.to_dict()
# create an instance of CalendarWeek from a dict
calendar_week_from_dict = CalendarWeek.from_dict(calendar_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


