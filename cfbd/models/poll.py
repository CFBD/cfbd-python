# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.1
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
from cfbd.models.poll_rank import PollRank

class Poll(BaseModel):
    """
    Poll
    """
    poll: StrictStr = Field(...)
    ranks: conlist(PollRank) = Field(...)
    __properties = ["poll", "ranks"]

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
    def from_json(cls, json_str: str) -> Poll:
        """Create an instance of Poll from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ranks (list)
        _items = []
        if self.ranks:
            for _item in self.ranks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ranks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Poll:
        """Create an instance of Poll from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Poll.parse_obj(obj)

        _obj = Poll.parse_obj({
            "poll": obj.get("poll"),
            "ranks": [PollRank.from_dict(_item) for _item in obj.get("ranks")] if obj.get("ranks") is not None else None
        })
        return _obj


