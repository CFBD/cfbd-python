# TeamElo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**elo** | **int** |  | 

## Example

```python
from cfbd.models.team_elo import TeamElo

# TODO update the JSON string below
json = "{}"
# create an instance of TeamElo from a JSON string
team_elo_instance = TeamElo.from_json(json)
# print the JSON string representation of the object
print TeamElo.to_json()

# convert the object into a dict
team_elo_dict = team_elo_instance.to_dict()
# create an instance of TeamElo from a dict
team_elo_from_dict = TeamElo.from_dict(team_elo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


