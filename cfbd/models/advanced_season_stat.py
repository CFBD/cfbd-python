# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.6.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class AdvancedSeasonStat(object):
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
        'team': 'str',
        'conference': 'str',
        'offense': 'AdvancedSeasonStatOffense',
        'defense': 'AdvancedSeasonStatOffense'
    }

    attribute_map = {
        'season': 'season',
        'team': 'team',
        'conference': 'conference',
        'offense': 'offense',
        'defense': 'defense'
    }

    def __init__(self, season=None, team=None, conference=None, offense=None, defense=None, _configuration=None):  # noqa: E501
        """AdvancedSeasonStat - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._season = None
        self._team = None
        self._conference = None
        self._offense = None
        self._defense = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if team is not None:
            self.team = team
        if conference is not None:
            self.conference = conference
        if offense is not None:
            self.offense = offense
        if defense is not None:
            self.defense = defense

    @property
    def season(self):
        """Gets the season of this AdvancedSeasonStat.  # noqa: E501


        :return: The season of this AdvancedSeasonStat.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this AdvancedSeasonStat.


        :param season: The season of this AdvancedSeasonStat.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def team(self):
        """Gets the team of this AdvancedSeasonStat.  # noqa: E501


        :return: The team of this AdvancedSeasonStat.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this AdvancedSeasonStat.


        :param team: The team of this AdvancedSeasonStat.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def conference(self):
        """Gets the conference of this AdvancedSeasonStat.  # noqa: E501


        :return: The conference of this AdvancedSeasonStat.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this AdvancedSeasonStat.


        :param conference: The conference of this AdvancedSeasonStat.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def offense(self):
        """Gets the offense of this AdvancedSeasonStat.  # noqa: E501


        :return: The offense of this AdvancedSeasonStat.  # noqa: E501
        :rtype: AdvancedSeasonStatOffense
        """
        return self._offense

    @offense.setter
    def offense(self, offense):
        """Sets the offense of this AdvancedSeasonStat.


        :param offense: The offense of this AdvancedSeasonStat.  # noqa: E501
        :type: AdvancedSeasonStatOffense
        """

        self._offense = offense

    @property
    def defense(self):
        """Gets the defense of this AdvancedSeasonStat.  # noqa: E501


        :return: The defense of this AdvancedSeasonStat.  # noqa: E501
        :rtype: AdvancedSeasonStatOffense
        """
        return self._defense

    @defense.setter
    def defense(self, defense):
        """Sets the defense of this AdvancedSeasonStat.


        :param defense: The defense of this AdvancedSeasonStat.  # noqa: E501
        :type: AdvancedSeasonStatOffense
        """

        self._defense = defense

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
        if issubclass(AdvancedSeasonStat, dict):
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
        if not isinstance(other, AdvancedSeasonStat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdvancedSeasonStat):
            return True

        return self.to_dict() != other.to_dict()
