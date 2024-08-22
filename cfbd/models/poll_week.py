# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.11
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
from cfbd.models.poll import Poll
from cfbd.models.season_type import SeasonType

class PollWeek(BaseModel):
    """
    PollWeek
    """
    season: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    week: StrictInt = Field(...)
    polls: conlist(Poll) = Field(...)
    __properties = ["season", "seasonType", "week", "polls"]

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
    def from_json(cls, json_str: str) -> PollWeek:
        """Create an instance of PollWeek from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in polls (list)
        _items = []
        if self.polls:
            for _item in self.polls:
                if _item:
                    _items.append(_item.to_dict())
            _dict['polls'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PollWeek:
        """Create an instance of PollWeek from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PollWeek.parse_obj(obj)

        _obj = PollWeek.parse_obj({
            "season": obj.get("season"),
            "season_type": obj.get("seasonType"),
            "week": obj.get("week"),
            "polls": [Poll.from_dict(_item) for _item in obj.get("polls")] if obj.get("polls") is not None else None
        })
        return _obj


