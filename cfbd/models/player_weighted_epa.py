# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.2
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

class PlayerWeightedEPA(BaseModel):
    """
    PlayerWeightedEPA
    """
    year: StrictInt = Field(...)
    athlete_id: StrictStr = Field(default=..., alias="athleteId")
    athlete_name: StrictStr = Field(default=..., alias="athleteName")
    position: StrictStr = Field(...)
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    wepa: Union[StrictFloat, StrictInt] = Field(...)
    plays: StrictInt = Field(...)
    __properties = ["year", "athleteId", "athleteName", "position", "team", "conference", "wepa", "plays"]

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
    def from_json(cls, json_str: str) -> PlayerWeightedEPA:
        """Create an instance of PlayerWeightedEPA from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerWeightedEPA:
        """Create an instance of PlayerWeightedEPA from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerWeightedEPA.parse_obj(obj)

        _obj = PlayerWeightedEPA.parse_obj({
            "year": obj.get("year"),
            "athlete_id": obj.get("athleteId"),
            "athlete_name": obj.get("athleteName"),
            "position": obj.get("position"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "wepa": obj.get("wepa"),
            "plays": obj.get("plays")
        })
        return _obj


