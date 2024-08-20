# DraftPick


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**college_athlete_id** | **int** |  | 
**nfl_athlete_id** | **int** |  | 
**college_id** | **int** |  | 
**college_team** | **str** |  | 
**college_conference** | **str** |  | 
**nfl_team_id** | **int** |  | 
**nfl_team** | **str** |  | 
**year** | **int** |  | 
**overall** | **int** |  | 
**round** | **int** |  | 
**pick** | **int** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**height** | **int** |  | 
**weight** | **int** |  | 
**pre_draft_ranking** | **int** |  | 
**pre_draft_position_ranking** | **int** |  | 
**pre_draft_grade** | **int** |  | 
**hometown_info** | [**DraftPickHometownInfo**](DraftPickHometownInfo.md) |  | 

## Example

```python
from cfbd.models.draft_pick import DraftPick

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPick from a JSON string
draft_pick_instance = DraftPick.from_json(json)
# print the JSON string representation of the object
print DraftPick.to_json()

# convert the object into a dict
draft_pick_dict = draft_pick_instance.to_dict()
# create an instance of DraftPick from a dict
draft_pick_from_dict = DraftPick.from_dict(draft_pick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


