# AdvancedBoxScoreTeams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_position** | [**List[TeamFieldPosition]**](TeamFieldPosition.md) |  | 
**scoring_opportunities** | [**List[TeamScoringOpportunities]**](TeamScoringOpportunities.md) |  | 
**havoc** | [**List[TeamHavoc]**](TeamHavoc.md) |  | 
**rushing** | [**List[TeamRushingStats]**](TeamRushingStats.md) |  | 
**explosiveness** | [**List[TeamExplosiveness]**](TeamExplosiveness.md) |  | 
**success_rates** | [**List[TeamSuccessRates]**](TeamSuccessRates.md) |  | 
**cumulative_ppa** | [**List[TeamPPA]**](TeamPPA.md) |  | 
**ppa** | [**List[TeamPPA]**](TeamPPA.md) |  | 

## Example

```python
from cfbd.models.advanced_box_score_teams import AdvancedBoxScoreTeams

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedBoxScoreTeams from a JSON string
advanced_box_score_teams_instance = AdvancedBoxScoreTeams.from_json(json)
# print the JSON string representation of the object
print AdvancedBoxScoreTeams.to_json()

# convert the object into a dict
advanced_box_score_teams_dict = advanced_box_score_teams_instance.to_dict()
# create an instance of AdvancedBoxScoreTeams from a dict
advanced_box_score_teams_from_dict = AdvancedBoxScoreTeams.from_dict(advanced_box_score_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


