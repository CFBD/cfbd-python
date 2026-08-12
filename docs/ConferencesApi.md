# cfbd.ConferencesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conferences**](ConferencesApi.md#get_conferences) | **GET** /conferences | 
[**get_team_conference_affiliations**](ConferencesApi.md#get_team_conference_affiliations) | **GET** /conferences/affiliations | 
[**get_team_conference_changes**](ConferencesApi.md#get_team_conference_changes) | **GET** /conferences/changes | 


# **get_conferences**
> List[Conference] get_conferences(year=year, classification=classification)



Returns conferences and member counts.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.conference import Conference
from cfbd.models.conference_classification import ConferenceClassification
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
    api_instance = cfbd.ConferencesApi(api_client)
    year = 56 # int | Season year used to calculate membership. (optional)
    classification = cfbd.ConferenceClassification() # ConferenceClassification | Conference classification. (optional)

    try:
        api_response = api_instance.get_conferences(year=year, classification=classification)
        print("The response of ConferencesApi->get_conferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->get_conferences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year used to calculate membership. | [optional] 
 **classification** | [**ConferenceClassification**](.md)| Conference classification. | [optional] 

### Return type

[**List[Conference]**](Conference.md)

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

# **get_team_conference_affiliations**
> List[TeamConferenceAffiliation] get_team_conference_affiliations(team=team, conference=conference, year=year, min_year=min_year, max_year=max_year, classification=classification)



Returns historical team conference affiliations.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.conference_classification import ConferenceClassification
from cfbd.models.team_conference_affiliation import TeamConferenceAffiliation
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
    api_instance = cfbd.ConferencesApi(api_client)
    team = 'team_example' # str | Team school name or abbreviation. (optional)
    conference = 'conference_example' # str | Conference name or abbreviation. (optional)
    year = 56 # int | Season year. Cannot be combined with `minYear` or `maxYear`. (optional)
    min_year = 56 # int | Earliest season year to include. (optional)
    max_year = 56 # int | Latest season year to include. (optional)
    classification = cfbd.ConferenceClassification() # ConferenceClassification | Conference classification. (optional)

    try:
        api_response = api_instance.get_team_conference_affiliations(team=team, conference=conference, year=year, min_year=min_year, max_year=max_year, classification=classification)
        print("The response of ConferencesApi->get_team_conference_affiliations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->get_team_conference_affiliations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | **str**| Team school name or abbreviation. | [optional] 
 **conference** | **str**| Conference name or abbreviation. | [optional] 
 **year** | **int**| Season year. Cannot be combined with &#x60;minYear&#x60; or &#x60;maxYear&#x60;. | [optional] 
 **min_year** | **int**| Earliest season year to include. | [optional] 
 **max_year** | **int**| Latest season year to include. | [optional] 
 **classification** | [**ConferenceClassification**](.md)| Conference classification. | [optional] 

### Return type

[**List[TeamConferenceAffiliation]**](TeamConferenceAffiliation.md)

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

# **get_team_conference_changes**
> List[TeamConferenceChange] get_team_conference_changes(year)



Returns team conference changes by season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cfbd
from cfbd.models.team_conference_change import TeamConferenceChange
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
    api_instance = cfbd.ConferencesApi(api_client)
    year = 56 # int | Season year.

    try:
        api_response = api_instance.get_team_conference_changes(year)
        print("The response of ConferencesApi->get_team_conference_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->get_team_conference_changes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Season year. | 

### Return type

[**List[TeamConferenceChange]**](TeamConferenceChange.md)

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

