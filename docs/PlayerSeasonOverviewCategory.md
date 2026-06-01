# PlayerSeasonOverviewCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**stats** | [**List[PlayerSeasonOverviewStat]**](PlayerSeasonOverviewStat.md) |  | 

## Example

```python
from cfbd.models.player_season_overview_category import PlayerSeasonOverviewCategory

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonOverviewCategory from a JSON string
player_season_overview_category_instance = PlayerSeasonOverviewCategory.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonOverviewCategory.to_json()

# convert the object into a dict
player_season_overview_category_dict = player_season_overview_category_instance.to_dict()
# create an instance of PlayerSeasonOverviewCategory from a dict
player_season_overview_category_from_dict = PlayerSeasonOverviewCategory.from_dict(player_season_overview_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


