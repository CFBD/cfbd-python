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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from cfbd.models.game_player_stat_types import GamePlayerStatTypes

class GamePlayerStatCategories(BaseModel):
    """
    GamePlayerStatCategories
    """
    name: StrictStr = Field(...)
    types: conlist(GamePlayerStatTypes) = Field(...)
    __properties = ["name", "types"]

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
    def from_json(cls, json_str: str) -> GamePlayerStatCategories:
        """Create an instance of GamePlayerStatCategories from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in types (list)
        _items = []
        if self.types:
            for _item in self.types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['types'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GamePlayerStatCategories:
        """Create an instance of GamePlayerStatCategories from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GamePlayerStatCategories.parse_obj(obj)

        _obj = GamePlayerStatCategories.parse_obj({
            "name": obj.get("name"),
            "types": [GamePlayerStatTypes.from_dict(_item) for _item in obj.get("types")] if obj.get("types") is not None else None
        })
        return _obj


