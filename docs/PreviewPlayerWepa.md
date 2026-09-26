# PreviewPlayerWepa


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**year** | **int** |  | 
**athlete_id** | **str** |  | 
**athlete_name** | **str** |  | 
**position** | **str** |  | 
**conference** | **str** |  | 
**wepa** | **float** |  | 
**plays** | **int** |  | 

## Example

```python
from cfbd.models.preview_player_wepa import PreviewPlayerWepa

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewPlayerWepa from a JSON string
preview_player_wepa_instance = PreviewPlayerWepa.from_json(json)
# print the JSON string representation of the object
print PreviewPlayerWepa.to_json()

# convert the object into a dict
preview_player_wepa_dict = preview_player_wepa_instance.to_dict()
# create an instance of PreviewPlayerWepa from a dict
preview_player_wepa_from_dict = PreviewPlayerWepa.from_dict(preview_player_wepa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


