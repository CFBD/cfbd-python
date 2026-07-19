# PlayoffAdvancement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchup_id** | **int** |  | 
**bracket_slot** | **str** |  | 
**position** | **int** |  | 

## Example

```python
from cfbd.models.playoff_advancement import PlayoffAdvancement

# TODO update the JSON string below
json = "{}"
# create an instance of PlayoffAdvancement from a JSON string
playoff_advancement_instance = PlayoffAdvancement.from_json(json)
# print the JSON string representation of the object
print PlayoffAdvancement.to_json()

# convert the object into a dict
playoff_advancement_dict = playoff_advancement_instance.to_dict()
# create an instance of PlayoffAdvancement from a dict
playoff_advancement_from_dict = PlayoffAdvancement.from_dict(playoff_advancement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


