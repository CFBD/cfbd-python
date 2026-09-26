# PreviewKeyPlayers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**ppa** | [**PlayerSourceAvailability**](PlayerSourceAvailability.md) |  | 
**usage** | [**PlayerSourceAvailability**](PlayerSourceAvailability.md) |  | 
**passing** | [**PreviewSectionPreviewKeyPlayerArray**](PreviewSectionPreviewKeyPlayerArray.md) |  | 
**rushing** | [**PreviewSectionPreviewKeyPlayerArray**](PreviewSectionPreviewKeyPlayerArray.md) |  | 
**receiving** | [**PreviewSectionPreviewKeyPlayerArray**](PreviewSectionPreviewKeyPlayerArray.md) |  | 

## Example

```python
from cfbd.models.preview_key_players import PreviewKeyPlayers

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewKeyPlayers from a JSON string
preview_key_players_instance = PreviewKeyPlayers.from_json(json)
# print the JSON string representation of the object
print PreviewKeyPlayers.to_json()

# convert the object into a dict
preview_key_players_dict = preview_key_players_instance.to_dict()
# create an instance of PreviewKeyPlayers from a dict
preview_key_players_from_dict = PreviewKeyPlayers.from_dict(preview_key_players_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


