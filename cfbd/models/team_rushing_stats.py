# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.8
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

class TeamRushingStats(BaseModel):
    """
    TeamRushingStats
    """
    team: StrictStr = Field(...)
    power_success: Union[StrictFloat, StrictInt] = Field(default=..., alias="powerSuccess")
    stuff_rate: Union[StrictFloat, StrictInt] = Field(default=..., alias="stuffRate")
    line_yards: Union[StrictFloat, StrictInt] = Field(default=..., alias="lineYards")
    line_yards_average: Union[StrictFloat, StrictInt] = Field(default=..., alias="lineYardsAverage")
    second_level_yards: Union[StrictFloat, StrictInt] = Field(default=..., alias="secondLevelYards")
    second_level_yards_average: Union[StrictFloat, StrictInt] = Field(default=..., alias="secondLevelYardsAverage")
    open_field_yards: Union[StrictFloat, StrictInt] = Field(default=..., alias="openFieldYards")
    open_field_yards_average: Union[StrictFloat, StrictInt] = Field(default=..., alias="openFieldYardsAverage")
    __properties = ["team", "powerSuccess", "stuffRate", "lineYards", "lineYardsAverage", "secondLevelYards", "secondLevelYardsAverage", "openFieldYards", "openFieldYardsAverage"]

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
    def from_json(cls, json_str: str) -> TeamRushingStats:
        """Create an instance of TeamRushingStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamRushingStats:
        """Create an instance of TeamRushingStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamRushingStats.parse_obj(obj)

        _obj = TeamRushingStats.parse_obj({
            "team": obj.get("team"),
            "power_success": obj.get("powerSuccess"),
            "stuff_rate": obj.get("stuffRate"),
            "line_yards": obj.get("lineYards"),
            "line_yards_average": obj.get("lineYardsAverage"),
            "second_level_yards": obj.get("secondLevelYards"),
            "second_level_yards_average": obj.get("secondLevelYardsAverage"),
            "open_field_yards": obj.get("openFieldYards"),
            "open_field_yards_average": obj.get("openFieldYardsAverage")
        })
        return _obj


