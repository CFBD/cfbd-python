# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr
from cfbd.models.player_game_predicted_points_added_average_ppa import PlayerGamePredictedPointsAddedAveragePPA
from cfbd.models.season_type import SeasonType

class PlayerGamePredictedPointsAdded(BaseModel):
    """
    PlayerGamePredictedPointsAdded
    """
    season: StrictInt = Field(...)
    week: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    position: StrictStr = Field(...)
    team: StrictStr = Field(...)
    opponent: StrictStr = Field(...)
    average_ppa: PlayerGamePredictedPointsAddedAveragePPA = Field(default=..., alias="averagePPA")
    __properties = ["season", "week", "seasonType", "id", "name", "position", "team", "opponent", "averagePPA"]

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
    def from_json(cls, json_str: str) -> PlayerGamePredictedPointsAdded:
        """Create an instance of PlayerGamePredictedPointsAdded from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of average_ppa
        if self.average_ppa:
            _dict['averagePPA'] = self.average_ppa.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerGamePredictedPointsAdded:
        """Create an instance of PlayerGamePredictedPointsAdded from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerGamePredictedPointsAdded.parse_obj(obj)

        _obj = PlayerGamePredictedPointsAdded.parse_obj({
            "season": obj.get("season"),
            "week": obj.get("week"),
            "season_type": obj.get("seasonType"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "position": obj.get("position"),
            "team": obj.get("team"),
            "opponent": obj.get("opponent"),
            "average_ppa": PlayerGamePredictedPointsAddedAveragePPA.from_dict(obj.get("averagePPA")) if obj.get("averagePPA") is not None else None
        })
        return _obj


