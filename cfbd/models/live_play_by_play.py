# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.2.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class LivePlayByPlay(object):
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
        'id': 'int',
        'teams': 'list[object]',
        'plays': 'list[object]'
    }

    attribute_map = {
        'id': 'id',
        'teams': 'teams',
        'plays': 'plays'
    }

    def __init__(self, id=None, teams=None, plays=None, _configuration=None):  # noqa: E501
        """LivePlayByPlay - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._teams = None
        self._plays = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if teams is not None:
            self.teams = teams
        if plays is not None:
            self.plays = plays

    @property
    def id(self):
        """Gets the id of this LivePlayByPlay.  # noqa: E501


        :return: The id of this LivePlayByPlay.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LivePlayByPlay.


        :param id: The id of this LivePlayByPlay.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def teams(self):
        """Gets the teams of this LivePlayByPlay.  # noqa: E501


        :return: The teams of this LivePlayByPlay.  # noqa: E501
        :rtype: list[object]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this LivePlayByPlay.


        :param teams: The teams of this LivePlayByPlay.  # noqa: E501
        :type: list[object]
        """

        self._teams = teams

    @property
    def plays(self):
        """Gets the plays of this LivePlayByPlay.  # noqa: E501


        :return: The plays of this LivePlayByPlay.  # noqa: E501
        :rtype: list[object]
        """
        return self._plays

    @plays.setter
    def plays(self, plays):
        """Sets the plays of this LivePlayByPlay.


        :param plays: The plays of this LivePlayByPlay.  # noqa: E501
        :type: list[object]
        """

        self._plays = plays

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
        if issubclass(LivePlayByPlay, dict):
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
        if not isinstance(other, LivePlayByPlay):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LivePlayByPlay):
            return True

        return self.to_dict() != other.to_dict()
