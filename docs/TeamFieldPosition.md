# TeamFieldPosition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**average_start** | **float** |  | 
**average_starting_predicted_points** | **float** |  | 

## Example

```python
from cfbd.models.team_field_position import TeamFieldPosition

# TODO update the JSON string below
json = "{}"
# create an instance of TeamFieldPosition from a JSON string
team_field_position_instance = TeamFieldPosition.from_json(json)
# print the JSON string representation of the object
print TeamFieldPosition.to_json()

# convert the object into a dict
team_field_position_dict = team_field_position_instance.to_dict()
# create an instance of TeamFieldPosition from a dict
team_field_position_from_dict = TeamFieldPosition.from_dict(team_field_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


