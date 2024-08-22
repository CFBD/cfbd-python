# Coach


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**hire_date** | **datetime** |  | 
**seasons** | [**List[CoachSeason]**](CoachSeason.md) |  | 

## Example

```python
from cfbd.models.coach import Coach

# TODO update the JSON string below
json = "{}"
# create an instance of Coach from a JSON string
coach_instance = Coach.from_json(json)
# print the JSON string representation of the object
print Coach.to_json()

# convert the object into a dict
coach_dict = coach_instance.to_dict()
# create an instance of Coach from a dict
coach_from_dict = Coach.from_dict(coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


