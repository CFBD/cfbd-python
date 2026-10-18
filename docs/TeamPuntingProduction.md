# TeamPuntingProduction

Production on a team's punts. On the returning side, punt and net yards describe opponent punts.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**punts** | **int** |  | 
**punt_yards_available** | **int** | Punts with known gross yards. | 
**punt_yards** | **int** |  | 
**yards_per_punt** | **float** |  | 
**longest_punt** | **int** |  | 
**punts50_plus** | **int** |  | 
**net_punt_yards_available** | **int** | Punts with known net yards. | 
**net_punt_yards** | **int** |  | 
**net_yards_per_punt** | **float** |  | 
**touchbacks** | **int** |  | 
**fair_catches** | **int** |  | 
**out_of_bounds** | **int** |  | 
**downed** | **int** |  | 
**inside20** | **int** | Punts after which the receiving team took possession inside its own 20, excluding touchbacks. | 
**blocked** | **int** |  | 
**returns** | **int** |  | 
**return_yards_available** | **int** | Returns with known yards. | 
**return_yards** | **int** |  | 
**yards_per_return** | **float** |  | 
**longest_return** | **int** |  | 
**returns20_plus** | **int** |  | 
**return_touchdowns** | **int** |  | 
**muffs** | **int** |  | 
**receiving_team_turnovers** | **int** |  | 

## Example

```python
from cfbd.models.team_punting_production import TeamPuntingProduction

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPuntingProduction from a JSON string
team_punting_production_instance = TeamPuntingProduction.from_json(json)
# print the JSON string representation of the object
print TeamPuntingProduction.to_json()

# convert the object into a dict
team_punting_production_dict = team_punting_production_instance.to_dict()
# create an instance of TeamPuntingProduction from a dict
team_punting_production_from_dict = TeamPuntingProduction.from_dict(team_punting_production_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


