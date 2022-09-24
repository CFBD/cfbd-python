# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.8
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class PlaysApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_live_plays(self, id, **kwargs):  # noqa: E501
        """Live metrics and PBP (Patreon only)  # noqa: E501

        Get live metrics and PBP  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_live_plays(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Game id (required)
        :return: LivePlayByPlay
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_live_plays_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_live_plays_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_live_plays_with_http_info(self, id, **kwargs):  # noqa: E501
        """Live metrics and PBP (Patreon only)  # noqa: E501

        Get live metrics and PBP  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_live_plays_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Game id (required)
        :return: LivePlayByPlay
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_live_plays" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_live_plays`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

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
            '/live/plays', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LivePlayByPlay',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_play_stat_types(self, **kwargs):  # noqa: E501
        """Types of player play stats  # noqa: E501

        Type of play stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_play_stat_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[PlayStatType]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_play_stat_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_play_stat_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_play_stat_types_with_http_info(self, **kwargs):  # noqa: E501
        """Types of player play stats  # noqa: E501

        Type of play stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_play_stat_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[PlayStatType]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_play_stat_types" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/play/stat/types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayStatType]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_play_stats(self, **kwargs):  # noqa: E501
        """Play stats by play  # noqa: E501

        Gets player stats associated by play (limit 1000)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_play_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param int week: Week filter
        :param str team: Team filter
        :param int game_id: gameId filter (from /games endpoint)
        :param int athlete_id: athleteId filter (from /roster endpoint)
        :param int stat_type_id: statTypeId filter (from /play/stat/types endpoint)
        :param str season_type: regular, postseason, or both
        :param str conference: conference abbreviation filter
        :return: list[PlayStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_play_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_play_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_play_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Play stats by play  # noqa: E501

        Gets player stats associated by play (limit 1000)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_play_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param int week: Week filter
        :param str team: Team filter
        :param int game_id: gameId filter (from /games endpoint)
        :param int athlete_id: athleteId filter (from /roster endpoint)
        :param int stat_type_id: statTypeId filter (from /play/stat/types endpoint)
        :param str season_type: regular, postseason, or both
        :param str conference: conference abbreviation filter
        :return: list[PlayStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'team', 'game_id', 'athlete_id', 'stat_type_id', 'season_type', 'conference']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_play_stats" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2013):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_play_stats`, must be a value greater than or equal to `2013`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_play_stats`, must be a value less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'game_id' in params:
            query_params.append(('gameId', params['game_id']))  # noqa: E501
        if 'athlete_id' in params:
            query_params.append(('athleteId', params['athlete_id']))  # noqa: E501
        if 'stat_type_id' in params:
            query_params.append(('statTypeId', params['stat_type_id']))  # noqa: E501
        if 'season_type' in params:
            query_params.append(('seasonType', params['season_type']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501

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
            '/play/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_play_types(self, **kwargs):  # noqa: E501
        """Play types  # noqa: E501

        Types of plays  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_play_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[PlayType]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_play_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_play_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_play_types_with_http_info(self, **kwargs):  # noqa: E501
        """Play types  # noqa: E501

        Types of plays  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_play_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[PlayType]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_play_types" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/play/types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayType]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_plays(self, year, week, **kwargs):  # noqa: E501
        """Play by play data  # noqa: E501

        Get play data and results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plays(year, week, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param int week: Week filter (required if team, offense, or defense, not specified) (required)
        :param str season_type: Season type filter
        :param str team: Team filter
        :param str offense: Offensive team filter
        :param str defense: Defensive team filter
        :param str conference: Conference filter
        :param str offense_conference: Offensive conference filter
        :param str defense_conference: Defensive conference filter
        :param int play_type: Play type filter
        :param str classification: Division classification filter (fbs/fcs/ii/iii)
        :return: list[Play]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_plays_with_http_info(year, week, **kwargs)  # noqa: E501
        else:
            (data) = self.get_plays_with_http_info(year, week, **kwargs)  # noqa: E501
            return data

    def get_plays_with_http_info(self, year, week, **kwargs):  # noqa: E501
        """Play by play data  # noqa: E501

        Get play data and results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plays_with_http_info(year, week, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param int week: Week filter (required if team, offense, or defense, not specified) (required)
        :param str season_type: Season type filter
        :param str team: Team filter
        :param str offense: Offensive team filter
        :param str defense: Defensive team filter
        :param str conference: Conference filter
        :param str offense_conference: Offensive conference filter
        :param str defense_conference: Defensive conference filter
        :param int play_type: Play type filter
        :param str classification: Division classification filter (fbs/fcs/ii/iii)
        :return: list[Play]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'season_type', 'team', 'offense', 'defense', 'conference', 'offense_conference', 'defense_conference', 'play_type', 'classification']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_plays" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if self.api_client.client_side_validation and ('year' not in params or
                                                       params['year'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `year` when calling `get_plays`")  # noqa: E501
        # verify the required parameter 'week' is set
        if self.api_client.client_side_validation and ('week' not in params or
                                                       params['week'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `week` when calling `get_plays`")  # noqa: E501

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2001):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_plays`, must be a value greater than or equal to `2001`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_plays`, must be a value less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'season_type' in params:
            query_params.append(('seasonType', params['season_type']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'offense' in params:
            query_params.append(('offense', params['offense']))  # noqa: E501
        if 'defense' in params:
            query_params.append(('defense', params['defense']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'offense_conference' in params:
            query_params.append(('offenseConference', params['offense_conference']))  # noqa: E501
        if 'defense_conference' in params:
            query_params.append(('defenseConference', params['defense_conference']))  # noqa: E501
        if 'play_type' in params:
            query_params.append(('playType', params['play_type']))  # noqa: E501
        if 'classification' in params:
            query_params.append(('classification', params['classification']))  # noqa: E501

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
            '/plays', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Play]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
