# MatchupGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | **str** |  | 
**var_date** | **str** |  | 
**neutral_site** | **bool** |  | 
**venue** | **str** |  | 
**home_team** | **str** |  | 
**home_score** | **int** |  | 
**away_team** | **str** |  | 
**away_score** | **int** |  | 
**winner** | **str** |  | 

## Example

```python
from cfbd.models.matchup_game import MatchupGame

# TODO update the JSON string below
json = "{}"
# create an instance of MatchupGame from a JSON string
matchup_game_instance = MatchupGame.from_json(json)
# print the JSON string representation of the object
print MatchupGame.to_json()

# convert the object into a dict
matchup_game_dict = matchup_game_instance.to_dict()
# create an instance of MatchupGame from a dict
matchup_game_from_dict = MatchupGame.from_dict(matchup_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


