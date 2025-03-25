# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.9
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr
from cfbd.models.player_usage_usage import PlayerUsageUsage

class PlayerUsage(BaseModel):
    """
    PlayerUsage
    """
    season: StrictInt = Field(...)
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    position: StrictStr = Field(...)
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    usage: PlayerUsageUsage = Field(...)
    __properties = ["season", "id", "name", "position", "team", "conference", "usage"]

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
    def from_json(cls, json_str: str) -> PlayerUsage:
        """Create an instance of PlayerUsage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of usage
        if self.usage:
            _dict['usage'] = self.usage.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerUsage:
        """Create an instance of PlayerUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerUsage.parse_obj(obj)

        _obj = PlayerUsage.parse_obj({
            "season": obj.get("season"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "position": obj.get("position"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "usage": PlayerUsageUsage.from_dict(obj.get("usage")) if obj.get("usage") is not None else None
        })
        return _obj


