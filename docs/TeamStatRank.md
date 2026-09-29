# TeamStatRank


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **float** |  | 
**population** | **float** |  | 
**tied** | **bool** |  | 
**percentile** | **float** |  | 

## Example

```python
from cfbd.models.team_stat_rank import TeamStatRank

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStatRank from a JSON string
team_stat_rank_instance = TeamStatRank.from_json(json)
# print the JSON string representation of the object
print TeamStatRank.to_json()

# convert the object into a dict
team_stat_rank_dict = team_stat_rank_instance.to_dict()
# create an instance of TeamStatRank from a dict
team_stat_rank_from_dict = TeamStatRank.from_dict(team_stat_rank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


