# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.18
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from cfbd.models.game_status import GameStatus
from cfbd.models.scoreboard_game_betting import ScoreboardGameBetting
from cfbd.models.scoreboard_game_home_team import ScoreboardGameHomeTeam
from cfbd.models.scoreboard_game_venue import ScoreboardGameVenue
from cfbd.models.scoreboard_game_weather import ScoreboardGameWeather

class ScoreboardGame(BaseModel):
    """
    ScoreboardGame
    """
    id: StrictInt = Field(...)
    start_date: datetime = Field(default=..., alias="startDate")
    start_time_tbd: StrictBool = Field(default=..., alias="startTimeTBD")
    tv: Optional[StrictStr] = Field(...)
    neutral_site: StrictBool = Field(default=..., alias="neutralSite")
    conference_game: StrictBool = Field(default=..., alias="conferenceGame")
    status: GameStatus = Field(...)
    period: Optional[StrictInt] = Field(...)
    clock: Optional[StrictStr] = Field(...)
    situation: Optional[StrictStr] = Field(...)
    possession: Optional[StrictStr] = Field(...)
    last_play: Optional[StrictStr] = Field(default=..., alias="lastPlay")
    venue: ScoreboardGameVenue = Field(...)
    home_team: ScoreboardGameHomeTeam = Field(default=..., alias="homeTeam")
    away_team: ScoreboardGameHomeTeam = Field(default=..., alias="awayTeam")
    weather: ScoreboardGameWeather = Field(...)
    betting: ScoreboardGameBetting = Field(...)
    __properties = ["id", "startDate", "startTimeTBD", "tv", "neutralSite", "conferenceGame", "status", "period", "clock", "situation", "possession", "lastPlay", "venue", "homeTeam", "awayTeam", "weather", "betting"]

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
    def from_json(cls, json_str: str) -> ScoreboardGame:
        """Create an instance of ScoreboardGame from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of venue
        if self.venue:
            _dict['venue'] = self.venue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of home_team
        if self.home_team:
            _dict['homeTeam'] = self.home_team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of away_team
        if self.away_team:
            _dict['awayTeam'] = self.away_team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of weather
        if self.weather:
            _dict['weather'] = self.weather.to_dict()
        # override the default output from pydantic by calling `to_dict()` of betting
        if self.betting:
            _dict['betting'] = self.betting.to_dict()
        # set to None if tv (nullable) is None
        # and __fields_set__ contains the field
        if self.tv is None and "tv" in self.__fields_set__:
            _dict['tv'] = None

        # set to None if period (nullable) is None
        # and __fields_set__ contains the field
        if self.period is None and "period" in self.__fields_set__:
            _dict['period'] = None

        # set to None if clock (nullable) is None
        # and __fields_set__ contains the field
        if self.clock is None and "clock" in self.__fields_set__:
            _dict['clock'] = None

        # set to None if situation (nullable) is None
        # and __fields_set__ contains the field
        if self.situation is None and "situation" in self.__fields_set__:
            _dict['situation'] = None

        # set to None if possession (nullable) is None
        # and __fields_set__ contains the field
        if self.possession is None and "possession" in self.__fields_set__:
            _dict['possession'] = None

        # set to None if last_play (nullable) is None
        # and __fields_set__ contains the field
        if self.last_play is None and "last_play" in self.__fields_set__:
            _dict['lastPlay'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScoreboardGame:
        """Create an instance of ScoreboardGame from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScoreboardGame.parse_obj(obj)

        _obj = ScoreboardGame.parse_obj({
            "id": obj.get("id"),
            "start_date": obj.get("startDate"),
            "start_time_tbd": obj.get("startTimeTBD"),
            "tv": obj.get("tv"),
            "neutral_site": obj.get("neutralSite"),
            "conference_game": obj.get("conferenceGame"),
            "status": obj.get("status"),
            "period": obj.get("period"),
            "clock": obj.get("clock"),
            "situation": obj.get("situation"),
            "possession": obj.get("possession"),
            "last_play": obj.get("lastPlay"),
            "venue": ScoreboardGameVenue.from_dict(obj.get("venue")) if obj.get("venue") is not None else None,
            "home_team": ScoreboardGameHomeTeam.from_dict(obj.get("homeTeam")) if obj.get("homeTeam") is not None else None,
            "away_team": ScoreboardGameHomeTeam.from_dict(obj.get("awayTeam")) if obj.get("awayTeam") is not None else None,
            "weather": ScoreboardGameWeather.from_dict(obj.get("weather")) if obj.get("weather") is not None else None,
            "betting": ScoreboardGameBetting.from_dict(obj.get("betting")) if obj.get("betting") is not None else None
        })
        return _obj


