# FieldGoalEP


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yards_to_goal** | **int** |  | 
**distance** | **int** |  | 
**expected_points** | **float** |  | 

## Example

```python
from cfbd.models.field_goal_ep import FieldGoalEP

# TODO update the JSON string below
json = "{}"
# create an instance of FieldGoalEP from a JSON string
field_goal_ep_instance = FieldGoalEP.from_json(json)
# print the JSON string representation of the object
print FieldGoalEP.to_json()

# convert the object into a dict
field_goal_ep_dict = field_goal_ep_instance.to_dict()
# create an instance of FieldGoalEP from a dict
field_goal_ep_from_dict = FieldGoalEP.from_dict(field_goal_ep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


