# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.5
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse200(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'seasons': 'list[TeamSeason]'
    }

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'seasons': 'seasons'
    }

    def __init__(self, first_name=None, last_name=None, seasons=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._seasons = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if seasons is not None:
            self.seasons = seasons

    @property
    def first_name(self):
        """Gets the first_name of this InlineResponse200.  # noqa: E501


        :return: The first_name of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this InlineResponse200.


        :param first_name: The first_name of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this InlineResponse200.  # noqa: E501


        :return: The last_name of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this InlineResponse200.


        :param last_name: The last_name of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def seasons(self):
        """Gets the seasons of this InlineResponse200.  # noqa: E501


        :return: The seasons of this InlineResponse200.  # noqa: E501
        :rtype: list[TeamSeason]
        """
        return self._seasons

    @seasons.setter
    def seasons(self, seasons):
        """Sets the seasons of this InlineResponse200.


        :param seasons: The seasons of this InlineResponse200.  # noqa: E501
        :type: list[TeamSeason]
        """

        self._seasons = seasons

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
