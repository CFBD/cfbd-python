# PassingLocations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_left** | [**PassingLocationProduction**](PassingLocationProduction.md) |  | 
**short_middle** | [**PassingLocationProduction**](PassingLocationProduction.md) |  | 
**short_right** | [**PassingLocationProduction**](PassingLocationProduction.md) |  | 
**deep_left** | [**PassingLocationProduction**](PassingLocationProduction.md) |  | 
**deep_middle** | [**PassingLocationProduction**](PassingLocationProduction.md) |  | 
**deep_right** | [**PassingLocationProduction**](PassingLocationProduction.md) |  | 
**unknown** | [**PassingLocationProduction**](PassingLocationProduction.md) |  | 

## Example

```python
from cfbd.models.passing_locations import PassingLocations

# TODO update the JSON string below
json = "{}"
# create an instance of PassingLocations from a JSON string
passing_locations_instance = PassingLocations.from_json(json)
# print the JSON string representation of the object
print PassingLocations.to_json()

# convert the object into a dict
passing_locations_dict = passing_locations_instance.to_dict()
# create an instance of PassingLocations from a dict
passing_locations_from_dict = PassingLocations.from_dict(passing_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


