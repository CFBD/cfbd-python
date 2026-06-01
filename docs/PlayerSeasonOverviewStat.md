# PlayerSeasonOverviewStat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from cfbd.models.player_season_overview_stat import PlayerSeasonOverviewStat

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonOverviewStat from a JSON string
player_season_overview_stat_instance = PlayerSeasonOverviewStat.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonOverviewStat.to_json()

# convert the object into a dict
player_season_overview_stat_dict = player_season_overview_stat_instance.to_dict()
# create an instance of PlayerSeasonOverviewStat from a dict
player_season_overview_stat_from_dict = PlayerSeasonOverviewStat.from_dict(player_season_overview_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


