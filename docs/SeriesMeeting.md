# SeriesMeeting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**start_date** | **datetime** |  | 
**home_team_id** | **int** |  | 
**home_team** | **str** |  | 
**away_team_id** | **int** |  | 
**away_team** | **str** |  | 
**neutral_site** | **bool** |  | 
**venue** | [**PreviewVenue**](PreviewVenue.md) |  | 
**home_points** | **int** |  | 
**away_points** | **int** |  | 
**winner_team_id** | **int** |  | 
**result** | **str** |  | 

## Example

```python
from cfbd.models.series_meeting import SeriesMeeting

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesMeeting from a JSON string
series_meeting_instance = SeriesMeeting.from_json(json)
# print the JSON string representation of the object
print SeriesMeeting.to_json()

# convert the object into a dict
series_meeting_dict = series_meeting_instance.to_dict()
# create an instance of SeriesMeeting from a dict
series_meeting_from_dict = SeriesMeeting.from_dict(series_meeting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


