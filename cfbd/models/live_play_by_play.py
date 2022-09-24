# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.8
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class LivePlayByPlay(object):
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
        'status': 'str',
        'period': 'int',
        'clock': 'str',
        'possession': 'str',
        'down': 'int',
        'distance': 'int',
        'yards_to_goal': 'int',
        'teams': 'list[LivePlayByPlayTeams]',
        'drives': 'list[LivePlayByPlayDrives]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'period': 'period',
        'clock': 'clock',
        'possession': 'possession',
        'down': 'down',
        'distance': 'distance',
        'yards_to_goal': 'yardsToGoal',
        'teams': 'teams',
        'drives': 'drives'
    }

    def __init__(self, id=None, status=None, period=None, clock=None, possession=None, down=None, distance=None, yards_to_goal=None, teams=None, drives=None, _configuration=None):  # noqa: E501
        """LivePlayByPlay - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._status = None
        self._period = None
        self._clock = None
        self._possession = None
        self._down = None
        self._distance = None
        self._yards_to_goal = None
        self._teams = None
        self._drives = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if period is not None:
            self.period = period
        if clock is not None:
            self.clock = clock
        if possession is not None:
            self.possession = possession
        if down is not None:
            self.down = down
        if distance is not None:
            self.distance = distance
        if yards_to_goal is not None:
            self.yards_to_goal = yards_to_goal
        if teams is not None:
            self.teams = teams
        if drives is not None:
            self.drives = drives

    @property
    def id(self):
        """Gets the id of this LivePlayByPlay.  # noqa: E501


        :return: The id of this LivePlayByPlay.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LivePlayByPlay.


        :param id: The id of this LivePlayByPlay.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this LivePlayByPlay.  # noqa: E501


        :return: The status of this LivePlayByPlay.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LivePlayByPlay.


        :param status: The status of this LivePlayByPlay.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def period(self):
        """Gets the period of this LivePlayByPlay.  # noqa: E501


        :return: The period of this LivePlayByPlay.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this LivePlayByPlay.


        :param period: The period of this LivePlayByPlay.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def clock(self):
        """Gets the clock of this LivePlayByPlay.  # noqa: E501


        :return: The clock of this LivePlayByPlay.  # noqa: E501
        :rtype: str
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """Sets the clock of this LivePlayByPlay.


        :param clock: The clock of this LivePlayByPlay.  # noqa: E501
        :type: str
        """

        self._clock = clock

    @property
    def possession(self):
        """Gets the possession of this LivePlayByPlay.  # noqa: E501


        :return: The possession of this LivePlayByPlay.  # noqa: E501
        :rtype: str
        """
        return self._possession

    @possession.setter
    def possession(self, possession):
        """Sets the possession of this LivePlayByPlay.


        :param possession: The possession of this LivePlayByPlay.  # noqa: E501
        :type: str
        """

        self._possession = possession

    @property
    def down(self):
        """Gets the down of this LivePlayByPlay.  # noqa: E501


        :return: The down of this LivePlayByPlay.  # noqa: E501
        :rtype: int
        """
        return self._down

    @down.setter
    def down(self, down):
        """Sets the down of this LivePlayByPlay.


        :param down: The down of this LivePlayByPlay.  # noqa: E501
        :type: int
        """

        self._down = down

    @property
    def distance(self):
        """Gets the distance of this LivePlayByPlay.  # noqa: E501


        :return: The distance of this LivePlayByPlay.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this LivePlayByPlay.


        :param distance: The distance of this LivePlayByPlay.  # noqa: E501
        :type: int
        """

        self._distance = distance

    @property
    def yards_to_goal(self):
        """Gets the yards_to_goal of this LivePlayByPlay.  # noqa: E501


        :return: The yards_to_goal of this LivePlayByPlay.  # noqa: E501
        :rtype: int
        """
        return self._yards_to_goal

    @yards_to_goal.setter
    def yards_to_goal(self, yards_to_goal):
        """Sets the yards_to_goal of this LivePlayByPlay.


        :param yards_to_goal: The yards_to_goal of this LivePlayByPlay.  # noqa: E501
        :type: int
        """

        self._yards_to_goal = yards_to_goal

    @property
    def teams(self):
        """Gets the teams of this LivePlayByPlay.  # noqa: E501


        :return: The teams of this LivePlayByPlay.  # noqa: E501
        :rtype: list[LivePlayByPlayTeams]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this LivePlayByPlay.


        :param teams: The teams of this LivePlayByPlay.  # noqa: E501
        :type: list[LivePlayByPlayTeams]
        """

        self._teams = teams

    @property
    def drives(self):
        """Gets the drives of this LivePlayByPlay.  # noqa: E501


        :return: The drives of this LivePlayByPlay.  # noqa: E501
        :rtype: list[LivePlayByPlayDrives]
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        """Sets the drives of this LivePlayByPlay.


        :param drives: The drives of this LivePlayByPlay.  # noqa: E501
        :type: list[LivePlayByPlayDrives]
        """

        self._drives = drives

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
        if issubclass(LivePlayByPlay, dict):
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
        if not isinstance(other, LivePlayByPlay):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LivePlayByPlay):
            return True

        return self.to_dict() != other.to_dict()
