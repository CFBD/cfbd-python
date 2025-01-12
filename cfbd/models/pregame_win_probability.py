# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.5
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from cfbd.models.season_type import SeasonType

class PregameWinProbability(BaseModel):
    """
    PregameWinProbability
    """
    season: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    week: StrictInt = Field(...)
    game_id: StrictInt = Field(default=..., alias="gameId")
    home_team: StrictStr = Field(default=..., alias="homeTeam")
    away_team: StrictStr = Field(default=..., alias="awayTeam")
    spread: Union[StrictFloat, StrictInt] = Field(...)
    home_win_probability: Union[StrictFloat, StrictInt] = Field(default=..., alias="homeWinProbability")
    __properties = ["season", "seasonType", "week", "gameId", "homeTeam", "awayTeam", "spread", "homeWinProbability"]

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
    def from_json(cls, json_str: str) -> PregameWinProbability:
        """Create an instance of PregameWinProbability from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PregameWinProbability:
        """Create an instance of PregameWinProbability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PregameWinProbability.parse_obj(obj)

        _obj = PregameWinProbability.parse_obj({
            "season": obj.get("season"),
            "season_type": obj.get("seasonType"),
            "week": obj.get("week"),
            "game_id": obj.get("gameId"),
            "home_team": obj.get("homeTeam"),
            "away_team": obj.get("awayTeam"),
            "spread": obj.get("spread"),
            "home_win_probability": obj.get("homeWinProbability")
        })
        return _obj


