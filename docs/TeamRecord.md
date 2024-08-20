# TeamRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**ties** | **int** |  | 

## Example

```python
from cfbd.models.team_record import TeamRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRecord from a JSON string
team_record_instance = TeamRecord.from_json(json)
# print the JSON string representation of the object
print TeamRecord.to_json()

# convert the object into a dict
team_record_dict = team_record_instance.to_dict()
# create an instance of TeamRecord from a dict
team_record_from_dict = TeamRecord.from_dict(team_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


