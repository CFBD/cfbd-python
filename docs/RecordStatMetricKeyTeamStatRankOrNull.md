# RecordStatMetricKeyTeamStatRankOrNull

Construct a type with a set of properties K of type T

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ppa** | [**TeamStatRank**](TeamStatRank.md) |  | 
**success_rate** | [**TeamStatRank**](TeamStatRank.md) |  | 
**explosiveness** | [**TeamStatRank**](TeamStatRank.md) |  | 
**standard_downs_success_rate** | [**TeamStatRank**](TeamStatRank.md) |  | 
**passing_downs_success_rate** | [**TeamStatRank**](TeamStatRank.md) |  | 
**passing_plays_ppa** | [**TeamStatRank**](TeamStatRank.md) |  | 
**rushing_plays_ppa** | [**TeamStatRank**](TeamStatRank.md) |  | 
**passing_plays_explosiveness** | [**TeamStatRank**](TeamStatRank.md) |  | 
**rushing_plays_explosiveness** | [**TeamStatRank**](TeamStatRank.md) |  | 
**line_yards** | [**TeamStatRank**](TeamStatRank.md) |  | 
**second_level_yards** | [**TeamStatRank**](TeamStatRank.md) |  | 
**open_field_yards** | [**TeamStatRank**](TeamStatRank.md) |  | 
**stuff_rate** | [**TeamStatRank**](TeamStatRank.md) |  | 
**power_success** | [**TeamStatRank**](TeamStatRank.md) |  | 
**havoc_total** | [**TeamStatRank**](TeamStatRank.md) |  | 
**havoc_front_seven** | [**TeamStatRank**](TeamStatRank.md) |  | 
**havoc_db** | [**TeamStatRank**](TeamStatRank.md) |  | 
**points_per_opportunity** | [**TeamStatRank**](TeamStatRank.md) |  | 
**field_position_average_start** | [**TeamStatRank**](TeamStatRank.md) |  | 
**field_position_average_predicted_points** | [**TeamStatRank**](TeamStatRank.md) |  | 

## Example

```python
from cfbd.models.record_stat_metric_key_team_stat_rank_or_null import RecordStatMetricKeyTeamStatRankOrNull

# TODO update the JSON string below
json = "{}"
# create an instance of RecordStatMetricKeyTeamStatRankOrNull from a JSON string
record_stat_metric_key_team_stat_rank_or_null_instance = RecordStatMetricKeyTeamStatRankOrNull.from_json(json)
# print the JSON string representation of the object
print RecordStatMetricKeyTeamStatRankOrNull.to_json()

# convert the object into a dict
record_stat_metric_key_team_stat_rank_or_null_dict = record_stat_metric_key_team_stat_rank_or_null_instance.to_dict()
# create an instance of RecordStatMetricKeyTeamStatRankOrNull from a dict
record_stat_metric_key_team_stat_rank_or_null_from_dict = RecordStatMetricKeyTeamStatRankOrNull.from_dict(record_stat_metric_key_team_stat_rank_or_null_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


