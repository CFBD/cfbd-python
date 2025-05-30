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

class PlayerGameUsage(BaseModel):
    """
    PlayerGameUsage
    """
    total: Union[StrictFloat, StrictInt] = Field(...)
    quarter1: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    quarter2: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    quarter3: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    quarter4: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    rushing: Union[StrictFloat, StrictInt] = Field(...)
    passing: Union[StrictFloat, StrictInt] = Field(...)
    player: StrictStr = Field(...)
    team: StrictStr = Field(...)
    position: StrictStr = Field(...)
    __properties = ["total", "quarter1", "quarter2", "quarter3", "quarter4", "rushing", "passing", "player", "team", "position"]

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
    def from_json(cls, json_str: str) -> PlayerGameUsage:
        """Create an instance of PlayerGameUsage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if quarter1 (nullable) is None
        # and __fields_set__ contains the field
        if self.quarter1 is None and "quarter1" in self.__fields_set__:
            _dict['quarter1'] = None

        # set to None if quarter2 (nullable) is None
        # and __fields_set__ contains the field
        if self.quarter2 is None and "quarter2" in self.__fields_set__:
            _dict['quarter2'] = None

        # set to None if quarter3 (nullable) is None
        # and __fields_set__ contains the field
        if self.quarter3 is None and "quarter3" in self.__fields_set__:
            _dict['quarter3'] = None

        # set to None if quarter4 (nullable) is None
        # and __fields_set__ contains the field
        if self.quarter4 is None and "quarter4" in self.__fields_set__:
            _dict['quarter4'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerGameUsage:
        """Create an instance of PlayerGameUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerGameUsage.parse_obj(obj)

        _obj = PlayerGameUsage.parse_obj({
            "total": obj.get("total"),
            "quarter1": obj.get("quarter1"),
            "quarter2": obj.get("quarter2"),
            "quarter3": obj.get("quarter3"),
            "quarter4": obj.get("quarter4"),
            "rushing": obj.get("rushing"),
            "passing": obj.get("passing"),
            "player": obj.get("player"),
            "team": obj.get("team"),
            "position": obj.get("position")
        })
        return _obj


