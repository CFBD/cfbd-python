# PreviewKeyPlayer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete_id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**usage** | **float** | Pass/rush involvement, not receiving target share. | 
**average_ppa** | **float** |  | 
**total_ppa** | **float** |  | 

## Example

```python
from cfbd.models.preview_key_player import PreviewKeyPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewKeyPlayer from a JSON string
preview_key_player_instance = PreviewKeyPlayer.from_json(json)
# print the JSON string representation of the object
print PreviewKeyPlayer.to_json()

# convert the object into a dict
preview_key_player_dict = preview_key_player_instance.to_dict()
# create an instance of PreviewKeyPlayer from a dict
preview_key_player_from_dict = PreviewKeyPlayer.from_dict(preview_key_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


