# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ReturningProduction(BaseModel):
    """
    ReturningProduction
    """
    season: StrictInt = Field(...)
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    total_ppa: Union[StrictFloat, StrictInt] = Field(default=..., alias="totalPPA")
    total_passing_ppa: Union[StrictFloat, StrictInt] = Field(default=..., alias="totalPassingPPA")
    total_receiving_ppa: Union[StrictFloat, StrictInt] = Field(default=..., alias="totalReceivingPPA")
    total_rushing_ppa: Union[StrictFloat, StrictInt] = Field(default=..., alias="totalRushingPPA")
    percent_ppa: Union[StrictFloat, StrictInt] = Field(default=..., alias="percentPPA")
    percent_passing_ppa: Union[StrictFloat, StrictInt] = Field(default=..., alias="percentPassingPPA")
    percent_receiving_ppa: Union[StrictFloat, StrictInt] = Field(default=..., alias="percentReceivingPPA")
    percent_rushing_ppa: Union[StrictFloat, StrictInt] = Field(default=..., alias="percentRushingPPA")
    usage: Union[StrictFloat, StrictInt] = Field(...)
    passing_usage: Union[StrictFloat, StrictInt] = Field(default=..., alias="passingUsage")
    receiving_usage: Union[StrictFloat, StrictInt] = Field(default=..., alias="receivingUsage")
    rushing_usage: Union[StrictFloat, StrictInt] = Field(default=..., alias="rushingUsage")
    __properties = ["season", "team", "conference", "totalPPA", "totalPassingPPA", "totalReceivingPPA", "totalRushingPPA", "percentPPA", "percentPassingPPA", "percentReceivingPPA", "percentRushingPPA", "usage", "passingUsage", "receivingUsage", "rushingUsage"]

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
    def from_json(cls, json_str: str) -> ReturningProduction:
        """Create an instance of ReturningProduction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReturningProduction:
        """Create an instance of ReturningProduction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReturningProduction.parse_obj(obj)

        _obj = ReturningProduction.parse_obj({
            "season": obj.get("season"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "total_ppa": obj.get("totalPPA"),
            "total_passing_ppa": obj.get("totalPassingPPA"),
            "total_receiving_ppa": obj.get("totalReceivingPPA"),
            "total_rushing_ppa": obj.get("totalRushingPPA"),
            "percent_ppa": obj.get("percentPPA"),
            "percent_passing_ppa": obj.get("percentPassingPPA"),
            "percent_receiving_ppa": obj.get("percentReceivingPPA"),
            "percent_rushing_ppa": obj.get("percentRushingPPA"),
            "usage": obj.get("usage"),
            "passing_usage": obj.get("passingUsage"),
            "receiving_usage": obj.get("receivingUsage"),
            "rushing_usage": obj.get("rushingUsage")
        })
        return _obj


