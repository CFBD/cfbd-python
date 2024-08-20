# CoachSeason


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | **str** |  | 
**year** | **int** |  | 
**games** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**ties** | **int** |  | 
**preseason_rank** | **int** |  | 
**postseason_rank** | **int** |  | 
**srs** | **float** |  | 
**sp_overall** | **float** |  | 
**sp_offense** | **float** |  | 
**sp_defense** | **float** |  | 

## Example

```python
from cfbd.models.coach_season import CoachSeason

# TODO update the JSON string below
json = "{}"
# create an instance of CoachSeason from a JSON string
coach_season_instance = CoachSeason.from_json(json)
# print the JSON string representation of the object
print CoachSeason.to_json()

# convert the object into a dict
coach_season_dict = coach_season_instance.to_dict()
# create an instance of CoachSeason from a dict
coach_season_from_dict = CoachSeason.from_dict(coach_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


