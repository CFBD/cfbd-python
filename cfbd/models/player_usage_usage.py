# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.8
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class PlayerUsageUsage(BaseModel):
    """
    PlayerUsageUsage
    """
    passing_downs: Union[StrictFloat, StrictInt] = Field(default=..., alias="passingDowns")
    standard_downs: Union[StrictFloat, StrictInt] = Field(default=..., alias="standardDowns")
    third_down: Union[StrictFloat, StrictInt] = Field(default=..., alias="thirdDown")
    second_down: Union[StrictFloat, StrictInt] = Field(default=..., alias="secondDown")
    first_down: Union[StrictFloat, StrictInt] = Field(default=..., alias="firstDown")
    rush: Union[StrictFloat, StrictInt] = Field(...)
    var_pass: Union[StrictFloat, StrictInt] = Field(default=..., alias="pass")
    overall: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["passingDowns", "standardDowns", "thirdDown", "secondDown", "firstDown", "rush", "pass", "overall"]

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
    def from_json(cls, json_str: str) -> PlayerUsageUsage:
        """Create an instance of PlayerUsageUsage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerUsageUsage:
        """Create an instance of PlayerUsageUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerUsageUsage.parse_obj(obj)

        _obj = PlayerUsageUsage.parse_obj({
            "passing_downs": obj.get("passingDowns"),
            "standard_downs": obj.get("standardDowns"),
            "third_down": obj.get("thirdDown"),
            "second_down": obj.get("secondDown"),
            "first_down": obj.get("firstDown"),
            "rush": obj.get("rush"),
            "var_pass": obj.get("pass"),
            "overall": obj.get("overall")
        })
        return _obj


