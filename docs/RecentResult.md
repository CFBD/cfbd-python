# RecentResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**start_date** | **datetime** |  | 
**opponent** | [**RecentResultOpponent**](RecentResultOpponent.md) |  | 
**home_away** | **str** |  | 
**neutral_site** | **bool** |  | 
**venue** | [**PreviewVenue**](PreviewVenue.md) |  | 
**team_points** | **int** |  | 
**opponent_points** | **int** |  | 
**result** | **str** |  | 

## Example

```python
from cfbd.models.recent_result import RecentResult

# TODO update the JSON string below
json = "{}"
# create an instance of RecentResult from a JSON string
recent_result_instance = RecentResult.from_json(json)
# print the JSON string representation of the object
print RecentResult.to_json()

# convert the object into a dict
recent_result_dict = recent_result_instance.to_dict()
# create an instance of RecentResult from a dict
recent_result_from_dict = RecentResult.from_dict(recent_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


