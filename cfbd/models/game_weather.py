# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.14
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from cfbd.models.season_type import SeasonType

class GameWeather(BaseModel):
    """
    GameWeather
    """
    id: StrictInt = Field(...)
    season: StrictInt = Field(...)
    week: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    start_time: datetime = Field(default=..., alias="startTime")
    game_indoors: StrictBool = Field(default=..., alias="gameIndoors")
    home_team: StrictStr = Field(default=..., alias="homeTeam")
    home_conference: Optional[StrictStr] = Field(default=..., alias="homeConference")
    away_team: StrictStr = Field(default=..., alias="awayTeam")
    away_conference: Optional[StrictStr] = Field(default=..., alias="awayConference")
    venue_id: StrictInt = Field(default=..., alias="venueId")
    venue: StrictStr = Field(...)
    temperature: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    dew_point: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="dewPoint")
    humidity: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    precipitation: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    snowfall: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    wind_direction: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="windDirection")
    wind_speed: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="windSpeed")
    pressure: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    weather_condition_code: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="weatherConditionCode")
    weather_condition: Optional[StrictStr] = Field(default=..., alias="weatherCondition")
    __properties = ["id", "season", "week", "seasonType", "startTime", "gameIndoors", "homeTeam", "homeConference", "awayTeam", "awayConference", "venueId", "venue", "temperature", "dewPoint", "humidity", "precipitation", "snowfall", "windDirection", "windSpeed", "pressure", "weatherConditionCode", "weatherCondition"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GameWeather:
        """Create an instance of GameWeather from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if home_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.home_conference is None and "home_conference" in self.__fields_set__:
            _dict['homeConference'] = None

        # set to None if away_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.away_conference is None and "away_conference" in self.__fields_set__:
            _dict['awayConference'] = None

        # set to None if temperature (nullable) is None
        # and __fields_set__ contains the field
        if self.temperature is None and "temperature" in self.__fields_set__:
            _dict['temperature'] = None

        # set to None if dew_point (nullable) is None
        # and __fields_set__ contains the field
        if self.dew_point is None and "dew_point" in self.__fields_set__:
            _dict['dewPoint'] = None

        # set to None if humidity (nullable) is None
        # and __fields_set__ contains the field
        if self.humidity is None and "humidity" in self.__fields_set__:
            _dict['humidity'] = None

        # set to None if precipitation (nullable) is None
        # and __fields_set__ contains the field
        if self.precipitation is None and "precipitation" in self.__fields_set__:
            _dict['precipitation'] = None

        # set to None if snowfall (nullable) is None
        # and __fields_set__ contains the field
        if self.snowfall is None and "snowfall" in self.__fields_set__:
            _dict['snowfall'] = None

        # set to None if wind_direction (nullable) is None
        # and __fields_set__ contains the field
        if self.wind_direction is None and "wind_direction" in self.__fields_set__:
            _dict['windDirection'] = None

        # set to None if wind_speed (nullable) is None
        # and __fields_set__ contains the field
        if self.wind_speed is None and "wind_speed" in self.__fields_set__:
            _dict['windSpeed'] = None

        # set to None if pressure (nullable) is None
        # and __fields_set__ contains the field
        if self.pressure is None and "pressure" in self.__fields_set__:
            _dict['pressure'] = None

        # set to None if weather_condition_code (nullable) is None
        # and __fields_set__ contains the field
        if self.weather_condition_code is None and "weather_condition_code" in self.__fields_set__:
            _dict['weatherConditionCode'] = None

        # set to None if weather_condition (nullable) is None
        # and __fields_set__ contains the field
        if self.weather_condition is None and "weather_condition" in self.__fields_set__:
            _dict['weatherCondition'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameWeather:
        """Create an instance of GameWeather from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameWeather.parse_obj(obj)

        _obj = GameWeather.parse_obj({
            "id": obj.get("id"),
            "season": obj.get("season"),
            "week": obj.get("week"),
            "season_type": obj.get("seasonType"),
            "start_time": obj.get("startTime"),
            "game_indoors": obj.get("gameIndoors"),
            "home_team": obj.get("homeTeam"),
            "home_conference": obj.get("homeConference"),
            "away_team": obj.get("awayTeam"),
            "away_conference": obj.get("awayConference"),
            "venue_id": obj.get("venueId"),
            "venue": obj.get("venue"),
            "temperature": obj.get("temperature"),
            "dew_point": obj.get("dewPoint"),
            "humidity": obj.get("humidity"),
            "precipitation": obj.get("precipitation"),
            "snowfall": obj.get("snowfall"),
            "wind_direction": obj.get("windDirection"),
            "wind_speed": obj.get("windSpeed"),
            "pressure": obj.get("pressure"),
            "weather_condition_code": obj.get("weatherConditionCode"),
            "weather_condition": obj.get("weatherCondition")
        })
        return _obj


