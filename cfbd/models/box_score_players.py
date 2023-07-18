# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.13
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class BoxScorePlayers(object):
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
        'usage': 'list[BoxScorePlayersUsage]',
        'ppa': 'list[BoxScorePlayersPpa]'
    }

    attribute_map = {
        'usage': 'usage',
        'ppa': 'ppa'
    }

    def __init__(self, usage=None, ppa=None, _configuration=None):  # noqa: E501
        """BoxScorePlayers - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._usage = None
        self._ppa = None
        self.discriminator = None

        if usage is not None:
            self.usage = usage
        if ppa is not None:
            self.ppa = ppa

    @property
    def usage(self):
        """Gets the usage of this BoxScorePlayers.  # noqa: E501


        :return: The usage of this BoxScorePlayers.  # noqa: E501
        :rtype: list[BoxScorePlayersUsage]
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this BoxScorePlayers.


        :param usage: The usage of this BoxScorePlayers.  # noqa: E501
        :type: list[BoxScorePlayersUsage]
        """

        self._usage = usage

    @property
    def ppa(self):
        """Gets the ppa of this BoxScorePlayers.  # noqa: E501


        :return: The ppa of this BoxScorePlayers.  # noqa: E501
        :rtype: list[BoxScorePlayersPpa]
        """
        return self._ppa

    @ppa.setter
    def ppa(self, ppa):
        """Sets the ppa of this BoxScorePlayers.


        :param ppa: The ppa of this BoxScorePlayers.  # noqa: E501
        :type: list[BoxScorePlayersPpa]
        """

        self._ppa = ppa

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
        if issubclass(BoxScorePlayers, dict):
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
        if not isinstance(other, BoxScorePlayers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoxScorePlayers):
            return True

        return self.to_dict() != other.to_dict()
