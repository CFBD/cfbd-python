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


class LivePlayByPlayTeams(object):
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
        'team_id': 'int',
        'team': 'str',
        'home_away': 'str',
        'points': 'int',
        'drives': 'int',
        'scoring_opportunities': 'int',
        'points_per_opportunity': 'float',
        'plays': 'int',
        'line_yards': 'int',
        'line_yards_per_rush': 'float',
        'second_level_yards': 'int',
        'second_level_yards_per_rush': 'float',
        'open_field_yards': 'int',
        'open_field_yards_per_rush': 'float',
        'epa_per_play': 'float',
        'total_epa': 'float',
        'passing_epa': 'float',
        'epa_per_pass': 'float',
        'rushing_epa': 'float',
        'epa_per_rush': 'float',
        'success_rate': 'float',
        'standard_down_success_rate': 'float',
        'passing_down_success_rate': 'float',
        'explosiveness': 'float'
    }

    attribute_map = {
        'team_id': 'teamId',
        'team': 'team',
        'home_away': 'homeAway',
        'points': 'points',
        'drives': 'drives',
        'scoring_opportunities': 'scoringOpportunities',
        'points_per_opportunity': 'pointsPerOpportunity',
        'plays': 'plays',
        'line_yards': 'lineYards',
        'line_yards_per_rush': 'lineYardsPerRush',
        'second_level_yards': 'secondLevelYards',
        'second_level_yards_per_rush': 'secondLevelYardsPerRush',
        'open_field_yards': 'openFieldYards',
        'open_field_yards_per_rush': 'openFieldYardsPerRush',
        'epa_per_play': 'epaPerPlay',
        'total_epa': 'totalEpa',
        'passing_epa': 'passingEpa',
        'epa_per_pass': 'epaPerPass',
        'rushing_epa': 'rushingEpa',
        'epa_per_rush': 'epaPerRush',
        'success_rate': 'successRate',
        'standard_down_success_rate': 'standardDownSuccessRate',
        'passing_down_success_rate': 'passingDownSuccessRate',
        'explosiveness': 'explosiveness'
    }

    def __init__(self, team_id=None, team=None, home_away=None, points=None, drives=None, scoring_opportunities=None, points_per_opportunity=None, plays=None, line_yards=None, line_yards_per_rush=None, second_level_yards=None, second_level_yards_per_rush=None, open_field_yards=None, open_field_yards_per_rush=None, epa_per_play=None, total_epa=None, passing_epa=None, epa_per_pass=None, rushing_epa=None, epa_per_rush=None, success_rate=None, standard_down_success_rate=None, passing_down_success_rate=None, explosiveness=None, _configuration=None):  # noqa: E501
        """LivePlayByPlayTeams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._team_id = None
        self._team = None
        self._home_away = None
        self._points = None
        self._drives = None
        self._scoring_opportunities = None
        self._points_per_opportunity = None
        self._plays = None
        self._line_yards = None
        self._line_yards_per_rush = None
        self._second_level_yards = None
        self._second_level_yards_per_rush = None
        self._open_field_yards = None
        self._open_field_yards_per_rush = None
        self._epa_per_play = None
        self._total_epa = None
        self._passing_epa = None
        self._epa_per_pass = None
        self._rushing_epa = None
        self._epa_per_rush = None
        self._success_rate = None
        self._standard_down_success_rate = None
        self._passing_down_success_rate = None
        self._explosiveness = None
        self.discriminator = None

        if team_id is not None:
            self.team_id = team_id
        if team is not None:
            self.team = team
        if home_away is not None:
            self.home_away = home_away
        if points is not None:
            self.points = points
        if drives is not None:
            self.drives = drives
        if scoring_opportunities is not None:
            self.scoring_opportunities = scoring_opportunities
        if points_per_opportunity is not None:
            self.points_per_opportunity = points_per_opportunity
        if plays is not None:
            self.plays = plays
        if line_yards is not None:
            self.line_yards = line_yards
        if line_yards_per_rush is not None:
            self.line_yards_per_rush = line_yards_per_rush
        if second_level_yards is not None:
            self.second_level_yards = second_level_yards
        if second_level_yards_per_rush is not None:
            self.second_level_yards_per_rush = second_level_yards_per_rush
        if open_field_yards is not None:
            self.open_field_yards = open_field_yards
        if open_field_yards_per_rush is not None:
            self.open_field_yards_per_rush = open_field_yards_per_rush
        if epa_per_play is not None:
            self.epa_per_play = epa_per_play
        if total_epa is not None:
            self.total_epa = total_epa
        if passing_epa is not None:
            self.passing_epa = passing_epa
        if epa_per_pass is not None:
            self.epa_per_pass = epa_per_pass
        if rushing_epa is not None:
            self.rushing_epa = rushing_epa
        if epa_per_rush is not None:
            self.epa_per_rush = epa_per_rush
        if success_rate is not None:
            self.success_rate = success_rate
        if standard_down_success_rate is not None:
            self.standard_down_success_rate = standard_down_success_rate
        if passing_down_success_rate is not None:
            self.passing_down_success_rate = passing_down_success_rate
        if explosiveness is not None:
            self.explosiveness = explosiveness

    @property
    def team_id(self):
        """Gets the team_id of this LivePlayByPlayTeams.  # noqa: E501


        :return: The team_id of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this LivePlayByPlayTeams.


        :param team_id: The team_id of this LivePlayByPlayTeams.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def team(self):
        """Gets the team of this LivePlayByPlayTeams.  # noqa: E501


        :return: The team of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this LivePlayByPlayTeams.


        :param team: The team of this LivePlayByPlayTeams.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def home_away(self):
        """Gets the home_away of this LivePlayByPlayTeams.  # noqa: E501


        :return: The home_away of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: str
        """
        return self._home_away

    @home_away.setter
    def home_away(self, home_away):
        """Sets the home_away of this LivePlayByPlayTeams.


        :param home_away: The home_away of this LivePlayByPlayTeams.  # noqa: E501
        :type: str
        """

        self._home_away = home_away

    @property
    def points(self):
        """Gets the points of this LivePlayByPlayTeams.  # noqa: E501


        :return: The points of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this LivePlayByPlayTeams.


        :param points: The points of this LivePlayByPlayTeams.  # noqa: E501
        :type: int
        """

        self._points = points

    @property
    def drives(self):
        """Gets the drives of this LivePlayByPlayTeams.  # noqa: E501


        :return: The drives of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: int
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        """Sets the drives of this LivePlayByPlayTeams.


        :param drives: The drives of this LivePlayByPlayTeams.  # noqa: E501
        :type: int
        """

        self._drives = drives

    @property
    def scoring_opportunities(self):
        """Gets the scoring_opportunities of this LivePlayByPlayTeams.  # noqa: E501


        :return: The scoring_opportunities of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: int
        """
        return self._scoring_opportunities

    @scoring_opportunities.setter
    def scoring_opportunities(self, scoring_opportunities):
        """Sets the scoring_opportunities of this LivePlayByPlayTeams.


        :param scoring_opportunities: The scoring_opportunities of this LivePlayByPlayTeams.  # noqa: E501
        :type: int
        """

        self._scoring_opportunities = scoring_opportunities

    @property
    def points_per_opportunity(self):
        """Gets the points_per_opportunity of this LivePlayByPlayTeams.  # noqa: E501


        :return: The points_per_opportunity of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._points_per_opportunity

    @points_per_opportunity.setter
    def points_per_opportunity(self, points_per_opportunity):
        """Sets the points_per_opportunity of this LivePlayByPlayTeams.


        :param points_per_opportunity: The points_per_opportunity of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._points_per_opportunity = points_per_opportunity

    @property
    def plays(self):
        """Gets the plays of this LivePlayByPlayTeams.  # noqa: E501


        :return: The plays of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: int
        """
        return self._plays

    @plays.setter
    def plays(self, plays):
        """Sets the plays of this LivePlayByPlayTeams.


        :param plays: The plays of this LivePlayByPlayTeams.  # noqa: E501
        :type: int
        """

        self._plays = plays

    @property
    def line_yards(self):
        """Gets the line_yards of this LivePlayByPlayTeams.  # noqa: E501


        :return: The line_yards of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: int
        """
        return self._line_yards

    @line_yards.setter
    def line_yards(self, line_yards):
        """Sets the line_yards of this LivePlayByPlayTeams.


        :param line_yards: The line_yards of this LivePlayByPlayTeams.  # noqa: E501
        :type: int
        """

        self._line_yards = line_yards

    @property
    def line_yards_per_rush(self):
        """Gets the line_yards_per_rush of this LivePlayByPlayTeams.  # noqa: E501


        :return: The line_yards_per_rush of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._line_yards_per_rush

    @line_yards_per_rush.setter
    def line_yards_per_rush(self, line_yards_per_rush):
        """Sets the line_yards_per_rush of this LivePlayByPlayTeams.


        :param line_yards_per_rush: The line_yards_per_rush of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._line_yards_per_rush = line_yards_per_rush

    @property
    def second_level_yards(self):
        """Gets the second_level_yards of this LivePlayByPlayTeams.  # noqa: E501


        :return: The second_level_yards of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: int
        """
        return self._second_level_yards

    @second_level_yards.setter
    def second_level_yards(self, second_level_yards):
        """Sets the second_level_yards of this LivePlayByPlayTeams.


        :param second_level_yards: The second_level_yards of this LivePlayByPlayTeams.  # noqa: E501
        :type: int
        """

        self._second_level_yards = second_level_yards

    @property
    def second_level_yards_per_rush(self):
        """Gets the second_level_yards_per_rush of this LivePlayByPlayTeams.  # noqa: E501


        :return: The second_level_yards_per_rush of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._second_level_yards_per_rush

    @second_level_yards_per_rush.setter
    def second_level_yards_per_rush(self, second_level_yards_per_rush):
        """Sets the second_level_yards_per_rush of this LivePlayByPlayTeams.


        :param second_level_yards_per_rush: The second_level_yards_per_rush of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._second_level_yards_per_rush = second_level_yards_per_rush

    @property
    def open_field_yards(self):
        """Gets the open_field_yards of this LivePlayByPlayTeams.  # noqa: E501


        :return: The open_field_yards of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: int
        """
        return self._open_field_yards

    @open_field_yards.setter
    def open_field_yards(self, open_field_yards):
        """Sets the open_field_yards of this LivePlayByPlayTeams.


        :param open_field_yards: The open_field_yards of this LivePlayByPlayTeams.  # noqa: E501
        :type: int
        """

        self._open_field_yards = open_field_yards

    @property
    def open_field_yards_per_rush(self):
        """Gets the open_field_yards_per_rush of this LivePlayByPlayTeams.  # noqa: E501


        :return: The open_field_yards_per_rush of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._open_field_yards_per_rush

    @open_field_yards_per_rush.setter
    def open_field_yards_per_rush(self, open_field_yards_per_rush):
        """Sets the open_field_yards_per_rush of this LivePlayByPlayTeams.


        :param open_field_yards_per_rush: The open_field_yards_per_rush of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._open_field_yards_per_rush = open_field_yards_per_rush

    @property
    def epa_per_play(self):
        """Gets the epa_per_play of this LivePlayByPlayTeams.  # noqa: E501


        :return: The epa_per_play of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._epa_per_play

    @epa_per_play.setter
    def epa_per_play(self, epa_per_play):
        """Sets the epa_per_play of this LivePlayByPlayTeams.


        :param epa_per_play: The epa_per_play of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._epa_per_play = epa_per_play

    @property
    def total_epa(self):
        """Gets the total_epa of this LivePlayByPlayTeams.  # noqa: E501


        :return: The total_epa of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._total_epa

    @total_epa.setter
    def total_epa(self, total_epa):
        """Sets the total_epa of this LivePlayByPlayTeams.


        :param total_epa: The total_epa of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._total_epa = total_epa

    @property
    def passing_epa(self):
        """Gets the passing_epa of this LivePlayByPlayTeams.  # noqa: E501


        :return: The passing_epa of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._passing_epa

    @passing_epa.setter
    def passing_epa(self, passing_epa):
        """Sets the passing_epa of this LivePlayByPlayTeams.


        :param passing_epa: The passing_epa of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._passing_epa = passing_epa

    @property
    def epa_per_pass(self):
        """Gets the epa_per_pass of this LivePlayByPlayTeams.  # noqa: E501


        :return: The epa_per_pass of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._epa_per_pass

    @epa_per_pass.setter
    def epa_per_pass(self, epa_per_pass):
        """Sets the epa_per_pass of this LivePlayByPlayTeams.


        :param epa_per_pass: The epa_per_pass of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._epa_per_pass = epa_per_pass

    @property
    def rushing_epa(self):
        """Gets the rushing_epa of this LivePlayByPlayTeams.  # noqa: E501


        :return: The rushing_epa of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._rushing_epa

    @rushing_epa.setter
    def rushing_epa(self, rushing_epa):
        """Sets the rushing_epa of this LivePlayByPlayTeams.


        :param rushing_epa: The rushing_epa of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._rushing_epa = rushing_epa

    @property
    def epa_per_rush(self):
        """Gets the epa_per_rush of this LivePlayByPlayTeams.  # noqa: E501


        :return: The epa_per_rush of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._epa_per_rush

    @epa_per_rush.setter
    def epa_per_rush(self, epa_per_rush):
        """Sets the epa_per_rush of this LivePlayByPlayTeams.


        :param epa_per_rush: The epa_per_rush of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._epa_per_rush = epa_per_rush

    @property
    def success_rate(self):
        """Gets the success_rate of this LivePlayByPlayTeams.  # noqa: E501


        :return: The success_rate of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this LivePlayByPlayTeams.


        :param success_rate: The success_rate of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._success_rate = success_rate

    @property
    def standard_down_success_rate(self):
        """Gets the standard_down_success_rate of this LivePlayByPlayTeams.  # noqa: E501


        :return: The standard_down_success_rate of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._standard_down_success_rate

    @standard_down_success_rate.setter
    def standard_down_success_rate(self, standard_down_success_rate):
        """Sets the standard_down_success_rate of this LivePlayByPlayTeams.


        :param standard_down_success_rate: The standard_down_success_rate of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._standard_down_success_rate = standard_down_success_rate

    @property
    def passing_down_success_rate(self):
        """Gets the passing_down_success_rate of this LivePlayByPlayTeams.  # noqa: E501


        :return: The passing_down_success_rate of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._passing_down_success_rate

    @passing_down_success_rate.setter
    def passing_down_success_rate(self, passing_down_success_rate):
        """Sets the passing_down_success_rate of this LivePlayByPlayTeams.


        :param passing_down_success_rate: The passing_down_success_rate of this LivePlayByPlayTeams.  # noqa: E501
        :type: float
        """

        self._passing_down_success_rate = passing_down_success_rate

    @property
    def explosiveness(self):
        """Gets the explosiveness of this LivePlayByPlayTeams.  # noqa: E501


        :return: The explosiveness of this LivePlayByPlayTeams.  # noqa: E501
        :rtype: float
        """
        return self._explosiveness

    @explosiveness.setter
    def explosiveness(self, explosiveness):
        """Sets the explosiveness of this LivePlayByPlayTeams.


        :param explosiveness: The explosiveness of this LivePlayByPlayTeams.  # noqa: E501
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
        if issubclass(LivePlayByPlayTeams, dict):
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
        if not isinstance(other, LivePlayByPlayTeams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LivePlayByPlayTeams):
            return True

        return self.to_dict() != other.to_dict()
