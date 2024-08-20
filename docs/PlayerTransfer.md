# PlayerTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**position** | **str** |  | 
**origin** | **str** |  | 
**destination** | **str** |  | 
**transfer_date** | **datetime** |  | 
**rating** | **float** |  | 
**stars** | **int** |  | 
**eligibility** | [**TransferEligibility**](TransferEligibility.md) |  | 

## Example

```python
from cfbd.models.player_transfer import PlayerTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerTransfer from a JSON string
player_transfer_instance = PlayerTransfer.from_json(json)
# print the JSON string representation of the object
print PlayerTransfer.to_json()

# convert the object into a dict
player_transfer_dict = player_transfer_instance.to_dict()
# create an instance of PlayerTransfer from a dict
player_transfer_from_dict = PlayerTransfer.from_dict(player_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


