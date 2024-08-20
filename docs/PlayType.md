# PlayType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**text** | **str** |  | 
**abbreviation** | **str** |  | 

## Example

```python
from cfbd.models.play_type import PlayType

# TODO update the JSON string below
json = "{}"
# create an instance of PlayType from a JSON string
play_type_instance = PlayType.from_json(json)
# print the JSON string representation of the object
print PlayType.to_json()

# convert the object into a dict
play_type_dict = play_type_instance.to_dict()
# create an instance of PlayType from a dict
play_type_from_dict = PlayType.from_dict(play_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


