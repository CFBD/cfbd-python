# PlayerSuccessRateSplit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plays** | **int** |  | 
**successes** | **int** |  | 
**success_rate** | **float** |  | 

## Example

```python
from cfbd.models.player_success_rate_split import PlayerSuccessRateSplit

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSuccessRateSplit from a JSON string
player_success_rate_split_instance = PlayerSuccessRateSplit.from_json(json)
# print the JSON string representation of the object
print PlayerSuccessRateSplit.to_json()

# convert the object into a dict
player_success_rate_split_dict = player_success_rate_split_instance.to_dict()
# create an instance of PlayerSuccessRateSplit from a dict
player_success_rate_split_from_dict = PlayerSuccessRateSplit.from_dict(player_success_rate_split_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


