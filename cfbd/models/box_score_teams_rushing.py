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


class BoxScoreTeamsRushing(object):
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
        'team': 'str',
        'power_success': 'float',
        'stuff_rate': 'float',
        'line_yards': 'float',
        'line_yards_average': 'float',
        'second_level_yards': 'int',
        'second_level_yards_average': 'float',
        'open_field_yards': 'int',
        'open_field_yards_average': 'float'
    }

    attribute_map = {
        'team': 'team',
        'power_success': 'powerSuccess',
        'stuff_rate': 'stuffRate',
        'line_yards': 'lineYards',
        'line_yards_average': 'lineYardsAverage',
        'second_level_yards': 'secondLevelYards',
        'second_level_yards_average': 'secondLevelYardsAverage',
        'open_field_yards': 'openFieldYards',
        'open_field_yards_average': 'openFieldYardsAverage'
    }

    def __init__(self, team=None, power_success=None, stuff_rate=None, line_yards=None, line_yards_average=None, second_level_yards=None, second_level_yards_average=None, open_field_yards=None, open_field_yards_average=None, _configuration=None):  # noqa: E501
        """BoxScoreTeamsRushing - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._team = None
        self._power_success = None
        self._stuff_rate = None
        self._line_yards = None
        self._line_yards_average = None
        self._second_level_yards = None
        self._second_level_yards_average = None
        self._open_field_yards = None
        self._open_field_yards_average = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if power_success is not None:
            self.power_success = power_success
        if stuff_rate is not None:
            self.stuff_rate = stuff_rate
        if line_yards is not None:
            self.line_yards = line_yards
        if line_yards_average is not None:
            self.line_yards_average = line_yards_average
        if second_level_yards is not None:
            self.second_level_yards = second_level_yards
        if second_level_yards_average is not None:
            self.second_level_yards_average = second_level_yards_average
        if open_field_yards is not None:
            self.open_field_yards = open_field_yards
        if open_field_yards_average is not None:
            self.open_field_yards_average = open_field_yards_average

    @property
    def team(self):
        """Gets the team of this BoxScoreTeamsRushing.  # noqa: E501


        :return: The team of this BoxScoreTeamsRushing.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BoxScoreTeamsRushing.


        :param team: The team of this BoxScoreTeamsRushing.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def power_success(self):
        """Gets the power_success of this BoxScoreTeamsRushing.  # noqa: E501


        :return: The power_success of this BoxScoreTeamsRushing.  # noqa: E501
        :rtype: float
        """
        return self._power_success

    @power_success.setter
    def power_success(self, power_success):
        """Sets the power_success of this BoxScoreTeamsRushing.


        :param power_success: The power_success of this BoxScoreTeamsRushing.  # noqa: E501
        :type: float
        """

        self._power_success = power_success

    @property
    def stuff_rate(self):
        """Gets the stuff_rate of this BoxScoreTeamsRushing.  # noqa: E501


        :return: The stuff_rate of this BoxScoreTeamsRushing.  # noqa: E501
        :rtype: float
        """
        return self._stuff_rate

    @stuff_rate.setter
    def stuff_rate(self, stuff_rate):
        """Sets the stuff_rate of this BoxScoreTeamsRushing.


        :param stuff_rate: The stuff_rate of this BoxScoreTeamsRushing.  # noqa: E501
        :type: float
        """

        self._stuff_rate = stuff_rate

    @property
    def line_yards(self):
        """Gets the line_yards of this BoxScoreTeamsRushing.  # noqa: E501


        :return: The line_yards of this BoxScoreTeamsRushing.  # noqa: E501
        :rtype: float
        """
        return self._line_yards

    @line_yards.setter
    def line_yards(self, line_yards):
        """Sets the line_yards of this BoxScoreTeamsRushing.


        :param line_yards: The line_yards of this BoxScoreTeamsRushing.  # noqa: E501
        :type: float
        """

        self._line_yards = line_yards

    @property
    def line_yards_average(self):
        """Gets the line_yards_average of this BoxScoreTeamsRushing.  # noqa: E501


        :return: The line_yards_average of this BoxScoreTeamsRushing.  # noqa: E501
        :rtype: float
        """
        return self._line_yards_average

    @line_yards_average.setter
    def line_yards_average(self, line_yards_average):
        """Sets the line_yards_average of this BoxScoreTeamsRushing.


        :param line_yards_average: The line_yards_average of this BoxScoreTeamsRushing.  # noqa: E501
        :type: float
        """

        self._line_yards_average = line_yards_average

    @property
    def second_level_yards(self):
        """Gets the second_level_yards of this BoxScoreTeamsRushing.  # noqa: E501


        :return: The second_level_yards of this BoxScoreTeamsRushing.  # noqa: E501
        :rtype: int
        """
        return self._second_level_yards

    @second_level_yards.setter
    def second_level_yards(self, second_level_yards):
        """Sets the second_level_yards of this BoxScoreTeamsRushing.


        :param second_level_yards: The second_level_yards of this BoxScoreTeamsRushing.  # noqa: E501
        :type: int
        """

        self._second_level_yards = second_level_yards

    @property
    def second_level_yards_average(self):
        """Gets the second_level_yards_average of this BoxScoreTeamsRushing.  # noqa: E501


        :return: The second_level_yards_average of this BoxScoreTeamsRushing.  # noqa: E501
        :rtype: float
        """
        return self._second_level_yards_average

    @second_level_yards_average.setter
    def second_level_yards_average(self, second_level_yards_average):
        """Sets the second_level_yards_average of this BoxScoreTeamsRushing.


        :param second_level_yards_average: The second_level_yards_average of this BoxScoreTeamsRushing.  # noqa: E501
        :type: float
        """

        self._second_level_yards_average = second_level_yards_average

    @property
    def open_field_yards(self):
        """Gets the open_field_yards of this BoxScoreTeamsRushing.  # noqa: E501


        :return: The open_field_yards of this BoxScoreTeamsRushing.  # noqa: E501
        :rtype: int
        """
        return self._open_field_yards

    @open_field_yards.setter
    def open_field_yards(self, open_field_yards):
        """Sets the open_field_yards of this BoxScoreTeamsRushing.


        :param open_field_yards: The open_field_yards of this BoxScoreTeamsRushing.  # noqa: E501
        :type: int
        """

        self._open_field_yards = open_field_yards

    @property
    def open_field_yards_average(self):
        """Gets the open_field_yards_average of this BoxScoreTeamsRushing.  # noqa: E501


        :return: The open_field_yards_average of this BoxScoreTeamsRushing.  # noqa: E501
        :rtype: float
        """
        return self._open_field_yards_average

    @open_field_yards_average.setter
    def open_field_yards_average(self, open_field_yards_average):
        """Sets the open_field_yards_average of this BoxScoreTeamsRushing.


        :param open_field_yards_average: The open_field_yards_average of this BoxScoreTeamsRushing.  # noqa: E501
        :type: float
        """

        self._open_field_yards_average = open_field_yards_average

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
        if issubclass(BoxScoreTeamsRushing, dict):
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
        if not isinstance(other, BoxScoreTeamsRushing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoxScoreTeamsRushing):
            return True

        return self.to_dict() != other.to_dict()
