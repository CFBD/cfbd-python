# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TeamMatchupGames(object):
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
        'season': 'int',
        'week': 'int',
        'season_type': 'str',
        '_date': 'str',
        'neutral_site': 'bool',
        'venue': 'str',
        'home_team': 'str',
        'home_score': 'int',
        'away_team': 'str',
        'away_score': 'int',
        'winner': 'str'
    }

    attribute_map = {
        'season': 'season',
        'week': 'week',
        'season_type': 'season_type',
        '_date': 'date',
        'neutral_site': 'neutralSite',
        'venue': 'venue',
        'home_team': 'homeTeam',
        'home_score': 'homeScore',
        'away_team': 'awayTeam',
        'away_score': 'awayScore',
        'winner': 'winner'
    }

    def __init__(self, season=None, week=None, season_type=None, _date=None, neutral_site=None, venue=None, home_team=None, home_score=None, away_team=None, away_score=None, winner=None):  # noqa: E501
        """TeamMatchupGames - a model defined in Swagger"""  # noqa: E501

        self._season = None
        self._week = None
        self._season_type = None
        self.__date = None
        self._neutral_site = None
        self._venue = None
        self._home_team = None
        self._home_score = None
        self._away_team = None
        self._away_score = None
        self._winner = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if season_type is not None:
            self.season_type = season_type
        if _date is not None:
            self._date = _date
        if neutral_site is not None:
            self.neutral_site = neutral_site
        if venue is not None:
            self.venue = venue
        if home_team is not None:
            self.home_team = home_team
        if home_score is not None:
            self.home_score = home_score
        if away_team is not None:
            self.away_team = away_team
        if away_score is not None:
            self.away_score = away_score
        if winner is not None:
            self.winner = winner

    @property
    def season(self):
        """Gets the season of this TeamMatchupGames.  # noqa: E501


        :return: The season of this TeamMatchupGames.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this TeamMatchupGames.


        :param season: The season of this TeamMatchupGames.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this TeamMatchupGames.  # noqa: E501


        :return: The week of this TeamMatchupGames.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this TeamMatchupGames.


        :param week: The week of this TeamMatchupGames.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def season_type(self):
        """Gets the season_type of this TeamMatchupGames.  # noqa: E501


        :return: The season_type of this TeamMatchupGames.  # noqa: E501
        :rtype: str
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this TeamMatchupGames.


        :param season_type: The season_type of this TeamMatchupGames.  # noqa: E501
        :type: str
        """

        self._season_type = season_type

    @property
    def _date(self):
        """Gets the _date of this TeamMatchupGames.  # noqa: E501


        :return: The _date of this TeamMatchupGames.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this TeamMatchupGames.


        :param _date: The _date of this TeamMatchupGames.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def neutral_site(self):
        """Gets the neutral_site of this TeamMatchupGames.  # noqa: E501


        :return: The neutral_site of this TeamMatchupGames.  # noqa: E501
        :rtype: bool
        """
        return self._neutral_site

    @neutral_site.setter
    def neutral_site(self, neutral_site):
        """Sets the neutral_site of this TeamMatchupGames.


        :param neutral_site: The neutral_site of this TeamMatchupGames.  # noqa: E501
        :type: bool
        """

        self._neutral_site = neutral_site

    @property
    def venue(self):
        """Gets the venue of this TeamMatchupGames.  # noqa: E501


        :return: The venue of this TeamMatchupGames.  # noqa: E501
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this TeamMatchupGames.


        :param venue: The venue of this TeamMatchupGames.  # noqa: E501
        :type: str
        """

        self._venue = venue

    @property
    def home_team(self):
        """Gets the home_team of this TeamMatchupGames.  # noqa: E501


        :return: The home_team of this TeamMatchupGames.  # noqa: E501
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this TeamMatchupGames.


        :param home_team: The home_team of this TeamMatchupGames.  # noqa: E501
        :type: str
        """

        self._home_team = home_team

    @property
    def home_score(self):
        """Gets the home_score of this TeamMatchupGames.  # noqa: E501


        :return: The home_score of this TeamMatchupGames.  # noqa: E501
        :rtype: int
        """
        return self._home_score

    @home_score.setter
    def home_score(self, home_score):
        """Sets the home_score of this TeamMatchupGames.


        :param home_score: The home_score of this TeamMatchupGames.  # noqa: E501
        :type: int
        """

        self._home_score = home_score

    @property
    def away_team(self):
        """Gets the away_team of this TeamMatchupGames.  # noqa: E501


        :return: The away_team of this TeamMatchupGames.  # noqa: E501
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this TeamMatchupGames.


        :param away_team: The away_team of this TeamMatchupGames.  # noqa: E501
        :type: str
        """

        self._away_team = away_team

    @property
    def away_score(self):
        """Gets the away_score of this TeamMatchupGames.  # noqa: E501


        :return: The away_score of this TeamMatchupGames.  # noqa: E501
        :rtype: int
        """
        return self._away_score

    @away_score.setter
    def away_score(self, away_score):
        """Sets the away_score of this TeamMatchupGames.


        :param away_score: The away_score of this TeamMatchupGames.  # noqa: E501
        :type: int
        """

        self._away_score = away_score

    @property
    def winner(self):
        """Gets the winner of this TeamMatchupGames.  # noqa: E501


        :return: The winner of this TeamMatchupGames.  # noqa: E501
        :rtype: str
        """
        return self._winner

    @winner.setter
    def winner(self, winner):
        """Sets the winner of this TeamMatchupGames.


        :param winner: The winner of this TeamMatchupGames.  # noqa: E501
        :type: str
        """

        self._winner = winner

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
        if issubclass(TeamMatchupGames, dict):
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
        if not isinstance(other, TeamMatchupGames):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other