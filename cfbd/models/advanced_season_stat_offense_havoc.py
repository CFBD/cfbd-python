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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class AdvancedSeasonStatOffenseHavoc(BaseModel):
    """
    AdvancedSeasonStatOffenseHavoc
    """
    db: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    front_seven: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="frontSeven")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["db", "frontSeven", "total"]

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
    def from_json(cls, json_str: str) -> AdvancedSeasonStatOffenseHavoc:
        """Create an instance of AdvancedSeasonStatOffenseHavoc from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if db (nullable) is None
        # and __fields_set__ contains the field
        if self.db is None and "db" in self.__fields_set__:
            _dict['db'] = None

        # set to None if front_seven (nullable) is None
        # and __fields_set__ contains the field
        if self.front_seven is None and "front_seven" in self.__fields_set__:
            _dict['frontSeven'] = None

        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedSeasonStatOffenseHavoc:
        """Create an instance of AdvancedSeasonStatOffenseHavoc from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedSeasonStatOffenseHavoc.parse_obj(obj)

        _obj = AdvancedSeasonStatOffenseHavoc.parse_obj({
            "db": obj.get("db"),
            "front_seven": obj.get("frontSeven"),
            "total": obj.get("total")
        })
        return _obj


