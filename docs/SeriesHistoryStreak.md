# SeriesHistoryStreak


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wins** | **float** |  | 
**team_id** | **float** |  | 

## Example

```python
from cfbd.models.series_history_streak import SeriesHistoryStreak

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesHistoryStreak from a JSON string
series_history_streak_instance = SeriesHistoryStreak.from_json(json)
# print the JSON string representation of the object
print SeriesHistoryStreak.to_json()

# convert the object into a dict
series_history_streak_dict = series_history_streak_instance.to_dict()
# create an instance of SeriesHistoryStreak from a dict
series_history_streak_from_dict = SeriesHistoryStreak.from_dict(series_history_streak_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


