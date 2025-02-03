# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.9
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
from cfbd.models.media_type import MediaType
from cfbd.models.season_type import SeasonType

class GameMedia(BaseModel):
    """
    GameMedia
    """
    id: StrictInt = Field(...)
    season: StrictInt = Field(...)
    week: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    start_time: datetime = Field(default=..., alias="startTime")
    is_start_time_tbd: StrictBool = Field(default=..., alias="isStartTimeTBD")
    home_team: StrictStr = Field(default=..., alias="homeTeam")
    home_conference: Optional[StrictStr] = Field(default=..., alias="homeConference")
    away_team: StrictStr = Field(default=..., alias="awayTeam")
    away_conference: Optional[StrictStr] = Field(default=..., alias="awayConference")
    media_type: MediaType = Field(default=..., alias="mediaType")
    outlet: StrictStr = Field(...)
    __properties = ["id", "season", "week", "seasonType", "startTime", "isStartTimeTBD", "homeTeam", "homeConference", "awayTeam", "awayConference", "mediaType", "outlet"]

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
    def from_json(cls, json_str: str) -> GameMedia:
        """Create an instance of GameMedia from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameMedia:
        """Create an instance of GameMedia from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameMedia.parse_obj(obj)

        _obj = GameMedia.parse_obj({
            "id": obj.get("id"),
            "season": obj.get("season"),
            "week": obj.get("week"),
            "season_type": obj.get("seasonType"),
            "start_time": obj.get("startTime"),
            "is_start_time_tbd": obj.get("isStartTimeTBD"),
            "home_team": obj.get("homeTeam"),
            "home_conference": obj.get("homeConference"),
            "away_team": obj.get("awayTeam"),
            "away_conference": obj.get("awayConference"),
            "media_type": obj.get("mediaType"),
            "outlet": obj.get("outlet")
        })
        return _obj


