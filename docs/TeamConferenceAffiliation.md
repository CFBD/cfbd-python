# TeamConferenceAffiliation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference_id** | **int** |  | 
**conference** | **str** |  | 
**conference_abbreviation** | **str** |  | 
**classification** | [**ConferenceClassification**](ConferenceClassification.md) |  | 
**conference_division** | **str** |  | 
**start_year** | **int** |  | 
**end_year** | **int** |  | 

## Example

```python
from cfbd.models.team_conference_affiliation import TeamConferenceAffiliation

# TODO update the JSON string below
json = "{}"
# create an instance of TeamConferenceAffiliation from a JSON string
team_conference_affiliation_instance = TeamConferenceAffiliation.from_json(json)
# print the JSON string representation of the object
print TeamConferenceAffiliation.to_json()

# convert the object into a dict
team_conference_affiliation_dict = team_conference_affiliation_instance.to_dict()
# create an instance of TeamConferenceAffiliation from a dict
team_conference_affiliation_from_dict = TeamConferenceAffiliation.from_dict(team_conference_affiliation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


