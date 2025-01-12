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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class AggregatedTeamRecruiting(BaseModel):
    """
    AggregatedTeamRecruiting
    """
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    position_group: Optional[StrictStr] = Field(default=..., alias="positionGroup")
    average_rating: Union[StrictFloat, StrictInt] = Field(default=..., alias="averageRating")
    total_rating: Union[StrictFloat, StrictInt] = Field(default=..., alias="totalRating")
    commits: StrictInt = Field(...)
    average_stars: Union[StrictFloat, StrictInt] = Field(default=..., alias="averageStars")
    __properties = ["team", "conference", "positionGroup", "averageRating", "totalRating", "commits", "averageStars"]

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
    def from_json(cls, json_str: str) -> AggregatedTeamRecruiting:
        """Create an instance of AggregatedTeamRecruiting from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if position_group (nullable) is None
        # and __fields_set__ contains the field
        if self.position_group is None and "position_group" in self.__fields_set__:
            _dict['positionGroup'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AggregatedTeamRecruiting:
        """Create an instance of AggregatedTeamRecruiting from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AggregatedTeamRecruiting.parse_obj(obj)

        _obj = AggregatedTeamRecruiting.parse_obj({
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "position_group": obj.get("positionGroup"),
            "average_rating": obj.get("averageRating"),
            "total_rating": obj.get("totalRating"),
            "commits": obj.get("commits"),
            "average_stars": obj.get("averageStars")
        })
        return _obj


