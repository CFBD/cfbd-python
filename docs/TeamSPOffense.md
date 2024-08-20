# TeamSPOffense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pace** | **float** |  | 
**run_rate** | **float** |  | 
**passing_downs** | **float** |  | 
**standard_downs** | **float** |  | 
**passing** | **float** |  | 
**rushing** | **float** |  | 
**explosiveness** | **float** |  | 
**success** | **float** |  | 
**rating** | **float** |  | 
**ranking** | **int** |  | 

## Example

```python
from cfbd.models.team_sp_offense import TeamSPOffense

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSPOffense from a JSON string
team_sp_offense_instance = TeamSPOffense.from_json(json)
# print the JSON string representation of the object
print TeamSPOffense.to_json()

# convert the object into a dict
team_sp_offense_dict = team_sp_offense_instance.to_dict()
# create an instance of TeamSPOffense from a dict
team_sp_offense_from_dict = TeamSPOffense.from_dict(team_sp_offense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


