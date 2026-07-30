# CoachProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**display_name** | **str** |  | 
**current_team** | [**CoachSeasonTeamReference**](CoachSeasonTeamReference.md) |  | 
**career** | [**CoachCareer**](CoachCareer.md) |  | 
**birth_date** | **str** |  | 
**alma_mater** | [**CoachAlmaMater**](CoachAlmaMater.md) |  | 
**graduation_year** | **int** |  | 
**wikidata_id** | **str** |  | 
**hall_of_fame_year** | **int** |  | 

## Example

```python
from cfbd.models.coach_profile import CoachProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CoachProfile from a JSON string
coach_profile_instance = CoachProfile.from_json(json)
# print the JSON string representation of the object
print CoachProfile.to_json()

# convert the object into a dict
coach_profile_dict = coach_profile_instance.to_dict()
# create an instance of CoachProfile from a dict
coach_profile_from_dict = CoachProfile.from_dict(coach_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


