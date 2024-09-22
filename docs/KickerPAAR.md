# KickerPAAR


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**athlete_id** | **str** |  | 
**athlete_name** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**paar** | **float** |  | 
**attempts** | **int** |  | 

## Example

```python
from cfbd.models.kicker_paar import KickerPAAR

# TODO update the JSON string below
json = "{}"
# create an instance of KickerPAAR from a JSON string
kicker_paar_instance = KickerPAAR.from_json(json)
# print the JSON string representation of the object
print KickerPAAR.to_json()

# convert the object into a dict
kicker_paar_dict = kicker_paar_instance.to_dict()
# create an instance of KickerPAAR from a dict
kicker_paar_from_dict = KickerPAAR.from_dict(kicker_paar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


