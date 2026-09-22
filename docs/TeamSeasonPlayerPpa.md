# TeamSeasonPlayerPpa


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**average_ppa** | [**TeamSeasonPlayerPpaValues**](TeamSeasonPlayerPpaValues.md) |  | 
**total_ppa** | [**TeamSeasonPlayerPpaValues**](TeamSeasonPlayerPpaValues.md) |  | 

## Example

```python
from cfbd.models.team_season_player_ppa import TeamSeasonPlayerPpa

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonPlayerPpa from a JSON string
team_season_player_ppa_instance = TeamSeasonPlayerPpa.from_json(json)
# print the JSON string representation of the object
print TeamSeasonPlayerPpa.to_json()

# convert the object into a dict
team_season_player_ppa_dict = team_season_player_ppa_instance.to_dict()
# create an instance of TeamSeasonPlayerPpa from a dict
team_season_player_ppa_from_dict = TeamSeasonPlayerPpa.from_dict(team_season_player_ppa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


