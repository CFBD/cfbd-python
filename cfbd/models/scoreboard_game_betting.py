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


class ScoreboardGameBetting(object):
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
        'spread': 'float',
        'over_under': 'float',
        'home_moneyline': 'int',
        'away_moneyline': 'int'
    }

    attribute_map = {
        'spread': 'spread',
        'over_under': 'overUnder',
        'home_moneyline': 'homeMoneyline',
        'away_moneyline': 'awayMoneyline'
    }

    def __init__(self, spread=None, over_under=None, home_moneyline=None, away_moneyline=None, _configuration=None):  # noqa: E501
        """ScoreboardGameBetting - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._spread = None
        self._over_under = None
        self._home_moneyline = None
        self._away_moneyline = None
        self.discriminator = None

        if spread is not None:
            self.spread = spread
        if over_under is not None:
            self.over_under = over_under
        if home_moneyline is not None:
            self.home_moneyline = home_moneyline
        if away_moneyline is not None:
            self.away_moneyline = away_moneyline

    @property
    def spread(self):
        """Gets the spread of this ScoreboardGameBetting.  # noqa: E501


        :return: The spread of this ScoreboardGameBetting.  # noqa: E501
        :rtype: float
        """
        return self._spread

    @spread.setter
    def spread(self, spread):
        """Sets the spread of this ScoreboardGameBetting.


        :param spread: The spread of this ScoreboardGameBetting.  # noqa: E501
        :type: float
        """

        self._spread = spread

    @property
    def over_under(self):
        """Gets the over_under of this ScoreboardGameBetting.  # noqa: E501


        :return: The over_under of this ScoreboardGameBetting.  # noqa: E501
        :rtype: float
        """
        return self._over_under

    @over_under.setter
    def over_under(self, over_under):
        """Sets the over_under of this ScoreboardGameBetting.


        :param over_under: The over_under of this ScoreboardGameBetting.  # noqa: E501
        :type: float
        """

        self._over_under = over_under

    @property
    def home_moneyline(self):
        """Gets the home_moneyline of this ScoreboardGameBetting.  # noqa: E501


        :return: The home_moneyline of this ScoreboardGameBetting.  # noqa: E501
        :rtype: int
        """
        return self._home_moneyline

    @home_moneyline.setter
    def home_moneyline(self, home_moneyline):
        """Sets the home_moneyline of this ScoreboardGameBetting.


        :param home_moneyline: The home_moneyline of this ScoreboardGameBetting.  # noqa: E501
        :type: int
        """

        self._home_moneyline = home_moneyline

    @property
    def away_moneyline(self):
        """Gets the away_moneyline of this ScoreboardGameBetting.  # noqa: E501


        :return: The away_moneyline of this ScoreboardGameBetting.  # noqa: E501
        :rtype: int
        """
        return self._away_moneyline

    @away_moneyline.setter
    def away_moneyline(self, away_moneyline):
        """Sets the away_moneyline of this ScoreboardGameBetting.


        :param away_moneyline: The away_moneyline of this ScoreboardGameBetting.  # noqa: E501
        :type: int
        """

        self._away_moneyline = away_moneyline

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
        if issubclass(ScoreboardGameBetting, dict):
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
        if not isinstance(other, ScoreboardGameBetting):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScoreboardGameBetting):
            return True

        return self.to_dict() != other.to_dict()
