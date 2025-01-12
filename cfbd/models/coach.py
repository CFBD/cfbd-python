# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.6
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from cfbd.models.coach_season import CoachSeason

class Coach(BaseModel):
    """
    Coach
    """
    first_name: StrictStr = Field(default=..., alias="firstName")
    last_name: StrictStr = Field(default=..., alias="lastName")
    hire_date: Optional[datetime] = Field(default=..., alias="hireDate")
    seasons: conlist(CoachSeason) = Field(...)
    __properties = ["firstName", "lastName", "hireDate", "seasons"]

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
    def from_json(cls, json_str: str) -> Coach:
        """Create an instance of Coach from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in seasons (list)
        _items = []
        if self.seasons:
            for _item in self.seasons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['seasons'] = _items
        # set to None if hire_date (nullable) is None
        # and __fields_set__ contains the field
        if self.hire_date is None and "hire_date" in self.__fields_set__:
            _dict['hireDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Coach:
        """Create an instance of Coach from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Coach.parse_obj(obj)

        _obj = Coach.parse_obj({
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "hire_date": obj.get("hireDate"),
            "seasons": [CoachSeason.from_dict(_item) for _item in obj.get("seasons")] if obj.get("seasons") is not None else None
        })
        return _obj


