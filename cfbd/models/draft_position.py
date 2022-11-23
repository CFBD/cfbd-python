# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.12
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class DraftPosition(object):
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
        'name': 'str',
        'abbreviation': 'str'
    }

    attribute_map = {
        'name': 'name',
        'abbreviation': 'abbreviation'
    }

    def __init__(self, name=None, abbreviation=None, _configuration=None):  # noqa: E501
        """DraftPosition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._abbreviation = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation

    @property
    def name(self):
        """Gets the name of this DraftPosition.  # noqa: E501


        :return: The name of this DraftPosition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DraftPosition.


        :param name: The name of this DraftPosition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this DraftPosition.  # noqa: E501


        :return: The abbreviation of this DraftPosition.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this DraftPosition.


        :param abbreviation: The abbreviation of this DraftPosition.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

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
        if issubclass(DraftPosition, dict):
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
        if not isinstance(other, DraftPosition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DraftPosition):
            return True

        return self.to_dict() != other.to_dict()
