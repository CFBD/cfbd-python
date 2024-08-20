# PlayerSearchResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**team** | **str** |  | 
**name** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**weight** | **int** |  | 
**height** | **int** |  | 
**jersey** | **int** |  | 
**position** | **str** |  | 
**hometown** | **str** |  | 
**team_color** | **str** |  | 
**team_color_secondary** | **str** |  | 

## Example

```python
from cfbd.models.player_search_result import PlayerSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSearchResult from a JSON string
player_search_result_instance = PlayerSearchResult.from_json(json)
# print the JSON string representation of the object
print PlayerSearchResult.to_json()

# convert the object into a dict
player_search_result_dict = player_search_result_instance.to_dict()
# create an instance of PlayerSearchResult from a dict
player_search_result_from_dict = PlayerSearchResult.from_dict(player_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


