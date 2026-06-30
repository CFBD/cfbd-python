# UserFeatureAccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_metrics** | **bool** |  | 
**weather** | **bool** |  | 
**scoreboard** | **bool** |  | 
**live_play_by_play** | **bool** |  | 
**graph_ql** | **bool** |  | 

## Example

```python
from cfbd.models.user_feature_access import UserFeatureAccess

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeatureAccess from a JSON string
user_feature_access_instance = UserFeatureAccess.from_json(json)
# print the JSON string representation of the object
print UserFeatureAccess.to_json()

# convert the object into a dict
user_feature_access_dict = user_feature_access_instance.to_dict()
# create an instance of UserFeatureAccess from a dict
user_feature_access_from_dict = UserFeatureAccess.from_dict(user_feature_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


