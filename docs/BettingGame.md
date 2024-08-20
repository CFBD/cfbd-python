# BettingGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**season** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**week** | **int** |  | 
**start_date** | **datetime** |  | 
**home_team** | **str** |  | 
**home_conference** | **str** |  | 
**home_classification** | [**DivisionClassification**](DivisionClassification.md) |  | 
**home_score** | **int** |  | 
**away_team** | **str** |  | 
**away_conference** | **str** |  | 
**away_classification** | [**DivisionClassification**](DivisionClassification.md) |  | 
**away_score** | **int** |  | 
**lines** | [**List[GameLine]**](GameLine.md) |  | 

## Example

```python
from cfbd.models.betting_game import BettingGame

# TODO update the JSON string below
json = "{}"
# create an instance of BettingGame from a JSON string
betting_game_instance = BettingGame.from_json(json)
# print the JSON string representation of the object
print BettingGame.to_json()

# convert the object into a dict
betting_game_dict = betting_game_instance.to_dict()
# create an instance of BettingGame from a dict
betting_game_from_dict = BettingGame.from_dict(betting_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


