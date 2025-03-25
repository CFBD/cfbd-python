# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.9
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from cfbd.models.division_classification import DivisionClassification

class ScoreboardGameHomeTeam(BaseModel):
    """
    ScoreboardGameHomeTeam
    """
    line_scores: Optional[conlist(StrictInt)] = Field(default=..., alias="lineScores")
    points: Optional[StrictInt] = Field(...)
    classification: Optional[DivisionClassification] = Field(...)
    conference: Optional[StrictStr] = Field(...)
    name: StrictStr = Field(...)
    id: StrictInt = Field(...)
    __properties = ["lineScores", "points", "classification", "conference", "name", "id"]

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
    def from_json(cls, json_str: str) -> ScoreboardGameHomeTeam:
        """Create an instance of ScoreboardGameHomeTeam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if line_scores (nullable) is None
        # and __fields_set__ contains the field
        if self.line_scores is None and "line_scores" in self.__fields_set__:
            _dict['lineScores'] = None

        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        # set to None if classification (nullable) is None
        # and __fields_set__ contains the field
        if self.classification is None and "classification" in self.__fields_set__:
            _dict['classification'] = None

        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScoreboardGameHomeTeam:
        """Create an instance of ScoreboardGameHomeTeam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScoreboardGameHomeTeam.parse_obj(obj)

        _obj = ScoreboardGameHomeTeam.parse_obj({
            "line_scores": obj.get("lineScores"),
            "points": obj.get("points"),
            "classification": obj.get("classification"),
            "conference": obj.get("conference"),
            "name": obj.get("name"),
            "id": obj.get("id")
        })
        return _obj


