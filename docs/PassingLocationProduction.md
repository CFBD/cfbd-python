# PassingLocationProduction

Production for analysis-eligible attempts in one location bucket.

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
**success_rate** | **float** | Successful eligible attempts / all eligible attempts; zero if empty. | 
**ppa** | **float** | Average available PPA on eligible attempts; zero if unavailable. | 
**total_ppa** | **float** | Sum of available PPA on eligible attempts; zero if unavailable. | 
**explosiveness** | **float** | Average available PPA on successful eligible attempts; zero if unavailable. | 
**ppa_attempts_available** | **int** | Eligible attempts with non-null PPA, including zero and negative values. | 
**success_attempts_available** | **int** | Eligible attempts with non-null success. Missing success remains in the success-rate denominator but does not count as successful. | 
**successful_attempts** | **int** | Eligible attempts with stored success equal to true. | 
**successful_ppa_attempts_available** | **int** | Successful eligible attempts with non-null PPA; explosiveness denominator. | 
**yards_per_attempt** | **float** | Total yards / attempts with total yards available; null if unavailable. | 
**air_yards_per_attempt** | **float** | Total air yards / attempts with air yards available; null if unavailable. Equivalent to averageDepthOfTarget. Yardage averages use one decimal. | 

## Example

```python
from cfbd.models.passing_location_production import PassingLocationProduction

# TODO update the JSON string below
json = "{}"
# create an instance of PassingLocationProduction from a JSON string
passing_location_production_instance = PassingLocationProduction.from_json(json)
# print the JSON string representation of the object
print PassingLocationProduction.to_json()

# convert the object into a dict
passing_location_production_dict = passing_location_production_instance.to_dict()
# create an instance of PassingLocationProduction from a dict
passing_location_production_from_dict = PassingLocationProduction.from_dict(passing_location_production_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


