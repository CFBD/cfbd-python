# PlayerGameSuccessRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**season_type** | [**SeasonTypeDB**](SeasonTypeDB.md) |  | 
**week** | **int** |  | 
**game_id** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**opponent** | **str** |  | 
**passing** | [**PlayerSuccessRateSplit**](PlayerSuccessRateSplit.md) |  | 
**rushing** | [**PlayerSuccessRateSplit**](PlayerSuccessRateSplit.md) |  | 

## Example

```python
from cfbd.models.player_game_success_rate import PlayerGameSuccessRate

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerGameSuccessRate from a JSON string
player_game_success_rate_instance = PlayerGameSuccessRate.from_json(json)
# print the JSON string representation of the object
print PlayerGameSuccessRate.to_json()

# convert the object into a dict
player_game_success_rate_dict = player_game_success_rate_instance.to_dict()
# create an instance of PlayerGameSuccessRate from a dict
player_game_success_rate_from_dict = PlayerGameSuccessRate.from_dict(player_game_success_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


