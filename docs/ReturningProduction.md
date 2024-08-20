# ReturningProduction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**total_ppa** | **float** |  | 
**total_passing_ppa** | **float** |  | 
**total_receiving_ppa** | **float** |  | 
**total_rushing_ppa** | **float** |  | 
**percent_ppa** | **float** |  | 
**percent_passing_ppa** | **float** |  | 
**percent_receiving_ppa** | **float** |  | 
**percent_rushing_ppa** | **float** |  | 
**usage** | **float** |  | 
**passing_usage** | **float** |  | 
**receiving_usage** | **float** |  | 
**rushing_usage** | **float** |  | 

## Example

```python
from cfbd.models.returning_production import ReturningProduction

# TODO update the JSON string below
json = "{}"
# create an instance of ReturningProduction from a JSON string
returning_production_instance = ReturningProduction.from_json(json)
# print the JSON string representation of the object
print ReturningProduction.to_json()

# convert the object into a dict
returning_production_dict = returning_production_instance.to_dict()
# create an instance of ReturningProduction from a dict
returning_production_from_dict = ReturningProduction.from_dict(returning_production_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


