# Recruit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**athlete_id** | **str** |  | 
**recruit_type** | [**RecruitClassification**](RecruitClassification.md) |  | 
**year** | **int** |  | 
**ranking** | **int** |  | 
**name** | **str** |  | 
**school** | **str** |  | 
**committed_to** | **str** |  | 
**position** | **str** |  | 
**height** | **int** |  | 
**weight** | **int** |  | 
**stars** | **int** |  | 
**rating** | **float** |  | 
**city** | **str** |  | 
**state_province** | **str** |  | 
**country** | **str** |  | 
**hometown_info** | [**RecruitHometownInfo**](RecruitHometownInfo.md) |  | 

## Example

```python
from cfbd.models.recruit import Recruit

# TODO update the JSON string below
json = "{}"
# create an instance of Recruit from a JSON string
recruit_instance = Recruit.from_json(json)
# print the JSON string representation of the object
print Recruit.to_json()

# convert the object into a dict
recruit_dict = recruit_instance.to_dict()
# create an instance of Recruit from a dict
recruit_from_dict = Recruit.from_dict(recruit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


