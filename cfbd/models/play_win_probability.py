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


from typing import Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class PlayWinProbability(BaseModel):
    """
    PlayWinProbability
    """
    game_id: StrictInt = Field(default=..., alias="gameId")
    play_id: StrictStr = Field(default=..., alias="playId")
    play_text: StrictStr = Field(default=..., alias="playText")
    home_id: StrictInt = Field(default=..., alias="homeId")
    home: StrictStr = Field(...)
    away_id: StrictInt = Field(default=..., alias="awayId")
    away: StrictStr = Field(...)
    spread: Union[StrictFloat, StrictInt] = Field(...)
    home_ball: StrictBool = Field(default=..., alias="homeBall")
    home_score: StrictInt = Field(default=..., alias="homeScore")
    away_score: StrictInt = Field(default=..., alias="awayScore")
    yard_line: StrictInt = Field(default=..., alias="yardLine")
    down: StrictInt = Field(...)
    distance: StrictInt = Field(...)
    home_win_probability: Union[StrictFloat, StrictInt] = Field(default=..., alias="homeWinProbability")
    play_number: StrictInt = Field(default=..., alias="playNumber")
    __properties = ["gameId", "playId", "playText", "homeId", "home", "awayId", "away", "spread", "homeBall", "homeScore", "awayScore", "yardLine", "down", "distance", "homeWinProbability", "playNumber"]

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
    def from_json(cls, json_str: str) -> PlayWinProbability:
        """Create an instance of PlayWinProbability from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayWinProbability:
        """Create an instance of PlayWinProbability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayWinProbability.parse_obj(obj)

        _obj = PlayWinProbability.parse_obj({
            "game_id": obj.get("gameId"),
            "play_id": obj.get("playId"),
            "play_text": obj.get("playText"),
            "home_id": obj.get("homeId"),
            "home": obj.get("home"),
            "away_id": obj.get("awayId"),
            "away": obj.get("away"),
            "spread": obj.get("spread"),
            "home_ball": obj.get("homeBall"),
            "home_score": obj.get("homeScore"),
            "away_score": obj.get("awayScore"),
            "yard_line": obj.get("yardLine"),
            "down": obj.get("down"),
            "distance": obj.get("distance"),
            "home_win_probability": obj.get("homeWinProbability"),
            "play_number": obj.get("playNumber")
        })
        return _obj


