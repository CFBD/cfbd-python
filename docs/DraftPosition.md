# DraftPosition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**abbreviation** | **str** |  | 

## Example

```python
from cfbd.models.draft_position import DraftPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPosition from a JSON string
draft_position_instance = DraftPosition.from_json(json)
# print the JSON string representation of the object
print DraftPosition.to_json()

# convert the object into a dict
draft_position_dict = draft_position_instance.to_dict()
# create an instance of DraftPosition from a dict
draft_position_from_dict = DraftPosition.from_dict(draft_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


