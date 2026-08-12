# TeamConferenceChange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**team** | **str** |  | 
**from_conference_id** | **int** |  | 
**from_conference** | **str** |  | 
**from_conference_abbreviation** | **str** |  | 
**from_classification** | [**ConferenceClassification**](ConferenceClassification.md) |  | 
**to_conference_id** | **int** |  | 
**to_conference** | **str** |  | 
**to_conference_abbreviation** | **str** |  | 
**to_classification** | [**ConferenceClassification**](ConferenceClassification.md) |  | 
**effective_year** | **int** |  | 

## Example

```python
from cfbd.models.team_conference_change import TeamConferenceChange

# TODO update the JSON string below
json = "{}"
# create an instance of TeamConferenceChange from a JSON string
team_conference_change_instance = TeamConferenceChange.from_json(json)
# print the JSON string representation of the object
print TeamConferenceChange.to_json()

# convert the object into a dict
team_conference_change_dict = team_conference_change_instance.to_dict()
# create an instance of TeamConferenceChange from a dict
team_conference_change_from_dict = TeamConferenceChange.from_dict(team_conference_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


