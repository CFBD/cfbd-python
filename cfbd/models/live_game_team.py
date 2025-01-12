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


from typing import List, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator

class LiveGameTeam(BaseModel):
    """
    LiveGameTeam
    """
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    home_away: StrictStr = Field(default=..., alias="homeAway")
    line_scores: conlist(StrictInt) = Field(default=..., alias="lineScores")
    points: StrictInt = Field(...)
    drives: StrictInt = Field(...)
    scoring_opportunities: StrictInt = Field(default=..., alias="scoringOpportunities")
    points_per_opportunity: Union[StrictFloat, StrictInt] = Field(default=..., alias="pointsPerOpportunity")
    plays: StrictInt = Field(...)
    line_yards: Union[StrictFloat, StrictInt] = Field(default=..., alias="lineYards")
    line_yards_per_rush: Union[StrictFloat, StrictInt] = Field(default=..., alias="lineYardsPerRush")
    second_level_yards: Union[StrictFloat, StrictInt] = Field(default=..., alias="secondLevelYards")
    second_level_yards_per_rush: Union[StrictFloat, StrictInt] = Field(default=..., alias="secondLevelYardsPerRush")
    open_field_yards: Union[StrictFloat, StrictInt] = Field(default=..., alias="openFieldYards")
    open_field_yards_per_rush: Union[StrictFloat, StrictInt] = Field(default=..., alias="openFieldYardsPerRush")
    epa_per_play: Union[StrictFloat, StrictInt] = Field(default=..., alias="epaPerPlay")
    total_epa: Union[StrictFloat, StrictInt] = Field(default=..., alias="totalEpa")
    passing_epa: Union[StrictFloat, StrictInt] = Field(default=..., alias="passingEpa")
    epa_per_pass: Union[StrictFloat, StrictInt] = Field(default=..., alias="epaPerPass")
    rushing_epa: Union[StrictFloat, StrictInt] = Field(default=..., alias="rushingEpa")
    epa_per_rush: Union[StrictFloat, StrictInt] = Field(default=..., alias="epaPerRush")
    success_rate: Union[StrictFloat, StrictInt] = Field(default=..., alias="successRate")
    standard_down_success_rate: Union[StrictFloat, StrictInt] = Field(default=..., alias="standardDownSuccessRate")
    passing_down_success_rate: Union[StrictFloat, StrictInt] = Field(default=..., alias="passingDownSuccessRate")
    explosiveness: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["teamId", "team", "homeAway", "lineScores", "points", "drives", "scoringOpportunities", "pointsPerOpportunity", "plays", "lineYards", "lineYardsPerRush", "secondLevelYards", "secondLevelYardsPerRush", "openFieldYards", "openFieldYardsPerRush", "epaPerPlay", "totalEpa", "passingEpa", "epaPerPass", "rushingEpa", "epaPerRush", "successRate", "standardDownSuccessRate", "passingDownSuccessRate", "explosiveness"]

    @validator('home_away')
    def home_away_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('home', 'away',):
            raise ValueError("must be one of enum values ('home', 'away')")
        return value

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
    def from_json(cls, json_str: str) -> LiveGameTeam:
        """Create an instance of LiveGameTeam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LiveGameTeam:
        """Create an instance of LiveGameTeam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LiveGameTeam.parse_obj(obj)

        _obj = LiveGameTeam.parse_obj({
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "home_away": obj.get("homeAway"),
            "line_scores": obj.get("lineScores"),
            "points": obj.get("points"),
            "drives": obj.get("drives"),
            "scoring_opportunities": obj.get("scoringOpportunities"),
            "points_per_opportunity": obj.get("pointsPerOpportunity"),
            "plays": obj.get("plays"),
            "line_yards": obj.get("lineYards"),
            "line_yards_per_rush": obj.get("lineYardsPerRush"),
            "second_level_yards": obj.get("secondLevelYards"),
            "second_level_yards_per_rush": obj.get("secondLevelYardsPerRush"),
            "open_field_yards": obj.get("openFieldYards"),
            "open_field_yards_per_rush": obj.get("openFieldYardsPerRush"),
            "epa_per_play": obj.get("epaPerPlay"),
            "total_epa": obj.get("totalEpa"),
            "passing_epa": obj.get("passingEpa"),
            "epa_per_pass": obj.get("epaPerPass"),
            "rushing_epa": obj.get("rushingEpa"),
            "epa_per_rush": obj.get("epaPerRush"),
            "success_rate": obj.get("successRate"),
            "standard_down_success_rate": obj.get("standardDownSuccessRate"),
            "passing_down_success_rate": obj.get("passingDownSuccessRate"),
            "explosiveness": obj.get("explosiveness")
        })
        return _obj


