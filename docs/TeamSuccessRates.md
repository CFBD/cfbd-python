# TeamSuccessRates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**overall** | [**StatsByQuarter**](StatsByQuarter.md) |  | 
**standard_downs** | [**StatsByQuarter**](StatsByQuarter.md) |  | 
**passing_downs** | [**StatsByQuarter**](StatsByQuarter.md) |  | 

## Example

```python
from cfbd.models.team_success_rates import TeamSuccessRates

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSuccessRates from a JSON string
team_success_rates_instance = TeamSuccessRates.from_json(json)
# print the JSON string representation of the object
print TeamSuccessRates.to_json()

# convert the object into a dict
team_success_rates_dict = team_success_rates_instance.to_dict()
# create an instance of TeamSuccessRates from a dict
team_success_rates_from_dict = TeamSuccessRates.from_dict(team_success_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


