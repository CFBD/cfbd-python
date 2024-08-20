# Poll


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll** | **str** |  | 
**ranks** | [**List[PollRank]**](PollRank.md) |  | 

## Example

```python
from cfbd.models.poll import Poll

# TODO update the JSON string below
json = "{}"
# create an instance of Poll from a JSON string
poll_instance = Poll.from_json(json)
# print the JSON string representation of the object
print Poll.to_json()

# convert the object into a dict
poll_dict = poll_instance.to_dict()
# create an instance of Poll from a dict
poll_from_dict = Poll.from_dict(poll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


