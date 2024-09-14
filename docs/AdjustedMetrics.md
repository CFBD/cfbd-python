# AdjustedMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**epa** | [**AdjustedMetricsEpa**](AdjustedMetricsEpa.md) |  | 
**epa_allowed** | [**AdjustedMetricsEpa**](AdjustedMetricsEpa.md) |  | 
**success_rate** | [**AdjustedMetricsSuccessRate**](AdjustedMetricsSuccessRate.md) |  | 
**success_rate_allowed** | [**AdjustedMetricsSuccessRate**](AdjustedMetricsSuccessRate.md) |  | 
**rushing** | [**AdjustedMetricsRushing**](AdjustedMetricsRushing.md) |  | 
**rushing_allowed** | [**AdjustedMetricsRushing**](AdjustedMetricsRushing.md) |  | 
**explosiveness** | **float** |  | 
**explosiveness_allowed** | **float** |  | 

## Example

```python
from cfbd.models.adjusted_metrics import AdjustedMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedMetrics from a JSON string
adjusted_metrics_instance = AdjustedMetrics.from_json(json)
# print the JSON string representation of the object
print AdjustedMetrics.to_json()

# convert the object into a dict
adjusted_metrics_dict = adjusted_metrics_instance.to_dict()
# create an instance of AdjustedMetrics from a dict
adjusted_metrics_from_dict = AdjustedMetrics.from_dict(adjusted_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


