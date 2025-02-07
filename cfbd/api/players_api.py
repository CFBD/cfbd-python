# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.5.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictInt, StrictStr

from typing import List, Optional

from cfbd.models.player_search_result import PlayerSearchResult
from cfbd.models.player_transfer import PlayerTransfer
from cfbd.models.player_usage import PlayerUsage
from cfbd.models.returning_production import ReturningProduction

from cfbd.api_client import ApiClient
from cfbd.api_response import ApiResponse
from cfbd.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PlayersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_player_usage(self, year : Annotated[StrictInt, Field(..., description="Required year filter")], conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position abbreivation filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, player_id : Annotated[Optional[StrictInt], Field(description="Optional player id filter")] = None, exclude_garbage_time : Annotated[Optional[StrictBool], Field(description="Optional exclude garbage time flag, defaults to false")] = None, **kwargs) -> List[PlayerUsage]:  # noqa: E501
        """get_player_usage  # noqa: E501

        Retrieves player usage data for a given season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_player_usage(year, conference, position, team, player_id, exclude_garbage_time, async_req=True)
        >>> result = thread.get()

        :param year: Required year filter (required)
        :type year: int
        :param conference: Optional conference abbreviation filter
        :type conference: str
        :param position: Optional position abbreivation filter
        :type position: str
        :param team: Optional team filter
        :type team: str
        :param player_id: Optional player id filter
        :type player_id: int
        :param exclude_garbage_time: Optional exclude garbage time flag, defaults to false
        :type exclude_garbage_time: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayerUsage]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_player_usage_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_player_usage_with_http_info(year, conference, position, team, player_id, exclude_garbage_time, **kwargs)  # noqa: E501

    @validate_arguments
    def get_player_usage_with_http_info(self, year : Annotated[StrictInt, Field(..., description="Required year filter")], conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position abbreivation filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, player_id : Annotated[Optional[StrictInt], Field(description="Optional player id filter")] = None, exclude_garbage_time : Annotated[Optional[StrictBool], Field(description="Optional exclude garbage time flag, defaults to false")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_player_usage  # noqa: E501

        Retrieves player usage data for a given season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_player_usage_with_http_info(year, conference, position, team, player_id, exclude_garbage_time, async_req=True)
        >>> result = thread.get()

        :param year: Required year filter (required)
        :type year: int
        :param conference: Optional conference abbreviation filter
        :type conference: str
        :param position: Optional position abbreivation filter
        :type position: str
        :param team: Optional team filter
        :type team: str
        :param player_id: Optional player id filter
        :type player_id: int
        :param exclude_garbage_time: Optional exclude garbage time flag, defaults to false
        :type exclude_garbage_time: bool
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
        :rtype: tuple(List[PlayerUsage], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year',
            'conference',
            'position',
            'team',
            'player_id',
            'exclude_garbage_time'
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
                    " to method get_player_usage" % _key
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

        if _params.get('conference') is not None:  # noqa: E501
            _query_params.append(('conference', _params['conference']))

        if _params.get('position') is not None:  # noqa: E501
            _query_params.append(('position', _params['position']))

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        if _params.get('player_id') is not None:  # noqa: E501
            _query_params.append(('playerId', _params['player_id']))

        if _params.get('exclude_garbage_time') is not None:  # noqa: E501
            _query_params.append(('excludeGarbageTime', _params['exclude_garbage_time']))

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
            '200': "List[PlayerUsage]",
        }

        return self.api_client.call_api(
            '/player/usage', 'GET',
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
    def get_returning_production(self, year : Annotated[Optional[StrictInt], Field(description="Year filter, required if team not specified")] = None, team : Annotated[Optional[StrictStr], Field(description="Team filter, required if year not specified")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference filter")] = None, **kwargs) -> List[ReturningProduction]:  # noqa: E501
        """get_returning_production  # noqa: E501

        Retrieves returning production data. Either a year or team filter must be specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_returning_production(year, team, conference, async_req=True)
        >>> result = thread.get()

        :param year: Year filter, required if team not specified
        :type year: int
        :param team: Team filter, required if year not specified
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
        :rtype: List[ReturningProduction]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_returning_production_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_returning_production_with_http_info(year, team, conference, **kwargs)  # noqa: E501

    @validate_arguments
    def get_returning_production_with_http_info(self, year : Annotated[Optional[StrictInt], Field(description="Year filter, required if team not specified")] = None, team : Annotated[Optional[StrictStr], Field(description="Team filter, required if year not specified")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference filter")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_returning_production  # noqa: E501

        Retrieves returning production data. Either a year or team filter must be specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_returning_production_with_http_info(year, team, conference, async_req=True)
        >>> result = thread.get()

        :param year: Year filter, required if team not specified
        :type year: int
        :param team: Team filter, required if year not specified
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
        :rtype: tuple(List[ReturningProduction], status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_returning_production" % _key
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
            '200': "List[ReturningProduction]",
        }

        return self.api_client.call_api(
            '/player/returning', 'GET',
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
    def get_transfer_portal(self, year : Annotated[StrictInt, Field(..., description="Required year filter")], **kwargs) -> List[PlayerTransfer]:  # noqa: E501
        """get_transfer_portal  # noqa: E501

        Retrieves transfer portal data for a given year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transfer_portal(year, async_req=True)
        >>> result = thread.get()

        :param year: Required year filter (required)
        :type year: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayerTransfer]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_transfer_portal_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_transfer_portal_with_http_info(year, **kwargs)  # noqa: E501

    @validate_arguments
    def get_transfer_portal_with_http_info(self, year : Annotated[StrictInt, Field(..., description="Required year filter")], **kwargs) -> ApiResponse:  # noqa: E501
        """get_transfer_portal  # noqa: E501

        Retrieves transfer portal data for a given year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transfer_portal_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param year: Required year filter (required)
        :type year: int
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
        :rtype: tuple(List[PlayerTransfer], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year'
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
                    " to method get_transfer_portal" % _key
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
            '200': "List[PlayerTransfer]",
        }

        return self.api_client.call_api(
            '/player/portal', 'GET',
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
    def search_players(self, search_term : Annotated[StrictStr, Field(..., description="Search term for matching player name")], year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position abbreviation filter")] = None, **kwargs) -> List[PlayerSearchResult]:  # noqa: E501
        """search_players  # noqa: E501

        Search for players (lists top 100 results)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_players(search_term, year, team, position, async_req=True)
        >>> result = thread.get()

        :param search_term: Search term for matching player name (required)
        :type search_term: str
        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
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
        :rtype: List[PlayerSearchResult]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the search_players_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.search_players_with_http_info(search_term, year, team, position, **kwargs)  # noqa: E501

    @validate_arguments
    def search_players_with_http_info(self, search_term : Annotated[StrictStr, Field(..., description="Search term for matching player name")], year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position abbreviation filter")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """search_players  # noqa: E501

        Search for players (lists top 100 results)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_players_with_http_info(search_term, year, team, position, async_req=True)
        >>> result = thread.get()

        :param search_term: Search term for matching player name (required)
        :type search_term: str
        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
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
        :rtype: tuple(List[PlayerSearchResult], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'search_term',
            'year',
            'team',
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
                    " to method search_players" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('search_term') is not None:  # noqa: E501
            _query_params.append(('searchTerm', _params['search_term']))

        if _params.get('year') is not None:  # noqa: E501
            _query_params.append(('year', _params['year']))

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

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
            '200': "List[PlayerSearchResult]",
        }

        return self.api_client.call_api(
            '/player/search', 'GET',
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
