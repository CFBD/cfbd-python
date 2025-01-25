# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.8
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictInt, StrictStr

from typing import List, Optional

from cfbd.models.division_classification import DivisionClassification
from cfbd.models.drive import Drive
from cfbd.models.season_type import SeasonType

from cfbd.api_client import ApiClient
from cfbd.api_response import ApiResponse
from cfbd.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DrivesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_drives(self, year : Annotated[StrictInt, Field(..., description="Required year filter")], season_type : Annotated[Optional[SeasonType], Field(description="Optional season type filter")] = None, week : Annotated[Optional[StrictInt], Field(description="Optional week filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, offense : Annotated[Optional[StrictStr], Field(description="Optional offensive team filter")] = None, defense : Annotated[Optional[StrictStr], Field(description="Optional defensive team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference filter")] = None, offense_conference : Annotated[Optional[StrictStr], Field(description="Optional offensive team conference filter")] = None, defense_conference : Annotated[Optional[StrictStr], Field(description="Optional defensive team conference filter")] = None, classification : Annotated[Optional[DivisionClassification], Field(description="Optional division classification filter")] = None, **kwargs) -> List[Drive]:  # noqa: E501
        """get_drives  # noqa: E501

        Retrieves historical drive data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_drives(year, season_type, week, team, offense, defense, conference, offense_conference, defense_conference, classification, async_req=True)
        >>> result = thread.get()

        :param year: Required year filter (required)
        :type year: int
        :param season_type: Optional season type filter
        :type season_type: SeasonType
        :param week: Optional week filter
        :type week: int
        :param team: Optional team filter
        :type team: str
        :param offense: Optional offensive team filter
        :type offense: str
        :param defense: Optional defensive team filter
        :type defense: str
        :param conference: Optional conference filter
        :type conference: str
        :param offense_conference: Optional offensive team conference filter
        :type offense_conference: str
        :param defense_conference: Optional defensive team conference filter
        :type defense_conference: str
        :param classification: Optional division classification filter
        :type classification: DivisionClassification
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[Drive]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_drives_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_drives_with_http_info(year, season_type, week, team, offense, defense, conference, offense_conference, defense_conference, classification, **kwargs)  # noqa: E501

    @validate_arguments
    def get_drives_with_http_info(self, year : Annotated[StrictInt, Field(..., description="Required year filter")], season_type : Annotated[Optional[SeasonType], Field(description="Optional season type filter")] = None, week : Annotated[Optional[StrictInt], Field(description="Optional week filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, offense : Annotated[Optional[StrictStr], Field(description="Optional offensive team filter")] = None, defense : Annotated[Optional[StrictStr], Field(description="Optional defensive team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference filter")] = None, offense_conference : Annotated[Optional[StrictStr], Field(description="Optional offensive team conference filter")] = None, defense_conference : Annotated[Optional[StrictStr], Field(description="Optional defensive team conference filter")] = None, classification : Annotated[Optional[DivisionClassification], Field(description="Optional division classification filter")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_drives  # noqa: E501

        Retrieves historical drive data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_drives_with_http_info(year, season_type, week, team, offense, defense, conference, offense_conference, defense_conference, classification, async_req=True)
        >>> result = thread.get()

        :param year: Required year filter (required)
        :type year: int
        :param season_type: Optional season type filter
        :type season_type: SeasonType
        :param week: Optional week filter
        :type week: int
        :param team: Optional team filter
        :type team: str
        :param offense: Optional offensive team filter
        :type offense: str
        :param defense: Optional defensive team filter
        :type defense: str
        :param conference: Optional conference filter
        :type conference: str
        :param offense_conference: Optional offensive team conference filter
        :type offense_conference: str
        :param defense_conference: Optional defensive team conference filter
        :type defense_conference: str
        :param classification: Optional division classification filter
        :type classification: DivisionClassification
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[Drive], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year',
            'season_type',
            'week',
            'team',
            'offense',
            'defense',
            'conference',
            'offense_conference',
            'defense_conference',
            'classification'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drives" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('year') is not None:  # noqa: E501
            _query_params.append(('year', _params['year']))

        if _params.get('season_type') is not None:  # noqa: E501
            _query_params.append(('seasonType', _params['season_type'].value))

        if _params.get('week') is not None:  # noqa: E501
            _query_params.append(('week', _params['week']))

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        if _params.get('offense') is not None:  # noqa: E501
            _query_params.append(('offense', _params['offense']))

        if _params.get('defense') is not None:  # noqa: E501
            _query_params.append(('defense', _params['defense']))

        if _params.get('conference') is not None:  # noqa: E501
            _query_params.append(('conference', _params['conference']))

        if _params.get('offense_conference') is not None:  # noqa: E501
            _query_params.append(('offenseConference', _params['offense_conference']))

        if _params.get('defense_conference') is not None:  # noqa: E501
            _query_params.append(('defenseConference', _params['defense_conference']))

        if _params.get('classification') is not None:  # noqa: E501
            _query_params.append(('classification', _params['classification'].value))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apiKey']  # noqa: E501

        _response_types_map = {
            '200': "List[Drive]",
        }

        return self.api_client.call_api(
            '/drives', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
