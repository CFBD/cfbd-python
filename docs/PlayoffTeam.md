# PlayoffTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**school** | **str** |  | 
**conference** | **str** |  | 

## Example

```python
from cfbd.models.playoff_team import PlayoffTeam

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffTeam from a JSON string
playoff_team_instance = PlayoffTeam.from_json(json)
# print the JSON string representation of the object
print PlayoffTeam.to_json()

# convert the object into a dict
playoff_team_dict = playoff_team_instance.to_dict()
# create an instance of PlayoffTeam from a dict
playoff_team_from_dict = PlayoffTeam.from_dict(playoff_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


