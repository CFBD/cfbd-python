# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.5.2
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class TeamFPIRatingEfficiencies(object):
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
        'overall': 'float',
        'offense': 'float',
        'defense': 'float',
        'special_teams': 'float'
    }

    attribute_map = {
        'overall': 'overall',
        'offense': 'offense',
        'defense': 'defense',
        'special_teams': 'specialTeams'
    }

    def __init__(self, overall=None, offense=None, defense=None, special_teams=None, _configuration=None):  # noqa: E501
        """TeamFPIRatingEfficiencies - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._overall = None
        self._offense = None
        self._defense = None
        self._special_teams = None
        self.discriminator = None

        if overall is not None:
            self.overall = overall
        if offense is not None:
            self.offense = offense
        if defense is not None:
            self.defense = defense
        if special_teams is not None:
            self.special_teams = special_teams

    @property
    def overall(self):
        """Gets the overall of this TeamFPIRatingEfficiencies.  # noqa: E501


        :return: The overall of this TeamFPIRatingEfficiencies.  # noqa: E501
        :rtype: float
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this TeamFPIRatingEfficiencies.


        :param overall: The overall of this TeamFPIRatingEfficiencies.  # noqa: E501
        :type: float
        """

        self._overall = overall

    @property
    def offense(self):
        """Gets the offense of this TeamFPIRatingEfficiencies.  # noqa: E501


        :return: The offense of this TeamFPIRatingEfficiencies.  # noqa: E501
        :rtype: float
        """
        return self._offense

    @offense.setter
    def offense(self, offense):
        """Sets the offense of this TeamFPIRatingEfficiencies.


        :param offense: The offense of this TeamFPIRatingEfficiencies.  # noqa: E501
        :type: float
        """

        self._offense = offense

    @property
    def defense(self):
        """Gets the defense of this TeamFPIRatingEfficiencies.  # noqa: E501


        :return: The defense of this TeamFPIRatingEfficiencies.  # noqa: E501
        :rtype: float
        """
        return self._defense

    @defense.setter
    def defense(self, defense):
        """Sets the defense of this TeamFPIRatingEfficiencies.


        :param defense: The defense of this TeamFPIRatingEfficiencies.  # noqa: E501
        :type: float
        """

        self._defense = defense

    @property
    def special_teams(self):
        """Gets the special_teams of this TeamFPIRatingEfficiencies.  # noqa: E501


        :return: The special_teams of this TeamFPIRatingEfficiencies.  # noqa: E501
        :rtype: float
        """
        return self._special_teams

    @special_teams.setter
    def special_teams(self, special_teams):
        """Sets the special_teams of this TeamFPIRatingEfficiencies.


        :param special_teams: The special_teams of this TeamFPIRatingEfficiencies.  # noqa: E501
        :type: float
        """

        self._special_teams = special_teams

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
        if issubclass(TeamFPIRatingEfficiencies, dict):
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
        if not isinstance(other, TeamFPIRatingEfficiencies):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamFPIRatingEfficiencies):
            return True

        return self.to_dict() != other.to_dict()
