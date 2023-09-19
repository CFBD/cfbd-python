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


class TeamSPRatingDefenseHavoc(object):
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
        'total': 'float',
        'front_seven': 'float',
        'db': 'float'
    }

    attribute_map = {
        'total': 'total',
        'front_seven': 'frontSeven',
        'db': 'db'
    }

    def __init__(self, total=None, front_seven=None, db=None, _configuration=None):  # noqa: E501
        """TeamSPRatingDefenseHavoc - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total = None
        self._front_seven = None
        self._db = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if front_seven is not None:
            self.front_seven = front_seven
        if db is not None:
            self.db = db

    @property
    def total(self):
        """Gets the total of this TeamSPRatingDefenseHavoc.  # noqa: E501


        :return: The total of this TeamSPRatingDefenseHavoc.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TeamSPRatingDefenseHavoc.


        :param total: The total of this TeamSPRatingDefenseHavoc.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def front_seven(self):
        """Gets the front_seven of this TeamSPRatingDefenseHavoc.  # noqa: E501


        :return: The front_seven of this TeamSPRatingDefenseHavoc.  # noqa: E501
        :rtype: float
        """
        return self._front_seven

    @front_seven.setter
    def front_seven(self, front_seven):
        """Sets the front_seven of this TeamSPRatingDefenseHavoc.


        :param front_seven: The front_seven of this TeamSPRatingDefenseHavoc.  # noqa: E501
        :type: float
        """

        self._front_seven = front_seven

    @property
    def db(self):
        """Gets the db of this TeamSPRatingDefenseHavoc.  # noqa: E501


        :return: The db of this TeamSPRatingDefenseHavoc.  # noqa: E501
        :rtype: float
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this TeamSPRatingDefenseHavoc.


        :param db: The db of this TeamSPRatingDefenseHavoc.  # noqa: E501
        :type: float
        """

        self._db = db

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
        if issubclass(TeamSPRatingDefenseHavoc, dict):
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
        if not isinstance(other, TeamSPRatingDefenseHavoc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamSPRatingDefenseHavoc):
            return True

        return self.to_dict() != other.to_dict()
