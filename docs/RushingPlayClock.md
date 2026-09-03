# RushingPlayClock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes** | **int** |  | 
**seconds** | **int** |  | 

## Example

```python
from cfbd.models.rushing_play_clock import RushingPlayClock

# TODO update the JSON string below
json = "{}"
# create an instance of RushingPlayClock from a JSON string
rushing_play_clock_instance = RushingPlayClock.from_json(json)
# print the JSON string representation of the object
print RushingPlayClock.to_json()

# convert the object into a dict
rushing_play_clock_dict = rushing_play_clock_instance.to_dict()
# create an instance of RushingPlayClock from a dict
rushing_play_clock_from_dict = RushingPlayClock.from_dict(rushing_play_clock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


