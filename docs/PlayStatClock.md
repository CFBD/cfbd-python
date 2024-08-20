# PlayStatClock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **float** |  | 
**minutes** | **float** |  | 

## Example

```python
from cfbd.models.play_stat_clock import PlayStatClock

# TODO update the JSON string below
json = "{}"
# create an instance of PlayStatClock from a JSON string
play_stat_clock_instance = PlayStatClock.from_json(json)
# print the JSON string representation of the object
print PlayStatClock.to_json()

# convert the object into a dict
play_stat_clock_dict = play_stat_clock_instance.to_dict()
# create an instance of PlayStatClock from a dict
play_stat_clock_from_dict = PlayStatClock.from_dict(play_stat_clock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


