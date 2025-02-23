# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from cfbd.models.player_game_usage import PlayerGameUsage
from cfbd.models.player_ppa import PlayerPPA

class AdvancedBoxScorePlayers(BaseModel):
    """
    AdvancedBoxScorePlayers
    """
    ppa: conlist(PlayerPPA) = Field(...)
    usage: conlist(PlayerGameUsage) = Field(...)
    __properties = ["ppa", "usage"]

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
    def from_json(cls, json_str: str) -> AdvancedBoxScorePlayers:
        """Create an instance of AdvancedBoxScorePlayers from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ppa (list)
        _items = []
        if self.ppa:
            for _item in self.ppa:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ppa'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in usage (list)
        _items = []
        if self.usage:
            for _item in self.usage:
                if _item:
                    _items.append(_item.to_dict())
            _dict['usage'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedBoxScorePlayers:
        """Create an instance of AdvancedBoxScorePlayers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedBoxScorePlayers.parse_obj(obj)

        _obj = AdvancedBoxScorePlayers.parse_obj({
            "ppa": [PlayerPPA.from_dict(_item) for _item in obj.get("ppa")] if obj.get("ppa") is not None else None,
            "usage": [PlayerGameUsage.from_dict(_item) for _item in obj.get("usage")] if obj.get("usage") is not None else None
        })
        return _obj


