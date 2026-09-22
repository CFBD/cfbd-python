# TeamSeasonOverviewRecord

Completed games for the requested season, including postseason.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ties** | **int** |  | 
**losses** | **int** |  | 
**wins** | **int** |  | 
**games** | **int** |  | 

## Example

```python
from cfbd.models.team_season_overview_record import TeamSeasonOverviewRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewRecord from a JSON string
team_season_overview_record_instance = TeamSeasonOverviewRecord.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewRecord.to_json()

# convert the object into a dict
team_season_overview_record_dict = team_season_overview_record_instance.to_dict()
# create an instance of TeamSeasonOverviewRecord from a dict
team_season_overview_record_from_dict = TeamSeasonOverviewRecord.from_dict(team_season_overview_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


