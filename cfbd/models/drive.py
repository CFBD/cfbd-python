# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\").  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class Drive(object):
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
        'offense': 'str',
        'offense_conference': 'str',
        'defense': 'str',
        'defense_conference': 'str',
        'game_id': 'int',
        'id': 'int',
        'drive_number': 'int',
        'scoring': 'bool',
        'start_period': 'int',
        'start_yardline': 'int',
        'start_yards_to_goal': 'int',
        'start_time': 'object',
        'end_period': 'int',
        'end_yardline': 'int',
        'end_yards_to_goal': 'int',
        'end_time': 'object',
        'plays': 'int',
        'yards': 'int',
        'drive_result': 'str',
        'is_home_offense': 'bool',
        'start_offense_score': 'int',
        'start_defense_score': 'int',
        'end_offense_score': 'int',
        'end_defense_score': 'int'
    }

    attribute_map = {
        'offense': 'offense',
        'offense_conference': 'offense_conference',
        'defense': 'defense',
        'defense_conference': 'defense_conference',
        'game_id': 'game_id',
        'id': 'id',
        'drive_number': 'drive_number',
        'scoring': 'scoring',
        'start_period': 'start_period',
        'start_yardline': 'start_yardline',
        'start_yards_to_goal': 'start_yards_to_goal',
        'start_time': 'start_time',
        'end_period': 'end_period',
        'end_yardline': 'end_yardline',
        'end_yards_to_goal': 'end_yards_to_goal',
        'end_time': 'end_time',
        'plays': 'plays',
        'yards': 'yards',
        'drive_result': 'drive_result',
        'is_home_offense': 'is_home_offense',
        'start_offense_score': 'start_offense_score',
        'start_defense_score': 'start_defense_score',
        'end_offense_score': 'end_offense_score',
        'end_defense_score': 'end_defense_score'
    }

    def __init__(self, offense=None, offense_conference=None, defense=None, defense_conference=None, game_id=None, id=None, drive_number=None, scoring=None, start_period=None, start_yardline=None, start_yards_to_goal=None, start_time=None, end_period=None, end_yardline=None, end_yards_to_goal=None, end_time=None, plays=None, yards=None, drive_result=None, is_home_offense=None, start_offense_score=None, start_defense_score=None, end_offense_score=None, end_defense_score=None, _configuration=None):  # noqa: E501
        """Drive - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._offense = None
        self._offense_conference = None
        self._defense = None
        self._defense_conference = None
        self._game_id = None
        self._id = None
        self._drive_number = None
        self._scoring = None
        self._start_period = None
        self._start_yardline = None
        self._start_yards_to_goal = None
        self._start_time = None
        self._end_period = None
        self._end_yardline = None
        self._end_yards_to_goal = None
        self._end_time = None
        self._plays = None
        self._yards = None
        self._drive_result = None
        self._is_home_offense = None
        self._start_offense_score = None
        self._start_defense_score = None
        self._end_offense_score = None
        self._end_defense_score = None
        self.discriminator = None

        if offense is not None:
            self.offense = offense
        if offense_conference is not None:
            self.offense_conference = offense_conference
        if defense is not None:
            self.defense = defense
        if defense_conference is not None:
            self.defense_conference = defense_conference
        if game_id is not None:
            self.game_id = game_id
        if id is not None:
            self.id = id
        if drive_number is not None:
            self.drive_number = drive_number
        if scoring is not None:
            self.scoring = scoring
        if start_period is not None:
            self.start_period = start_period
        if start_yardline is not None:
            self.start_yardline = start_yardline
        if start_yards_to_goal is not None:
            self.start_yards_to_goal = start_yards_to_goal
        if start_time is not None:
            self.start_time = start_time
        if end_period is not None:
            self.end_period = end_period
        if end_yardline is not None:
            self.end_yardline = end_yardline
        if end_yards_to_goal is not None:
            self.end_yards_to_goal = end_yards_to_goal
        if end_time is not None:
            self.end_time = end_time
        if plays is not None:
            self.plays = plays
        if yards is not None:
            self.yards = yards
        if drive_result is not None:
            self.drive_result = drive_result
        if is_home_offense is not None:
            self.is_home_offense = is_home_offense
        if start_offense_score is not None:
            self.start_offense_score = start_offense_score
        if start_defense_score is not None:
            self.start_defense_score = start_defense_score
        if end_offense_score is not None:
            self.end_offense_score = end_offense_score
        if end_defense_score is not None:
            self.end_defense_score = end_defense_score

    @property
    def offense(self):
        """Gets the offense of this Drive.  # noqa: E501


        :return: The offense of this Drive.  # noqa: E501
        :rtype: str
        """
        return self._offense

    @offense.setter
    def offense(self, offense):
        """Sets the offense of this Drive.


        :param offense: The offense of this Drive.  # noqa: E501
        :type: str
        """

        self._offense = offense

    @property
    def offense_conference(self):
        """Gets the offense_conference of this Drive.  # noqa: E501


        :return: The offense_conference of this Drive.  # noqa: E501
        :rtype: str
        """
        return self._offense_conference

    @offense_conference.setter
    def offense_conference(self, offense_conference):
        """Sets the offense_conference of this Drive.


        :param offense_conference: The offense_conference of this Drive.  # noqa: E501
        :type: str
        """

        self._offense_conference = offense_conference

    @property
    def defense(self):
        """Gets the defense of this Drive.  # noqa: E501


        :return: The defense of this Drive.  # noqa: E501
        :rtype: str
        """
        return self._defense

    @defense.setter
    def defense(self, defense):
        """Sets the defense of this Drive.


        :param defense: The defense of this Drive.  # noqa: E501
        :type: str
        """

        self._defense = defense

    @property
    def defense_conference(self):
        """Gets the defense_conference of this Drive.  # noqa: E501


        :return: The defense_conference of this Drive.  # noqa: E501
        :rtype: str
        """
        return self._defense_conference

    @defense_conference.setter
    def defense_conference(self, defense_conference):
        """Sets the defense_conference of this Drive.


        :param defense_conference: The defense_conference of this Drive.  # noqa: E501
        :type: str
        """

        self._defense_conference = defense_conference

    @property
    def game_id(self):
        """Gets the game_id of this Drive.  # noqa: E501


        :return: The game_id of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this Drive.


        :param game_id: The game_id of this Drive.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def id(self):
        """Gets the id of this Drive.  # noqa: E501


        :return: The id of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Drive.


        :param id: The id of this Drive.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def drive_number(self):
        """Gets the drive_number of this Drive.  # noqa: E501


        :return: The drive_number of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._drive_number

    @drive_number.setter
    def drive_number(self, drive_number):
        """Sets the drive_number of this Drive.


        :param drive_number: The drive_number of this Drive.  # noqa: E501
        :type: int
        """

        self._drive_number = drive_number

    @property
    def scoring(self):
        """Gets the scoring of this Drive.  # noqa: E501


        :return: The scoring of this Drive.  # noqa: E501
        :rtype: bool
        """
        return self._scoring

    @scoring.setter
    def scoring(self, scoring):
        """Sets the scoring of this Drive.


        :param scoring: The scoring of this Drive.  # noqa: E501
        :type: bool
        """

        self._scoring = scoring

    @property
    def start_period(self):
        """Gets the start_period of this Drive.  # noqa: E501


        :return: The start_period of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._start_period

    @start_period.setter
    def start_period(self, start_period):
        """Sets the start_period of this Drive.


        :param start_period: The start_period of this Drive.  # noqa: E501
        :type: int
        """

        self._start_period = start_period

    @property
    def start_yardline(self):
        """Gets the start_yardline of this Drive.  # noqa: E501


        :return: The start_yardline of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._start_yardline

    @start_yardline.setter
    def start_yardline(self, start_yardline):
        """Sets the start_yardline of this Drive.


        :param start_yardline: The start_yardline of this Drive.  # noqa: E501
        :type: int
        """

        self._start_yardline = start_yardline

    @property
    def start_yards_to_goal(self):
        """Gets the start_yards_to_goal of this Drive.  # noqa: E501


        :return: The start_yards_to_goal of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._start_yards_to_goal

    @start_yards_to_goal.setter
    def start_yards_to_goal(self, start_yards_to_goal):
        """Sets the start_yards_to_goal of this Drive.


        :param start_yards_to_goal: The start_yards_to_goal of this Drive.  # noqa: E501
        :type: int
        """

        self._start_yards_to_goal = start_yards_to_goal

    @property
    def start_time(self):
        """Gets the start_time of this Drive.  # noqa: E501


        :return: The start_time of this Drive.  # noqa: E501
        :rtype: object
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Drive.


        :param start_time: The start_time of this Drive.  # noqa: E501
        :type: object
        """

        self._start_time = start_time

    @property
    def end_period(self):
        """Gets the end_period of this Drive.  # noqa: E501


        :return: The end_period of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._end_period

    @end_period.setter
    def end_period(self, end_period):
        """Sets the end_period of this Drive.


        :param end_period: The end_period of this Drive.  # noqa: E501
        :type: int
        """

        self._end_period = end_period

    @property
    def end_yardline(self):
        """Gets the end_yardline of this Drive.  # noqa: E501


        :return: The end_yardline of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._end_yardline

    @end_yardline.setter
    def end_yardline(self, end_yardline):
        """Sets the end_yardline of this Drive.


        :param end_yardline: The end_yardline of this Drive.  # noqa: E501
        :type: int
        """

        self._end_yardline = end_yardline

    @property
    def end_yards_to_goal(self):
        """Gets the end_yards_to_goal of this Drive.  # noqa: E501


        :return: The end_yards_to_goal of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._end_yards_to_goal

    @end_yards_to_goal.setter
    def end_yards_to_goal(self, end_yards_to_goal):
        """Sets the end_yards_to_goal of this Drive.


        :param end_yards_to_goal: The end_yards_to_goal of this Drive.  # noqa: E501
        :type: int
        """

        self._end_yards_to_goal = end_yards_to_goal

    @property
    def end_time(self):
        """Gets the end_time of this Drive.  # noqa: E501


        :return: The end_time of this Drive.  # noqa: E501
        :rtype: object
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Drive.


        :param end_time: The end_time of this Drive.  # noqa: E501
        :type: object
        """

        self._end_time = end_time

    @property
    def plays(self):
        """Gets the plays of this Drive.  # noqa: E501


        :return: The plays of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._plays

    @plays.setter
    def plays(self, plays):
        """Sets the plays of this Drive.


        :param plays: The plays of this Drive.  # noqa: E501
        :type: int
        """

        self._plays = plays

    @property
    def yards(self):
        """Gets the yards of this Drive.  # noqa: E501


        :return: The yards of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._yards

    @yards.setter
    def yards(self, yards):
        """Sets the yards of this Drive.


        :param yards: The yards of this Drive.  # noqa: E501
        :type: int
        """

        self._yards = yards

    @property
    def drive_result(self):
        """Gets the drive_result of this Drive.  # noqa: E501


        :return: The drive_result of this Drive.  # noqa: E501
        :rtype: str
        """
        return self._drive_result

    @drive_result.setter
    def drive_result(self, drive_result):
        """Sets the drive_result of this Drive.


        :param drive_result: The drive_result of this Drive.  # noqa: E501
        :type: str
        """

        self._drive_result = drive_result

    @property
    def is_home_offense(self):
        """Gets the is_home_offense of this Drive.  # noqa: E501


        :return: The is_home_offense of this Drive.  # noqa: E501
        :rtype: bool
        """
        return self._is_home_offense

    @is_home_offense.setter
    def is_home_offense(self, is_home_offense):
        """Sets the is_home_offense of this Drive.


        :param is_home_offense: The is_home_offense of this Drive.  # noqa: E501
        :type: bool
        """

        self._is_home_offense = is_home_offense

    @property
    def start_offense_score(self):
        """Gets the start_offense_score of this Drive.  # noqa: E501


        :return: The start_offense_score of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._start_offense_score

    @start_offense_score.setter
    def start_offense_score(self, start_offense_score):
        """Sets the start_offense_score of this Drive.


        :param start_offense_score: The start_offense_score of this Drive.  # noqa: E501
        :type: int
        """

        self._start_offense_score = start_offense_score

    @property
    def start_defense_score(self):
        """Gets the start_defense_score of this Drive.  # noqa: E501


        :return: The start_defense_score of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._start_defense_score

    @start_defense_score.setter
    def start_defense_score(self, start_defense_score):
        """Sets the start_defense_score of this Drive.


        :param start_defense_score: The start_defense_score of this Drive.  # noqa: E501
        :type: int
        """

        self._start_defense_score = start_defense_score

    @property
    def end_offense_score(self):
        """Gets the end_offense_score of this Drive.  # noqa: E501


        :return: The end_offense_score of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._end_offense_score

    @end_offense_score.setter
    def end_offense_score(self, end_offense_score):
        """Sets the end_offense_score of this Drive.


        :param end_offense_score: The end_offense_score of this Drive.  # noqa: E501
        :type: int
        """

        self._end_offense_score = end_offense_score

    @property
    def end_defense_score(self):
        """Gets the end_defense_score of this Drive.  # noqa: E501


        :return: The end_defense_score of this Drive.  # noqa: E501
        :rtype: int
        """
        return self._end_defense_score

    @end_defense_score.setter
    def end_defense_score(self, end_defense_score):
        """Sets the end_defense_score of this Drive.


        :param end_defense_score: The end_defense_score of this Drive.  # noqa: E501
        :type: int
        """

        self._end_defense_score = end_defense_score

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
        if issubclass(Drive, dict):
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
        if not isinstance(other, Drive):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Drive):
            return True

        return self.to_dict() != other.to_dict()
