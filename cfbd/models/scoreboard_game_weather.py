# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.17
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

class ScoreboardGameWeather(BaseModel):
    """
    ScoreboardGameWeather
    """
    wind_direction: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="windDirection")
    wind_speed: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="windSpeed")
    description: Optional[StrictStr] = Field(...)
    temperature: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["windDirection", "windSpeed", "description", "temperature"]

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
    def from_json(cls, json_str: str) -> ScoreboardGameWeather:
        """Create an instance of ScoreboardGameWeather from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if wind_direction (nullable) is None
        # and __fields_set__ contains the field
        if self.wind_direction is None and "wind_direction" in self.__fields_set__:
            _dict['windDirection'] = None

        # set to None if wind_speed (nullable) is None
        # and __fields_set__ contains the field
        if self.wind_speed is None and "wind_speed" in self.__fields_set__:
            _dict['windSpeed'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if temperature (nullable) is None
        # and __fields_set__ contains the field
        if self.temperature is None and "temperature" in self.__fields_set__:
            _dict['temperature'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScoreboardGameWeather:
        """Create an instance of ScoreboardGameWeather from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScoreboardGameWeather.parse_obj(obj)

        _obj = ScoreboardGameWeather.parse_obj({
            "wind_direction": obj.get("windDirection"),
            "wind_speed": obj.get("windSpeed"),
            "description": obj.get("description"),
            "temperature": obj.get("temperature")
        })
        return _obj


