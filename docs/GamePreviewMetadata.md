# GamePreviewMetadata


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

## Example

```python
from cfbd.models.game_preview_metadata import GamePreviewMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GamePreviewMetadata from a JSON string
game_preview_metadata_instance = GamePreviewMetadata.from_json(json)
# print the JSON string representation of the object
print GamePreviewMetadata.to_json()

# convert the object into a dict
game_preview_metadata_dict = game_preview_metadata_instance.to_dict()
# create an instance of GamePreviewMetadata from a dict
game_preview_metadata_from_dict = GamePreviewMetadata.from_dict(game_preview_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


