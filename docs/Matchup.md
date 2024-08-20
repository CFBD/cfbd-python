# Matchup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team1** | **str** |  | 
**team2** | **str** |  | 
**start_year** | **int** |  | [optional] 
**end_year** | **int** |  | [optional] 
**team1_wins** | **int** |  | 
**team2_wins** | **int** |  | 
**ties** | **int** |  | 
**games** | [**List[MatchupGame]**](MatchupGame.md) |  | 

## Example

```python
from cfbd.models.matchup import Matchup

# TODO update the JSON string below
json = "{}"
# create an instance of Matchup from a JSON string
matchup_instance = Matchup.from_json(json)
# print the JSON string representation of the object
print Matchup.to_json()

# convert the object into a dict
matchup_dict = matchup_instance.to_dict()
# create an instance of Matchup from a dict
matchup_from_dict = Matchup.from_dict(matchup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


