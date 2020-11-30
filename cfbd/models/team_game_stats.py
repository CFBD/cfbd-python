# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.3.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TeamGameStats(object):
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
        'category': 'str',
        'stat': 'str'
    }

    attribute_map = {
        'category': 'category',
        'stat': 'stat'
    }

    def __init__(self, category=None, stat=None):  # noqa: E501
        """TeamGameStats - a model defined in Swagger"""  # noqa: E501

        self._category = None
        self._stat = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if stat is not None:
            self.stat = stat

    @property
    def category(self):
        """Gets the category of this TeamGameStats.  # noqa: E501


        :return: The category of this TeamGameStats.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this TeamGameStats.


        :param category: The category of this TeamGameStats.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def stat(self):
        """Gets the stat of this TeamGameStats.  # noqa: E501


        :return: The stat of this TeamGameStats.  # noqa: E501
        :rtype: str
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this TeamGameStats.


        :param stat: The stat of this TeamGameStats.  # noqa: E501
        :type: str
        """

        self._stat = stat

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
        if issubclass(TeamGameStats, dict):
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
        if not isinstance(other, TeamGameStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
