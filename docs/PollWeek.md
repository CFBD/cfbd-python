# PollWeek


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**week** | **int** |  | 
**polls** | [**List[Poll]**](Poll.md) |  | 

## Example

```python
from cfbd.models.poll_week import PollWeek

# TODO update the JSON string below
json = "{}"
# create an instance of PollWeek from a JSON string
poll_week_instance = PollWeek.from_json(json)
# print the JSON string representation of the object
print PollWeek.to_json()

# convert the object into a dict
poll_week_dict = poll_week_instance.to_dict()
# create an instance of PollWeek from a dict
poll_week_from_dict = PollWeek.from_dict(poll_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


