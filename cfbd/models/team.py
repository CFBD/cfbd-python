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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from cfbd.models.venue import Venue

class Team(BaseModel):
    """
    Team
    """
    id: StrictInt = Field(...)
    school: StrictStr = Field(...)
    mascot: Optional[StrictStr] = Field(...)
    abbreviation: Optional[StrictStr] = Field(...)
    alternate_names: Optional[conlist(StrictStr)] = Field(default=..., alias="alternateNames")
    conference: Optional[StrictStr] = Field(...)
    division: Optional[StrictStr] = Field(...)
    classification: Optional[StrictStr] = Field(...)
    color: Optional[StrictStr] = Field(...)
    alternate_color: Optional[StrictStr] = Field(default=..., alias="alternateColor")
    logos: Optional[conlist(StrictStr)] = Field(...)
    twitter: Optional[StrictStr] = Field(...)
    location: Optional[Venue] = Field(...)
    __properties = ["id", "school", "mascot", "abbreviation", "alternateNames", "conference", "division", "classification", "color", "alternateColor", "logos", "twitter", "location"]

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
    def from_json(cls, json_str: str) -> Team:
        """Create an instance of Team from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # set to None if mascot (nullable) is None
        # and __fields_set__ contains the field
        if self.mascot is None and "mascot" in self.__fields_set__:
            _dict['mascot'] = None

        # set to None if abbreviation (nullable) is None
        # and __fields_set__ contains the field
        if self.abbreviation is None and "abbreviation" in self.__fields_set__:
            _dict['abbreviation'] = None

        # set to None if alternate_names (nullable) is None
        # and __fields_set__ contains the field
        if self.alternate_names is None and "alternate_names" in self.__fields_set__:
            _dict['alternateNames'] = None

        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if division (nullable) is None
        # and __fields_set__ contains the field
        if self.division is None and "division" in self.__fields_set__:
            _dict['division'] = None

        # set to None if classification (nullable) is None
        # and __fields_set__ contains the field
        if self.classification is None and "classification" in self.__fields_set__:
            _dict['classification'] = None

        # set to None if color (nullable) is None
        # and __fields_set__ contains the field
        if self.color is None and "color" in self.__fields_set__:
            _dict['color'] = None

        # set to None if alternate_color (nullable) is None
        # and __fields_set__ contains the field
        if self.alternate_color is None and "alternate_color" in self.__fields_set__:
            _dict['alternateColor'] = None

        # set to None if logos (nullable) is None
        # and __fields_set__ contains the field
        if self.logos is None and "logos" in self.__fields_set__:
            _dict['logos'] = None

        # set to None if twitter (nullable) is None
        # and __fields_set__ contains the field
        if self.twitter is None and "twitter" in self.__fields_set__:
            _dict['twitter'] = None

        # set to None if location (nullable) is None
        # and __fields_set__ contains the field
        if self.location is None and "location" in self.__fields_set__:
            _dict['location'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Team:
        """Create an instance of Team from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Team.parse_obj(obj)

        _obj = Team.parse_obj({
            "id": obj.get("id"),
            "school": obj.get("school"),
            "mascot": obj.get("mascot"),
            "abbreviation": obj.get("abbreviation"),
            "alternate_names": obj.get("alternateNames"),
            "conference": obj.get("conference"),
            "division": obj.get("division"),
            "classification": obj.get("classification"),
            "color": obj.get("color"),
            "alternate_color": obj.get("alternateColor"),
            "logos": obj.get("logos"),
            "twitter": obj.get("twitter"),
            "location": Venue.from_dict(obj.get("location")) if obj.get("location") is not None else None
        })
        return _obj


