# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.5.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class AdvancedGameStatOffenseStandardDowns(object):
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
        'ppa': 'float',
        'success_rate': 'float',
        'explosiveness': 'float'
    }

    attribute_map = {
        'ppa': 'ppa',
        'success_rate': 'successRate',
        'explosiveness': 'explosiveness'
    }

    def __init__(self, ppa=None, success_rate=None, explosiveness=None, _configuration=None):  # noqa: E501
        """AdvancedGameStatOffenseStandardDowns - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ppa = None
        self._success_rate = None
        self._explosiveness = None
        self.discriminator = None

        if ppa is not None:
            self.ppa = ppa
        if success_rate is not None:
            self.success_rate = success_rate
        if explosiveness is not None:
            self.explosiveness = explosiveness

    @property
    def ppa(self):
        """Gets the ppa of this AdvancedGameStatOffenseStandardDowns.  # noqa: E501


        :return: The ppa of this AdvancedGameStatOffenseStandardDowns.  # noqa: E501
        :rtype: float
        """
        return self._ppa

    @ppa.setter
    def ppa(self, ppa):
        """Sets the ppa of this AdvancedGameStatOffenseStandardDowns.


        :param ppa: The ppa of this AdvancedGameStatOffenseStandardDowns.  # noqa: E501
        :type: float
        """

        self._ppa = ppa

    @property
    def success_rate(self):
        """Gets the success_rate of this AdvancedGameStatOffenseStandardDowns.  # noqa: E501


        :return: The success_rate of this AdvancedGameStatOffenseStandardDowns.  # noqa: E501
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this AdvancedGameStatOffenseStandardDowns.


        :param success_rate: The success_rate of this AdvancedGameStatOffenseStandardDowns.  # noqa: E501
        :type: float
        """

        self._success_rate = success_rate

    @property
    def explosiveness(self):
        """Gets the explosiveness of this AdvancedGameStatOffenseStandardDowns.  # noqa: E501


        :return: The explosiveness of this AdvancedGameStatOffenseStandardDowns.  # noqa: E501
        :rtype: float
        """
        return self._explosiveness

    @explosiveness.setter
    def explosiveness(self, explosiveness):
        """Sets the explosiveness of this AdvancedGameStatOffenseStandardDowns.


        :param explosiveness: The explosiveness of this AdvancedGameStatOffenseStandardDowns.  # noqa: E501
        :type: float
        """

        self._explosiveness = explosiveness

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
        if issubclass(AdvancedGameStatOffenseStandardDowns, dict):
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
        if not isinstance(other, AdvancedGameStatOffenseStandardDowns):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdvancedGameStatOffenseStandardDowns):
            return True

        return self.to_dict() != other.to_dict()
