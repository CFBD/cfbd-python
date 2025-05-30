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

class RecruitHometownInfo(BaseModel):
    """
    RecruitHometownInfo
    """
    fips_code: Optional[StrictStr] = Field(default=..., alias="fipsCode")
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["fipsCode", "longitude", "latitude"]

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
    def from_json(cls, json_str: str) -> RecruitHometownInfo:
        """Create an instance of RecruitHometownInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if fips_code (nullable) is None
        # and __fields_set__ contains the field
        if self.fips_code is None and "fips_code" in self.__fields_set__:
            _dict['fipsCode'] = None

        # set to None if longitude (nullable) is None
        # and __fields_set__ contains the field
        if self.longitude is None and "longitude" in self.__fields_set__:
            _dict['longitude'] = None

        # set to None if latitude (nullable) is None
        # and __fields_set__ contains the field
        if self.latitude is None and "latitude" in self.__fields_set__:
            _dict['latitude'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RecruitHometownInfo:
        """Create an instance of RecruitHometownInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RecruitHometownInfo.parse_obj(obj)

        _obj = RecruitHometownInfo.parse_obj({
            "fips_code": obj.get("fipsCode"),
            "longitude": obj.get("longitude"),
            "latitude": obj.get("latitude")
        })
        return _obj


