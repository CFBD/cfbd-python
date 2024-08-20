# RecruitHometownInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fips_code** | **str** |  | 
**longitude** | **float** |  | 
**latitude** | **float** |  | 

## Example

```python
from cfbd.models.recruit_hometown_info import RecruitHometownInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RecruitHometownInfo from a JSON string
recruit_hometown_info_instance = RecruitHometownInfo.from_json(json)
# print the JSON string representation of the object
print RecruitHometownInfo.to_json()

# convert the object into a dict
recruit_hometown_info_dict = recruit_hometown_info_instance.to_dict()
# create an instance of RecruitHometownInfo from a dict
recruit_hometown_info_from_dict = RecruitHometownInfo.from_dict(recruit_hometown_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


