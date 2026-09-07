# PassingPlay


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
**clock** | [**PassingPlayClock**](PassingPlayClock.md) |  | 
**down** | **int** |  | 
**distance** | **int** |  | 
**play_text** | **str** |  | 
**passer_id** | **str** |  | 
**passer** | **str** |  | 
**target_id** | **str** |  | 
**target** | **str** |  | 
**outcome** | [**PassOutcome**](PassOutcome.md) |  | 
**air_yards** | **int** |  | 
**pass_depth** | [**PassDepth**](PassDepth.md) |  | 
**pass_direction** | [**PassDirection**](PassDirection.md) |  | 
**pass_location** | [**PassLocation**](PassLocation.md) |  | 
**total_yards** | **int** |  | 
**yards_after_catch** | **int** |  | 
**start_yardline** | **int** |  | 
**start_yards_to_goal** | **int** |  | 
**target_yards_to_goal** | **int** |  | 
**is_spike** | **bool** |  | 
**is_throwaway** | **bool** |  | 
**is_intentional_grounding** | **bool** |  | 
**parse_status** | [**PassParseStatus**](PassParseStatus.md) |  | 
**ppa** | **float** | Stored offensive PPA, including zero and negative values. | 
**success** | **bool** | Stored success classification; null means unavailable. | 
**location_analysis_eligible** | **bool** | Excludes spikes, intentional grounding, and invalid parses. Throwaways, partial parses, and attempts with missing location or air yards qualify. | 

## Example

```python
from cfbd.models.passing_play import PassingPlay

# TODO update the JSON string below
json = "{}"
# create an instance of PassingPlay from a JSON string
passing_play_instance = PassingPlay.from_json(json)
# print the JSON string representation of the object
print PassingPlay.to_json()

# convert the object into a dict
passing_play_dict = passing_play_instance.to_dict()
# create an instance of PassingPlay from a dict
passing_play_from_dict = PassingPlay.from_dict(passing_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


