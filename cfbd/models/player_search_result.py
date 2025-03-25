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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class PlayerSearchResult(BaseModel):
    """
    PlayerSearchResult
    """
    id: StrictStr = Field(...)
    team: StrictStr = Field(...)
    name: StrictStr = Field(...)
    first_name: Optional[StrictStr] = Field(default=..., alias="firstName")
    last_name: Optional[StrictStr] = Field(default=..., alias="lastName")
    weight: Optional[StrictInt] = Field(...)
    height: Optional[StrictInt] = Field(...)
    jersey: Optional[StrictInt] = Field(...)
    position: StrictStr = Field(...)
    hometown: StrictStr = Field(...)
    team_color: StrictStr = Field(default=..., alias="teamColor")
    team_color_secondary: StrictStr = Field(default=..., alias="teamColorSecondary")
    __properties = ["id", "team", "name", "firstName", "lastName", "weight", "height", "jersey", "position", "hometown", "teamColor", "teamColorSecondary"]

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
    def from_json(cls, json_str: str) -> PlayerSearchResult:
        """Create an instance of PlayerSearchResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if first_name (nullable) is None
        # and __fields_set__ contains the field
        if self.first_name is None and "first_name" in self.__fields_set__:
            _dict['firstName'] = None

        # set to None if last_name (nullable) is None
        # and __fields_set__ contains the field
        if self.last_name is None and "last_name" in self.__fields_set__:
            _dict['lastName'] = None

        # set to None if weight (nullable) is None
        # and __fields_set__ contains the field
        if self.weight is None and "weight" in self.__fields_set__:
            _dict['weight'] = None

        # set to None if height (nullable) is None
        # and __fields_set__ contains the field
        if self.height is None and "height" in self.__fields_set__:
            _dict['height'] = None

        # set to None if jersey (nullable) is None
        # and __fields_set__ contains the field
        if self.jersey is None and "jersey" in self.__fields_set__:
            _dict['jersey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerSearchResult:
        """Create an instance of PlayerSearchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerSearchResult.parse_obj(obj)

        _obj = PlayerSearchResult.parse_obj({
            "id": obj.get("id"),
            "team": obj.get("team"),
            "name": obj.get("name"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "weight": obj.get("weight"),
            "height": obj.get("height"),
            "jersey": obj.get("jersey"),
            "position": obj.get("position"),
            "hometown": obj.get("hometown"),
            "team_color": obj.get("teamColor"),
            "team_color_secondary": obj.get("teamColorSecondary")
        })
        return _obj


