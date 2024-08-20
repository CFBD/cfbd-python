# PlayerPPA


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **str** |  | 
**team** | **str** |  | 
**position** | **str** |  | 
**average** | [**PlayerStatsByQuarter**](PlayerStatsByQuarter.md) |  | 
**cumulative** | [**PlayerStatsByQuarter**](PlayerStatsByQuarter.md) |  | 

## Example

```python
from cfbd.models.player_ppa import PlayerPPA

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPPA from a JSON string
player_ppa_instance = PlayerPPA.from_json(json)
# print the JSON string representation of the object
print PlayerPPA.to_json()

# convert the object into a dict
player_ppa_dict = player_ppa_instance.to_dict()
# create an instance of PlayerPPA from a dict
player_ppa_from_dict = PlayerPPA.from_dict(player_ppa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


