# GameMedia


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**start_time** | **datetime** |  | 
**is_start_time_tbd** | **bool** |  | 
**home_team** | **str** |  | 
**home_conference** | **str** |  | 
**away_team** | **str** |  | 
**away_conference** | **str** |  | 
**media_type** | [**MediaType**](MediaType.md) |  | 
**outlet** | **str** |  | 

## Example

```python
from cfbd.models.game_media import GameMedia

# TODO update the JSON string below
json = "{}"
# create an instance of GameMedia from a JSON string
game_media_instance = GameMedia.from_json(json)
# print the JSON string representation of the object
print GameMedia.to_json()

# convert the object into a dict
game_media_dict = game_media_instance.to_dict()
# create an instance of GameMedia from a dict
game_media_from_dict = GameMedia.from_dict(game_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


