# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.9
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

from cfbd.models.adjusted_team_metrics import AdjustedTeamMetrics
from cfbd.models.kicker_paar import KickerPAAR
from cfbd.models.player_weighted_epa import PlayerWeightedEPA

from cfbd.api_client import ApiClient
from cfbd.api_response import ApiResponse
from cfbd.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AdjustedMetricsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_adjusted_player_passing_stats(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position abbreviation filter")] = None, **kwargs) -> List[PlayerWeightedEPA]:  # noqa: E501
        """get_adjusted_player_passing_stats  # noqa: E501

        Retrieve opponent-adjusted player passing statistics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_adjusted_player_passing_stats(year, team, conference, position, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference abbreviation filter
        :type conference: str
        :param position: Optional position abbreviation filter
        :type position: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayerWeightedEPA]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_adjusted_player_passing_stats_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_adjusted_player_passing_stats_with_http_info(year, team, conference, position, **kwargs)  # noqa: E501

    @validate_arguments
    def get_adjusted_player_passing_stats_with_http_info(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position abbreviation filter")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_adjusted_player_passing_stats  # noqa: E501

        Retrieve opponent-adjusted player passing statistics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_adjusted_player_passing_stats_with_http_info(year, team, conference, position, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference abbreviation filter
        :type conference: str
        :param position: Optional position abbreviation filter
        :type position: str
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
        :rtype: tuple(List[PlayerWeightedEPA], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year',
            'team',
            'conference',
            'position'
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
                    " to method get_adjusted_player_passing_stats" % _key
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

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        if _params.get('conference') is not None:  # noqa: E501
            _query_params.append(('conference', _params['conference']))

        if _params.get('position') is not None:  # noqa: E501
            _query_params.append(('position', _params['position']))

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
            '200': "List[PlayerWeightedEPA]",
        }

        return self.api_client.call_api(
            '/wepa/players/passing', 'GET',
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

    @validate_arguments
    def get_adjusted_player_rushing_stats(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position abbreviation filter")] = None, **kwargs) -> List[PlayerWeightedEPA]:  # noqa: E501
        """get_adjusted_player_rushing_stats  # noqa: E501

        Retrieve opponent-adjusted player rushing statistics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_adjusted_player_rushing_stats(year, team, conference, position, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference abbreviation filter
        :type conference: str
        :param position: Optional position abbreviation filter
        :type position: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayerWeightedEPA]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_adjusted_player_rushing_stats_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_adjusted_player_rushing_stats_with_http_info(year, team, conference, position, **kwargs)  # noqa: E501

    @validate_arguments
    def get_adjusted_player_rushing_stats_with_http_info(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position abbreviation filter")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_adjusted_player_rushing_stats  # noqa: E501

        Retrieve opponent-adjusted player rushing statistics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_adjusted_player_rushing_stats_with_http_info(year, team, conference, position, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference abbreviation filter
        :type conference: str
        :param position: Optional position abbreviation filter
        :type position: str
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
        :rtype: tuple(List[PlayerWeightedEPA], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year',
            'team',
            'conference',
            'position'
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
                    " to method get_adjusted_player_rushing_stats" % _key
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

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        if _params.get('conference') is not None:  # noqa: E501
            _query_params.append(('conference', _params['conference']))

        if _params.get('position') is not None:  # noqa: E501
            _query_params.append(('position', _params['position']))

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
            '200': "List[PlayerWeightedEPA]",
        }

        return self.api_client.call_api(
            '/wepa/players/rushing', 'GET',
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

    @validate_arguments
    def get_adjusted_team_season_stats(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference filter")] = None, **kwargs) -> List[AdjustedTeamMetrics]:  # noqa: E501
        """get_adjusted_team_season_stats  # noqa: E501

        Retrieve opponent-adjusted team season statistics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_adjusted_team_season_stats(year, team, conference, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference filter
        :type conference: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[AdjustedTeamMetrics]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_adjusted_team_season_stats_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_adjusted_team_season_stats_with_http_info(year, team, conference, **kwargs)  # noqa: E501

    @validate_arguments
    def get_adjusted_team_season_stats_with_http_info(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference filter")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_adjusted_team_season_stats  # noqa: E501

        Retrieve opponent-adjusted team season statistics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_adjusted_team_season_stats_with_http_info(year, team, conference, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference filter
        :type conference: str
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
        :rtype: tuple(List[AdjustedTeamMetrics], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year',
            'team',
            'conference'
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
                    " to method get_adjusted_team_season_stats" % _key
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

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        if _params.get('conference') is not None:  # noqa: E501
            _query_params.append(('conference', _params['conference']))

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
            '200': "List[AdjustedTeamMetrics]",
        }

        return self.api_client.call_api(
            '/wepa/team/season', 'GET',
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

    @validate_arguments
    def get_kicker_paar(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, **kwargs) -> List[KickerPAAR]:  # noqa: E501
        """get_kicker_paar  # noqa: E501

        Retrieve Points Added Above Replacement (PAAR) ratings for kickers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_kicker_paar(year, team, conference, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference abbreviation filter
        :type conference: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[KickerPAAR]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_kicker_paar_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_kicker_paar_with_http_info(year, team, conference, **kwargs)  # noqa: E501

    @validate_arguments
    def get_kicker_paar_with_http_info(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_kicker_paar  # noqa: E501

        Retrieve Points Added Above Replacement (PAAR) ratings for kickers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_kicker_paar_with_http_info(year, team, conference, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference abbreviation filter
        :type conference: str
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
        :rtype: tuple(List[KickerPAAR], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year',
            'team',
            'conference'
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
                    " to method get_kicker_paar" % _key
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

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        if _params.get('conference') is not None:  # noqa: E501
            _query_params.append(('conference', _params['conference']))

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
            '200': "List[KickerPAAR]",
        }

        return self.api_client.call_api(
            '/wepa/players/kicking', 'GET',
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
