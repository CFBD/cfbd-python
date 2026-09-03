# RushingDirectionProduction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carries** | **int** |  | 
**yards** | **int** |  | 
**yards_per_carry** | **float** |  | 
**success_rate** | **float** |  | 
**ppa** | **float** |  | 
**total_ppa** | **float** |  | 
**line_yards** | **float** |  | 
**line_yards_total** | **float** |  | 
**second_level_yards** | **float** |  | 
**second_level_yards_total** | **float** |  | 
**open_field_yards** | **float** |  | 
**open_field_yards_total** | **float** |  | 
**stuff_rate** | **float** |  | 
**power_success** | **float** |  | 
**explosiveness** | **float** |  | 

## Example

```python
from cfbd.models.rushing_direction_production import RushingDirectionProduction

# TODO update the JSON string below
json = "{}"
# create an instance of RushingDirectionProduction from a JSON string
rushing_direction_production_instance = RushingDirectionProduction.from_json(json)
# print the JSON string representation of the object
print RushingDirectionProduction.to_json()

# convert the object into a dict
rushing_direction_production_dict = rushing_direction_production_instance.to_dict()
# create an instance of RushingDirectionProduction from a dict
rushing_direction_production_from_dict = RushingDirectionProduction.from_dict(rushing_direction_production_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


