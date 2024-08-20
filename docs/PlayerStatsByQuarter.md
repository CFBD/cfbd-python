# PlayerStatsByQuarter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**quarter1** | **float** |  | 
**quarter2** | **float** |  | 
**quarter3** | **float** |  | 
**quarter4** | **float** |  | 
**rushing** | **float** |  | 
**passing** | **float** |  | 

## Example

```python
from cfbd.models.player_stats_by_quarter import PlayerStatsByQuarter

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatsByQuarter from a JSON string
player_stats_by_quarter_instance = PlayerStatsByQuarter.from_json(json)
# print the JSON string representation of the object
print PlayerStatsByQuarter.to_json()

# convert the object into a dict
player_stats_by_quarter_dict = player_stats_by_quarter_instance.to_dict()
# create an instance of PlayerStatsByQuarter from a dict
player_stats_by_quarter_from_dict = PlayerStatsByQuarter.from_dict(player_stats_by_quarter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


