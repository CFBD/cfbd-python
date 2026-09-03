# TeamRushingSeason


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**offense** | [**TeamRushingProduction**](TeamRushingProduction.md) |  | 
**defense** | [**TeamRushingProduction**](TeamRushingProduction.md) |  | 

## Example

```python
from cfbd.models.team_rushing_season import TeamRushingSeason

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRushingSeason from a JSON string
team_rushing_season_instance = TeamRushingSeason.from_json(json)
# print the JSON string representation of the object
print TeamRushingSeason.to_json()

# convert the object into a dict
team_rushing_season_dict = team_rushing_season_instance.to_dict()
# create an instance of TeamRushingSeason from a dict
team_rushing_season_from_dict = TeamRushingSeason.from_dict(team_rushing_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


