# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.12
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class MetricsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_game_ppa(self, year, **kwargs):  # noqa: E501
        """Team Predicated Points Added (PPA/EPA) by game  # noqa: E501

        Predicted Points Added (PPA) by game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_game_ppa(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param int week: Week filter
        :param str team: Team filter
        :param str conference: Conference filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :param str season_type: Season type filter (regular or postseason)
        :return: list[GamePPA]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_game_ppa_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_game_ppa_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_game_ppa_with_http_info(self, year, **kwargs):  # noqa: E501
        """Team Predicated Points Added (PPA/EPA) by game  # noqa: E501

        Predicted Points Added (PPA) by game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_game_ppa_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param int week: Week filter
        :param str team: Team filter
        :param str conference: Conference filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :param str season_type: Season type filter (regular or postseason)
        :return: list[GamePPA]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'team', 'conference', 'exclude_garbage_time', 'season_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_game_ppa" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if self.api_client.client_side_validation and ('year' not in params or
                                                       params['year'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `year` when calling `get_game_ppa`")  # noqa: E501

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2001):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_game_ppa`, must be a value greater than or equal to `2001`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_game_ppa`, must be a value less than or equal to `16`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_game_ppa`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'exclude_garbage_time' in params:
            query_params.append(('excludeGarbageTime', params['exclude_garbage_time']))  # noqa: E501
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
            '/ppa/games', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GamePPA]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_game_ppa(self, **kwargs):  # noqa: E501
        """Player Predicated Points Added (PPA/EPA) broken down by game  # noqa: E501

        Predicted Points Added (PPA) by player game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_game_ppa(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param int week: Week filter
        :param str team: Team filter
        :param str position: Position abbreviation filter
        :param int player_id: Player id filter
        :param str threshold: Minimum play threshold filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :param str season_type: Season type filter (regular or postseason)
        :return: list[PlayerGamePPA]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_game_ppa_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_player_game_ppa_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_player_game_ppa_with_http_info(self, **kwargs):  # noqa: E501
        """Player Predicated Points Added (PPA/EPA) broken down by game  # noqa: E501

        Predicted Points Added (PPA) by player game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_game_ppa_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param int week: Week filter
        :param str team: Team filter
        :param str position: Position abbreviation filter
        :param int player_id: Player id filter
        :param str threshold: Minimum play threshold filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :param str season_type: Season type filter (regular or postseason)
        :return: list[PlayerGamePPA]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'team', 'position', 'player_id', 'threshold', 'exclude_garbage_time', 'season_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_game_ppa" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2013):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_player_game_ppa`, must be a value greater than or equal to `2013`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_player_game_ppa`, must be a value less than or equal to `16`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_player_game_ppa`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'position' in params:
            query_params.append(('position', params['position']))  # noqa: E501
        if 'player_id' in params:
            query_params.append(('playerId', params['player_id']))  # noqa: E501
        if 'threshold' in params:
            query_params.append(('threshold', params['threshold']))  # noqa: E501
        if 'exclude_garbage_time' in params:
            query_params.append(('excludeGarbageTime', params['exclude_garbage_time']))  # noqa: E501
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
            '/ppa/players/games', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayerGamePPA]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_season_ppa(self, **kwargs):  # noqa: E501
        """Player Predicated Points Added (PPA/EPA) broken down by season  # noqa: E501

        Predicted Points Added (PPA) by player season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_season_ppa(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param str position: Position abbreviation filter
        :param int player_id: Player id filter
        :param str threshold: Minimum play threshold filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :return: list[PlayerSeasonPPA]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_season_ppa_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_player_season_ppa_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_player_season_ppa_with_http_info(self, **kwargs):  # noqa: E501
        """Player Predicated Points Added (PPA/EPA) broken down by season  # noqa: E501

        Predicted Points Added (PPA) by player season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_season_ppa_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param str position: Position abbreviation filter
        :param int player_id: Player id filter
        :param str threshold: Minimum play threshold filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :return: list[PlayerSeasonPPA]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'team', 'conference', 'position', 'player_id', 'threshold', 'exclude_garbage_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_season_ppa" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2013):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_player_season_ppa`, must be a value greater than or equal to `2013`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'position' in params:
            query_params.append(('position', params['position']))  # noqa: E501
        if 'player_id' in params:
            query_params.append(('playerId', params['player_id']))  # noqa: E501
        if 'threshold' in params:
            query_params.append(('threshold', params['threshold']))  # noqa: E501
        if 'exclude_garbage_time' in params:
            query_params.append(('excludeGarbageTime', params['exclude_garbage_time']))  # noqa: E501

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
            '/ppa/players/season', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayerSeasonPPA]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_predicted_points(self, down, distance, **kwargs):  # noqa: E501
        """Predicted Points (i.e. Expected Points or EP)  # noqa: E501

        Predicted Points  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_predicted_points(down, distance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int down: Down filter (required)
        :param int distance: Distance filter (required)
        :return: list[PredictedPoints]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_predicted_points_with_http_info(down, distance, **kwargs)  # noqa: E501
        else:
            (data) = self.get_predicted_points_with_http_info(down, distance, **kwargs)  # noqa: E501
            return data

    def get_predicted_points_with_http_info(self, down, distance, **kwargs):  # noqa: E501
        """Predicted Points (i.e. Expected Points or EP)  # noqa: E501

        Predicted Points  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_predicted_points_with_http_info(down, distance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int down: Down filter (required)
        :param int distance: Distance filter (required)
        :return: list[PredictedPoints]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['down', 'distance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_predicted_points" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'down' is set
        if self.api_client.client_side_validation and ('down' not in params or
                                                       params['down'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `down` when calling `get_predicted_points`")  # noqa: E501
        # verify the required parameter 'distance' is set
        if self.api_client.client_side_validation and ('distance' not in params or
                                                       params['distance'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `distance` when calling `get_predicted_points`")  # noqa: E501

        if self.api_client.client_side_validation and ('down' in params and params['down'] > 4):  # noqa: E501
            raise ValueError("Invalid value for parameter `down` when calling `get_predicted_points`, must be a value less than or equal to `4`")  # noqa: E501
        if self.api_client.client_side_validation and ('down' in params and params['down'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `down` when calling `get_predicted_points`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('distance' in params and params['distance'] > 99):  # noqa: E501
            raise ValueError("Invalid value for parameter `distance` when calling `get_predicted_points`, must be a value less than or equal to `99`")  # noqa: E501
        if self.api_client.client_side_validation and ('distance' in params and params['distance'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `distance` when calling `get_predicted_points`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'down' in params:
            query_params.append(('down', params['down']))  # noqa: E501
        if 'distance' in params:
            query_params.append(('distance', params['distance']))  # noqa: E501

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
            '/ppa/predicted', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PredictedPoints]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pregame_win_probabilities(self, **kwargs):  # noqa: E501
        """Pregame win probability data  # noqa: E501

        Pregame win probabilities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pregame_win_probabilities(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param int week: Week filter
        :param str team: Team filter
        :param str season_type: regular or postseason
        :return: list[PregameWP]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pregame_win_probabilities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_pregame_win_probabilities_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_pregame_win_probabilities_with_http_info(self, **kwargs):  # noqa: E501
        """Pregame win probability data  # noqa: E501

        Pregame win probabilities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pregame_win_probabilities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param int week: Week filter
        :param str team: Team filter
        :param str season_type: regular or postseason
        :return: list[PregameWP]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'team', 'season_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pregame_win_probabilities" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2001):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_pregame_win_probabilities`, must be a value greater than or equal to `2001`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_pregame_win_probabilities`, must be a value less than or equal to `16`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_pregame_win_probabilities`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
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
            '/metrics/wp/pregame', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PregameWP]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_ppa(self, **kwargs):  # noqa: E501
        """Predicted Points Added (PPA/EPA) data by team  # noqa: E501

        Predicted Points Added (PPA)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_ppa(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required if team not specified)
        :param str team: Team filter (required if year not specified)
        :param str conference: Conference filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :return: list[TeamPPA]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_team_ppa_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_team_ppa_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_team_ppa_with_http_info(self, **kwargs):  # noqa: E501
        """Predicted Points Added (PPA/EPA) data by team  # noqa: E501

        Predicted Points Added (PPA)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_ppa_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required if team not specified)
        :param str team: Team filter (required if year not specified)
        :param str conference: Conference filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :return: list[TeamPPA]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'team', 'conference', 'exclude_garbage_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_ppa" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2001):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_team_ppa`, must be a value greater than or equal to `2001`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'exclude_garbage_time' in params:
            query_params.append(('excludeGarbageTime', params['exclude_garbage_time']))  # noqa: E501

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
            '/ppa/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamPPA]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_win_probability_data(self, game_id, **kwargs):  # noqa: E501
        """Win probability chart data  # noqa: E501

        Win probability data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_win_probability_data(game_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int game_id: Game id filter (required)
        :return: list[PlayWP]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_win_probability_data_with_http_info(game_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_win_probability_data_with_http_info(game_id, **kwargs)  # noqa: E501
            return data

    def get_win_probability_data_with_http_info(self, game_id, **kwargs):  # noqa: E501
        """Win probability chart data  # noqa: E501

        Win probability data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_win_probability_data_with_http_info(game_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int game_id: Game id filter (required)
        :return: list[PlayWP]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['game_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_win_probability_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'game_id' is set
        if self.api_client.client_side_validation and ('game_id' not in params or
                                                       params['game_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `game_id` when calling `get_win_probability_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'game_id' in params:
            query_params.append(('gameId', params['game_id']))  # noqa: E501

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
            '/metrics/wp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayWP]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
