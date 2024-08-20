# PollRank


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | 
**school** | **str** |  | 
**conference** | **str** |  | 
**first_place_votes** | **int** |  | 
**points** | **int** |  | 

## Example

```python
from cfbd.models.poll_rank import PollRank

# TODO update the JSON string below
json = "{}"
# create an instance of PollRank from a JSON string
poll_rank_instance = PollRank.from_json(json)
# print the JSON string representation of the object
print PollRank.to_json()

# convert the object into a dict
poll_rank_dict = poll_rank_instance.to_dict()
# create an instance of PollRank from a dict
poll_rank_from_dict = PollRank.from_dict(poll_rank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


