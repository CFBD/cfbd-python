# CoachCareer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**ties** | **int** |  | 
**win_percentage** | **float** |  | 
**seasons** | **int** |  | 
**teams** | **int** |  | 
**first_year** | **int** |  | 
**last_year** | **int** |  | 

## Example

```python
from cfbd.models.coach_career import CoachCareer

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCareer from a JSON string
coach_career_instance = CoachCareer.from_json(json)
# print the JSON string representation of the object
print CoachCareer.to_json()

# convert the object into a dict
coach_career_dict = coach_career_instance.to_dict()
# create an instance of CoachCareer from a dict
coach_career_from_dict = CoachCareer.from_dict(coach_career_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


