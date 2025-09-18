# TeamATS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**games** | **int** |  | 
**ats_wins** | **int** |  | 
**ats_losses** | **int** |  | 
**ats_pushes** | **int** |  | 
**avg_cover_margin** | **float** |  | 

## Example

```python
from cfbd.models.team_ats import TeamATS

# TODO update the JSON string below
json = "{}"
# create an instance of TeamATS from a JSON string
team_ats_instance = TeamATS.from_json(json)
# print the JSON string representation of the object
print TeamATS.to_json()

# convert the object into a dict
team_ats_dict = team_ats_instance.to_dict()
# create an instance of TeamATS from a dict
team_ats_from_dict = TeamATS.from_dict(team_ats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


