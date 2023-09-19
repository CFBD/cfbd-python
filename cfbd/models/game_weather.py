# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.5.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class GameWeather(object):
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
        'start_time': 'str',
        'game_indoors': 'bool',
        'home_team': 'str',
        'home_conference': 'str',
        'away_team': 'str',
        'away_conference': 'str',
        'venue_id': 'int',
        'venue': 'str',
        'temperature': 'float',
        'dew_point': 'float',
        'humidity': 'float',
        'precipitation': 'float',
        'snowfall': 'float',
        'wind_direction': 'float',
        'wind_speed': 'float',
        'pressure': 'float',
        'weather_condition_code': 'int',
        'weather_condition': 'str'
    }

    attribute_map = {
        'id': 'id',
        'season': 'season',
        'week': 'week',
        'season_type': 'seasonType',
        'start_time': 'startTime',
        'game_indoors': 'gameIndoors',
        'home_team': 'homeTeam',
        'home_conference': 'homeConference',
        'away_team': 'awayTeam',
        'away_conference': 'awayConference',
        'venue_id': 'venueId',
        'venue': 'venue',
        'temperature': 'temperature',
        'dew_point': 'dewPoint',
        'humidity': 'humidity',
        'precipitation': 'precipitation',
        'snowfall': 'snowfall',
        'wind_direction': 'windDirection',
        'wind_speed': 'windSpeed',
        'pressure': 'pressure',
        'weather_condition_code': 'weatherConditionCode',
        'weather_condition': 'weatherCondition'
    }

    def __init__(self, id=None, season=None, week=None, season_type=None, start_time=None, game_indoors=None, home_team=None, home_conference=None, away_team=None, away_conference=None, venue_id=None, venue=None, temperature=None, dew_point=None, humidity=None, precipitation=None, snowfall=None, wind_direction=None, wind_speed=None, pressure=None, weather_condition_code=None, weather_condition=None, _configuration=None):  # noqa: E501
        """GameWeather - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._season = None
        self._week = None
        self._season_type = None
        self._start_time = None
        self._game_indoors = None
        self._home_team = None
        self._home_conference = None
        self._away_team = None
        self._away_conference = None
        self._venue_id = None
        self._venue = None
        self._temperature = None
        self._dew_point = None
        self._humidity = None
        self._precipitation = None
        self._snowfall = None
        self._wind_direction = None
        self._wind_speed = None
        self._pressure = None
        self._weather_condition_code = None
        self._weather_condition = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if season_type is not None:
            self.season_type = season_type
        if start_time is not None:
            self.start_time = start_time
        if game_indoors is not None:
            self.game_indoors = game_indoors
        if home_team is not None:
            self.home_team = home_team
        if home_conference is not None:
            self.home_conference = home_conference
        if away_team is not None:
            self.away_team = away_team
        if away_conference is not None:
            self.away_conference = away_conference
        if venue_id is not None:
            self.venue_id = venue_id
        if venue is not None:
            self.venue = venue
        if temperature is not None:
            self.temperature = temperature
        if dew_point is not None:
            self.dew_point = dew_point
        if humidity is not None:
            self.humidity = humidity
        if precipitation is not None:
            self.precipitation = precipitation
        if snowfall is not None:
            self.snowfall = snowfall
        if wind_direction is not None:
            self.wind_direction = wind_direction
        if wind_speed is not None:
            self.wind_speed = wind_speed
        if pressure is not None:
            self.pressure = pressure
        if weather_condition_code is not None:
            self.weather_condition_code = weather_condition_code
        if weather_condition is not None:
            self.weather_condition = weather_condition

    @property
    def id(self):
        """Gets the id of this GameWeather.  # noqa: E501


        :return: The id of this GameWeather.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GameWeather.


        :param id: The id of this GameWeather.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def season(self):
        """Gets the season of this GameWeather.  # noqa: E501


        :return: The season of this GameWeather.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this GameWeather.


        :param season: The season of this GameWeather.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this GameWeather.  # noqa: E501


        :return: The week of this GameWeather.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this GameWeather.


        :param week: The week of this GameWeather.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def season_type(self):
        """Gets the season_type of this GameWeather.  # noqa: E501


        :return: The season_type of this GameWeather.  # noqa: E501
        :rtype: str
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this GameWeather.


        :param season_type: The season_type of this GameWeather.  # noqa: E501
        :type: str
        """

        self._season_type = season_type

    @property
    def start_time(self):
        """Gets the start_time of this GameWeather.  # noqa: E501


        :return: The start_time of this GameWeather.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GameWeather.


        :param start_time: The start_time of this GameWeather.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def game_indoors(self):
        """Gets the game_indoors of this GameWeather.  # noqa: E501


        :return: The game_indoors of this GameWeather.  # noqa: E501
        :rtype: bool
        """
        return self._game_indoors

    @game_indoors.setter
    def game_indoors(self, game_indoors):
        """Sets the game_indoors of this GameWeather.


        :param game_indoors: The game_indoors of this GameWeather.  # noqa: E501
        :type: bool
        """

        self._game_indoors = game_indoors

    @property
    def home_team(self):
        """Gets the home_team of this GameWeather.  # noqa: E501


        :return: The home_team of this GameWeather.  # noqa: E501
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this GameWeather.


        :param home_team: The home_team of this GameWeather.  # noqa: E501
        :type: str
        """

        self._home_team = home_team

    @property
    def home_conference(self):
        """Gets the home_conference of this GameWeather.  # noqa: E501


        :return: The home_conference of this GameWeather.  # noqa: E501
        :rtype: str
        """
        return self._home_conference

    @home_conference.setter
    def home_conference(self, home_conference):
        """Sets the home_conference of this GameWeather.


        :param home_conference: The home_conference of this GameWeather.  # noqa: E501
        :type: str
        """

        self._home_conference = home_conference

    @property
    def away_team(self):
        """Gets the away_team of this GameWeather.  # noqa: E501


        :return: The away_team of this GameWeather.  # noqa: E501
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this GameWeather.


        :param away_team: The away_team of this GameWeather.  # noqa: E501
        :type: str
        """

        self._away_team = away_team

    @property
    def away_conference(self):
        """Gets the away_conference of this GameWeather.  # noqa: E501


        :return: The away_conference of this GameWeather.  # noqa: E501
        :rtype: str
        """
        return self._away_conference

    @away_conference.setter
    def away_conference(self, away_conference):
        """Sets the away_conference of this GameWeather.


        :param away_conference: The away_conference of this GameWeather.  # noqa: E501
        :type: str
        """

        self._away_conference = away_conference

    @property
    def venue_id(self):
        """Gets the venue_id of this GameWeather.  # noqa: E501


        :return: The venue_id of this GameWeather.  # noqa: E501
        :rtype: int
        """
        return self._venue_id

    @venue_id.setter
    def venue_id(self, venue_id):
        """Sets the venue_id of this GameWeather.


        :param venue_id: The venue_id of this GameWeather.  # noqa: E501
        :type: int
        """

        self._venue_id = venue_id

    @property
    def venue(self):
        """Gets the venue of this GameWeather.  # noqa: E501


        :return: The venue of this GameWeather.  # noqa: E501
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this GameWeather.


        :param venue: The venue of this GameWeather.  # noqa: E501
        :type: str
        """

        self._venue = venue

    @property
    def temperature(self):
        """Gets the temperature of this GameWeather.  # noqa: E501


        :return: The temperature of this GameWeather.  # noqa: E501
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this GameWeather.


        :param temperature: The temperature of this GameWeather.  # noqa: E501
        :type: float
        """

        self._temperature = temperature

    @property
    def dew_point(self):
        """Gets the dew_point of this GameWeather.  # noqa: E501


        :return: The dew_point of this GameWeather.  # noqa: E501
        :rtype: float
        """
        return self._dew_point

    @dew_point.setter
    def dew_point(self, dew_point):
        """Sets the dew_point of this GameWeather.


        :param dew_point: The dew_point of this GameWeather.  # noqa: E501
        :type: float
        """

        self._dew_point = dew_point

    @property
    def humidity(self):
        """Gets the humidity of this GameWeather.  # noqa: E501


        :return: The humidity of this GameWeather.  # noqa: E501
        :rtype: float
        """
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        """Sets the humidity of this GameWeather.


        :param humidity: The humidity of this GameWeather.  # noqa: E501
        :type: float
        """

        self._humidity = humidity

    @property
    def precipitation(self):
        """Gets the precipitation of this GameWeather.  # noqa: E501


        :return: The precipitation of this GameWeather.  # noqa: E501
        :rtype: float
        """
        return self._precipitation

    @precipitation.setter
    def precipitation(self, precipitation):
        """Sets the precipitation of this GameWeather.


        :param precipitation: The precipitation of this GameWeather.  # noqa: E501
        :type: float
        """

        self._precipitation = precipitation

    @property
    def snowfall(self):
        """Gets the snowfall of this GameWeather.  # noqa: E501


        :return: The snowfall of this GameWeather.  # noqa: E501
        :rtype: float
        """
        return self._snowfall

    @snowfall.setter
    def snowfall(self, snowfall):
        """Sets the snowfall of this GameWeather.


        :param snowfall: The snowfall of this GameWeather.  # noqa: E501
        :type: float
        """

        self._snowfall = snowfall

    @property
    def wind_direction(self):
        """Gets the wind_direction of this GameWeather.  # noqa: E501


        :return: The wind_direction of this GameWeather.  # noqa: E501
        :rtype: float
        """
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, wind_direction):
        """Sets the wind_direction of this GameWeather.


        :param wind_direction: The wind_direction of this GameWeather.  # noqa: E501
        :type: float
        """

        self._wind_direction = wind_direction

    @property
    def wind_speed(self):
        """Gets the wind_speed of this GameWeather.  # noqa: E501


        :return: The wind_speed of this GameWeather.  # noqa: E501
        :rtype: float
        """
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, wind_speed):
        """Sets the wind_speed of this GameWeather.


        :param wind_speed: The wind_speed of this GameWeather.  # noqa: E501
        :type: float
        """

        self._wind_speed = wind_speed

    @property
    def pressure(self):
        """Gets the pressure of this GameWeather.  # noqa: E501


        :return: The pressure of this GameWeather.  # noqa: E501
        :rtype: float
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this GameWeather.


        :param pressure: The pressure of this GameWeather.  # noqa: E501
        :type: float
        """

        self._pressure = pressure

    @property
    def weather_condition_code(self):
        """Gets the weather_condition_code of this GameWeather.  # noqa: E501


        :return: The weather_condition_code of this GameWeather.  # noqa: E501
        :rtype: int
        """
        return self._weather_condition_code

    @weather_condition_code.setter
    def weather_condition_code(self, weather_condition_code):
        """Sets the weather_condition_code of this GameWeather.


        :param weather_condition_code: The weather_condition_code of this GameWeather.  # noqa: E501
        :type: int
        """

        self._weather_condition_code = weather_condition_code

    @property
    def weather_condition(self):
        """Gets the weather_condition of this GameWeather.  # noqa: E501


        :return: The weather_condition of this GameWeather.  # noqa: E501
        :rtype: str
        """
        return self._weather_condition

    @weather_condition.setter
    def weather_condition(self, weather_condition):
        """Sets the weather_condition of this GameWeather.


        :param weather_condition: The weather_condition of this GameWeather.  # noqa: E501
        :type: str
        """

        self._weather_condition = weather_condition

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
        if issubclass(GameWeather, dict):
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
        if not isinstance(other, GameWeather):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GameWeather):
            return True

        return self.to_dict() != other.to_dict()
