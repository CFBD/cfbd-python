# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.3.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from cfbd.models.game_player_stats_team import GamePlayerStatsTeam

class GamePlayerStats(BaseModel):
    """
    GamePlayerStats
    """
    id: StrictInt = Field(...)
    teams: conlist(GamePlayerStatsTeam) = Field(...)
    __properties = ["id", "teams"]

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
    def from_json(cls, json_str: str) -> GamePlayerStats:
        """Create an instance of GamePlayerStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item in self.teams:
                if _item:
                    _items.append(_item.to_dict())
            _dict['teams'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GamePlayerStats:
        """Create an instance of GamePlayerStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GamePlayerStats.parse_obj(obj)

        _obj = GamePlayerStats.parse_obj({
            "id": obj.get("id"),
            "teams": [GamePlayerStatsTeam.from_dict(_item) for _item in obj.get("teams")] if obj.get("teams") is not None else None
        })
        return _obj


