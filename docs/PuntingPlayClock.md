# PuntingPlayClock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes** | **int** |  | 
**seconds** | **int** |  | 

## Example

```python
from cfbd.models.punting_play_clock import PuntingPlayClock

# TODO update the JSON string below
json = "{}"
# create an instance of PuntingPlayClock from a JSON string
punting_play_clock_instance = PuntingPlayClock.from_json(json)
# print the JSON string representation of the object
print PuntingPlayClock.to_json()

# convert the object into a dict
punting_play_clock_dict = punting_play_clock_instance.to_dict()
# create an instance of PuntingPlayClock from a dict
punting_play_clock_from_dict = PuntingPlayClock.from_dict(punting_play_clock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


