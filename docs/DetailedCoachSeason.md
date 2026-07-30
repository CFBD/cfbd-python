# DetailedCoachSeason


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**ties** | **int** |  | 
**win_percentage** | **float** |  | 
**coach** | [**CoachReference**](CoachReference.md) |  | 
**team** | [**CoachSeasonTeamReference**](CoachSeasonTeamReference.md) |  | 
**year** | **int** |  | 
**preseason_rank** | **int** |  | 
**postseason_rank** | **int** |  | 
**srs** | **float** |  | 
**sp_overall** | **float** |  | 
**sp_offense** | **float** |  | 
**sp_defense** | **float** |  | 
**team_metrics** | [**CoachRatingContext**](CoachRatingContext.md) |  | 
**recruiting** | [**CoachRecruitingContext**](CoachRecruitingContext.md) |  | 
**poll_resume** | [**CoachPollResume**](CoachPollResume.md) |  | 
**attribution_complete** | **bool** |  | 
**record_splits** | [**CoachRecordSplits**](CoachRecordSplits.md) |  | 
**scoring** | [**CoachScoring**](CoachScoring.md) |  | 
**cfp** | [**CoachCfpContext**](CoachCfpContext.md) |  | 
**draft_following_season** | [**CoachDraftContext**](CoachDraftContext.md) |  | 

## Example

```python
from cfbd.models.detailed_coach_season import DetailedCoachSeason

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedCoachSeason from a JSON string
detailed_coach_season_instance = DetailedCoachSeason.from_json(json)
# print the JSON string representation of the object
print DetailedCoachSeason.to_json()

# convert the object into a dict
detailed_coach_season_dict = detailed_coach_season_instance.to_dict()
# create an instance of DetailedCoachSeason from a dict
detailed_coach_season_from_dict = DetailedCoachSeason.from_dict(detailed_coach_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


