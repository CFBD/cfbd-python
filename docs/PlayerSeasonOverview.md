# PlayerSeasonOverview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**games** | **int** |  | 
**box_score_stats** | [**PlayerSeasonOverviewBoxScoreStats**](PlayerSeasonOverviewBoxScoreStats.md) |  | 
**usage** | [**PlayerUsageUsage**](PlayerUsageUsage.md) |  | [optional] 
**ppa** | [**PlayerSeasonOverviewPPA**](PlayerSeasonOverviewPPA.md) |  | [optional] 

## Example

```python
from cfbd.models.player_season_overview import PlayerSeasonOverview

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonOverview from a JSON string
player_season_overview_instance = PlayerSeasonOverview.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonOverview.to_json()

# convert the object into a dict
player_season_overview_dict = player_season_overview_instance.to_dict()
# create an instance of PlayerSeasonOverview from a dict
player_season_overview_from_dict = PlayerSeasonOverview.from_dict(player_season_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


