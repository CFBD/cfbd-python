# GameLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**spread** | **float** |  | 
**formatted_spread** | **str** |  | 
**spread_open** | **float** |  | 
**over_under** | **float** |  | 
**over_under_open** | **float** |  | 
**home_moneyline** | **float** |  | 
**away_moneyline** | **float** |  | 

## Example

```python
from cfbd.models.game_line import GameLine

# TODO update the JSON string below
json = "{}"
# create an instance of GameLine from a JSON string
game_line_instance = GameLine.from_json(json)
# print the JSON string representation of the object
print GameLine.to_json()

# convert the object into a dict
game_line_dict = game_line_instance.to_dict()
# create an instance of GameLine from a dict
game_line_from_dict = GameLine.from_dict(game_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


