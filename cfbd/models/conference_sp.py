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
from cfbd.models.conference_sp_defense import ConferenceSPDefense
from cfbd.models.conference_sp_offense import ConferenceSPOffense
from cfbd.models.team_sp_special_teams import TeamSPSpecialTeams

class ConferenceSP(BaseModel):
    """
    ConferenceSP
    """
    year: StrictInt = Field(...)
    conference: StrictStr = Field(...)
    rating: Union[StrictFloat, StrictInt] = Field(...)
    second_order_wins: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="secondOrderWins")
    sos: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    offense: ConferenceSPOffense = Field(...)
    defense: ConferenceSPDefense = Field(...)
    special_teams: TeamSPSpecialTeams = Field(default=..., alias="specialTeams")
    __properties = ["year", "conference", "rating", "secondOrderWins", "sos", "offense", "defense", "specialTeams"]

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
    def from_json(cls, json_str: str) -> ConferenceSP:
        """Create an instance of ConferenceSP from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of offense
        if self.offense:
            _dict['offense'] = self.offense.to_dict()
        # override the default output from pydantic by calling `to_dict()` of defense
        if self.defense:
            _dict['defense'] = self.defense.to_dict()
        # override the default output from pydantic by calling `to_dict()` of special_teams
        if self.special_teams:
            _dict['specialTeams'] = self.special_teams.to_dict()
        # set to None if second_order_wins (nullable) is None
        # and __fields_set__ contains the field
        if self.second_order_wins is None and "second_order_wins" in self.__fields_set__:
            _dict['secondOrderWins'] = None

        # set to None if sos (nullable) is None
        # and __fields_set__ contains the field
        if self.sos is None and "sos" in self.__fields_set__:
            _dict['sos'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConferenceSP:
        """Create an instance of ConferenceSP from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConferenceSP.parse_obj(obj)

        _obj = ConferenceSP.parse_obj({
            "year": obj.get("year"),
            "conference": obj.get("conference"),
            "rating": obj.get("rating"),
            "second_order_wins": obj.get("secondOrderWins"),
            "sos": obj.get("sos"),
            "offense": ConferenceSPOffense.from_dict(obj.get("offense")) if obj.get("offense") is not None else None,
            "defense": ConferenceSPDefense.from_dict(obj.get("defense")) if obj.get("defense") is not None else None,
            "special_teams": TeamSPSpecialTeams.from_dict(obj.get("specialTeams")) if obj.get("specialTeams") is not None else None
        })
        return _obj


