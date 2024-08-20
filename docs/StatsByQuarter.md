# StatsByQuarter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**quarter1** | **float** |  | 
**quarter2** | **float** |  | 
**quarter3** | **float** |  | 
**quarter4** | **float** |  | 

## Example

```python
from cfbd.models.stats_by_quarter import StatsByQuarter

# TODO update the JSON string below
json = "{}"
# create an instance of StatsByQuarter from a JSON string
stats_by_quarter_instance = StatsByQuarter.from_json(json)
# print the JSON string representation of the object
print StatsByQuarter.to_json()

# convert the object into a dict
stats_by_quarter_dict = stats_by_quarter_instance.to_dict()
# create an instance of StatsByQuarter from a dict
stats_by_quarter_from_dict = StatsByQuarter.from_dict(stats_by_quarter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


