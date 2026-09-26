# PreviewVenue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from cfbd.models.preview_venue import PreviewVenue

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewVenue from a JSON string
preview_venue_instance = PreviewVenue.from_json(json)
# print the JSON string representation of the object
print PreviewVenue.to_json()

# convert the object into a dict
preview_venue_dict = preview_venue_instance.to_dict()
# create an instance of PreviewVenue from a dict
preview_venue_from_dict = PreviewVenue.from_dict(preview_venue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


