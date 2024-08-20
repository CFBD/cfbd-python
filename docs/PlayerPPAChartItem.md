# PlayerPPAChartItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_number** | **int** |  | 
**avg_ppa** | **float** |  | 

## Example

```python
from cfbd.models.player_ppa_chart_item import PlayerPPAChartItem

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPPAChartItem from a JSON string
player_ppa_chart_item_instance = PlayerPPAChartItem.from_json(json)
# print the JSON string representation of the object
print PlayerPPAChartItem.to_json()

# convert the object into a dict
player_ppa_chart_item_dict = player_ppa_chart_item_instance.to_dict()
# create an instance of PlayerPPAChartItem from a dict
player_ppa_chart_item_from_dict = PlayerPPAChartItem.from_dict(player_ppa_chart_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


