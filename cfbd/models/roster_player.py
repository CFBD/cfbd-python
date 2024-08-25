# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.15
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist

class RosterPlayer(BaseModel):
    """
    RosterPlayer
    """
    id: StrictStr = Field(...)
    first_name: StrictStr = Field(default=..., alias="firstName")
    last_name: StrictStr = Field(default=..., alias="lastName")
    team: StrictStr = Field(...)
    height: Optional[StrictInt] = Field(...)
    weight: Optional[StrictInt] = Field(...)
    jersey: Optional[StrictInt] = Field(...)
    year: StrictInt = Field(...)
    position: Optional[StrictStr] = Field(...)
    home_city: Optional[StrictStr] = Field(default=..., alias="homeCity")
    home_state: Optional[StrictStr] = Field(default=..., alias="homeState")
    home_country: Optional[StrictStr] = Field(default=..., alias="homeCountry")
    home_latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="homeLatitude")
    home_longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="homeLongitude")
    home_county_fips: Optional[StrictStr] = Field(default=..., alias="homeCountyFIPS")
    recruit_ids: Optional[conlist(StrictStr)] = Field(default=..., alias="recruitIds")
    __properties = ["id", "firstName", "lastName", "team", "height", "weight", "jersey", "year", "position", "homeCity", "homeState", "homeCountry", "homeLatitude", "homeLongitude", "homeCountyFIPS", "recruitIds"]

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
    def from_json(cls, json_str: str) -> RosterPlayer:
        """Create an instance of RosterPlayer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if height (nullable) is None
        # and __fields_set__ contains the field
        if self.height is None and "height" in self.__fields_set__:
            _dict['height'] = None

        # set to None if weight (nullable) is None
        # and __fields_set__ contains the field
        if self.weight is None and "weight" in self.__fields_set__:
            _dict['weight'] = None

        # set to None if jersey (nullable) is None
        # and __fields_set__ contains the field
        if self.jersey is None and "jersey" in self.__fields_set__:
            _dict['jersey'] = None

        # set to None if position (nullable) is None
        # and __fields_set__ contains the field
        if self.position is None and "position" in self.__fields_set__:
            _dict['position'] = None

        # set to None if home_city (nullable) is None
        # and __fields_set__ contains the field
        if self.home_city is None and "home_city" in self.__fields_set__:
            _dict['homeCity'] = None

        # set to None if home_state (nullable) is None
        # and __fields_set__ contains the field
        if self.home_state is None and "home_state" in self.__fields_set__:
            _dict['homeState'] = None

        # set to None if home_country (nullable) is None
        # and __fields_set__ contains the field
        if self.home_country is None and "home_country" in self.__fields_set__:
            _dict['homeCountry'] = None

        # set to None if home_latitude (nullable) is None
        # and __fields_set__ contains the field
        if self.home_latitude is None and "home_latitude" in self.__fields_set__:
            _dict['homeLatitude'] = None

        # set to None if home_longitude (nullable) is None
        # and __fields_set__ contains the field
        if self.home_longitude is None and "home_longitude" in self.__fields_set__:
            _dict['homeLongitude'] = None

        # set to None if home_county_fips (nullable) is None
        # and __fields_set__ contains the field
        if self.home_county_fips is None and "home_county_fips" in self.__fields_set__:
            _dict['homeCountyFIPS'] = None

        # set to None if recruit_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.recruit_ids is None and "recruit_ids" in self.__fields_set__:
            _dict['recruitIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RosterPlayer:
        """Create an instance of RosterPlayer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RosterPlayer.parse_obj(obj)

        _obj = RosterPlayer.parse_obj({
            "id": obj.get("id"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "team": obj.get("team"),
            "height": obj.get("height"),
            "weight": obj.get("weight"),
            "jersey": obj.get("jersey"),
            "year": obj.get("year"),
            "position": obj.get("position"),
            "home_city": obj.get("homeCity"),
            "home_state": obj.get("homeState"),
            "home_country": obj.get("homeCountry"),
            "home_latitude": obj.get("homeLatitude"),
            "home_longitude": obj.get("homeLongitude"),
            "home_county_fips": obj.get("homeCountyFIPS"),
            "recruit_ids": obj.get("recruitIds")
        })
        return _obj


