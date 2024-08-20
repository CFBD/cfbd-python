# TeamHavoc


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**total** | **float** |  | 
**front_seven** | **float** |  | 
**db** | **float** |  | 

## Example

```python
from cfbd.models.team_havoc import TeamHavoc

# TODO update the JSON string below
json = "{}"
# create an instance of TeamHavoc from a JSON string
team_havoc_instance = TeamHavoc.from_json(json)
# print the JSON string representation of the object
print TeamHavoc.to_json()

# convert the object into a dict
team_havoc_dict = team_havoc_instance.to_dict()
# create an instance of TeamHavoc from a dict
team_havoc_from_dict = TeamHavoc.from_dict(team_havoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


