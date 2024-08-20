# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.10
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
from cfbd.models.team_season_predicted_points_added_offense_cumulative import TeamSeasonPredictedPointsAddedOffenseCumulative

class TeamSeasonPredictedPointsAddedOffense(BaseModel):
    """
    TeamSeasonPredictedPointsAddedOffense
    """
    cumulative: TeamSeasonPredictedPointsAddedOffenseCumulative = Field(...)
    third_down: Union[StrictFloat, StrictInt] = Field(default=..., alias="thirdDown")
    second_down: Union[StrictFloat, StrictInt] = Field(default=..., alias="secondDown")
    first_down: Union[StrictFloat, StrictInt] = Field(default=..., alias="firstDown")
    rushing: Union[StrictFloat, StrictInt] = Field(...)
    passing: Union[StrictFloat, StrictInt] = Field(...)
    overall: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["cumulative", "thirdDown", "secondDown", "firstDown", "rushing", "passing", "overall"]

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
    def from_json(cls, json_str: str) -> TeamSeasonPredictedPointsAddedOffense:
        """Create an instance of TeamSeasonPredictedPointsAddedOffense from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cumulative
        if self.cumulative:
            _dict['cumulative'] = self.cumulative.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamSeasonPredictedPointsAddedOffense:
        """Create an instance of TeamSeasonPredictedPointsAddedOffense from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamSeasonPredictedPointsAddedOffense.parse_obj(obj)

        _obj = TeamSeasonPredictedPointsAddedOffense.parse_obj({
            "cumulative": TeamSeasonPredictedPointsAddedOffenseCumulative.from_dict(obj.get("cumulative")) if obj.get("cumulative") is not None else None,
            "third_down": obj.get("thirdDown"),
            "second_down": obj.get("secondDown"),
            "first_down": obj.get("firstDown"),
            "rushing": obj.get("rushing"),
            "passing": obj.get("passing"),
            "overall": obj.get("overall")
        })
        return _obj

