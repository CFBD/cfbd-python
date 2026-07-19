# CfpPlayoff


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**competition** | [**PlayoffCompetitionCfp**](PlayoffCompetitionCfp.md) |  | 
**format** | **str** |  | 
**team_count** | **int** |  | 
**status** | [**PlayoffStatus**](PlayoffStatus.md) |  | 
**participants** | [**List[PlayoffParticipant]**](PlayoffParticipant.md) |  | 
**rounds** | [**List[PlayoffRoundRecord]**](PlayoffRoundRecord.md) |  | 
**champion** | [**PlayoffTeam**](PlayoffTeam.md) |  | 

## Example

```python
from cfbd.models.cfp_playoff import CfpPlayoff

# TODO update the JSON string below
json = "{}"
# create an instance of CfpPlayoff from a JSON string
cfp_playoff_instance = CfpPlayoff.from_json(json)
# print the JSON string representation of the object
print CfpPlayoff.to_json()

# convert the object into a dict
cfp_playoff_dict = cfp_playoff_instance.to_dict()
# create an instance of CfpPlayoff from a dict
cfp_playoff_from_dict = CfpPlayoff.from_dict(cfp_playoff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


