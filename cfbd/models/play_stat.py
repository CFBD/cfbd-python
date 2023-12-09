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


class PlayStat(object):
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
        'game_id': 'int',
        'season': 'int',
        'week': 'int',
        'team': 'str',
        'conference': 'str',
        'opponent': 'str',
        'team_score': 'int',
        'opponent_score': 'int',
        'drive_id': 'int',
        'play_id': 'int',
        'period': 'int',
        'clock': 'DriveStartTime',
        'yards_to_goal': 'int',
        'down': 'int',
        'distance': 'int',
        'athlete_id': 'int',
        'athlete_name': 'str',
        'stat_type': 'str',
        'stat': 'int'
    }

    attribute_map = {
        'game_id': 'gameId',
        'season': 'season',
        'week': 'week',
        'team': 'team',
        'conference': 'conference',
        'opponent': 'opponent',
        'team_score': 'teamScore',
        'opponent_score': 'opponentScore',
        'drive_id': 'driveId',
        'play_id': 'playId',
        'period': 'period',
        'clock': 'clock',
        'yards_to_goal': 'yardsToGoal',
        'down': 'down',
        'distance': 'distance',
        'athlete_id': 'athleteId',
        'athlete_name': 'athleteName',
        'stat_type': 'statType',
        'stat': 'stat'
    }

    def __init__(self, game_id=None, season=None, week=None, team=None, conference=None, opponent=None, team_score=None, opponent_score=None, drive_id=None, play_id=None, period=None, clock=None, yards_to_goal=None, down=None, distance=None, athlete_id=None, athlete_name=None, stat_type=None, stat=None, _configuration=None):  # noqa: E501
        """PlayStat - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._game_id = None
        self._season = None
        self._week = None
        self._team = None
        self._conference = None
        self._opponent = None
        self._team_score = None
        self._opponent_score = None
        self._drive_id = None
        self._play_id = None
        self._period = None
        self._clock = None
        self._yards_to_goal = None
        self._down = None
        self._distance = None
        self._athlete_id = None
        self._athlete_name = None
        self._stat_type = None
        self._stat = None
        self.discriminator = None

        if game_id is not None:
            self.game_id = game_id
        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if team is not None:
            self.team = team
        if conference is not None:
            self.conference = conference
        if opponent is not None:
            self.opponent = opponent
        if team_score is not None:
            self.team_score = team_score
        if opponent_score is not None:
            self.opponent_score = opponent_score
        if drive_id is not None:
            self.drive_id = drive_id
        if play_id is not None:
            self.play_id = play_id
        if period is not None:
            self.period = period
        if clock is not None:
            self.clock = clock
        if yards_to_goal is not None:
            self.yards_to_goal = yards_to_goal
        if down is not None:
            self.down = down
        if distance is not None:
            self.distance = distance
        if athlete_id is not None:
            self.athlete_id = athlete_id
        if athlete_name is not None:
            self.athlete_name = athlete_name
        if stat_type is not None:
            self.stat_type = stat_type
        if stat is not None:
            self.stat = stat

    @property
    def game_id(self):
        """Gets the game_id of this PlayStat.  # noqa: E501


        :return: The game_id of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this PlayStat.


        :param game_id: The game_id of this PlayStat.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def season(self):
        """Gets the season of this PlayStat.  # noqa: E501


        :return: The season of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this PlayStat.


        :param season: The season of this PlayStat.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this PlayStat.  # noqa: E501


        :return: The week of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this PlayStat.


        :param week: The week of this PlayStat.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def team(self):
        """Gets the team of this PlayStat.  # noqa: E501


        :return: The team of this PlayStat.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayStat.


        :param team: The team of this PlayStat.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def conference(self):
        """Gets the conference of this PlayStat.  # noqa: E501


        :return: The conference of this PlayStat.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this PlayStat.


        :param conference: The conference of this PlayStat.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def opponent(self):
        """Gets the opponent of this PlayStat.  # noqa: E501


        :return: The opponent of this PlayStat.  # noqa: E501
        :rtype: str
        """
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        """Sets the opponent of this PlayStat.


        :param opponent: The opponent of this PlayStat.  # noqa: E501
        :type: str
        """

        self._opponent = opponent

    @property
    def team_score(self):
        """Gets the team_score of this PlayStat.  # noqa: E501


        :return: The team_score of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._team_score

    @team_score.setter
    def team_score(self, team_score):
        """Sets the team_score of this PlayStat.


        :param team_score: The team_score of this PlayStat.  # noqa: E501
        :type: int
        """

        self._team_score = team_score

    @property
    def opponent_score(self):
        """Gets the opponent_score of this PlayStat.  # noqa: E501


        :return: The opponent_score of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._opponent_score

    @opponent_score.setter
    def opponent_score(self, opponent_score):
        """Sets the opponent_score of this PlayStat.


        :param opponent_score: The opponent_score of this PlayStat.  # noqa: E501
        :type: int
        """

        self._opponent_score = opponent_score

    @property
    def drive_id(self):
        """Gets the drive_id of this PlayStat.  # noqa: E501


        :return: The drive_id of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._drive_id

    @drive_id.setter
    def drive_id(self, drive_id):
        """Sets the drive_id of this PlayStat.


        :param drive_id: The drive_id of this PlayStat.  # noqa: E501
        :type: int
        """

        self._drive_id = drive_id

    @property
    def play_id(self):
        """Gets the play_id of this PlayStat.  # noqa: E501


        :return: The play_id of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._play_id

    @play_id.setter
    def play_id(self, play_id):
        """Sets the play_id of this PlayStat.


        :param play_id: The play_id of this PlayStat.  # noqa: E501
        :type: int
        """

        self._play_id = play_id

    @property
    def period(self):
        """Gets the period of this PlayStat.  # noqa: E501


        :return: The period of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PlayStat.


        :param period: The period of this PlayStat.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def clock(self):
        """Gets the clock of this PlayStat.  # noqa: E501


        :return: The clock of this PlayStat.  # noqa: E501
        :rtype: DriveStartTime
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """Sets the clock of this PlayStat.


        :param clock: The clock of this PlayStat.  # noqa: E501
        :type: DriveStartTime
        """

        self._clock = clock

    @property
    def yards_to_goal(self):
        """Gets the yards_to_goal of this PlayStat.  # noqa: E501


        :return: The yards_to_goal of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._yards_to_goal

    @yards_to_goal.setter
    def yards_to_goal(self, yards_to_goal):
        """Sets the yards_to_goal of this PlayStat.


        :param yards_to_goal: The yards_to_goal of this PlayStat.  # noqa: E501
        :type: int
        """

        self._yards_to_goal = yards_to_goal

    @property
    def down(self):
        """Gets the down of this PlayStat.  # noqa: E501


        :return: The down of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._down

    @down.setter
    def down(self, down):
        """Sets the down of this PlayStat.


        :param down: The down of this PlayStat.  # noqa: E501
        :type: int
        """

        self._down = down

    @property
    def distance(self):
        """Gets the distance of this PlayStat.  # noqa: E501


        :return: The distance of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this PlayStat.


        :param distance: The distance of this PlayStat.  # noqa: E501
        :type: int
        """

        self._distance = distance

    @property
    def athlete_id(self):
        """Gets the athlete_id of this PlayStat.  # noqa: E501


        :return: The athlete_id of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._athlete_id

    @athlete_id.setter
    def athlete_id(self, athlete_id):
        """Sets the athlete_id of this PlayStat.


        :param athlete_id: The athlete_id of this PlayStat.  # noqa: E501
        :type: int
        """

        self._athlete_id = athlete_id

    @property
    def athlete_name(self):
        """Gets the athlete_name of this PlayStat.  # noqa: E501


        :return: The athlete_name of this PlayStat.  # noqa: E501
        :rtype: str
        """
        return self._athlete_name

    @athlete_name.setter
    def athlete_name(self, athlete_name):
        """Sets the athlete_name of this PlayStat.


        :param athlete_name: The athlete_name of this PlayStat.  # noqa: E501
        :type: str
        """

        self._athlete_name = athlete_name

    @property
    def stat_type(self):
        """Gets the stat_type of this PlayStat.  # noqa: E501


        :return: The stat_type of this PlayStat.  # noqa: E501
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this PlayStat.


        :param stat_type: The stat_type of this PlayStat.  # noqa: E501
        :type: str
        """

        self._stat_type = stat_type

    @property
    def stat(self):
        """Gets the stat of this PlayStat.  # noqa: E501


        :return: The stat of this PlayStat.  # noqa: E501
        :rtype: int
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this PlayStat.


        :param stat: The stat of this PlayStat.  # noqa: E501
        :type: int
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
        if issubclass(PlayStat, dict):
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
        if not isinstance(other, PlayStat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayStat):
            return True

        return self.to_dict() != other.to_dict()
