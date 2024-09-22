# PlayerWeightedEPA


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**athlete_id** | **str** |  | 
**athlete_name** | **str** |  | 
**position** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**wepa** | **float** |  | 
**plays** | **int** |  | 

## Example

```python
from cfbd.models.player_weighted_epa import PlayerWeightedEPA

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerWeightedEPA from a JSON string
player_weighted_epa_instance = PlayerWeightedEPA.from_json(json)
# print the JSON string representation of the object
print PlayerWeightedEPA.to_json()

# convert the object into a dict
player_weighted_epa_dict = player_weighted_epa_instance.to_dict()
# create an instance of PlayerWeightedEPA from a dict
player_weighted_epa_from_dict = PlayerWeightedEPA.from_dict(player_weighted_epa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


