# PlayClock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** |  | 
**minutes** | **int** |  | 

## Example

```python
from cfbd.models.play_clock import PlayClock

# TODO update the JSON string below
json = "{}"
# create an instance of PlayClock from a JSON string
play_clock_instance = PlayClock.from_json(json)
# print the JSON string representation of the object
print PlayClock.to_json()

# convert the object into a dict
play_clock_dict = play_clock_instance.to_dict()
# create an instance of PlayClock from a dict
play_clock_from_dict = PlayClock.from_dict(play_clock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


