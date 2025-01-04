# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr
from cfbd.models.advanced_season_stat_defense import AdvancedSeasonStatDefense
from cfbd.models.advanced_season_stat_offense import AdvancedSeasonStatOffense

class AdvancedSeasonStat(BaseModel):
    """
    AdvancedSeasonStat
    """
    season: StrictInt = Field(...)
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    offense: AdvancedSeasonStatOffense = Field(...)
    defense: AdvancedSeasonStatDefense = Field(...)
    __properties = ["season", "team", "conference", "offense", "defense"]

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
    def from_json(cls, json_str: str) -> AdvancedSeasonStat:
        """Create an instance of AdvancedSeasonStat from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedSeasonStat:
        """Create an instance of AdvancedSeasonStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedSeasonStat.parse_obj(obj)

        _obj = AdvancedSeasonStat.parse_obj({
            "season": obj.get("season"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "offense": AdvancedSeasonStatOffense.from_dict(obj.get("offense")) if obj.get("offense") is not None else None,
            "defense": AdvancedSeasonStatDefense.from_dict(obj.get("defense")) if obj.get("defense") is not None else None
        })
        return _obj


