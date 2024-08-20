# AggregatedTeamRecruiting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**conference** | **str** |  | 
**position_group** | **str** |  | 
**average_rating** | **float** |  | 
**total_rating** | **float** |  | 
**commits** | **int** |  | 
**average_stars** | **float** |  | 

## Example

```python
from cfbd.models.aggregated_team_recruiting import AggregatedTeamRecruiting

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedTeamRecruiting from a JSON string
aggregated_team_recruiting_instance = AggregatedTeamRecruiting.from_json(json)
# print the JSON string representation of the object
print AggregatedTeamRecruiting.to_json()

# convert the object into a dict
aggregated_team_recruiting_dict = aggregated_team_recruiting_instance.to_dict()
# create an instance of AggregatedTeamRecruiting from a dict
aggregated_team_recruiting_from_dict = AggregatedTeamRecruiting.from_dict(aggregated_team_recruiting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


