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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from cfbd.models.live_game_play import LiveGamePlay

class LiveGameDrive(BaseModel):
    """
    LiveGameDrive
    """
    id: StrictStr = Field(...)
    offense_id: StrictInt = Field(default=..., alias="offenseId")
    offense: StrictStr = Field(...)
    defense_id: StrictInt = Field(default=..., alias="defenseId")
    defense: StrictStr = Field(...)
    play_count: StrictInt = Field(default=..., alias="playCount")
    yards: StrictInt = Field(...)
    start_period: StrictInt = Field(default=..., alias="startPeriod")
    start_clock: Optional[StrictStr] = Field(default=..., alias="startClock")
    start_yards_to_goal: StrictInt = Field(default=..., alias="startYardsToGoal")
    end_period: Optional[StrictInt] = Field(default=..., alias="endPeriod")
    end_clock: Optional[StrictStr] = Field(default=..., alias="endClock")
    end_yards_to_goal: Optional[StrictInt] = Field(default=..., alias="endYardsToGoal")
    duration: Optional[StrictStr] = Field(...)
    scoring_opportunity: StrictBool = Field(default=..., alias="scoringOpportunity")
    result: StrictStr = Field(...)
    points_gained: StrictInt = Field(default=..., alias="pointsGained")
    plays: conlist(LiveGamePlay) = Field(...)
    __properties = ["id", "offenseId", "offense", "defenseId", "defense", "playCount", "yards", "startPeriod", "startClock", "startYardsToGoal", "endPeriod", "endClock", "endYardsToGoal", "duration", "scoringOpportunity", "result", "pointsGained", "plays"]

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
    def from_json(cls, json_str: str) -> LiveGameDrive:
        """Create an instance of LiveGameDrive from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in plays (list)
        _items = []
        if self.plays:
            for _item in self.plays:
                if _item:
                    _items.append(_item.to_dict())
            _dict['plays'] = _items
        # set to None if start_clock (nullable) is None
        # and __fields_set__ contains the field
        if self.start_clock is None and "start_clock" in self.__fields_set__:
            _dict['startClock'] = None

        # set to None if end_period (nullable) is None
        # and __fields_set__ contains the field
        if self.end_period is None and "end_period" in self.__fields_set__:
            _dict['endPeriod'] = None

        # set to None if end_clock (nullable) is None
        # and __fields_set__ contains the field
        if self.end_clock is None and "end_clock" in self.__fields_set__:
            _dict['endClock'] = None

        # set to None if end_yards_to_goal (nullable) is None
        # and __fields_set__ contains the field
        if self.end_yards_to_goal is None and "end_yards_to_goal" in self.__fields_set__:
            _dict['endYardsToGoal'] = None

        # set to None if duration (nullable) is None
        # and __fields_set__ contains the field
        if self.duration is None and "duration" in self.__fields_set__:
            _dict['duration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LiveGameDrive:
        """Create an instance of LiveGameDrive from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LiveGameDrive.parse_obj(obj)

        _obj = LiveGameDrive.parse_obj({
            "id": obj.get("id"),
            "offense_id": obj.get("offenseId"),
            "offense": obj.get("offense"),
            "defense_id": obj.get("defenseId"),
            "defense": obj.get("defense"),
            "play_count": obj.get("playCount"),
            "yards": obj.get("yards"),
            "start_period": obj.get("startPeriod"),
            "start_clock": obj.get("startClock"),
            "start_yards_to_goal": obj.get("startYardsToGoal"),
            "end_period": obj.get("endPeriod"),
            "end_clock": obj.get("endClock"),
            "end_yards_to_goal": obj.get("endYardsToGoal"),
            "duration": obj.get("duration"),
            "scoring_opportunity": obj.get("scoringOpportunity"),
            "result": obj.get("result"),
            "points_gained": obj.get("pointsGained"),
            "plays": [LiveGamePlay.from_dict(_item) for _item in obj.get("plays")] if obj.get("plays") is not None else None
        })
        return _obj


