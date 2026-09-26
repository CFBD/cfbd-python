# ScheduleGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**ScheduleGameSeasonType**](ScheduleGameSeasonType.md) |  | 
**start_date** | **datetime** |  | 
**start_time_tbd** | **bool** |  | 
**status** | [**GameStatus**](GameStatus.md) |  | 
**status_checked_at** | **datetime** |  | 
**neutral_site** | **bool** |  | 
**conference_game** | **bool** |  | 
**venue** | [**PreviewVenue**](PreviewVenue.md) |  | 
**home_team** | [**PreviewTeamIdentity**](PreviewTeamIdentity.md) |  | 
**away_team** | [**PreviewTeamIdentity**](PreviewTeamIdentity.md) |  | 
**playoff** | [**GamePlayoff**](GamePlayoff.md) |  | 
**broadcasts** | [**PreviewSectionPreviewBroadcastArray**](PreviewSectionPreviewBroadcastArray.md) |  | 
**odds** | [**PreviewSectionSelectedOdds**](PreviewSectionSelectedOdds.md) |  | 

## Example

```python
from cfbd.models.schedule_game import ScheduleGame

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGame from a JSON string
schedule_game_instance = ScheduleGame.from_json(json)
# print the JSON string representation of the object
print ScheduleGame.to_json()

# convert the object into a dict
schedule_game_dict = schedule_game_instance.to_dict()
# create an instance of ScheduleGame from a dict
schedule_game_from_dict = ScheduleGame.from_dict(schedule_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


