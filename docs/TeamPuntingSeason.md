# TeamPuntingSeason


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**punting** | [**TeamPuntingProduction**](TeamPuntingProduction.md) |  | 
**returning** | [**TeamPuntingProduction**](TeamPuntingProduction.md) |  | 

## Example

```python
from cfbd.models.team_punting_season import TeamPuntingSeason

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPuntingSeason from a JSON string
team_punting_season_instance = TeamPuntingSeason.from_json(json)
# print the JSON string representation of the object
print TeamPuntingSeason.to_json()

# convert the object into a dict
team_punting_season_dict = team_punting_season_instance.to_dict()
# create an instance of TeamPuntingSeason from a dict
team_punting_season_from_dict = TeamPuntingSeason.from_dict(team_punting_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


