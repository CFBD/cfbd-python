# TeamFPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**fpi** | **float** |  | 
**resume_ranks** | [**TeamFPIResumeRanks**](TeamFPIResumeRanks.md) |  | 
**efficiencies** | [**TeamFPIEfficiencies**](TeamFPIEfficiencies.md) |  | 

## Example

```python
from cfbd.models.team_fpi import TeamFPI

# TODO update the JSON string below
json = "{}"
# create an instance of TeamFPI from a JSON string
team_fpi_instance = TeamFPI.from_json(json)
# print the JSON string representation of the object
print TeamFPI.to_json()

# convert the object into a dict
team_fpi_dict = team_fpi_instance.to_dict()
# create an instance of TeamFPI from a dict
team_fpi_from_dict = TeamFPI.from_dict(team_fpi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


