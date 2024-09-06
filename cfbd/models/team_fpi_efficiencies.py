# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.18
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

class TeamFPIEfficiencies(BaseModel):
    """
    TeamFPIEfficiencies
    """
    special_teams: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="specialTeams")
    defense: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    offense: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    overall: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["specialTeams", "defense", "offense", "overall"]

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
    def from_json(cls, json_str: str) -> TeamFPIEfficiencies:
        """Create an instance of TeamFPIEfficiencies from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if special_teams (nullable) is None
        # and __fields_set__ contains the field
        if self.special_teams is None and "special_teams" in self.__fields_set__:
            _dict['specialTeams'] = None

        # set to None if defense (nullable) is None
        # and __fields_set__ contains the field
        if self.defense is None and "defense" in self.__fields_set__:
            _dict['defense'] = None

        # set to None if offense (nullable) is None
        # and __fields_set__ contains the field
        if self.offense is None and "offense" in self.__fields_set__:
            _dict['offense'] = None

        # set to None if overall (nullable) is None
        # and __fields_set__ contains the field
        if self.overall is None and "overall" in self.__fields_set__:
            _dict['overall'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamFPIEfficiencies:
        """Create an instance of TeamFPIEfficiencies from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamFPIEfficiencies.parse_obj(obj)

        _obj = TeamFPIEfficiencies.parse_obj({
            "special_teams": obj.get("specialTeams"),
            "defense": obj.get("defense"),
            "offense": obj.get("offense"),
            "overall": obj.get("overall")
        })
        return _obj


