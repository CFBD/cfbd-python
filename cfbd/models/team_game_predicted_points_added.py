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



from pydantic import BaseModel, Field, StrictInt, StrictStr
from cfbd.models.season_type import SeasonType
from cfbd.models.team_game_predicted_points_added_offense import TeamGamePredictedPointsAddedOffense

class TeamGamePredictedPointsAdded(BaseModel):
    """
    TeamGamePredictedPointsAdded
    """
    game_id: StrictInt = Field(default=..., alias="gameId")
    season: StrictInt = Field(...)
    week: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    opponent: StrictStr = Field(...)
    offense: TeamGamePredictedPointsAddedOffense = Field(...)
    defense: TeamGamePredictedPointsAddedOffense = Field(...)
    __properties = ["gameId", "season", "week", "seasonType", "team", "conference", "opponent", "offense", "defense"]

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
    def from_json(cls, json_str: str) -> TeamGamePredictedPointsAdded:
        """Create an instance of TeamGamePredictedPointsAdded from a JSON string"""
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
    def from_dict(cls, obj: dict) -> TeamGamePredictedPointsAdded:
        """Create an instance of TeamGamePredictedPointsAdded from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamGamePredictedPointsAdded.parse_obj(obj)

        _obj = TeamGamePredictedPointsAdded.parse_obj({
            "game_id": obj.get("gameId"),
            "season": obj.get("season"),
            "week": obj.get("week"),
            "season_type": obj.get("seasonType"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "opponent": obj.get("opponent"),
            "offense": TeamGamePredictedPointsAddedOffense.from_dict(obj.get("offense")) if obj.get("offense") is not None else None,
            "defense": TeamGamePredictedPointsAddedOffense.from_dict(obj.get("defense")) if obj.get("defense") is not None else None
        })
        return _obj


