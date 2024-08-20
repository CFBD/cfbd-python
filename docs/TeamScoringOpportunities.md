# TeamScoringOpportunities


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**opportunities** | **int** |  | 
**points** | **int** |  | 
**points_per_opportunity** | **float** |  | 

## Example

```python
from cfbd.models.team_scoring_opportunities import TeamScoringOpportunities

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScoringOpportunities from a JSON string
team_scoring_opportunities_instance = TeamScoringOpportunities.from_json(json)
# print the JSON string representation of the object
print TeamScoringOpportunities.to_json()

# convert the object into a dict
team_scoring_opportunities_dict = team_scoring_opportunities_instance.to_dict()
# create an instance of TeamScoringOpportunities from a dict
team_scoring_opportunities_from_dict = TeamScoringOpportunities.from_dict(team_scoring_opportunities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


