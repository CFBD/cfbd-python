# PassingPlayClock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes** | **int** |  | 
**seconds** | **int** |  | 

## Example

```python
from cfbd.models.passing_play_clock import PassingPlayClock

# TODO update the JSON string below
json = "{}"
# create an instance of PassingPlayClock from a JSON string
passing_play_clock_instance = PassingPlayClock.from_json(json)
# print the JSON string representation of the object
print PassingPlayClock.to_json()

# convert the object into a dict
passing_play_clock_dict = passing_play_clock_instance.to_dict()
# create an instance of PassingPlayClock from a dict
passing_play_clock_from_dict = PassingPlayClock.from_dict(passing_play_clock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


