# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.6.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class LivePlayByPlayPlays(object):
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
        'home_score': 'int',
        'away_score': 'int',
        'period': 'int',
        'clock': 'str',
        'wallclock': 'str',
        'team_id': 'int',
        'team': 'str',
        'down': 'int',
        'distance': 'int',
        'yards_to_goal': 'int',
        'yards_gained': 'int',
        'play_type_id': 'int',
        'play_type': 'str',
        'epa': 'float',
        'garbage_time': 'bool',
        'success': 'bool',
        'rush_pass': 'str',
        'down_type': 'str',
        'play_text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'home_score': 'homeScore',
        'away_score': 'awayScore',
        'period': 'period',
        'clock': 'clock',
        'wallclock': 'wallclock',
        'team_id': 'teamId',
        'team': 'team',
        'down': 'down',
        'distance': 'distance',
        'yards_to_goal': 'yardsToGoal',
        'yards_gained': 'yardsGained',
        'play_type_id': 'playTypeId',
        'play_type': 'playType',
        'epa': 'epa',
        'garbage_time': 'garbageTime',
        'success': 'success',
        'rush_pass': 'rushPass',
        'down_type': 'downType',
        'play_text': 'playText'
    }

    def __init__(self, id=None, home_score=None, away_score=None, period=None, clock=None, wallclock=None, team_id=None, team=None, down=None, distance=None, yards_to_goal=None, yards_gained=None, play_type_id=None, play_type=None, epa=None, garbage_time=None, success=None, rush_pass=None, down_type=None, play_text=None, _configuration=None):  # noqa: E501
        """LivePlayByPlayPlays - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._home_score = None
        self._away_score = None
        self._period = None
        self._clock = None
        self._wallclock = None
        self._team_id = None
        self._team = None
        self._down = None
        self._distance = None
        self._yards_to_goal = None
        self._yards_gained = None
        self._play_type_id = None
        self._play_type = None
        self._epa = None
        self._garbage_time = None
        self._success = None
        self._rush_pass = None
        self._down_type = None
        self._play_text = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if home_score is not None:
            self.home_score = home_score
        if away_score is not None:
            self.away_score = away_score
        if period is not None:
            self.period = period
        if clock is not None:
            self.clock = clock
        if wallclock is not None:
            self.wallclock = wallclock
        if team_id is not None:
            self.team_id = team_id
        if team is not None:
            self.team = team
        if down is not None:
            self.down = down
        if distance is not None:
            self.distance = distance
        if yards_to_goal is not None:
            self.yards_to_goal = yards_to_goal
        if yards_gained is not None:
            self.yards_gained = yards_gained
        if play_type_id is not None:
            self.play_type_id = play_type_id
        if play_type is not None:
            self.play_type = play_type
        if epa is not None:
            self.epa = epa
        if garbage_time is not None:
            self.garbage_time = garbage_time
        if success is not None:
            self.success = success
        if rush_pass is not None:
            self.rush_pass = rush_pass
        if down_type is not None:
            self.down_type = down_type
        if play_text is not None:
            self.play_text = play_text

    @property
    def id(self):
        """Gets the id of this LivePlayByPlayPlays.  # noqa: E501


        :return: The id of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LivePlayByPlayPlays.


        :param id: The id of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def home_score(self):
        """Gets the home_score of this LivePlayByPlayPlays.  # noqa: E501


        :return: The home_score of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._home_score

    @home_score.setter
    def home_score(self, home_score):
        """Sets the home_score of this LivePlayByPlayPlays.


        :param home_score: The home_score of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._home_score = home_score

    @property
    def away_score(self):
        """Gets the away_score of this LivePlayByPlayPlays.  # noqa: E501


        :return: The away_score of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._away_score

    @away_score.setter
    def away_score(self, away_score):
        """Sets the away_score of this LivePlayByPlayPlays.


        :param away_score: The away_score of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._away_score = away_score

    @property
    def period(self):
        """Gets the period of this LivePlayByPlayPlays.  # noqa: E501


        :return: The period of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this LivePlayByPlayPlays.


        :param period: The period of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def clock(self):
        """Gets the clock of this LivePlayByPlayPlays.  # noqa: E501


        :return: The clock of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: str
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """Sets the clock of this LivePlayByPlayPlays.


        :param clock: The clock of this LivePlayByPlayPlays.  # noqa: E501
        :type: str
        """

        self._clock = clock

    @property
    def wallclock(self):
        """Gets the wallclock of this LivePlayByPlayPlays.  # noqa: E501


        :return: The wallclock of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: str
        """
        return self._wallclock

    @wallclock.setter
    def wallclock(self, wallclock):
        """Sets the wallclock of this LivePlayByPlayPlays.


        :param wallclock: The wallclock of this LivePlayByPlayPlays.  # noqa: E501
        :type: str
        """

        self._wallclock = wallclock

    @property
    def team_id(self):
        """Gets the team_id of this LivePlayByPlayPlays.  # noqa: E501


        :return: The team_id of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this LivePlayByPlayPlays.


        :param team_id: The team_id of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def team(self):
        """Gets the team of this LivePlayByPlayPlays.  # noqa: E501


        :return: The team of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this LivePlayByPlayPlays.


        :param team: The team of this LivePlayByPlayPlays.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def down(self):
        """Gets the down of this LivePlayByPlayPlays.  # noqa: E501


        :return: The down of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._down

    @down.setter
    def down(self, down):
        """Sets the down of this LivePlayByPlayPlays.


        :param down: The down of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._down = down

    @property
    def distance(self):
        """Gets the distance of this LivePlayByPlayPlays.  # noqa: E501


        :return: The distance of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this LivePlayByPlayPlays.


        :param distance: The distance of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._distance = distance

    @property
    def yards_to_goal(self):
        """Gets the yards_to_goal of this LivePlayByPlayPlays.  # noqa: E501


        :return: The yards_to_goal of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._yards_to_goal

    @yards_to_goal.setter
    def yards_to_goal(self, yards_to_goal):
        """Sets the yards_to_goal of this LivePlayByPlayPlays.


        :param yards_to_goal: The yards_to_goal of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._yards_to_goal = yards_to_goal

    @property
    def yards_gained(self):
        """Gets the yards_gained of this LivePlayByPlayPlays.  # noqa: E501


        :return: The yards_gained of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._yards_gained

    @yards_gained.setter
    def yards_gained(self, yards_gained):
        """Sets the yards_gained of this LivePlayByPlayPlays.


        :param yards_gained: The yards_gained of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._yards_gained = yards_gained

    @property
    def play_type_id(self):
        """Gets the play_type_id of this LivePlayByPlayPlays.  # noqa: E501


        :return: The play_type_id of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: int
        """
        return self._play_type_id

    @play_type_id.setter
    def play_type_id(self, play_type_id):
        """Sets the play_type_id of this LivePlayByPlayPlays.


        :param play_type_id: The play_type_id of this LivePlayByPlayPlays.  # noqa: E501
        :type: int
        """

        self._play_type_id = play_type_id

    @property
    def play_type(self):
        """Gets the play_type of this LivePlayByPlayPlays.  # noqa: E501


        :return: The play_type of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: str
        """
        return self._play_type

    @play_type.setter
    def play_type(self, play_type):
        """Sets the play_type of this LivePlayByPlayPlays.


        :param play_type: The play_type of this LivePlayByPlayPlays.  # noqa: E501
        :type: str
        """

        self._play_type = play_type

    @property
    def epa(self):
        """Gets the epa of this LivePlayByPlayPlays.  # noqa: E501


        :return: The epa of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: float
        """
        return self._epa

    @epa.setter
    def epa(self, epa):
        """Sets the epa of this LivePlayByPlayPlays.


        :param epa: The epa of this LivePlayByPlayPlays.  # noqa: E501
        :type: float
        """

        self._epa = epa

    @property
    def garbage_time(self):
        """Gets the garbage_time of this LivePlayByPlayPlays.  # noqa: E501


        :return: The garbage_time of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: bool
        """
        return self._garbage_time

    @garbage_time.setter
    def garbage_time(self, garbage_time):
        """Sets the garbage_time of this LivePlayByPlayPlays.


        :param garbage_time: The garbage_time of this LivePlayByPlayPlays.  # noqa: E501
        :type: bool
        """

        self._garbage_time = garbage_time

    @property
    def success(self):
        """Gets the success of this LivePlayByPlayPlays.  # noqa: E501


        :return: The success of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this LivePlayByPlayPlays.


        :param success: The success of this LivePlayByPlayPlays.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def rush_pass(self):
        """Gets the rush_pass of this LivePlayByPlayPlays.  # noqa: E501


        :return: The rush_pass of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: str
        """
        return self._rush_pass

    @rush_pass.setter
    def rush_pass(self, rush_pass):
        """Sets the rush_pass of this LivePlayByPlayPlays.


        :param rush_pass: The rush_pass of this LivePlayByPlayPlays.  # noqa: E501
        :type: str
        """

        self._rush_pass = rush_pass

    @property
    def down_type(self):
        """Gets the down_type of this LivePlayByPlayPlays.  # noqa: E501


        :return: The down_type of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: str
        """
        return self._down_type

    @down_type.setter
    def down_type(self, down_type):
        """Sets the down_type of this LivePlayByPlayPlays.


        :param down_type: The down_type of this LivePlayByPlayPlays.  # noqa: E501
        :type: str
        """

        self._down_type = down_type

    @property
    def play_text(self):
        """Gets the play_text of this LivePlayByPlayPlays.  # noqa: E501


        :return: The play_text of this LivePlayByPlayPlays.  # noqa: E501
        :rtype: str
        """
        return self._play_text

    @play_text.setter
    def play_text(self, play_text):
        """Sets the play_text of this LivePlayByPlayPlays.


        :param play_text: The play_text of this LivePlayByPlayPlays.  # noqa: E501
        :type: str
        """

        self._play_text = play_text

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
        if issubclass(LivePlayByPlayPlays, dict):
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
        if not isinstance(other, LivePlayByPlayPlays):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LivePlayByPlayPlays):
            return True

        return self.to_dict() != other.to_dict()
