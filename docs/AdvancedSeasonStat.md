# AdvancedSeasonStat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**offense** | [**AdvancedSeasonStatOffense**](AdvancedSeasonStatOffense.md) |  | 
**defense** | [**AdvancedSeasonStatDefense**](AdvancedSeasonStatDefense.md) |  | 

## Example

```python
from cfbd.models.advanced_season_stat import AdvancedSeasonStat

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedSeasonStat from a JSON string
advanced_season_stat_instance = AdvancedSeasonStat.from_json(json)
# print the JSON string representation of the object
print AdvancedSeasonStat.to_json()

# convert the object into a dict
advanced_season_stat_dict = advanced_season_stat_instance.to_dict()
# create an instance of AdvancedSeasonStat from a dict
advanced_season_stat_from_dict = AdvancedSeasonStat.from_dict(advanced_season_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


