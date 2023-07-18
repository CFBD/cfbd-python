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


class DraftTeam(object):
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
        'location': 'str',
        'nickname': 'str',
        'display_name': 'str',
        'logo': 'str'
    }

    attribute_map = {
        'location': 'location',
        'nickname': 'nickname',
        'display_name': 'displayName',
        'logo': 'logo'
    }

    def __init__(self, location=None, nickname=None, display_name=None, logo=None, _configuration=None):  # noqa: E501
        """DraftTeam - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._location = None
        self._nickname = None
        self._display_name = None
        self._logo = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if nickname is not None:
            self.nickname = nickname
        if display_name is not None:
            self.display_name = display_name
        if logo is not None:
            self.logo = logo

    @property
    def location(self):
        """Gets the location of this DraftTeam.  # noqa: E501


        :return: The location of this DraftTeam.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DraftTeam.


        :param location: The location of this DraftTeam.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def nickname(self):
        """Gets the nickname of this DraftTeam.  # noqa: E501


        :return: The nickname of this DraftTeam.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this DraftTeam.


        :param nickname: The nickname of this DraftTeam.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

    @property
    def display_name(self):
        """Gets the display_name of this DraftTeam.  # noqa: E501


        :return: The display_name of this DraftTeam.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DraftTeam.


        :param display_name: The display_name of this DraftTeam.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def logo(self):
        """Gets the logo of this DraftTeam.  # noqa: E501


        :return: The logo of this DraftTeam.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this DraftTeam.


        :param logo: The logo of this DraftTeam.  # noqa: E501
        :type: str
        """

        self._logo = logo

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
        if issubclass(DraftTeam, dict):
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
        if not isinstance(other, DraftTeam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DraftTeam):
            return True

        return self.to_dict() != other.to_dict()
