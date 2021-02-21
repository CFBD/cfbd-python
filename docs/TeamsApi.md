# cfbd.TeamsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fbs_teams**](TeamsApi.md#get_fbs_teams) | **GET** /teams/fbs | FBS team list
[**get_roster**](TeamsApi.md#get_roster) | **GET** /roster | Team rosters
[**get_talent**](TeamsApi.md#get_talent) | **GET** /talent | Team talent composite rankings
[**get_team_matchup**](TeamsApi.md#get_team_matchup) | **GET** /teams/matchup | Team matchup history
[**get_teams**](TeamsApi.md#get_teams) | **GET** /teams | Team information


# **get_fbs_teams**
> list[Team] get_fbs_teams(year=year)

FBS team list

Information on major division teams

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter (optional)

try:
    # FBS team list
    api_response = api_instance.get_fbs_teams(year=year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_fbs_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [optional] 

### Return type

[**list[Team]**](Team.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roster**
> list[Player] get_roster(team=team, year=year)

Team rosters

Roster data

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
team = 'team_example' # str | Team name (optional)
year = 56 # int | Season year (optional)

try:
    # Team rosters
    api_response = api_instance.get_roster(team=team, year=year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_roster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | **str**| Team name | [optional] 
 **year** | **int**| Season year | [optional] 

### Return type

[**list[Player]**](Player.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_talent**
> list[TeamTalent] get_talent(year=year)

Team talent composite rankings

Team talent composite

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
year = 56 # int | Year filter (optional)

try:
    # Team talent composite rankings
    api_response = api_instance.get_talent(year=year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_talent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year filter | [optional] 

### Return type

[**list[TeamTalent]**](TeamTalent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_matchup**
> list[TeamMatchup] get_team_matchup(team1, team2, min_year=min_year, max_year=max_year)

Team matchup history

Matchup history

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
team1 = 'team1_example' # str | First team
team2 = 'team2_example' # str | Second team
min_year = 56 # int | Minimum year (optional)
max_year = 56 # int | Maximum year (optional)

try:
    # Team matchup history
    api_response = api_instance.get_team_matchup(team1, team2, min_year=min_year, max_year=max_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_matchup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team1** | **str**| First team | 
 **team2** | **str**| Second team | 
 **min_year** | **int**| Minimum year | [optional] 
 **max_year** | **int**| Maximum year | [optional] 

### Return type

[**list[TeamMatchup]**](TeamMatchup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> list[Team] get_teams(conference=conference)

Team information

Get team information

### Example
```python
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
conference = 'conference_example' # str | Conference abbreviation filter (optional)

try:
    # Team information
    api_response = api_instance.get_teams(conference=conference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conference** | **str**| Conference abbreviation filter | [optional] 

### Return type

[**list[Team]**](Team.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

