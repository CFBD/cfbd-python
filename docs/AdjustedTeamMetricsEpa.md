# AdjustedTeamMetricsEpa


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rushing** | **float** |  | 
**passing** | **float** |  | 
**total** | **float** |  | 

## Example

```python
from cfbd.models.adjusted_team_metrics_epa import AdjustedTeamMetricsEpa

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedTeamMetricsEpa from a JSON string
adjusted_team_metrics_epa_instance = AdjustedTeamMetricsEpa.from_json(json)
# print the JSON string representation of the object
print AdjustedTeamMetricsEpa.to_json()

# convert the object into a dict
adjusted_team_metrics_epa_dict = adjusted_team_metrics_epa_instance.to_dict()
# create an instance of AdjustedTeamMetricsEpa from a dict
adjusted_team_metrics_epa_from_dict = AdjustedTeamMetricsEpa.from_dict(adjusted_team_metrics_epa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


