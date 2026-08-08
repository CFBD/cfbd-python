# cfbd.RatingsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conference_sp**](RatingsApi.md#get_conference_sp) | **GET** /ratings/sp/conferences | 
[**get_core**](RatingsApi.md#get_core) | **GET** /ratings/core | 
[**get_elo**](RatingsApi.md#get_elo) | **GET** /ratings/elo | 
[**get_expanded_srs**](RatingsApi.md#get_expanded_srs) | **GET** /ratings/srs/expanded | 
[**get_fpi**](RatingsApi.md#get_fpi) | **GET** /ratings/fpi | 
[**get_sp**](RatingsApi.md#get_sp) | **GET** /ratings/sp | 
[**get_srs**](RatingsApi.md#get_srs) | **GET** /ratings/srs | 


# **get_conference_sp**
> List[ConferenceSP] get_conference_sp(year=year, conference=conference, classification=classification)



Returns conference-level SP+ ratings by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.conference_sp import ConferenceSP
from cfbd.models.division_classification import DivisionClassification
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Season year. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification. Defaults to `fbs`. (optional)

    try:
        api_response = api_instance.get_conference_sp(year=year, conference=conference, classification=classification)
        print("The response of RatingsApi->get_conference_sp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_conference_sp: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification. Defaults to &#x60;fbs&#x60;. | [optional] 

### Return type

[**List[ConferenceSP]**](ConferenceSP.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_core**
> List[TeamCoreRating] get_core(year=year, team=team, conference=conference)



Returns Context & Opponent-Relative Efficiency (CORE) ratings.
At least one of `year` or `team` is required.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_core_rating import TeamCoreRating
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Exact team name. Required unless `year` is specified. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)

    try:
        api_response = api_instance.get_core(year=year, team=team, conference=conference)
        print("The response of RatingsApi->get_core:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_core: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Exact team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 

### Return type

[**List[TeamCoreRating]**](TeamCoreRating.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elo**
> List[TeamElo] get_elo(year=year, week=week, season_type=season_type, team=team, conference=conference)



Returns historical Elo ratings.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.season_type import SeasonType
from cfbd.models.team_elo import TeamElo
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Season year. (optional)
    week = 56 # int | Week number. Defaults to the latest available week in the season. (optional)
    season_type = cfbd.SeasonType() # SeasonType | Season type. (optional)
    team = 'team_example' # str | Team name. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)

    try:
        api_response = api_instance.get_elo(year=year, week=week, season_type=season_type, team=team, conference=conference)
        print("The response of RatingsApi->get_elo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_elo: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | [optional] 
 **week** | **int**| Week number. Defaults to the latest available week in the season. | [optional] 
 **season_type** | [**SeasonType**](.md)| Season type. | [optional] 
 **team** | **str**| Team name. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 

### Return type

[**List[TeamElo]**](TeamElo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expanded_srs**
> List[ExpandedTeamSRS] get_expanded_srs(year=year, team=team, conference=conference, classification=classification)



Returns expanded Simple Rating System (SRS) ratings, including FCS teams.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.expanded_team_srs import ExpandedTeamSRS
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    classification = cfbd.DivisionClassification() # DivisionClassification | Division classification: `fbs` or `fcs`. (optional)

    try:
        api_response = api_instance.get_expanded_srs(year=year, team=team, conference=conference, classification=classification)
        print("The response of RatingsApi->get_expanded_srs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_expanded_srs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **classification** | [**DivisionClassification**](.md)| Division classification: &#x60;fbs&#x60; or &#x60;fcs&#x60;. | [optional] 

### Return type

[**List[ExpandedTeamSRS]**](ExpandedTeamSRS.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fpi**
> List[TeamFPI] get_fpi(year=year, team=team, conference=conference)



Returns historical Football Power Index (FPI) ratings.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_fpi import TeamFPI
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)

    try:
        api_response = api_instance.get_fpi(year=year, team=team, conference=conference)
        print("The response of RatingsApi->get_fpi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_fpi: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 

### Return type

[**List[TeamFPI]**](TeamFPI.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp**
> List[TeamSP] get_sp(year=year, team=team)



Returns SP+ ratings by team and season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_sp import TeamSP
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)

    try:
        api_response = api_instance.get_sp(year=year, team=team)
        print("The response of RatingsApi->get_sp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_sp: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 

### Return type

[**List[TeamSP]**](TeamSP.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_srs**
> List[TeamSRS] get_srs(year=year, team=team, conference=conference)



Returns Simple Rating System (SRS) ratings by team and season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_srs import TeamSRS
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.RatingsApi(api_client)
    year = 56 # int | Season year. Required unless `team` is specified. (optional)
    team = 'team_example' # str | Team name. Required unless `year` is specified. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)

    try:
        api_response = api_instance.get_srs(year=year, team=team, conference=conference)
        print("The response of RatingsApi->get_srs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_srs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. Required unless &#x60;team&#x60; is specified. | [optional] 
 **team** | **str**| Team name. Required unless &#x60;year&#x60; is specified. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 

### Return type

[**List[TeamSRS]**](TeamSRS.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

