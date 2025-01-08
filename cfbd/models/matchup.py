# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from cfbd.models.matchup_game import MatchupGame

class Matchup(BaseModel):
    """
    Matchup
    """
    team1: StrictStr = Field(...)
    team2: StrictStr = Field(...)
    start_year: Optional[StrictInt] = Field(default=None, alias="startYear")
    end_year: Optional[StrictInt] = Field(default=None, alias="endYear")
    team1_wins: StrictInt = Field(default=..., alias="team1Wins")
    team2_wins: StrictInt = Field(default=..., alias="team2Wins")
    ties: StrictInt = Field(...)
    games: conlist(MatchupGame) = Field(...)
    __properties = ["team1", "team2", "startYear", "endYear", "team1Wins", "team2Wins", "ties", "games"]

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
    def from_json(cls, json_str: str) -> Matchup:
        """Create an instance of Matchup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in games (list)
        _items = []
        if self.games:
            for _item in self.games:
                if _item:
                    _items.append(_item.to_dict())
            _dict['games'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Matchup:
        """Create an instance of Matchup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Matchup.parse_obj(obj)

        _obj = Matchup.parse_obj({
            "team1": obj.get("team1"),
            "team2": obj.get("team2"),
            "start_year": obj.get("startYear"),
            "end_year": obj.get("endYear"),
            "team1_wins": obj.get("team1Wins"),
            "team2_wins": obj.get("team2Wins"),
            "ties": obj.get("ties"),
            "games": [MatchupGame.from_dict(_item) for _item in obj.get("games")] if obj.get("games") is not None else None
        })
        return _obj


