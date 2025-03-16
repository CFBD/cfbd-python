# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.7
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class GameLine(BaseModel):
    """
    GameLine
    """
    provider: StrictStr = Field(...)
    spread: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    formatted_spread: StrictStr = Field(default=..., alias="formattedSpread")
    spread_open: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="spreadOpen")
    over_under: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="overUnder")
    over_under_open: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="overUnderOpen")
    home_moneyline: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="homeMoneyline")
    away_moneyline: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="awayMoneyline")
    __properties = ["provider", "spread", "formattedSpread", "spreadOpen", "overUnder", "overUnderOpen", "homeMoneyline", "awayMoneyline"]

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
    def from_json(cls, json_str: str) -> GameLine:
        """Create an instance of GameLine from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if spread (nullable) is None
        # and __fields_set__ contains the field
        if self.spread is None and "spread" in self.__fields_set__:
            _dict['spread'] = None

        # set to None if spread_open (nullable) is None
        # and __fields_set__ contains the field
        if self.spread_open is None and "spread_open" in self.__fields_set__:
            _dict['spreadOpen'] = None

        # set to None if over_under (nullable) is None
        # and __fields_set__ contains the field
        if self.over_under is None and "over_under" in self.__fields_set__:
            _dict['overUnder'] = None

        # set to None if over_under_open (nullable) is None
        # and __fields_set__ contains the field
        if self.over_under_open is None and "over_under_open" in self.__fields_set__:
            _dict['overUnderOpen'] = None

        # set to None if home_moneyline (nullable) is None
        # and __fields_set__ contains the field
        if self.home_moneyline is None and "home_moneyline" in self.__fields_set__:
            _dict['homeMoneyline'] = None

        # set to None if away_moneyline (nullable) is None
        # and __fields_set__ contains the field
        if self.away_moneyline is None and "away_moneyline" in self.__fields_set__:
            _dict['awayMoneyline'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameLine:
        """Create an instance of GameLine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameLine.parse_obj(obj)

        _obj = GameLine.parse_obj({
            "provider": obj.get("provider"),
            "spread": obj.get("spread"),
            "formatted_spread": obj.get("formattedSpread"),
            "spread_open": obj.get("spreadOpen"),
            "over_under": obj.get("overUnder"),
            "over_under_open": obj.get("overUnderOpen"),
            "home_moneyline": obj.get("homeMoneyline"),
            "away_moneyline": obj.get("awayMoneyline")
        })
        return _obj


