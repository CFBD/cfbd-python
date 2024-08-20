# Conference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 
**abbreviation** | **str** |  | 
**classification** | [**DivisionClassification**](DivisionClassification.md) |  | 

## Example

```python
from cfbd.models.conference import Conference

# TODO update the JSON string below
json = "{}"
# create an instance of Conference from a JSON string
conference_instance = Conference.from_json(json)
# print the JSON string representation of the object
print Conference.to_json()

# convert the object into a dict
conference_dict = conference_instance.to_dict()
# create an instance of Conference from a dict
conference_from_dict = Conference.from_dict(conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


