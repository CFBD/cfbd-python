# SeriesHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_team_id** | **int** |  | 
**away_team_id** | **int** |  | 
**meetings** | **int** |  | 
**known_results** | **int** |  | 
**unknown_results** | **int** |  | 
**home_wins** | **int** |  | 
**away_wins** | **int** |  | 
**ties** | **int** |  | 
**first_season** | **int** |  | 
**last_season** | **int** |  | 
**latest_meeting** | [**SeriesMeeting**](SeriesMeeting.md) |  | 
**streak** | [**SeriesHistoryStreak**](SeriesHistoryStreak.md) |  | 
**recent_meetings** | [**List[SeriesMeeting]**](SeriesMeeting.md) |  | 

## Example

```python
from cfbd.models.series_history import SeriesHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesHistory from a JSON string
series_history_instance = SeriesHistory.from_json(json)
# print the JSON string representation of the object
print SeriesHistory.to_json()

# convert the object into a dict
series_history_dict = series_history_instance.to_dict()
# create an instance of SeriesHistory from a dict
series_history_from_dict = SeriesHistory.from_dict(series_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


