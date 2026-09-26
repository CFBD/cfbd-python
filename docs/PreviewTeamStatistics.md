# PreviewTeamStatistics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**is_previous_season** | **bool** |  | 
**advanced** | [**TeamSeasonAdvancedStats**](TeamSeasonAdvancedStats.md) |  | 
**passing** | [**TeamPassingSeason**](TeamPassingSeason.md) |  | 
**rushing** | [**TeamRushingSeason**](TeamRushingSeason.md) |  | 

## Example

```python
from cfbd.models.preview_team_statistics import PreviewTeamStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewTeamStatistics from a JSON string
preview_team_statistics_instance = PreviewTeamStatistics.from_json(json)
# print the JSON string representation of the object
print PreviewTeamStatistics.to_json()

# convert the object into a dict
preview_team_statistics_dict = preview_team_statistics_instance.to_dict()
# create an instance of PreviewTeamStatistics from a dict
preview_team_statistics_from_dict = PreviewTeamStatistics.from_dict(preview_team_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


