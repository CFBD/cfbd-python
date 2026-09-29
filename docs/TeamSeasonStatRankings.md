# TeamSeasonStatRankings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **float** |  | 
**season** | **float** |  | 
**division** | [**Division**](Division.md) |  | 
**division_team_count** | **float** |  | 
**calculated_at** | **str** |  | 
**expires_at** | **str** |  | 
**source_updated_at** | **str** |  | 
**offense** | [**RecordStatMetricKeyTeamStatRankOrNull**](RecordStatMetricKeyTeamStatRankOrNull.md) |  | 
**defense** | [**RecordStatMetricKeyTeamStatRankOrNull**](RecordStatMetricKeyTeamStatRankOrNull.md) |  | 

## Example

```python
from cfbd.models.team_season_stat_rankings import TeamSeasonStatRankings

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonStatRankings from a JSON string
team_season_stat_rankings_instance = TeamSeasonStatRankings.from_json(json)
# print the JSON string representation of the object
print TeamSeasonStatRankings.to_json()

# convert the object into a dict
team_season_stat_rankings_dict = team_season_stat_rankings_instance.to_dict()
# create an instance of TeamSeasonStatRankings from a dict
team_season_stat_rankings_from_dict = TeamSeasonStatRankings.from_dict(team_season_stat_rankings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


