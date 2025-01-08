# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.4.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr
from cfbd.models.stats_by_quarter import StatsByQuarter

class TeamExplosiveness(BaseModel):
    """
    TeamExplosiveness
    """
    team: StrictStr = Field(...)
    overall: StatsByQuarter = Field(...)
    __properties = ["team", "overall"]

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
    def from_json(cls, json_str: str) -> TeamExplosiveness:
        """Create an instance of TeamExplosiveness from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of overall
        if self.overall:
            _dict['overall'] = self.overall.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamExplosiveness:
        """Create an instance of TeamExplosiveness from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamExplosiveness.parse_obj(obj)

        _obj = TeamExplosiveness.parse_obj({
            "team": obj.get("team"),
            "overall": StatsByQuarter.from_dict(obj.get("overall")) if obj.get("overall") is not None else None
        })
        return _obj


