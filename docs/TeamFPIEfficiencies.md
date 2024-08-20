# TeamFPIEfficiencies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_teams** | **float** |  | 
**defense** | **float** |  | 
**offense** | **float** |  | 
**overall** | **float** |  | 

## Example

```python
from cfbd.models.team_fpi_efficiencies import TeamFPIEfficiencies

# TODO update the JSON string below
json = "{}"
# create an instance of TeamFPIEfficiencies from a JSON string
team_fpi_efficiencies_instance = TeamFPIEfficiencies.from_json(json)
# print the JSON string representation of the object
print TeamFPIEfficiencies.to_json()

# convert the object into a dict
team_fpi_efficiencies_dict = team_fpi_efficiencies_instance.to_dict()
# create an instance of TeamFPIEfficiencies from a dict
team_fpi_efficiencies_from_dict = TeamFPIEfficiencies.from_dict(team_fpi_efficiencies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


