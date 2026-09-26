# PlayerSourceAvailability


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 
**assembled_at** | **datetime** |  | 
**source_updated_at** | **datetime** |  | 

## Example

```python
from cfbd.models.player_source_availability import PlayerSourceAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSourceAvailability from a JSON string
player_source_availability_instance = PlayerSourceAvailability.from_json(json)
# print the JSON string representation of the object
print PlayerSourceAvailability.to_json()

# convert the object into a dict
player_source_availability_dict = player_source_availability_instance.to_dict()
# create an instance of PlayerSourceAvailability from a dict
player_source_availability_from_dict = PlayerSourceAvailability.from_dict(player_source_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


