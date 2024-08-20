# ScoreboardGameBetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_moneyline** | **float** |  | 
**home_moneyline** | **float** |  | 
**over_under** | **float** |  | 
**spread** | **float** |  | 

## Example

```python
from cfbd.models.scoreboard_game_betting import ScoreboardGameBetting

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreboardGameBetting from a JSON string
scoreboard_game_betting_instance = ScoreboardGameBetting.from_json(json)
# print the JSON string representation of the object
print ScoreboardGameBetting.to_json()

# convert the object into a dict
scoreboard_game_betting_dict = scoreboard_game_betting_instance.to_dict()
# create an instance of ScoreboardGameBetting from a dict
scoreboard_game_betting_from_dict = ScoreboardGameBetting.from_dict(scoreboard_game_betting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


