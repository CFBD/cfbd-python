# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class PlayerGamePredictedPointsAddedAveragePPA(BaseModel):
    """
    PlayerGamePredictedPointsAddedAveragePPA
    """
    rush: Optional[Union[StrictFloat, StrictInt]] = None
    var_pass: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pass")
    all: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["rush", "pass", "all"]

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
    def from_json(cls, json_str: str) -> PlayerGamePredictedPointsAddedAveragePPA:
        """Create an instance of PlayerGamePredictedPointsAddedAveragePPA from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerGamePredictedPointsAddedAveragePPA:
        """Create an instance of PlayerGamePredictedPointsAddedAveragePPA from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerGamePredictedPointsAddedAveragePPA.parse_obj(obj)

        _obj = PlayerGamePredictedPointsAddedAveragePPA.parse_obj({
            "rush": obj.get("rush"),
            "var_pass": obj.get("pass"),
            "all": obj.get("all")
        })
        return _obj


