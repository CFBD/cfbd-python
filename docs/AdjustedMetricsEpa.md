# AdjustedMetricsEpa


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rushing** | **float** |  | 
**passing** | **float** |  | 
**total** | **float** |  | 

## Example

```python
from cfbd.models.adjusted_metrics_epa import AdjustedMetricsEpa

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedMetricsEpa from a JSON string
adjusted_metrics_epa_instance = AdjustedMetricsEpa.from_json(json)
# print the JSON string representation of the object
print AdjustedMetricsEpa.to_json()

# convert the object into a dict
adjusted_metrics_epa_dict = adjusted_metrics_epa_instance.to_dict()
# create an instance of AdjustedMetricsEpa from a dict
adjusted_metrics_epa_from_dict = AdjustedMetricsEpa.from_dict(adjusted_metrics_epa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


