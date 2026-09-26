# SelectedOdds


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **int** |  | 
**provider** | **str** |  | 
**spread** | **float** | Home-relative spread; negative favors home. | 
**over_under** | **float** |  | 
**home_moneyline** | **float** |  | 
**away_moneyline** | **float** |  | 

## Example

```python
from cfbd.models.selected_odds import SelectedOdds

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedOdds from a JSON string
selected_odds_instance = SelectedOdds.from_json(json)
# print the JSON string representation of the object
print SelectedOdds.to_json()

# convert the object into a dict
selected_odds_dict = selected_odds_instance.to_dict()
# create an instance of SelectedOdds from a dict
selected_odds_from_dict = SelectedOdds.from_dict(selected_odds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


