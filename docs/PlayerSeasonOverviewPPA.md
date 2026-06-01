# PlayerSeasonOverviewPPA


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | [**PlayerSeasonOverviewPPAAverage**](PlayerSeasonOverviewPPAAverage.md) |  | 
**total** | [**PlayerSeasonOverviewPPAAverage**](PlayerSeasonOverviewPPAAverage.md) |  | 

## Example

```python
from cfbd.models.player_season_overview_ppa import PlayerSeasonOverviewPPA

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonOverviewPPA from a JSON string
player_season_overview_ppa_instance = PlayerSeasonOverviewPPA.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonOverviewPPA.to_json()

# convert the object into a dict
player_season_overview_ppa_dict = player_season_overview_ppa_instance.to_dict()
# create an instance of PlayerSeasonOverviewPPA from a dict
player_season_overview_ppa_from_dict = PlayerSeasonOverviewPPA.from_dict(player_season_overview_ppa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


