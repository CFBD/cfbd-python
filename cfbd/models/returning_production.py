# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.4
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class ReturningProduction(object):
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
        'total_ppa': 'float',
        'total_passing_ppa': 'float',
        'total_receiving_ppa': 'float',
        'total_rushing_ppa': 'float',
        'percent_ppa': 'float',
        'percent_passing_ppa': 'float',
        'percent_receiving_ppa': 'float',
        'percent_rushing_ppa': 'float',
        'usage': 'float',
        'passing_usage': 'float',
        'receiving_usage': 'float',
        'rushing_usage': 'float'
    }

    attribute_map = {
        'season': 'season',
        'team': 'team',
        'conference': 'conference',
        'total_ppa': 'totalPPA',
        'total_passing_ppa': 'totalPassingPPA',
        'total_receiving_ppa': 'totalReceivingPPA',
        'total_rushing_ppa': 'totalRushingPPA',
        'percent_ppa': 'percentPPA',
        'percent_passing_ppa': 'percentPassingPPA',
        'percent_receiving_ppa': 'percentReceivingPPA',
        'percent_rushing_ppa': 'percentRushingPPA',
        'usage': 'usage',
        'passing_usage': 'passingUsage',
        'receiving_usage': 'receivingUsage',
        'rushing_usage': 'rushingUsage'
    }

    def __init__(self, season=None, team=None, conference=None, total_ppa=None, total_passing_ppa=None, total_receiving_ppa=None, total_rushing_ppa=None, percent_ppa=None, percent_passing_ppa=None, percent_receiving_ppa=None, percent_rushing_ppa=None, usage=None, passing_usage=None, receiving_usage=None, rushing_usage=None, _configuration=None):  # noqa: E501
        """ReturningProduction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._season = None
        self._team = None
        self._conference = None
        self._total_ppa = None
        self._total_passing_ppa = None
        self._total_receiving_ppa = None
        self._total_rushing_ppa = None
        self._percent_ppa = None
        self._percent_passing_ppa = None
        self._percent_receiving_ppa = None
        self._percent_rushing_ppa = None
        self._usage = None
        self._passing_usage = None
        self._receiving_usage = None
        self._rushing_usage = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if team is not None:
            self.team = team
        if conference is not None:
            self.conference = conference
        if total_ppa is not None:
            self.total_ppa = total_ppa
        if total_passing_ppa is not None:
            self.total_passing_ppa = total_passing_ppa
        if total_receiving_ppa is not None:
            self.total_receiving_ppa = total_receiving_ppa
        if total_rushing_ppa is not None:
            self.total_rushing_ppa = total_rushing_ppa
        if percent_ppa is not None:
            self.percent_ppa = percent_ppa
        if percent_passing_ppa is not None:
            self.percent_passing_ppa = percent_passing_ppa
        if percent_receiving_ppa is not None:
            self.percent_receiving_ppa = percent_receiving_ppa
        if percent_rushing_ppa is not None:
            self.percent_rushing_ppa = percent_rushing_ppa
        if usage is not None:
            self.usage = usage
        if passing_usage is not None:
            self.passing_usage = passing_usage
        if receiving_usage is not None:
            self.receiving_usage = receiving_usage
        if rushing_usage is not None:
            self.rushing_usage = rushing_usage

    @property
    def season(self):
        """Gets the season of this ReturningProduction.  # noqa: E501


        :return: The season of this ReturningProduction.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this ReturningProduction.


        :param season: The season of this ReturningProduction.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def team(self):
        """Gets the team of this ReturningProduction.  # noqa: E501


        :return: The team of this ReturningProduction.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this ReturningProduction.


        :param team: The team of this ReturningProduction.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def conference(self):
        """Gets the conference of this ReturningProduction.  # noqa: E501


        :return: The conference of this ReturningProduction.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this ReturningProduction.


        :param conference: The conference of this ReturningProduction.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def total_ppa(self):
        """Gets the total_ppa of this ReturningProduction.  # noqa: E501


        :return: The total_ppa of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._total_ppa

    @total_ppa.setter
    def total_ppa(self, total_ppa):
        """Sets the total_ppa of this ReturningProduction.


        :param total_ppa: The total_ppa of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._total_ppa = total_ppa

    @property
    def total_passing_ppa(self):
        """Gets the total_passing_ppa of this ReturningProduction.  # noqa: E501


        :return: The total_passing_ppa of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._total_passing_ppa

    @total_passing_ppa.setter
    def total_passing_ppa(self, total_passing_ppa):
        """Sets the total_passing_ppa of this ReturningProduction.


        :param total_passing_ppa: The total_passing_ppa of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._total_passing_ppa = total_passing_ppa

    @property
    def total_receiving_ppa(self):
        """Gets the total_receiving_ppa of this ReturningProduction.  # noqa: E501


        :return: The total_receiving_ppa of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._total_receiving_ppa

    @total_receiving_ppa.setter
    def total_receiving_ppa(self, total_receiving_ppa):
        """Sets the total_receiving_ppa of this ReturningProduction.


        :param total_receiving_ppa: The total_receiving_ppa of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._total_receiving_ppa = total_receiving_ppa

    @property
    def total_rushing_ppa(self):
        """Gets the total_rushing_ppa of this ReturningProduction.  # noqa: E501


        :return: The total_rushing_ppa of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._total_rushing_ppa

    @total_rushing_ppa.setter
    def total_rushing_ppa(self, total_rushing_ppa):
        """Sets the total_rushing_ppa of this ReturningProduction.


        :param total_rushing_ppa: The total_rushing_ppa of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._total_rushing_ppa = total_rushing_ppa

    @property
    def percent_ppa(self):
        """Gets the percent_ppa of this ReturningProduction.  # noqa: E501


        :return: The percent_ppa of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._percent_ppa

    @percent_ppa.setter
    def percent_ppa(self, percent_ppa):
        """Sets the percent_ppa of this ReturningProduction.


        :param percent_ppa: The percent_ppa of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._percent_ppa = percent_ppa

    @property
    def percent_passing_ppa(self):
        """Gets the percent_passing_ppa of this ReturningProduction.  # noqa: E501


        :return: The percent_passing_ppa of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._percent_passing_ppa

    @percent_passing_ppa.setter
    def percent_passing_ppa(self, percent_passing_ppa):
        """Sets the percent_passing_ppa of this ReturningProduction.


        :param percent_passing_ppa: The percent_passing_ppa of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._percent_passing_ppa = percent_passing_ppa

    @property
    def percent_receiving_ppa(self):
        """Gets the percent_receiving_ppa of this ReturningProduction.  # noqa: E501


        :return: The percent_receiving_ppa of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._percent_receiving_ppa

    @percent_receiving_ppa.setter
    def percent_receiving_ppa(self, percent_receiving_ppa):
        """Sets the percent_receiving_ppa of this ReturningProduction.


        :param percent_receiving_ppa: The percent_receiving_ppa of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._percent_receiving_ppa = percent_receiving_ppa

    @property
    def percent_rushing_ppa(self):
        """Gets the percent_rushing_ppa of this ReturningProduction.  # noqa: E501


        :return: The percent_rushing_ppa of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._percent_rushing_ppa

    @percent_rushing_ppa.setter
    def percent_rushing_ppa(self, percent_rushing_ppa):
        """Sets the percent_rushing_ppa of this ReturningProduction.


        :param percent_rushing_ppa: The percent_rushing_ppa of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._percent_rushing_ppa = percent_rushing_ppa

    @property
    def usage(self):
        """Gets the usage of this ReturningProduction.  # noqa: E501


        :return: The usage of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ReturningProduction.


        :param usage: The usage of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._usage = usage

    @property
    def passing_usage(self):
        """Gets the passing_usage of this ReturningProduction.  # noqa: E501


        :return: The passing_usage of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._passing_usage

    @passing_usage.setter
    def passing_usage(self, passing_usage):
        """Sets the passing_usage of this ReturningProduction.


        :param passing_usage: The passing_usage of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._passing_usage = passing_usage

    @property
    def receiving_usage(self):
        """Gets the receiving_usage of this ReturningProduction.  # noqa: E501


        :return: The receiving_usage of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._receiving_usage

    @receiving_usage.setter
    def receiving_usage(self, receiving_usage):
        """Sets the receiving_usage of this ReturningProduction.


        :param receiving_usage: The receiving_usage of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._receiving_usage = receiving_usage

    @property
    def rushing_usage(self):
        """Gets the rushing_usage of this ReturningProduction.  # noqa: E501


        :return: The rushing_usage of this ReturningProduction.  # noqa: E501
        :rtype: float
        """
        return self._rushing_usage

    @rushing_usage.setter
    def rushing_usage(self, rushing_usage):
        """Sets the rushing_usage of this ReturningProduction.


        :param rushing_usage: The rushing_usage of this ReturningProduction.  # noqa: E501
        :type: float
        """

        self._rushing_usage = rushing_usage

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
        if issubclass(ReturningProduction, dict):
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
        if not isinstance(other, ReturningProduction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReturningProduction):
            return True

        return self.to_dict() != other.to_dict()
