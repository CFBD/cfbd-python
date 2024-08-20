# Drive


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offense** | **str** |  | 
**offense_conference** | **str** |  | 
**defense** | **str** |  | 
**defense_conference** | **str** |  | 
**game_id** | **int** |  | 
**id** | **str** |  | 
**drive_number** | **int** |  | 
**scoring** | **bool** |  | 
**start_period** | **int** |  | 
**start_yardline** | **int** |  | 
**start_yards_to_goal** | **int** |  | 
**start_time** | [**PlayClock**](PlayClock.md) |  | 
**end_period** | **int** |  | 
**end_yardline** | **int** |  | 
**end_yards_to_goal** | **int** |  | 
**end_time** | [**PlayClock**](PlayClock.md) |  | 
**plays** | **int** |  | 
**yards** | **int** |  | 
**drive_result** | **str** |  | 
**is_home_offense** | **bool** |  | 
**start_offense_score** | **int** |  | 
**start_defense_score** | **int** |  | 
**end_offense_score** | **int** |  | 
**end_defense_score** | **int** |  | 

## Example

```python
from cfbd.models.drive import Drive

# TODO update the JSON string below
json = "{}"
# create an instance of Drive from a JSON string
drive_instance = Drive.from_json(json)
# print the JSON string representation of the object
print Drive.to_json()

# convert the object into a dict
drive_dict = drive_instance.to_dict()
# create an instance of Drive from a dict
drive_from_dict = Drive.from_dict(drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


