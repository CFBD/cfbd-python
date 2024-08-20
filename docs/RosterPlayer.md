# RosterPlayer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**team** | **str** |  | 
**height** | **int** |  | 
**weight** | **int** |  | 
**jersey** | **int** |  | 
**year** | **int** |  | 
**position** | **str** |  | 
**home_city** | **str** |  | 
**home_state** | **str** |  | 
**home_country** | **str** |  | 
**home_latitude** | **float** |  | 
**home_longitude** | **float** |  | 
**home_county_fips** | **str** |  | 
**recruit_ids** | **List[str]** |  | 

## Example

```python
from cfbd.models.roster_player import RosterPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of RosterPlayer from a JSON string
roster_player_instance = RosterPlayer.from_json(json)
# print the JSON string representation of the object
print RosterPlayer.to_json()

# convert the object into a dict
roster_player_dict = roster_player_instance.to_dict()
# create an instance of RosterPlayer from a dict
roster_player_from_dict = RosterPlayer.from_dict(roster_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


