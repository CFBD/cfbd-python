# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.10
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime

from pydantic import BaseModel, Field, StrictInt
from cfbd.models.season_type import SeasonType

class CalendarWeek(BaseModel):
    """
    CalendarWeek
    """
    season: StrictInt = Field(...)
    week: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    first_game_start: datetime = Field(default=..., alias="firstGameStart")
    last_game_start: datetime = Field(default=..., alias="lastGameStart")
    __properties = ["season", "week", "seasonType", "firstGameStart", "lastGameStart"]

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
    def from_json(cls, json_str: str) -> CalendarWeek:
        """Create an instance of CalendarWeek from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CalendarWeek:
        """Create an instance of CalendarWeek from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CalendarWeek.parse_obj(obj)

        _obj = CalendarWeek.parse_obj({
            "season": obj.get("season"),
            "week": obj.get("week"),
            "season_type": obj.get("seasonType"),
            "first_game_start": obj.get("firstGameStart"),
            "last_game_start": obj.get("lastGameStart")
        })
        return _obj

