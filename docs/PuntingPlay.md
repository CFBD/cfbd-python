# PuntingPlay


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**play_id** | **str** |  | 
**drive_id** | **str** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**punting_team_id** | **int** |  | 
**punting_team** | **str** |  | 
**punting_conference** | **str** |  | 
**receiving_team_id** | **int** |  | 
**receiving_team** | **str** |  | 
**receiving_conference** | **str** |  | 
**period** | **int** |  | 
**clock** | [**PuntingPlayClock**](PuntingPlayClock.md) |  | 
**down** | **int** |  | 
**distance** | **int** |  | 
**play_type** | **str** |  | 
**play_text** | **str** |  | 
**punter_id** | **str** |  | 
**punter** | **str** |  | 
**receiver_id** | **str** |  | 
**receiver** | **str** |  | 
**returner_id** | **str** |  | 
**returner** | **str** |  | 
**blocker_id** | **str** |  | 
**blocker** | **str** |  | 
**counts_as_punt** | **bool** | Whether the play counts as a punt; null when unknown. | 
**counts_as_return** | **bool** | Whether the play counts as a punt return; null when unknown. | 
**start_yards_to_goal** | **int** |  | 
**punt_yards** | **int** | Gross punt yards. | 
**return_yards** | **int** | Return yards for the receiving team. | 
**returner_yards** | **int** | Return yards credited to the returner; null when not credited individually. | 
**net_punt_yards** | **int** | Gross punt yards minus return yards, less 20 yards for a touchback. | 
**kick_end_yardline** | **int** | Where the kick ended, from the punting team&#39;s goal line (0) to the receiving team&#39;s goal line (100). | 
**end_yardline** | **int** | Where the play ended, on the same scale as kickEndYardline. | 
**is_touchback** | **bool** |  | 
**is_fair_catch** | **bool** |  | 
**is_out_of_bounds** | **bool** |  | 
**is_downed** | **bool** |  | 
**is_blocked** | **bool** |  | 
**is_muffed** | **bool** |  | 
**is_return_touchdown** | **bool** |  | 
**is_receiving_team_turnover** | **bool** | The receiving team lost possession, such as on a muff or fumble. | 
**has_penalty** | **bool** |  | 
**parse_status** | [**PuntParseStatus**](PuntParseStatus.md) |  | 

## Example

```python
from cfbd.models.punting_play import PuntingPlay

# TODO update the JSON string below
json = "{}"
# create an instance of PuntingPlay from a JSON string
punting_play_instance = PuntingPlay.from_json(json)
# print the JSON string representation of the object
print PuntingPlay.to_json()

# convert the object into a dict
punting_play_dict = punting_play_instance.to_dict()
# create an instance of PuntingPlay from a dict
punting_play_from_dict = PuntingPlay.from_dict(punting_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


