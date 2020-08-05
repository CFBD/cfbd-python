# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.9
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BoxScoreTeamsScoringOpportunities(object):
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
        'opportunities': 'int',
        'points': 'int',
        'points_per_opportunity': 'float'
    }

    attribute_map = {
        'team': 'team',
        'opportunities': 'opportunities',
        'points': 'points',
        'points_per_opportunity': 'pointsPerOpportunity'
    }

    def __init__(self, team=None, opportunities=None, points=None, points_per_opportunity=None):  # noqa: E501
        """BoxScoreTeamsScoringOpportunities - a model defined in Swagger"""  # noqa: E501

        self._team = None
        self._opportunities = None
        self._points = None
        self._points_per_opportunity = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if opportunities is not None:
            self.opportunities = opportunities
        if points is not None:
            self.points = points
        if points_per_opportunity is not None:
            self.points_per_opportunity = points_per_opportunity

    @property
    def team(self):
        """Gets the team of this BoxScoreTeamsScoringOpportunities.  # noqa: E501


        :return: The team of this BoxScoreTeamsScoringOpportunities.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BoxScoreTeamsScoringOpportunities.


        :param team: The team of this BoxScoreTeamsScoringOpportunities.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def opportunities(self):
        """Gets the opportunities of this BoxScoreTeamsScoringOpportunities.  # noqa: E501


        :return: The opportunities of this BoxScoreTeamsScoringOpportunities.  # noqa: E501
        :rtype: int
        """
        return self._opportunities

    @opportunities.setter
    def opportunities(self, opportunities):
        """Sets the opportunities of this BoxScoreTeamsScoringOpportunities.


        :param opportunities: The opportunities of this BoxScoreTeamsScoringOpportunities.  # noqa: E501
        :type: int
        """

        self._opportunities = opportunities

    @property
    def points(self):
        """Gets the points of this BoxScoreTeamsScoringOpportunities.  # noqa: E501


        :return: The points of this BoxScoreTeamsScoringOpportunities.  # noqa: E501
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this BoxScoreTeamsScoringOpportunities.


        :param points: The points of this BoxScoreTeamsScoringOpportunities.  # noqa: E501
        :type: int
        """

        self._points = points

    @property
    def points_per_opportunity(self):
        """Gets the points_per_opportunity of this BoxScoreTeamsScoringOpportunities.  # noqa: E501


        :return: The points_per_opportunity of this BoxScoreTeamsScoringOpportunities.  # noqa: E501
        :rtype: float
        """
        return self._points_per_opportunity

    @points_per_opportunity.setter
    def points_per_opportunity(self, points_per_opportunity):
        """Sets the points_per_opportunity of this BoxScoreTeamsScoringOpportunities.


        :param points_per_opportunity: The points_per_opportunity of this BoxScoreTeamsScoringOpportunities.  # noqa: E501
        :type: float
        """

        self._points_per_opportunity = points_per_opportunity

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
        if issubclass(BoxScoreTeamsScoringOpportunities, dict):
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
        if not isinstance(other, BoxScoreTeamsScoringOpportunities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
