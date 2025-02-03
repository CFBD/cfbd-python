# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.9
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr
from cfbd.models.team_stat_stat_value import TeamStatStatValue

class TeamStat(BaseModel):
    """
    TeamStat
    """
    season: StrictInt = Field(...)
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    stat_name: StrictStr = Field(default=..., alias="statName")
    stat_value: TeamStatStatValue = Field(default=..., alias="statValue")
    __properties = ["season", "team", "conference", "statName", "statValue"]

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
    def from_json(cls, json_str: str) -> TeamStat:
        """Create an instance of TeamStat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of stat_value
        if self.stat_value:
            _dict['statValue'] = self.stat_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamStat:
        """Create an instance of TeamStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamStat.parse_obj(obj)

        _obj = TeamStat.parse_obj({
            "season": obj.get("season"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "stat_name": obj.get("statName"),
            "stat_value": TeamStatStatValue.from_dict(obj.get("statValue")) if obj.get("statValue") is not None else None
        })
        return _obj


