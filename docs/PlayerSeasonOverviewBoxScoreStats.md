# PlayerSeasonOverviewBoxScoreStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[PlayerSeasonOverviewCategory]**](PlayerSeasonOverviewCategory.md) |  | 

## Example

```python
from cfbd.models.player_season_overview_box_score_stats import PlayerSeasonOverviewBoxScoreStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonOverviewBoxScoreStats from a JSON string
player_season_overview_box_score_stats_instance = PlayerSeasonOverviewBoxScoreStats.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonOverviewBoxScoreStats.to_json()

# convert the object into a dict
player_season_overview_box_score_stats_dict = player_season_overview_box_score_stats_instance.to_dict()
# create an instance of PlayerSeasonOverviewBoxScoreStats from a dict
player_season_overview_box_score_stats_from_dict = PlayerSeasonOverviewBoxScoreStats.from_dict(player_season_overview_box_score_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


