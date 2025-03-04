# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.6
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from cfbd.models.game_team_stats_team_stat import GameTeamStatsTeamStat

class GameTeamStatsTeam(BaseModel):
    """
    GameTeamStatsTeam
    """
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    conference: Optional[StrictStr] = Field(...)
    home_away: StrictStr = Field(default=..., alias="homeAway")
    points: Optional[StrictInt] = Field(...)
    stats: conlist(GameTeamStatsTeamStat) = Field(...)
    __properties = ["teamId", "team", "conference", "homeAway", "points", "stats"]

    @validator('home_away')
    def home_away_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('home', 'away',):
            raise ValueError("must be one of enum values ('home', 'away')")
        return value

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
    def from_json(cls, json_str: str) -> GameTeamStatsTeam:
        """Create an instance of GameTeamStatsTeam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in stats (list)
        _items = []
        if self.stats:
            for _item in self.stats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stats'] = _items
        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameTeamStatsTeam:
        """Create an instance of GameTeamStatsTeam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameTeamStatsTeam.parse_obj(obj)

        _obj = GameTeamStatsTeam.parse_obj({
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "home_away": obj.get("homeAway"),
            "points": obj.get("points"),
            "stats": [GameTeamStatsTeamStat.from_dict(_item) for _item in obj.get("stats")] if obj.get("stats") is not None else None
        })
        return _obj


