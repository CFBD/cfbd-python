# ConferenceSP


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**conference** | **str** |  | 
**rating** | **float** |  | 
**second_order_wins** | **float** |  | 
**sos** | **float** |  | 
**offense** | [**ConferenceSPOffense**](ConferenceSPOffense.md) |  | 
**defense** | [**ConferenceSPDefense**](ConferenceSPDefense.md) |  | 
**special_teams** | [**TeamSPSpecialTeams**](TeamSPSpecialTeams.md) |  | 

## Example

```python
from cfbd.models.conference_sp import ConferenceSP

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceSP from a JSON string
conference_sp_instance = ConferenceSP.from_json(json)
# print the JSON string representation of the object
print ConferenceSP.to_json()

# convert the object into a dict
conference_sp_dict = conference_sp_instance.to_dict()
# create an instance of ConferenceSP from a dict
conference_sp_from_dict = ConferenceSP.from_dict(conference_sp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


