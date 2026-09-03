# RushingPlay


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**play_id** | **str** |  | 
**drive_id** | **str** |  | 
**season** | **int** |  | 
**week** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**offense_id** | **int** |  | 
**offense** | **str** |  | 
**offense_conference** | **str** |  | 
**defense_id** | **int** |  | 
**defense** | **str** |  | 
**defense_conference** | **str** |  | 
**period** | **int** |  | 
**clock** | [**RushingPlayClock**](RushingPlayClock.md) |  | 
**down** | **int** |  | 
**distance** | **int** |  | 
**play_text** | **str** |  | 
**start_yardline** | **int** |  | 
**start_yards_to_goal** | **int** |  | 
**rusher_id** | **str** |  | 
**rusher** | **str** |  | 
**rush_direction** | [**RushDirection**](RushDirection.md) |  | 
**rushing_yards** | **int** |  | 
**rusher_yards** | **int** |  | 
**is_rushing_touchdown** | **bool** |  | 
**is_sack** | **bool** |  | 
**is_kneel** | **bool** |  | 
**is_team_rush** | **bool** |  | 
**attribution_status** | [**RushAttributionStatus**](RushAttributionStatus.md) |  | 
**direction_analysis_eligible** | **bool** |  | 
**parse_status** | [**RushParseStatus**](RushParseStatus.md) |  | 
**ppa** | **float** |  | 
**success** | **bool** |  | 

## Example

```python
from cfbd.models.rushing_play import RushingPlay

# TODO update the JSON string below
json = "{}"
# create an instance of RushingPlay from a JSON string
rushing_play_instance = RushingPlay.from_json(json)
# print the JSON string representation of the object
print RushingPlay.to_json()

# convert the object into a dict
rushing_play_dict = rushing_play_instance.to_dict()
# create an instance of RushingPlay from a dict
rushing_play_from_dict = RushingPlay.from_dict(rushing_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


