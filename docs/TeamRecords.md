# TeamRecords


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**classification** | [**DivisionClassification**](DivisionClassification.md) |  | 
**conference** | **str** |  | 
**division** | **str** |  | 
**expected_wins** | **float** |  | 
**total** | [**TeamRecord**](TeamRecord.md) |  | 
**conference_games** | [**TeamRecord**](TeamRecord.md) |  | 
**home_games** | [**TeamRecord**](TeamRecord.md) |  | 
**away_games** | [**TeamRecord**](TeamRecord.md) |  | 
**neutral_site_games** | [**TeamRecord**](TeamRecord.md) |  | 
**regular_season** | [**TeamRecord**](TeamRecord.md) |  | 
**postseason** | [**TeamRecord**](TeamRecord.md) |  | 

## Example

```python
from cfbd.models.team_records import TeamRecords

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRecords from a JSON string
team_records_instance = TeamRecords.from_json(json)
# print the JSON string representation of the object
print TeamRecords.to_json()

# convert the object into a dict
team_records_dict = team_records_instance.to_dict()
# create an instance of TeamRecords from a dict
team_records_from_dict = TeamRecords.from_dict(team_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


