# PlayerSeasonSuccessRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**passing** | [**PlayerSuccessRateSplit**](PlayerSuccessRateSplit.md) |  | 
**rushing** | [**PlayerSuccessRateSplit**](PlayerSuccessRateSplit.md) |  | 

## Example

```python
from cfbd.models.player_season_success_rate import PlayerSeasonSuccessRate

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonSuccessRate from a JSON string
player_season_success_rate_instance = PlayerSeasonSuccessRate.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonSuccessRate.to_json()

# convert the object into a dict
player_season_success_rate_dict = player_season_success_rate_instance.to_dict()
# create an instance of PlayerSeasonSuccessRate from a dict
player_season_success_rate_from_dict = PlayerSeasonSuccessRate.from_dict(player_season_success_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


