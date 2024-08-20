# DraftPickHometownInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**county_fips** | **str** |  | 
**longitude** | **str** |  | 
**latitude** | **str** |  | 
**country** | **str** |  | 
**state** | **str** |  | 
**city** | **str** |  | 

## Example

```python
from cfbd.models.draft_pick_hometown_info import DraftPickHometownInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickHometownInfo from a JSON string
draft_pick_hometown_info_instance = DraftPickHometownInfo.from_json(json)
# print the JSON string representation of the object
print DraftPickHometownInfo.to_json()

# convert the object into a dict
draft_pick_hometown_info_dict = draft_pick_hometown_info_instance.to_dict()
# create an instance of DraftPickHometownInfo from a dict
draft_pick_hometown_info_from_dict = DraftPickHometownInfo.from_dict(draft_pick_hometown_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


