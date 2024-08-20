# ConferenceSPOffense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pace** | **float** |  | 
**run_rate** | **float** |  | 
**passing_downs** | **float** |  | 
**standard_downs** | **float** |  | 
**passing** | **float** |  | 
**rushing** | **float** |  | 
**explosiveness** | **float** |  | 
**success** | **float** |  | 
**rating** | **float** |  | 

## Example

```python
from cfbd.models.conference_sp_offense import ConferenceSPOffense

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceSPOffense from a JSON string
conference_sp_offense_instance = ConferenceSPOffense.from_json(json)
# print the JSON string representation of the object
print ConferenceSPOffense.to_json()

# convert the object into a dict
conference_sp_offense_dict = conference_sp_offense_instance.to_dict()
# create an instance of ConferenceSPOffense from a dict
conference_sp_offense_from_dict = ConferenceSPOffense.from_dict(conference_sp_offense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


