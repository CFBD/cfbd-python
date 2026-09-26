# PreviewKickerPaar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**year** | **int** |  | 
**athlete_id** | **str** |  | 
**athlete_name** | **str** |  | 
**conference** | **str** |  | 
**paar** | **float** |  | 
**attempts** | **int** |  | 

## Example

```python
from cfbd.models.preview_kicker_paar import PreviewKickerPaar

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewKickerPaar from a JSON string
preview_kicker_paar_instance = PreviewKickerPaar.from_json(json)
# print the JSON string representation of the object
print PreviewKickerPaar.to_json()

# convert the object into a dict
preview_kicker_paar_dict = preview_kicker_paar_instance.to_dict()
# create an instance of PreviewKickerPaar from a dict
preview_kicker_paar_from_dict = PreviewKickerPaar.from_dict(preview_kicker_paar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


