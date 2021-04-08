# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\").  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class PlayerSeasonStat(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'season': 'int',
        'player_id': 'int',
        'player': 'str',
        'team': 'str',
        'conference': 'str',
        'category': 'str',
        'stat_type': 'str',
        'stat': 'float'
    }

    attribute_map = {
        'season': 'season',
        'player_id': 'playerId',
        'player': 'player',
        'team': 'team',
        'conference': 'conference',
        'category': 'category',
        'stat_type': 'statType',
        'stat': 'stat'
    }

    def __init__(self, season=None, player_id=None, player=None, team=None, conference=None, category=None, stat_type=None, stat=None, _configuration=None):  # noqa: E501
        """PlayerSeasonStat - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._season = None
        self._player_id = None
        self._player = None
        self._team = None
        self._conference = None
        self._category = None
        self._stat_type = None
        self._stat = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if player_id is not None:
            self.player_id = player_id
        if player is not None:
            self.player = player
        if team is not None:
            self.team = team
        if conference is not None:
            self.conference = conference
        if category is not None:
            self.category = category
        if stat_type is not None:
            self.stat_type = stat_type
        if stat is not None:
            self.stat = stat

    @property
    def season(self):
        """Gets the season of this PlayerSeasonStat.  # noqa: E501


        :return: The season of this PlayerSeasonStat.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this PlayerSeasonStat.


        :param season: The season of this PlayerSeasonStat.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def player_id(self):
        """Gets the player_id of this PlayerSeasonStat.  # noqa: E501


        :return: The player_id of this PlayerSeasonStat.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this PlayerSeasonStat.


        :param player_id: The player_id of this PlayerSeasonStat.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def player(self):
        """Gets the player of this PlayerSeasonStat.  # noqa: E501


        :return: The player of this PlayerSeasonStat.  # noqa: E501
        :rtype: str
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this PlayerSeasonStat.


        :param player: The player of this PlayerSeasonStat.  # noqa: E501
        :type: str
        """

        self._player = player

    @property
    def team(self):
        """Gets the team of this PlayerSeasonStat.  # noqa: E501


        :return: The team of this PlayerSeasonStat.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerSeasonStat.


        :param team: The team of this PlayerSeasonStat.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def conference(self):
        """Gets the conference of this PlayerSeasonStat.  # noqa: E501


        :return: The conference of this PlayerSeasonStat.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this PlayerSeasonStat.


        :param conference: The conference of this PlayerSeasonStat.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def category(self):
        """Gets the category of this PlayerSeasonStat.  # noqa: E501


        :return: The category of this PlayerSeasonStat.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this PlayerSeasonStat.


        :param category: The category of this PlayerSeasonStat.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def stat_type(self):
        """Gets the stat_type of this PlayerSeasonStat.  # noqa: E501


        :return: The stat_type of this PlayerSeasonStat.  # noqa: E501
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this PlayerSeasonStat.


        :param stat_type: The stat_type of this PlayerSeasonStat.  # noqa: E501
        :type: str
        """

        self._stat_type = stat_type

    @property
    def stat(self):
        """Gets the stat of this PlayerSeasonStat.  # noqa: E501


        :return: The stat of this PlayerSeasonStat.  # noqa: E501
        :rtype: float
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this PlayerSeasonStat.


        :param stat: The stat of this PlayerSeasonStat.  # noqa: E501
        :type: float
        """

        self._stat = stat

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PlayerSeasonStat, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlayerSeasonStat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayerSeasonStat):
            return True

        return self.to_dict() != other.to_dict()
