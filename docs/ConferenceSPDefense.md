# ConferenceSPDefense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**havoc** | [**AdvancedSeasonStatOffenseHavoc**](AdvancedSeasonStatOffenseHavoc.md) |  | 
**passing_downs** | **float** |  | 
**standard_downs** | **float** |  | 
**passing** | **float** |  | 
**rushing** | **float** |  | 
**explosiveness** | **float** |  | 
**success** | **float** |  | 
**rating** | **float** |  | 

## Example

```python
from cfbd.models.conference_sp_defense import ConferenceSPDefense

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceSPDefense from a JSON string
conference_sp_defense_instance = ConferenceSPDefense.from_json(json)
# print the JSON string representation of the object
print ConferenceSPDefense.to_json()

# convert the object into a dict
conference_sp_defense_dict = conference_sp_defense_instance.to_dict()
# create an instance of ConferenceSPDefense from a dict
conference_sp_defense_from_dict = ConferenceSPDefense.from_dict(conference_sp_defense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


