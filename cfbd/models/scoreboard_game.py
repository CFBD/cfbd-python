# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.11
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class ScoreboardGame(object):
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
        'start_date': 'str',
        'tv': 'str',
        'neutral_site': 'bool',
        'conference_game': 'bool',
        'status': 'str',
        'period': 'int',
        'clock': 'str',
        'venue': 'object',
        'home_team': 'object',
        'away_team': 'object',
        'weather': 'object',
        'betting': 'object'
    }

    attribute_map = {
        'id': 'id',
        'start_date': 'startDate',
        'tv': 'tv',
        'neutral_site': 'neutralSite',
        'conference_game': 'conferenceGame',
        'status': 'status',
        'period': 'period',
        'clock': 'clock',
        'venue': 'venue',
        'home_team': 'homeTeam',
        'away_team': 'awayTeam',
        'weather': 'weather',
        'betting': 'betting'
    }

    def __init__(self, id=None, start_date=None, tv=None, neutral_site=None, conference_game=None, status=None, period=None, clock=None, venue=None, home_team=None, away_team=None, weather=None, betting=None, _configuration=None):  # noqa: E501
        """ScoreboardGame - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._start_date = None
        self._tv = None
        self._neutral_site = None
        self._conference_game = None
        self._status = None
        self._period = None
        self._clock = None
        self._venue = None
        self._home_team = None
        self._away_team = None
        self._weather = None
        self._betting = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if start_date is not None:
            self.start_date = start_date
        if tv is not None:
            self.tv = tv
        if neutral_site is not None:
            self.neutral_site = neutral_site
        if conference_game is not None:
            self.conference_game = conference_game
        if status is not None:
            self.status = status
        if period is not None:
            self.period = period
        if clock is not None:
            self.clock = clock
        if venue is not None:
            self.venue = venue
        if home_team is not None:
            self.home_team = home_team
        if away_team is not None:
            self.away_team = away_team
        if weather is not None:
            self.weather = weather
        if betting is not None:
            self.betting = betting

    @property
    def id(self):
        """Gets the id of this ScoreboardGame.  # noqa: E501


        :return: The id of this ScoreboardGame.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScoreboardGame.


        :param id: The id of this ScoreboardGame.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def start_date(self):
        """Gets the start_date of this ScoreboardGame.  # noqa: E501


        :return: The start_date of this ScoreboardGame.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ScoreboardGame.


        :param start_date: The start_date of this ScoreboardGame.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def tv(self):
        """Gets the tv of this ScoreboardGame.  # noqa: E501


        :return: The tv of this ScoreboardGame.  # noqa: E501
        :rtype: str
        """
        return self._tv

    @tv.setter
    def tv(self, tv):
        """Sets the tv of this ScoreboardGame.


        :param tv: The tv of this ScoreboardGame.  # noqa: E501
        :type: str
        """

        self._tv = tv

    @property
    def neutral_site(self):
        """Gets the neutral_site of this ScoreboardGame.  # noqa: E501


        :return: The neutral_site of this ScoreboardGame.  # noqa: E501
        :rtype: bool
        """
        return self._neutral_site

    @neutral_site.setter
    def neutral_site(self, neutral_site):
        """Sets the neutral_site of this ScoreboardGame.


        :param neutral_site: The neutral_site of this ScoreboardGame.  # noqa: E501
        :type: bool
        """

        self._neutral_site = neutral_site

    @property
    def conference_game(self):
        """Gets the conference_game of this ScoreboardGame.  # noqa: E501


        :return: The conference_game of this ScoreboardGame.  # noqa: E501
        :rtype: bool
        """
        return self._conference_game

    @conference_game.setter
    def conference_game(self, conference_game):
        """Sets the conference_game of this ScoreboardGame.


        :param conference_game: The conference_game of this ScoreboardGame.  # noqa: E501
        :type: bool
        """

        self._conference_game = conference_game

    @property
    def status(self):
        """Gets the status of this ScoreboardGame.  # noqa: E501


        :return: The status of this ScoreboardGame.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScoreboardGame.


        :param status: The status of this ScoreboardGame.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def period(self):
        """Gets the period of this ScoreboardGame.  # noqa: E501


        :return: The period of this ScoreboardGame.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ScoreboardGame.


        :param period: The period of this ScoreboardGame.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def clock(self):
        """Gets the clock of this ScoreboardGame.  # noqa: E501


        :return: The clock of this ScoreboardGame.  # noqa: E501
        :rtype: str
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """Sets the clock of this ScoreboardGame.


        :param clock: The clock of this ScoreboardGame.  # noqa: E501
        :type: str
        """

        self._clock = clock

    @property
    def venue(self):
        """Gets the venue of this ScoreboardGame.  # noqa: E501


        :return: The venue of this ScoreboardGame.  # noqa: E501
        :rtype: object
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this ScoreboardGame.


        :param venue: The venue of this ScoreboardGame.  # noqa: E501
        :type: object
        """

        self._venue = venue

    @property
    def home_team(self):
        """Gets the home_team of this ScoreboardGame.  # noqa: E501


        :return: The home_team of this ScoreboardGame.  # noqa: E501
        :rtype: object
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this ScoreboardGame.


        :param home_team: The home_team of this ScoreboardGame.  # noqa: E501
        :type: object
        """

        self._home_team = home_team

    @property
    def away_team(self):
        """Gets the away_team of this ScoreboardGame.  # noqa: E501


        :return: The away_team of this ScoreboardGame.  # noqa: E501
        :rtype: object
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this ScoreboardGame.


        :param away_team: The away_team of this ScoreboardGame.  # noqa: E501
        :type: object
        """

        self._away_team = away_team

    @property
    def weather(self):
        """Gets the weather of this ScoreboardGame.  # noqa: E501


        :return: The weather of this ScoreboardGame.  # noqa: E501
        :rtype: object
        """
        return self._weather

    @weather.setter
    def weather(self, weather):
        """Sets the weather of this ScoreboardGame.


        :param weather: The weather of this ScoreboardGame.  # noqa: E501
        :type: object
        """

        self._weather = weather

    @property
    def betting(self):
        """Gets the betting of this ScoreboardGame.  # noqa: E501


        :return: The betting of this ScoreboardGame.  # noqa: E501
        :rtype: object
        """
        return self._betting

    @betting.setter
    def betting(self, betting):
        """Sets the betting of this ScoreboardGame.


        :param betting: The betting of this ScoreboardGame.  # noqa: E501
        :type: object
        """

        self._betting = betting

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
        if issubclass(ScoreboardGame, dict):
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
        if not isinstance(other, ScoreboardGame):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScoreboardGame):
            return True

        return self.to_dict() != other.to_dict()