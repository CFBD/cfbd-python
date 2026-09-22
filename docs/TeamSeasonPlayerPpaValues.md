# TeamSeasonPlayerPpaValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **float** |  | 
**var_pass** | **float** |  | 
**rush** | **float** |  | 
**first_down** | **float** |  | 
**second_down** | **float** |  | 
**third_down** | **float** |  | 
**standard_downs** | **float** |  | 
**passing_downs** | **float** |  | 

## Example

```python
from cfbd.models.team_season_player_ppa_values import TeamSeasonPlayerPpaValues

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonPlayerPpaValues from a JSON string
team_season_player_ppa_values_instance = TeamSeasonPlayerPpaValues.from_json(json)
# print the JSON string representation of the object
print TeamSeasonPlayerPpaValues.to_json()

# convert the object into a dict
team_season_player_ppa_values_dict = team_season_player_ppa_values_instance.to_dict()
# create an instance of TeamSeasonPlayerPpaValues from a dict
team_season_player_ppa_values_from_dict = TeamSeasonPlayerPpaValues.from_dict(team_season_player_ppa_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


