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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from cfbd.models.advanced_season_stat_offense_havoc import AdvancedSeasonStatOffenseHavoc

class ConferenceSPDefense(BaseModel):
    """
    ConferenceSPDefense
    """
    havoc: AdvancedSeasonStatOffenseHavoc = Field(...)
    passing_downs: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="passingDowns")
    standard_downs: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="standardDowns")
    passing: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    rushing: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    explosiveness: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    success: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    rating: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["havoc", "passingDowns", "standardDowns", "passing", "rushing", "explosiveness", "success", "rating"]

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
    def from_json(cls, json_str: str) -> ConferenceSPDefense:
        """Create an instance of ConferenceSPDefense from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of havoc
        if self.havoc:
            _dict['havoc'] = self.havoc.to_dict()
        # set to None if passing_downs (nullable) is None
        # and __fields_set__ contains the field
        if self.passing_downs is None and "passing_downs" in self.__fields_set__:
            _dict['passingDowns'] = None

        # set to None if standard_downs (nullable) is None
        # and __fields_set__ contains the field
        if self.standard_downs is None and "standard_downs" in self.__fields_set__:
            _dict['standardDowns'] = None

        # set to None if passing (nullable) is None
        # and __fields_set__ contains the field
        if self.passing is None and "passing" in self.__fields_set__:
            _dict['passing'] = None

        # set to None if rushing (nullable) is None
        # and __fields_set__ contains the field
        if self.rushing is None and "rushing" in self.__fields_set__:
            _dict['rushing'] = None

        # set to None if explosiveness (nullable) is None
        # and __fields_set__ contains the field
        if self.explosiveness is None and "explosiveness" in self.__fields_set__:
            _dict['explosiveness'] = None

        # set to None if success (nullable) is None
        # and __fields_set__ contains the field
        if self.success is None and "success" in self.__fields_set__:
            _dict['success'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConferenceSPDefense:
        """Create an instance of ConferenceSPDefense from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConferenceSPDefense.parse_obj(obj)

        _obj = ConferenceSPDefense.parse_obj({
            "havoc": AdvancedSeasonStatOffenseHavoc.from_dict(obj.get("havoc")) if obj.get("havoc") is not None else None,
            "passing_downs": obj.get("passingDowns"),
            "standard_downs": obj.get("standardDowns"),
            "passing": obj.get("passing"),
            "rushing": obj.get("rushing"),
            "explosiveness": obj.get("explosiveness"),
            "success": obj.get("success"),
            "rating": obj.get("rating")
        })
        return _obj


