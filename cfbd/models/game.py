# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.2.3
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class Game(object):
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
        'season': 'int',
        'week': 'int',
        'season_type': 'str',
        'start_date': 'str',
        'start_time_tbd': 'bool',
        'neutral_site': 'bool',
        'conference_game': 'bool',
        'attendance': 'int',
        'venue_id': 'int',
        'venue': 'str',
        'home_id': 'int',
        'home_team': 'str',
        'home_conference': 'str',
        'home_points': 'int',
        'home_line_scores': 'list[int]',
        'home_post_win_prob': 'float',
        'home_pregame_elo': 'int',
        'home_postgame_elo': 'int',
        'away_id': 'int',
        'away_team': 'str',
        'away_conference': 'str',
        'away_points': 'int',
        'away_line_scores': 'list[int]',
        'away_post_win_prob': 'float',
        'away_pregame_elo': 'int',
        'away_postgame_elo': 'int',
        'excitement_index': 'float',
        'highlights': 'str',
        'notes': 'str'
    }

    attribute_map = {
        'id': 'id',
        'season': 'season',
        'week': 'week',
        'season_type': 'season_type',
        'start_date': 'start_date',
        'start_time_tbd': 'start_time_tbd',
        'neutral_site': 'neutral_site',
        'conference_game': 'conference_game',
        'attendance': 'attendance',
        'venue_id': 'venue_id',
        'venue': 'venue',
        'home_id': 'home_id',
        'home_team': 'home_team',
        'home_conference': 'home_conference',
        'home_points': 'home_points',
        'home_line_scores': 'home_line_scores',
        'home_post_win_prob': 'home_post_win_prob',
        'home_pregame_elo': 'home_pregame_elo',
        'home_postgame_elo': 'home_postgame_elo',
        'away_id': 'away_id',
        'away_team': 'away_team',
        'away_conference': 'away_conference',
        'away_points': 'away_points',
        'away_line_scores': 'away_line_scores',
        'away_post_win_prob': 'away_post_win_prob',
        'away_pregame_elo': 'away_pregame_elo',
        'away_postgame_elo': 'away_postgame_elo',
        'excitement_index': 'excitement_index',
        'highlights': 'highlights',
        'notes': 'notes'
    }

    def __init__(self, id=None, season=None, week=None, season_type=None, start_date=None, start_time_tbd=None, neutral_site=None, conference_game=None, attendance=None, venue_id=None, venue=None, home_id=None, home_team=None, home_conference=None, home_points=None, home_line_scores=None, home_post_win_prob=None, home_pregame_elo=None, home_postgame_elo=None, away_id=None, away_team=None, away_conference=None, away_points=None, away_line_scores=None, away_post_win_prob=None, away_pregame_elo=None, away_postgame_elo=None, excitement_index=None, highlights=None, notes=None, _configuration=None):  # noqa: E501
        """Game - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._season = None
        self._week = None
        self._season_type = None
        self._start_date = None
        self._start_time_tbd = None
        self._neutral_site = None
        self._conference_game = None
        self._attendance = None
        self._venue_id = None
        self._venue = None
        self._home_id = None
        self._home_team = None
        self._home_conference = None
        self._home_points = None
        self._home_line_scores = None
        self._home_post_win_prob = None
        self._home_pregame_elo = None
        self._home_postgame_elo = None
        self._away_id = None
        self._away_team = None
        self._away_conference = None
        self._away_points = None
        self._away_line_scores = None
        self._away_post_win_prob = None
        self._away_pregame_elo = None
        self._away_postgame_elo = None
        self._excitement_index = None
        self._highlights = None
        self._notes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if season_type is not None:
            self.season_type = season_type
        if start_date is not None:
            self.start_date = start_date
        if start_time_tbd is not None:
            self.start_time_tbd = start_time_tbd
        if neutral_site is not None:
            self.neutral_site = neutral_site
        if conference_game is not None:
            self.conference_game = conference_game
        if attendance is not None:
            self.attendance = attendance
        if venue_id is not None:
            self.venue_id = venue_id
        if venue is not None:
            self.venue = venue
        if home_id is not None:
            self.home_id = home_id
        if home_team is not None:
            self.home_team = home_team
        if home_conference is not None:
            self.home_conference = home_conference
        if home_points is not None:
            self.home_points = home_points
        if home_line_scores is not None:
            self.home_line_scores = home_line_scores
        if home_post_win_prob is not None:
            self.home_post_win_prob = home_post_win_prob
        if home_pregame_elo is not None:
            self.home_pregame_elo = home_pregame_elo
        if home_postgame_elo is not None:
            self.home_postgame_elo = home_postgame_elo
        if away_id is not None:
            self.away_id = away_id
        if away_team is not None:
            self.away_team = away_team
        if away_conference is not None:
            self.away_conference = away_conference
        if away_points is not None:
            self.away_points = away_points
        if away_line_scores is not None:
            self.away_line_scores = away_line_scores
        if away_post_win_prob is not None:
            self.away_post_win_prob = away_post_win_prob
        if away_pregame_elo is not None:
            self.away_pregame_elo = away_pregame_elo
        if away_postgame_elo is not None:
            self.away_postgame_elo = away_postgame_elo
        if excitement_index is not None:
            self.excitement_index = excitement_index
        if highlights is not None:
            self.highlights = highlights
        if notes is not None:
            self.notes = notes

    @property
    def id(self):
        """Gets the id of this Game.  # noqa: E501


        :return: The id of this Game.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Game.


        :param id: The id of this Game.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def season(self):
        """Gets the season of this Game.  # noqa: E501


        :return: The season of this Game.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Game.


        :param season: The season of this Game.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this Game.  # noqa: E501


        :return: The week of this Game.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this Game.


        :param week: The week of this Game.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def season_type(self):
        """Gets the season_type of this Game.  # noqa: E501


        :return: The season_type of this Game.  # noqa: E501
        :rtype: str
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this Game.


        :param season_type: The season_type of this Game.  # noqa: E501
        :type: str
        """

        self._season_type = season_type

    @property
    def start_date(self):
        """Gets the start_date of this Game.  # noqa: E501


        :return: The start_date of this Game.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Game.


        :param start_date: The start_date of this Game.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def start_time_tbd(self):
        """Gets the start_time_tbd of this Game.  # noqa: E501


        :return: The start_time_tbd of this Game.  # noqa: E501
        :rtype: bool
        """
        return self._start_time_tbd

    @start_time_tbd.setter
    def start_time_tbd(self, start_time_tbd):
        """Sets the start_time_tbd of this Game.


        :param start_time_tbd: The start_time_tbd of this Game.  # noqa: E501
        :type: bool
        """

        self._start_time_tbd = start_time_tbd

    @property
    def neutral_site(self):
        """Gets the neutral_site of this Game.  # noqa: E501


        :return: The neutral_site of this Game.  # noqa: E501
        :rtype: bool
        """
        return self._neutral_site

    @neutral_site.setter
    def neutral_site(self, neutral_site):
        """Sets the neutral_site of this Game.


        :param neutral_site: The neutral_site of this Game.  # noqa: E501
        :type: bool
        """

        self._neutral_site = neutral_site

    @property
    def conference_game(self):
        """Gets the conference_game of this Game.  # noqa: E501


        :return: The conference_game of this Game.  # noqa: E501
        :rtype: bool
        """
        return self._conference_game

    @conference_game.setter
    def conference_game(self, conference_game):
        """Sets the conference_game of this Game.


        :param conference_game: The conference_game of this Game.  # noqa: E501
        :type: bool
        """

        self._conference_game = conference_game

    @property
    def attendance(self):
        """Gets the attendance of this Game.  # noqa: E501


        :return: The attendance of this Game.  # noqa: E501
        :rtype: int
        """
        return self._attendance

    @attendance.setter
    def attendance(self, attendance):
        """Sets the attendance of this Game.


        :param attendance: The attendance of this Game.  # noqa: E501
        :type: int
        """

        self._attendance = attendance

    @property
    def venue_id(self):
        """Gets the venue_id of this Game.  # noqa: E501


        :return: The venue_id of this Game.  # noqa: E501
        :rtype: int
        """
        return self._venue_id

    @venue_id.setter
    def venue_id(self, venue_id):
        """Sets the venue_id of this Game.


        :param venue_id: The venue_id of this Game.  # noqa: E501
        :type: int
        """

        self._venue_id = venue_id

    @property
    def venue(self):
        """Gets the venue of this Game.  # noqa: E501


        :return: The venue of this Game.  # noqa: E501
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this Game.


        :param venue: The venue of this Game.  # noqa: E501
        :type: str
        """

        self._venue = venue

    @property
    def home_id(self):
        """Gets the home_id of this Game.  # noqa: E501


        :return: The home_id of this Game.  # noqa: E501
        :rtype: int
        """
        return self._home_id

    @home_id.setter
    def home_id(self, home_id):
        """Sets the home_id of this Game.


        :param home_id: The home_id of this Game.  # noqa: E501
        :type: int
        """

        self._home_id = home_id

    @property
    def home_team(self):
        """Gets the home_team of this Game.  # noqa: E501


        :return: The home_team of this Game.  # noqa: E501
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this Game.


        :param home_team: The home_team of this Game.  # noqa: E501
        :type: str
        """

        self._home_team = home_team

    @property
    def home_conference(self):
        """Gets the home_conference of this Game.  # noqa: E501


        :return: The home_conference of this Game.  # noqa: E501
        :rtype: str
        """
        return self._home_conference

    @home_conference.setter
    def home_conference(self, home_conference):
        """Sets the home_conference of this Game.


        :param home_conference: The home_conference of this Game.  # noqa: E501
        :type: str
        """

        self._home_conference = home_conference

    @property
    def home_points(self):
        """Gets the home_points of this Game.  # noqa: E501


        :return: The home_points of this Game.  # noqa: E501
        :rtype: int
        """
        return self._home_points

    @home_points.setter
    def home_points(self, home_points):
        """Sets the home_points of this Game.


        :param home_points: The home_points of this Game.  # noqa: E501
        :type: int
        """

        self._home_points = home_points

    @property
    def home_line_scores(self):
        """Gets the home_line_scores of this Game.  # noqa: E501


        :return: The home_line_scores of this Game.  # noqa: E501
        :rtype: list[int]
        """
        return self._home_line_scores

    @home_line_scores.setter
    def home_line_scores(self, home_line_scores):
        """Sets the home_line_scores of this Game.


        :param home_line_scores: The home_line_scores of this Game.  # noqa: E501
        :type: list[int]
        """

        self._home_line_scores = home_line_scores

    @property
    def home_post_win_prob(self):
        """Gets the home_post_win_prob of this Game.  # noqa: E501


        :return: The home_post_win_prob of this Game.  # noqa: E501
        :rtype: float
        """
        return self._home_post_win_prob

    @home_post_win_prob.setter
    def home_post_win_prob(self, home_post_win_prob):
        """Sets the home_post_win_prob of this Game.


        :param home_post_win_prob: The home_post_win_prob of this Game.  # noqa: E501
        :type: float
        """

        self._home_post_win_prob = home_post_win_prob

    @property
    def home_pregame_elo(self):
        """Gets the home_pregame_elo of this Game.  # noqa: E501


        :return: The home_pregame_elo of this Game.  # noqa: E501
        :rtype: int
        """
        return self._home_pregame_elo

    @home_pregame_elo.setter
    def home_pregame_elo(self, home_pregame_elo):
        """Sets the home_pregame_elo of this Game.


        :param home_pregame_elo: The home_pregame_elo of this Game.  # noqa: E501
        :type: int
        """

        self._home_pregame_elo = home_pregame_elo

    @property
    def home_postgame_elo(self):
        """Gets the home_postgame_elo of this Game.  # noqa: E501


        :return: The home_postgame_elo of this Game.  # noqa: E501
        :rtype: int
        """
        return self._home_postgame_elo

    @home_postgame_elo.setter
    def home_postgame_elo(self, home_postgame_elo):
        """Sets the home_postgame_elo of this Game.


        :param home_postgame_elo: The home_postgame_elo of this Game.  # noqa: E501
        :type: int
        """

        self._home_postgame_elo = home_postgame_elo

    @property
    def away_id(self):
        """Gets the away_id of this Game.  # noqa: E501


        :return: The away_id of this Game.  # noqa: E501
        :rtype: int
        """
        return self._away_id

    @away_id.setter
    def away_id(self, away_id):
        """Sets the away_id of this Game.


        :param away_id: The away_id of this Game.  # noqa: E501
        :type: int
        """

        self._away_id = away_id

    @property
    def away_team(self):
        """Gets the away_team of this Game.  # noqa: E501


        :return: The away_team of this Game.  # noqa: E501
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this Game.


        :param away_team: The away_team of this Game.  # noqa: E501
        :type: str
        """

        self._away_team = away_team

    @property
    def away_conference(self):
        """Gets the away_conference of this Game.  # noqa: E501


        :return: The away_conference of this Game.  # noqa: E501
        :rtype: str
        """
        return self._away_conference

    @away_conference.setter
    def away_conference(self, away_conference):
        """Sets the away_conference of this Game.


        :param away_conference: The away_conference of this Game.  # noqa: E501
        :type: str
        """

        self._away_conference = away_conference

    @property
    def away_points(self):
        """Gets the away_points of this Game.  # noqa: E501


        :return: The away_points of this Game.  # noqa: E501
        :rtype: int
        """
        return self._away_points

    @away_points.setter
    def away_points(self, away_points):
        """Sets the away_points of this Game.


        :param away_points: The away_points of this Game.  # noqa: E501
        :type: int
        """

        self._away_points = away_points

    @property
    def away_line_scores(self):
        """Gets the away_line_scores of this Game.  # noqa: E501


        :return: The away_line_scores of this Game.  # noqa: E501
        :rtype: list[int]
        """
        return self._away_line_scores

    @away_line_scores.setter
    def away_line_scores(self, away_line_scores):
        """Sets the away_line_scores of this Game.


        :param away_line_scores: The away_line_scores of this Game.  # noqa: E501
        :type: list[int]
        """

        self._away_line_scores = away_line_scores

    @property
    def away_post_win_prob(self):
        """Gets the away_post_win_prob of this Game.  # noqa: E501


        :return: The away_post_win_prob of this Game.  # noqa: E501
        :rtype: float
        """
        return self._away_post_win_prob

    @away_post_win_prob.setter
    def away_post_win_prob(self, away_post_win_prob):
        """Sets the away_post_win_prob of this Game.


        :param away_post_win_prob: The away_post_win_prob of this Game.  # noqa: E501
        :type: float
        """

        self._away_post_win_prob = away_post_win_prob

    @property
    def away_pregame_elo(self):
        """Gets the away_pregame_elo of this Game.  # noqa: E501


        :return: The away_pregame_elo of this Game.  # noqa: E501
        :rtype: int
        """
        return self._away_pregame_elo

    @away_pregame_elo.setter
    def away_pregame_elo(self, away_pregame_elo):
        """Sets the away_pregame_elo of this Game.


        :param away_pregame_elo: The away_pregame_elo of this Game.  # noqa: E501
        :type: int
        """

        self._away_pregame_elo = away_pregame_elo

    @property
    def away_postgame_elo(self):
        """Gets the away_postgame_elo of this Game.  # noqa: E501


        :return: The away_postgame_elo of this Game.  # noqa: E501
        :rtype: int
        """
        return self._away_postgame_elo

    @away_postgame_elo.setter
    def away_postgame_elo(self, away_postgame_elo):
        """Sets the away_postgame_elo of this Game.


        :param away_postgame_elo: The away_postgame_elo of this Game.  # noqa: E501
        :type: int
        """

        self._away_postgame_elo = away_postgame_elo

    @property
    def excitement_index(self):
        """Gets the excitement_index of this Game.  # noqa: E501


        :return: The excitement_index of this Game.  # noqa: E501
        :rtype: float
        """
        return self._excitement_index

    @excitement_index.setter
    def excitement_index(self, excitement_index):
        """Sets the excitement_index of this Game.


        :param excitement_index: The excitement_index of this Game.  # noqa: E501
        :type: float
        """

        self._excitement_index = excitement_index

    @property
    def highlights(self):
        """Gets the highlights of this Game.  # noqa: E501


        :return: The highlights of this Game.  # noqa: E501
        :rtype: str
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this Game.


        :param highlights: The highlights of this Game.  # noqa: E501
        :type: str
        """

        self._highlights = highlights

    @property
    def notes(self):
        """Gets the notes of this Game.  # noqa: E501


        :return: The notes of this Game.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Game.


        :param notes: The notes of this Game.  # noqa: E501
        :type: str
        """

        self._notes = notes

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
        if issubclass(Game, dict):
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
        if not isinstance(other, Game):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Game):
            return True

        return self.to_dict() != other.to_dict()
