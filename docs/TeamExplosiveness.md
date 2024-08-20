# TeamExplosiveness


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**overall** | [**StatsByQuarter**](StatsByQuarter.md) |  | 

## Example

```python
from cfbd.models.team_explosiveness import TeamExplosiveness

# TODO update the JSON string below
json = "{}"
# create an instance of TeamExplosiveness from a JSON string
team_explosiveness_instance = TeamExplosiveness.from_json(json)
# print the JSON string representation of the object
print TeamExplosiveness.to_json()

# convert the object into a dict
team_explosiveness_dict = team_explosiveness_instance.to_dict()
# create an instance of TeamExplosiveness from a dict
team_explosiveness_from_dict = TeamExplosiveness.from_dict(team_explosiveness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


