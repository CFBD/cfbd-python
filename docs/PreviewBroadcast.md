# PreviewBroadcast


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | [**MediaType**](MediaType.md) |  | 
**outlet** | **str** |  | 

## Example

```python
from cfbd.models.preview_broadcast import PreviewBroadcast

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewBroadcast from a JSON string
preview_broadcast_instance = PreviewBroadcast.from_json(json)
# print the JSON string representation of the object
print PreviewBroadcast.to_json()

# convert the object into a dict
preview_broadcast_dict = preview_broadcast_instance.to_dict()
# create an instance of PreviewBroadcast from a dict
preview_broadcast_from_dict = PreviewBroadcast.from_dict(preview_broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


