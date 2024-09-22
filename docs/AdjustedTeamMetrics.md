# AdjustedTeamMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**epa** | [**AdjustedTeamMetricsEpa**](AdjustedTeamMetricsEpa.md) |  | 
**epa_allowed** | [**AdjustedTeamMetricsEpa**](AdjustedTeamMetricsEpa.md) |  | 
**success_rate** | [**AdjustedTeamMetricsSuccessRate**](AdjustedTeamMetricsSuccessRate.md) |  | 
**success_rate_allowed** | [**AdjustedTeamMetricsSuccessRate**](AdjustedTeamMetricsSuccessRate.md) |  | 
**rushing** | [**AdjustedTeamMetricsRushing**](AdjustedTeamMetricsRushing.md) |  | 
**rushing_allowed** | [**AdjustedTeamMetricsRushing**](AdjustedTeamMetricsRushing.md) |  | 
**explosiveness** | **float** |  | 
**explosiveness_allowed** | **float** |  | 

## Example

```python
from cfbd.models.adjusted_team_metrics import AdjustedTeamMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedTeamMetrics from a JSON string
adjusted_team_metrics_instance = AdjustedTeamMetrics.from_json(json)
# print the JSON string representation of the object
print AdjustedTeamMetrics.to_json()

# convert the object into a dict
adjusted_team_metrics_dict = adjusted_team_metrics_instance.to_dict()
# create an instance of AdjustedTeamMetrics from a dict
adjusted_team_metrics_from_dict = AdjustedTeamMetrics.from_dict(adjusted_team_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


