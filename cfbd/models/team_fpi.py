# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.4
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
from cfbd.models.team_fpi_efficiencies import TeamFPIEfficiencies
from cfbd.models.team_fpi_resume_ranks import TeamFPIResumeRanks

class TeamFPI(BaseModel):
    """
    TeamFPI
    """
    year: StrictInt = Field(...)
    team: StrictStr = Field(...)
    conference: Optional[StrictStr] = Field(...)
    fpi: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    resume_ranks: TeamFPIResumeRanks = Field(default=..., alias="resumeRanks")
    efficiencies: TeamFPIEfficiencies = Field(...)
    __properties = ["year", "team", "conference", "fpi", "resumeRanks", "efficiencies"]

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
    def from_json(cls, json_str: str) -> TeamFPI:
        """Create an instance of TeamFPI from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of resume_ranks
        if self.resume_ranks:
            _dict['resumeRanks'] = self.resume_ranks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of efficiencies
        if self.efficiencies:
            _dict['efficiencies'] = self.efficiencies.to_dict()
        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if fpi (nullable) is None
        # and __fields_set__ contains the field
        if self.fpi is None and "fpi" in self.__fields_set__:
            _dict['fpi'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamFPI:
        """Create an instance of TeamFPI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamFPI.parse_obj(obj)

        _obj = TeamFPI.parse_obj({
            "year": obj.get("year"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "fpi": obj.get("fpi"),
            "resume_ranks": TeamFPIResumeRanks.from_dict(obj.get("resumeRanks")) if obj.get("resumeRanks") is not None else None,
            "efficiencies": TeamFPIEfficiencies.from_dict(obj.get("efficiencies")) if obj.get("efficiencies") is not None else None
        })
        return _obj


