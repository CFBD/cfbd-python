# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.5.0
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

class AdvancedSeasonStatOffenseFieldPosition(BaseModel):
    """
    AdvancedSeasonStatOffenseFieldPosition
    """
    average_predicted_points: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="averagePredictedPoints")
    average_start: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="averageStart")
    __properties = ["averagePredictedPoints", "averageStart"]

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
    def from_json(cls, json_str: str) -> AdvancedSeasonStatOffenseFieldPosition:
        """Create an instance of AdvancedSeasonStatOffenseFieldPosition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if average_predicted_points (nullable) is None
        # and __fields_set__ contains the field
        if self.average_predicted_points is None and "average_predicted_points" in self.__fields_set__:
            _dict['averagePredictedPoints'] = None

        # set to None if average_start (nullable) is None
        # and __fields_set__ contains the field
        if self.average_start is None and "average_start" in self.__fields_set__:
            _dict['averageStart'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedSeasonStatOffenseFieldPosition:
        """Create an instance of AdvancedSeasonStatOffenseFieldPosition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedSeasonStatOffenseFieldPosition.parse_obj(obj)

        _obj = AdvancedSeasonStatOffenseFieldPosition.parse_obj({
            "average_predicted_points": obj.get("averagePredictedPoints"),
            "average_start": obj.get("averageStart")
        })
        return _obj


