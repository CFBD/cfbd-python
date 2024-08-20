# TeamFPIResumeRanks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_control** | **int** |  | 
**remaining_strength_of_schedule** | **int** |  | 
**strength_of_schedule** | **int** |  | 
**average_win_probability** | **int** |  | 
**fpi** | **int** |  | 
**strength_of_record** | **int** |  | 

## Example

```python
from cfbd.models.team_fpi_resume_ranks import TeamFPIResumeRanks

# TODO update the JSON string below
json = "{}"
# create an instance of TeamFPIResumeRanks from a JSON string
team_fpi_resume_ranks_instance = TeamFPIResumeRanks.from_json(json)
# print the JSON string representation of the object
print TeamFPIResumeRanks.to_json()

# convert the object into a dict
team_fpi_resume_ranks_dict = team_fpi_resume_ranks_instance.to_dict()
# create an instance of TeamFPIResumeRanks from a dict
team_fpi_resume_ranks_from_dict = TeamFPIResumeRanks.from_dict(team_fpi_resume_ranks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


