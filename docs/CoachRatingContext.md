# CoachRatingContext


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sp_special_teams** | **float** |  | 
**strength_of_schedule** | **float** |  | 
**second_order_wins** | **float** |  | 
**fpi** | **float** |  | 
**year_over_year** | [**CoachRatingContextYearOverYear**](CoachRatingContextYearOverYear.md) |  | 

## Example

```python
from cfbd.models.coach_rating_context import CoachRatingContext

# TODO update the JSON string below
json = "{}"
# create an instance of CoachRatingContext from a JSON string
coach_rating_context_instance = CoachRatingContext.from_json(json)
# print the JSON string representation of the object
print CoachRatingContext.to_json()

# convert the object into a dict
coach_rating_context_dict = coach_rating_context_instance.to_dict()
# create an instance of CoachRatingContext from a dict
coach_rating_context_from_dict = CoachRatingContext.from_dict(coach_rating_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


