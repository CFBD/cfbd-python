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


class LivePlayByPlayDrives(object):
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
        'id': 'int',
        'offense_id': 'int',
        'offense': 'str',
        'defense_id': 'int',
        'defense': 'str',
        'play_count': 'int',
        'yards': 'int',
        'start_period': 'int',
        'start_clock': 'str',
        'start_yards_to_goal': 'int',
        'end_period': 'int',
        'end_clock': 'str',
        'end_yards_to_goal': 'int',
        'duration': 'str',
        'scoring_opportunity': 'bool',
        'plays': 'list[LivePlayByPlayPlays]'
    }

    attribute_map = {
        'id': 'id',
        'offense_id': 'offenseId',
        'offense': 'offense',
        'defense_id': 'defenseId',
        'defense': 'defense',
        'play_count': 'playCount',
        'yards': 'yards',
        'start_period': 'startPeriod',
        'start_clock': 'startClock',
        'start_yards_to_goal': 'startYardsToGoal',
        'end_period': 'endPeriod',
        'end_clock': 'endClock',
        'end_yards_to_goal': 'endYardsToGoal',
        'duration': 'duration',
        'scoring_opportunity': 'scoringOpportunity',
        'plays': 'plays'
    }

    def __init__(self, id=None, offense_id=None, offense=None, defense_id=None, defense=None, play_count=None, yards=None, start_period=None, start_clock=None, start_yards_to_goal=None, end_period=None, end_clock=None, end_yards_to_goal=None, duration=None, scoring_opportunity=None, plays=None, _configuration=None):  # noqa: E501
        """LivePlayByPlayDrives - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._offense_id = None
        self._offense = None
        self._defense_id = None
        self._defense = None
        self._play_count = None
        self._yards = None
        self._start_period = None
        self._start_clock = None
        self._start_yards_to_goal = None
        self._end_period = None
        self._end_clock = None
        self._end_yards_to_goal = None
        self._duration = None
        self._scoring_opportunity = None
        self._plays = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if offense_id is not None:
            self.offense_id = offense_id
        if offense is not None:
            self.offense = offense
        if defense_id is not None:
            self.defense_id = defense_id
        if defense is not None:
            self.defense = defense
        if play_count is not None:
            self.play_count = play_count
        if yards is not None:
            self.yards = yards
        if start_period is not None:
            self.start_period = start_period
        if start_clock is not None:
            self.start_clock = start_clock
        if start_yards_to_goal is not None:
            self.start_yards_to_goal = start_yards_to_goal
        if end_period is not None:
            self.end_period = end_period
        if end_clock is not None:
            self.end_clock = end_clock
        if end_yards_to_goal is not None:
            self.end_yards_to_goal = end_yards_to_goal
        if duration is not None:
            self.duration = duration
        if scoring_opportunity is not None:
            self.scoring_opportunity = scoring_opportunity
        if plays is not None:
            self.plays = plays

    @property
    def id(self):
        """Gets the id of this LivePlayByPlayDrives.  # noqa: E501


        :return: The id of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LivePlayByPlayDrives.


        :param id: The id of this LivePlayByPlayDrives.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def offense_id(self):
        """Gets the offense_id of this LivePlayByPlayDrives.  # noqa: E501


        :return: The offense_id of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: int
        """
        return self._offense_id

    @offense_id.setter
    def offense_id(self, offense_id):
        """Sets the offense_id of this LivePlayByPlayDrives.


        :param offense_id: The offense_id of this LivePlayByPlayDrives.  # noqa: E501
        :type: int
        """

        self._offense_id = offense_id

    @property
    def offense(self):
        """Gets the offense of this LivePlayByPlayDrives.  # noqa: E501


        :return: The offense of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: str
        """
        return self._offense

    @offense.setter
    def offense(self, offense):
        """Sets the offense of this LivePlayByPlayDrives.


        :param offense: The offense of this LivePlayByPlayDrives.  # noqa: E501
        :type: str
        """

        self._offense = offense

    @property
    def defense_id(self):
        """Gets the defense_id of this LivePlayByPlayDrives.  # noqa: E501


        :return: The defense_id of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: int
        """
        return self._defense_id

    @defense_id.setter
    def defense_id(self, defense_id):
        """Sets the defense_id of this LivePlayByPlayDrives.


        :param defense_id: The defense_id of this LivePlayByPlayDrives.  # noqa: E501
        :type: int
        """

        self._defense_id = defense_id

    @property
    def defense(self):
        """Gets the defense of this LivePlayByPlayDrives.  # noqa: E501


        :return: The defense of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: str
        """
        return self._defense

    @defense.setter
    def defense(self, defense):
        """Sets the defense of this LivePlayByPlayDrives.


        :param defense: The defense of this LivePlayByPlayDrives.  # noqa: E501
        :type: str
        """

        self._defense = defense

    @property
    def play_count(self):
        """Gets the play_count of this LivePlayByPlayDrives.  # noqa: E501


        :return: The play_count of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: int
        """
        return self._play_count

    @play_count.setter
    def play_count(self, play_count):
        """Sets the play_count of this LivePlayByPlayDrives.


        :param play_count: The play_count of this LivePlayByPlayDrives.  # noqa: E501
        :type: int
        """

        self._play_count = play_count

    @property
    def yards(self):
        """Gets the yards of this LivePlayByPlayDrives.  # noqa: E501


        :return: The yards of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: int
        """
        return self._yards

    @yards.setter
    def yards(self, yards):
        """Sets the yards of this LivePlayByPlayDrives.


        :param yards: The yards of this LivePlayByPlayDrives.  # noqa: E501
        :type: int
        """

        self._yards = yards

    @property
    def start_period(self):
        """Gets the start_period of this LivePlayByPlayDrives.  # noqa: E501


        :return: The start_period of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: int
        """
        return self._start_period

    @start_period.setter
    def start_period(self, start_period):
        """Sets the start_period of this LivePlayByPlayDrives.


        :param start_period: The start_period of this LivePlayByPlayDrives.  # noqa: E501
        :type: int
        """

        self._start_period = start_period

    @property
    def start_clock(self):
        """Gets the start_clock of this LivePlayByPlayDrives.  # noqa: E501


        :return: The start_clock of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: str
        """
        return self._start_clock

    @start_clock.setter
    def start_clock(self, start_clock):
        """Sets the start_clock of this LivePlayByPlayDrives.


        :param start_clock: The start_clock of this LivePlayByPlayDrives.  # noqa: E501
        :type: str
        """

        self._start_clock = start_clock

    @property
    def start_yards_to_goal(self):
        """Gets the start_yards_to_goal of this LivePlayByPlayDrives.  # noqa: E501


        :return: The start_yards_to_goal of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: int
        """
        return self._start_yards_to_goal

    @start_yards_to_goal.setter
    def start_yards_to_goal(self, start_yards_to_goal):
        """Sets the start_yards_to_goal of this LivePlayByPlayDrives.


        :param start_yards_to_goal: The start_yards_to_goal of this LivePlayByPlayDrives.  # noqa: E501
        :type: int
        """

        self._start_yards_to_goal = start_yards_to_goal

    @property
    def end_period(self):
        """Gets the end_period of this LivePlayByPlayDrives.  # noqa: E501


        :return: The end_period of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: int
        """
        return self._end_period

    @end_period.setter
    def end_period(self, end_period):
        """Sets the end_period of this LivePlayByPlayDrives.


        :param end_period: The end_period of this LivePlayByPlayDrives.  # noqa: E501
        :type: int
        """

        self._end_period = end_period

    @property
    def end_clock(self):
        """Gets the end_clock of this LivePlayByPlayDrives.  # noqa: E501


        :return: The end_clock of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: str
        """
        return self._end_clock

    @end_clock.setter
    def end_clock(self, end_clock):
        """Sets the end_clock of this LivePlayByPlayDrives.


        :param end_clock: The end_clock of this LivePlayByPlayDrives.  # noqa: E501
        :type: str
        """

        self._end_clock = end_clock

    @property
    def end_yards_to_goal(self):
        """Gets the end_yards_to_goal of this LivePlayByPlayDrives.  # noqa: E501


        :return: The end_yards_to_goal of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: int
        """
        return self._end_yards_to_goal

    @end_yards_to_goal.setter
    def end_yards_to_goal(self, end_yards_to_goal):
        """Sets the end_yards_to_goal of this LivePlayByPlayDrives.


        :param end_yards_to_goal: The end_yards_to_goal of this LivePlayByPlayDrives.  # noqa: E501
        :type: int
        """

        self._end_yards_to_goal = end_yards_to_goal

    @property
    def duration(self):
        """Gets the duration of this LivePlayByPlayDrives.  # noqa: E501


        :return: The duration of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this LivePlayByPlayDrives.


        :param duration: The duration of this LivePlayByPlayDrives.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def scoring_opportunity(self):
        """Gets the scoring_opportunity of this LivePlayByPlayDrives.  # noqa: E501


        :return: The scoring_opportunity of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: bool
        """
        return self._scoring_opportunity

    @scoring_opportunity.setter
    def scoring_opportunity(self, scoring_opportunity):
        """Sets the scoring_opportunity of this LivePlayByPlayDrives.


        :param scoring_opportunity: The scoring_opportunity of this LivePlayByPlayDrives.  # noqa: E501
        :type: bool
        """

        self._scoring_opportunity = scoring_opportunity

    @property
    def plays(self):
        """Gets the plays of this LivePlayByPlayDrives.  # noqa: E501


        :return: The plays of this LivePlayByPlayDrives.  # noqa: E501
        :rtype: list[LivePlayByPlayPlays]
        """
        return self._plays

    @plays.setter
    def plays(self, plays):
        """Sets the plays of this LivePlayByPlayDrives.


        :param plays: The plays of this LivePlayByPlayDrives.  # noqa: E501
        :type: list[LivePlayByPlayPlays]
        """

        self._plays = plays

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
        if issubclass(LivePlayByPlayDrives, dict):
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
        if not isinstance(other, LivePlayByPlayDrives):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LivePlayByPlayDrives):
            return True

        return self.to_dict() != other.to_dict()
