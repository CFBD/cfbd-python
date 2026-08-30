# PassingProduction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int** |  | 
**completions** | **int** |  | 
**incompletions** | **int** |  | 
**interceptions** | **int** |  | 
**completion_rate** | **float** |  | 
**air_yards_attempts_available** | **int** | Number of attempts with non-null air yards, including zero-yard values. | 
**total_air_yards** | **int** |  | 
**average_depth_of_target** | **float** |  | 
**total_yards_attempts_available** | **int** | Number of attempts with non-null total yards, including zero-yard incompletions and interceptions. | 
**total_yards** | **int** |  | 
**yards_after_catch_attempts_available** | **int** | Number of completed attempts with valid total yards and air yards to calculate yards after catch, including zero-yard values. | 
**total_yards_after_catch** | **int** |  | 
**average_yards_after_catch** | **float** |  | 

## Example

```python
from cfbd.models.passing_production import PassingProduction

# TODO update the JSON string below
json = "{}"
# create an instance of PassingProduction from a JSON string
passing_production_instance = PassingProduction.from_json(json)
# print the JSON string representation of the object
print PassingProduction.to_json()

# convert the object into a dict
passing_production_dict = passing_production_instance.to_dict()
# create an instance of PassingProduction from a dict
passing_production_from_dict = PassingProduction.from_dict(passing_production_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


