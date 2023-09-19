# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.5.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class RankingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_rankings(self, year, **kwargs):  # noqa: E501
        """Historical polls and rankings  # noqa: E501

        Poll rankings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rankings(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year/season filter for games (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :return: list[RankingWeek]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rankings_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rankings_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_rankings_with_http_info(self, year, **kwargs):  # noqa: E501
        """Historical polls and rankings  # noqa: E501

        Poll rankings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rankings_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year/season filter for games (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :return: list[RankingWeek]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'season_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rankings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if self.api_client.client_side_validation and ('year' not in params or
                                                       params['year'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `year` when calling `get_rankings`")  # noqa: E501

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 1936):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_rankings`, must be a value greater than or equal to `1936`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_rankings`, must be a value less than or equal to `16`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_rankings`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'season_type' in params:
            query_params.append(('seasonType', params['season_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/rankings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RankingWeek]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
