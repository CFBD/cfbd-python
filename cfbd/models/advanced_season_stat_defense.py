# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.14
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from cfbd.models.advanced_season_stat_offense_field_position import AdvancedSeasonStatOffenseFieldPosition
from cfbd.models.advanced_season_stat_offense_havoc import AdvancedSeasonStatOffenseHavoc
from cfbd.models.advanced_season_stat_offense_passing_downs import AdvancedSeasonStatOffensePassingDowns
from cfbd.models.advanced_season_stat_offense_passing_plays import AdvancedSeasonStatOffensePassingPlays

class AdvancedSeasonStatDefense(BaseModel):
    """
    AdvancedSeasonStatDefense
    """
    passing_plays: AdvancedSeasonStatOffensePassingPlays = Field(default=..., alias="passingPlays")
    rushing_plays: AdvancedSeasonStatOffensePassingPlays = Field(default=..., alias="rushingPlays")
    passing_downs: AdvancedSeasonStatOffensePassingPlays = Field(default=..., alias="passingDowns")
    standard_downs: AdvancedSeasonStatOffensePassingDowns = Field(default=..., alias="standardDowns")
    havoc: AdvancedSeasonStatOffenseHavoc = Field(...)
    field_position: AdvancedSeasonStatOffenseFieldPosition = Field(default=..., alias="fieldPosition")
    points_per_opportunity: Union[StrictFloat, StrictInt] = Field(default=..., alias="pointsPerOpportunity")
    total_opportunies: StrictInt = Field(default=..., alias="totalOpportunies")
    open_field_yards_total: StrictInt = Field(default=..., alias="openFieldYardsTotal")
    open_field_yards: Union[StrictFloat, StrictInt] = Field(default=..., alias="openFieldYards")
    second_level_yards_total: StrictInt = Field(default=..., alias="secondLevelYardsTotal")
    second_level_yards: Union[StrictFloat, StrictInt] = Field(default=..., alias="secondLevelYards")
    line_yards_total: StrictInt = Field(default=..., alias="lineYardsTotal")
    line_yards: Union[StrictFloat, StrictInt] = Field(default=..., alias="lineYards")
    stuff_rate: Union[StrictFloat, StrictInt] = Field(default=..., alias="stuffRate")
    power_success: Union[StrictFloat, StrictInt] = Field(default=..., alias="powerSuccess")
    explosiveness: Union[StrictFloat, StrictInt] = Field(...)
    success_rate: Union[StrictFloat, StrictInt] = Field(default=..., alias="successRate")
    total_ppa: Union[StrictFloat, StrictInt] = Field(default=..., alias="totalPPA")
    ppa: Union[StrictFloat, StrictInt] = Field(...)
    drives: StrictInt = Field(...)
    plays: StrictInt = Field(...)
    __properties = ["passingPlays", "rushingPlays", "passingDowns", "standardDowns", "havoc", "fieldPosition", "pointsPerOpportunity", "totalOpportunies", "openFieldYardsTotal", "openFieldYards", "secondLevelYardsTotal", "secondLevelYards", "lineYardsTotal", "lineYards", "stuffRate", "powerSuccess", "explosiveness", "successRate", "totalPPA", "ppa", "drives", "plays"]

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
    def from_json(cls, json_str: str) -> AdvancedSeasonStatDefense:
        """Create an instance of AdvancedSeasonStatDefense from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of passing_plays
        if self.passing_plays:
            _dict['passingPlays'] = self.passing_plays.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rushing_plays
        if self.rushing_plays:
            _dict['rushingPlays'] = self.rushing_plays.to_dict()
        # override the default output from pydantic by calling `to_dict()` of passing_downs
        if self.passing_downs:
            _dict['passingDowns'] = self.passing_downs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of standard_downs
        if self.standard_downs:
            _dict['standardDowns'] = self.standard_downs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of havoc
        if self.havoc:
            _dict['havoc'] = self.havoc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of field_position
        if self.field_position:
            _dict['fieldPosition'] = self.field_position.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedSeasonStatDefense:
        """Create an instance of AdvancedSeasonStatDefense from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedSeasonStatDefense.parse_obj(obj)

        _obj = AdvancedSeasonStatDefense.parse_obj({
            "passing_plays": AdvancedSeasonStatOffensePassingPlays.from_dict(obj.get("passingPlays")) if obj.get("passingPlays") is not None else None,
            "rushing_plays": AdvancedSeasonStatOffensePassingPlays.from_dict(obj.get("rushingPlays")) if obj.get("rushingPlays") is not None else None,
            "passing_downs": AdvancedSeasonStatOffensePassingPlays.from_dict(obj.get("passingDowns")) if obj.get("passingDowns") is not None else None,
            "standard_downs": AdvancedSeasonStatOffensePassingDowns.from_dict(obj.get("standardDowns")) if obj.get("standardDowns") is not None else None,
            "havoc": AdvancedSeasonStatOffenseHavoc.from_dict(obj.get("havoc")) if obj.get("havoc") is not None else None,
            "field_position": AdvancedSeasonStatOffenseFieldPosition.from_dict(obj.get("fieldPosition")) if obj.get("fieldPosition") is not None else None,
            "points_per_opportunity": obj.get("pointsPerOpportunity"),
            "total_opportunies": obj.get("totalOpportunies"),
            "open_field_yards_total": obj.get("openFieldYardsTotal"),
            "open_field_yards": obj.get("openFieldYards"),
            "second_level_yards_total": obj.get("secondLevelYardsTotal"),
            "second_level_yards": obj.get("secondLevelYards"),
            "line_yards_total": obj.get("lineYardsTotal"),
            "line_yards": obj.get("lineYards"),
            "stuff_rate": obj.get("stuffRate"),
            "power_success": obj.get("powerSuccess"),
            "explosiveness": obj.get("explosiveness"),
            "success_rate": obj.get("successRate"),
            "total_ppa": obj.get("totalPPA"),
            "ppa": obj.get("ppa"),
            "drives": obj.get("drives"),
            "plays": obj.get("plays")
        })
        return _obj


