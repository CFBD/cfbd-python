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


class TeamTalent(object):
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
        'year': 'int',
        'school': 'str',
        'talent': 'float'
    }

    attribute_map = {
        'year': 'year',
        'school': 'school',
        'talent': 'talent'
    }

    def __init__(self, year=None, school=None, talent=None, _configuration=None):  # noqa: E501
        """TeamTalent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._year = None
        self._school = None
        self._talent = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if school is not None:
            self.school = school
        if talent is not None:
            self.talent = talent

    @property
    def year(self):
        """Gets the year of this TeamTalent.  # noqa: E501


        :return: The year of this TeamTalent.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this TeamTalent.


        :param year: The year of this TeamTalent.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def school(self):
        """Gets the school of this TeamTalent.  # noqa: E501


        :return: The school of this TeamTalent.  # noqa: E501
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this TeamTalent.


        :param school: The school of this TeamTalent.  # noqa: E501
        :type: str
        """

        self._school = school

    @property
    def talent(self):
        """Gets the talent of this TeamTalent.  # noqa: E501


        :return: The talent of this TeamTalent.  # noqa: E501
        :rtype: float
        """
        return self._talent

    @talent.setter
    def talent(self, talent):
        """Sets the talent of this TeamTalent.


        :param talent: The talent of this TeamTalent.  # noqa: E501
        :type: float
        """

        self._talent = talent

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
        if issubclass(TeamTalent, dict):
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
        if not isinstance(other, TeamTalent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamTalent):
            return True

        return self.to_dict() != other.to_dict()
