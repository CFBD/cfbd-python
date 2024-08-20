# TeamPPA


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**plays** | **int** |  | 
**overall** | [**StatsByQuarter**](StatsByQuarter.md) |  | 
**passing** | [**StatsByQuarter**](StatsByQuarter.md) |  | 
**rushing** | [**StatsByQuarter**](StatsByQuarter.md) |  | 

## Example

```python
from cfbd.models.team_ppa import TeamPPA

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPPA from a JSON string
team_ppa_instance = TeamPPA.from_json(json)
# print the JSON string representation of the object
print TeamPPA.to_json()

# convert the object into a dict
team_ppa_dict = team_ppa_instance.to_dict()
# create an instance of TeamPPA from a dict
team_ppa_from_dict = TeamPPA.from_dict(team_ppa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


