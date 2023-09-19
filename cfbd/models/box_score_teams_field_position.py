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


class BoxScoreTeamsFieldPosition(object):
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
        'team': 'str',
        'average_start': 'float',
        'average_starting_predicted_points': 'float'
    }

    attribute_map = {
        'team': 'team',
        'average_start': 'averageStart',
        'average_starting_predicted_points': 'averageStartingPredictedPoints'
    }

    def __init__(self, team=None, average_start=None, average_starting_predicted_points=None, _configuration=None):  # noqa: E501
        """BoxScoreTeamsFieldPosition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._team = None
        self._average_start = None
        self._average_starting_predicted_points = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if average_start is not None:
            self.average_start = average_start
        if average_starting_predicted_points is not None:
            self.average_starting_predicted_points = average_starting_predicted_points

    @property
    def team(self):
        """Gets the team of this BoxScoreTeamsFieldPosition.  # noqa: E501


        :return: The team of this BoxScoreTeamsFieldPosition.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BoxScoreTeamsFieldPosition.


        :param team: The team of this BoxScoreTeamsFieldPosition.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def average_start(self):
        """Gets the average_start of this BoxScoreTeamsFieldPosition.  # noqa: E501


        :return: The average_start of this BoxScoreTeamsFieldPosition.  # noqa: E501
        :rtype: float
        """
        return self._average_start

    @average_start.setter
    def average_start(self, average_start):
        """Sets the average_start of this BoxScoreTeamsFieldPosition.


        :param average_start: The average_start of this BoxScoreTeamsFieldPosition.  # noqa: E501
        :type: float
        """

        self._average_start = average_start

    @property
    def average_starting_predicted_points(self):
        """Gets the average_starting_predicted_points of this BoxScoreTeamsFieldPosition.  # noqa: E501


        :return: The average_starting_predicted_points of this BoxScoreTeamsFieldPosition.  # noqa: E501
        :rtype: float
        """
        return self._average_starting_predicted_points

    @average_starting_predicted_points.setter
    def average_starting_predicted_points(self, average_starting_predicted_points):
        """Sets the average_starting_predicted_points of this BoxScoreTeamsFieldPosition.


        :param average_starting_predicted_points: The average_starting_predicted_points of this BoxScoreTeamsFieldPosition.  # noqa: E501
        :type: float
        """

        self._average_starting_predicted_points = average_starting_predicted_points

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
        if issubclass(BoxScoreTeamsFieldPosition, dict):
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
        if not isinstance(other, BoxScoreTeamsFieldPosition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoxScoreTeamsFieldPosition):
            return True

        return self.to_dict() != other.to_dict()
