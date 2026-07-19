# PlayerSearchTeamStint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**start_year** | **int** |  | 
**end_year** | **int** |  | 

## Example

```python
from cfbd.models.player_search_team_stint import PlayerSearchTeamStint

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSearchTeamStint from a JSON string
player_search_team_stint_instance = PlayerSearchTeamStint.from_json(json)
# print the JSON string representation of the object
print PlayerSearchTeamStint.to_json()

# convert the object into a dict
player_search_team_stint_dict = player_search_team_stint_instance.to_dict()
# create an instance of PlayerSearchTeamStint from a dict
player_search_team_stint_from_dict = PlayerSearchTeamStint.from_dict(player_search_team_stint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


