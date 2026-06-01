# PlayerSeasonOverviewPPAAverage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passing_downs** | **float** |  | [optional] 
**standard_downs** | **float** |  | [optional] 
**third_down** | **float** |  | [optional] 
**second_down** | **float** |  | [optional] 
**first_down** | **float** |  | [optional] 
**rush** | **float** |  | [optional] 
**var_pass** | **float** |  | [optional] 
**all** | **float** |  | 

## Example

```python
from cfbd.models.player_season_overview_ppa_average import PlayerSeasonOverviewPPAAverage

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonOverviewPPAAverage from a JSON string
player_season_overview_ppa_average_instance = PlayerSeasonOverviewPPAAverage.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonOverviewPPAAverage.to_json()

# convert the object into a dict
player_season_overview_ppa_average_dict = player_season_overview_ppa_average_instance.to_dict()
# create an instance of PlayerSeasonOverviewPPAAverage from a dict
player_season_overview_ppa_average_from_dict = PlayerSeasonOverviewPPAAverage.from_dict(player_season_overview_ppa_average_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


