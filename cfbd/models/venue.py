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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class Venue(BaseModel):
    """
    Venue
    """
    id: Optional[StrictInt] = Field(...)
    name: Optional[StrictStr] = Field(...)
    city: Optional[StrictStr] = Field(...)
    state: Optional[StrictStr] = Field(...)
    zip: Optional[StrictStr] = Field(...)
    country_code: Optional[StrictStr] = Field(default=..., alias="countryCode")
    timezone: Optional[StrictStr] = Field(...)
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    elevation: Optional[StrictStr] = Field(...)
    capacity: Optional[StrictInt] = Field(...)
    construction_year: Optional[StrictInt] = Field(default=..., alias="constructionYear")
    grass: Optional[StrictBool] = None
    dome: Optional[StrictBool] = None
    __properties = ["id", "name", "city", "state", "zip", "countryCode", "timezone", "latitude", "longitude", "elevation", "capacity", "constructionYear", "grass", "dome"]

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
    def from_json(cls, json_str: str) -> Venue:
        """Create an instance of Venue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if city (nullable) is None
        # and __fields_set__ contains the field
        if self.city is None and "city" in self.__fields_set__:
            _dict['city'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        # set to None if zip (nullable) is None
        # and __fields_set__ contains the field
        if self.zip is None and "zip" in self.__fields_set__:
            _dict['zip'] = None

        # set to None if country_code (nullable) is None
        # and __fields_set__ contains the field
        if self.country_code is None and "country_code" in self.__fields_set__:
            _dict['countryCode'] = None

        # set to None if timezone (nullable) is None
        # and __fields_set__ contains the field
        if self.timezone is None and "timezone" in self.__fields_set__:
            _dict['timezone'] = None

        # set to None if latitude (nullable) is None
        # and __fields_set__ contains the field
        if self.latitude is None and "latitude" in self.__fields_set__:
            _dict['latitude'] = None

        # set to None if longitude (nullable) is None
        # and __fields_set__ contains the field
        if self.longitude is None and "longitude" in self.__fields_set__:
            _dict['longitude'] = None

        # set to None if elevation (nullable) is None
        # and __fields_set__ contains the field
        if self.elevation is None and "elevation" in self.__fields_set__:
            _dict['elevation'] = None

        # set to None if capacity (nullable) is None
        # and __fields_set__ contains the field
        if self.capacity is None and "capacity" in self.__fields_set__:
            _dict['capacity'] = None

        # set to None if construction_year (nullable) is None
        # and __fields_set__ contains the field
        if self.construction_year is None and "construction_year" in self.__fields_set__:
            _dict['constructionYear'] = None

        # set to None if grass (nullable) is None
        # and __fields_set__ contains the field
        if self.grass is None and "grass" in self.__fields_set__:
            _dict['grass'] = None

        # set to None if dome (nullable) is None
        # and __fields_set__ contains the field
        if self.dome is None and "dome" in self.__fields_set__:
            _dict['dome'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Venue:
        """Create an instance of Venue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Venue.parse_obj(obj)

        _obj = Venue.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "zip": obj.get("zip"),
            "country_code": obj.get("countryCode"),
            "timezone": obj.get("timezone"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "elevation": obj.get("elevation"),
            "capacity": obj.get("capacity"),
            "construction_year": obj.get("constructionYear"),
            "grass": obj.get("grass"),
            "dome": obj.get("dome")
        })
        return _obj


