# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.18
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

class TeamSRS(BaseModel):
    """
    TeamSRS
    """
    year: StrictInt = Field(...)
    team: StrictStr = Field(...)
    conference: Optional[StrictStr] = Field(...)
    division: Optional[StrictStr] = Field(...)
    rating: Union[StrictFloat, StrictInt] = Field(...)
    ranking: Optional[StrictInt] = Field(...)
    __properties = ["year", "team", "conference", "division", "rating", "ranking"]

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
    def from_json(cls, json_str: str) -> TeamSRS:
        """Create an instance of TeamSRS from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if division (nullable) is None
        # and __fields_set__ contains the field
        if self.division is None and "division" in self.__fields_set__:
            _dict['division'] = None

        # set to None if ranking (nullable) is None
        # and __fields_set__ contains the field
        if self.ranking is None and "ranking" in self.__fields_set__:
            _dict['ranking'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamSRS:
        """Create an instance of TeamSRS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamSRS.parse_obj(obj)

        _obj = TeamSRS.parse_obj({
            "year": obj.get("year"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "division": obj.get("division"),
            "rating": obj.get("rating"),
            "ranking": obj.get("ranking")
        })
        return _obj


