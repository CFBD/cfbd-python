# TeamPassingSeason


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**offense** | [**PassingProduction**](PassingProduction.md) |  | 
**defense** | [**PassingProduction**](PassingProduction.md) |  | 

## Example

```python
from cfbd.models.team_passing_season import TeamPassingSeason

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPassingSeason from a JSON string
team_passing_season_instance = TeamPassingSeason.from_json(json)
# print the JSON string representation of the object
print TeamPassingSeason.to_json()

# convert the object into a dict
team_passing_season_dict = team_passing_season_instance.to_dict()
# create an instance of TeamPassingSeason from a dict
team_passing_season_from_dict = TeamPassingSeason.from_dict(team_passing_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


