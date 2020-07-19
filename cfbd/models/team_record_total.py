# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.4
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TeamRecordTotal(object):
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
        'games': 'int',
        'wins': 'int',
        'losses': 'int',
        'ties': 'int'
    }

    attribute_map = {
        'games': 'games',
        'wins': 'wins',
        'losses': 'losses',
        'ties': 'ties'
    }

    def __init__(self, games=None, wins=None, losses=None, ties=None):  # noqa: E501
        """TeamRecordTotal - a model defined in Swagger"""  # noqa: E501

        self._games = None
        self._wins = None
        self._losses = None
        self._ties = None
        self.discriminator = None

        if games is not None:
            self.games = games
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if ties is not None:
            self.ties = ties

    @property
    def games(self):
        """Gets the games of this TeamRecordTotal.  # noqa: E501


        :return: The games of this TeamRecordTotal.  # noqa: E501
        :rtype: int
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this TeamRecordTotal.


        :param games: The games of this TeamRecordTotal.  # noqa: E501
        :type: int
        """

        self._games = games

    @property
    def wins(self):
        """Gets the wins of this TeamRecordTotal.  # noqa: E501


        :return: The wins of this TeamRecordTotal.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this TeamRecordTotal.


        :param wins: The wins of this TeamRecordTotal.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this TeamRecordTotal.  # noqa: E501


        :return: The losses of this TeamRecordTotal.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this TeamRecordTotal.


        :param losses: The losses of this TeamRecordTotal.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def ties(self):
        """Gets the ties of this TeamRecordTotal.  # noqa: E501


        :return: The ties of this TeamRecordTotal.  # noqa: E501
        :rtype: int
        """
        return self._ties

    @ties.setter
    def ties(self, ties):
        """Sets the ties of this TeamRecordTotal.


        :param ties: The ties of this TeamRecordTotal.  # noqa: E501
        :type: int
        """

        self._ties = ties

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
        if issubclass(TeamRecordTotal, dict):
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
        if not isinstance(other, TeamRecordTotal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
