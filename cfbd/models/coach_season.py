# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.5
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

class CoachSeason(BaseModel):
    """
    CoachSeason
    """
    school: StrictStr = Field(...)
    year: StrictInt = Field(...)
    games: StrictInt = Field(...)
    wins: StrictInt = Field(...)
    losses: StrictInt = Field(...)
    ties: StrictInt = Field(...)
    preseason_rank: Optional[StrictInt] = Field(default=..., alias="preseasonRank")
    postseason_rank: Optional[StrictInt] = Field(default=..., alias="postseasonRank")
    srs: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    sp_overall: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="spOverall")
    sp_offense: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="spOffense")
    sp_defense: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="spDefense")
    __properties = ["school", "year", "games", "wins", "losses", "ties", "preseasonRank", "postseasonRank", "srs", "spOverall", "spOffense", "spDefense"]

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
    def from_json(cls, json_str: str) -> CoachSeason:
        """Create an instance of CoachSeason from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if preseason_rank (nullable) is None
        # and __fields_set__ contains the field
        if self.preseason_rank is None and "preseason_rank" in self.__fields_set__:
            _dict['preseasonRank'] = None

        # set to None if postseason_rank (nullable) is None
        # and __fields_set__ contains the field
        if self.postseason_rank is None and "postseason_rank" in self.__fields_set__:
            _dict['postseasonRank'] = None

        # set to None if srs (nullable) is None
        # and __fields_set__ contains the field
        if self.srs is None and "srs" in self.__fields_set__:
            _dict['srs'] = None

        # set to None if sp_overall (nullable) is None
        # and __fields_set__ contains the field
        if self.sp_overall is None and "sp_overall" in self.__fields_set__:
            _dict['spOverall'] = None

        # set to None if sp_offense (nullable) is None
        # and __fields_set__ contains the field
        if self.sp_offense is None and "sp_offense" in self.__fields_set__:
            _dict['spOffense'] = None

        # set to None if sp_defense (nullable) is None
        # and __fields_set__ contains the field
        if self.sp_defense is None and "sp_defense" in self.__fields_set__:
            _dict['spDefense'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CoachSeason:
        """Create an instance of CoachSeason from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CoachSeason.parse_obj(obj)

        _obj = CoachSeason.parse_obj({
            "school": obj.get("school"),
            "year": obj.get("year"),
            "games": obj.get("games"),
            "wins": obj.get("wins"),
            "losses": obj.get("losses"),
            "ties": obj.get("ties"),
            "preseason_rank": obj.get("preseasonRank"),
            "postseason_rank": obj.get("postseasonRank"),
            "srs": obj.get("srs"),
            "sp_overall": obj.get("spOverall"),
            "sp_offense": obj.get("spOffense"),
            "sp_defense": obj.get("spDefense")
        })
        return _obj


