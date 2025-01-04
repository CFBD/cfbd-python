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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from cfbd.models.play_clock import PlayClock

class Drive(BaseModel):
    """
    Drive
    """
    offense: StrictStr = Field(...)
    offense_conference: Optional[StrictStr] = Field(default=..., alias="offenseConference")
    defense: StrictStr = Field(...)
    defense_conference: Optional[StrictStr] = Field(default=..., alias="defenseConference")
    game_id: StrictInt = Field(default=..., alias="gameId")
    id: StrictStr = Field(...)
    drive_number: Optional[StrictInt] = Field(default=..., alias="driveNumber")
    scoring: StrictBool = Field(...)
    start_period: StrictInt = Field(default=..., alias="startPeriod")
    start_yardline: StrictInt = Field(default=..., alias="startYardline")
    start_yards_to_goal: StrictInt = Field(default=..., alias="startYardsToGoal")
    start_time: PlayClock = Field(default=..., alias="startTime")
    end_period: StrictInt = Field(default=..., alias="endPeriod")
    end_yardline: StrictInt = Field(default=..., alias="endYardline")
    end_yards_to_goal: StrictInt = Field(default=..., alias="endYardsToGoal")
    end_time: PlayClock = Field(default=..., alias="endTime")
    plays: StrictInt = Field(...)
    yards: StrictInt = Field(...)
    drive_result: StrictStr = Field(default=..., alias="driveResult")
    is_home_offense: StrictBool = Field(default=..., alias="isHomeOffense")
    start_offense_score: StrictInt = Field(default=..., alias="startOffenseScore")
    start_defense_score: StrictInt = Field(default=..., alias="startDefenseScore")
    end_offense_score: StrictInt = Field(default=..., alias="endOffenseScore")
    end_defense_score: StrictInt = Field(default=..., alias="endDefenseScore")
    __properties = ["offense", "offenseConference", "defense", "defenseConference", "gameId", "id", "driveNumber", "scoring", "startPeriod", "startYardline", "startYardsToGoal", "startTime", "endPeriod", "endYardline", "endYardsToGoal", "endTime", "plays", "yards", "driveResult", "isHomeOffense", "startOffenseScore", "startDefenseScore", "endOffenseScore", "endDefenseScore"]

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
    def from_json(cls, json_str: str) -> Drive:
        """Create an instance of Drive from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of start_time
        if self.start_time:
            _dict['startTime'] = self.start_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_time
        if self.end_time:
            _dict['endTime'] = self.end_time.to_dict()
        # set to None if offense_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.offense_conference is None and "offense_conference" in self.__fields_set__:
            _dict['offenseConference'] = None

        # set to None if defense_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.defense_conference is None and "defense_conference" in self.__fields_set__:
            _dict['defenseConference'] = None

        # set to None if drive_number (nullable) is None
        # and __fields_set__ contains the field
        if self.drive_number is None and "drive_number" in self.__fields_set__:
            _dict['driveNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Drive:
        """Create an instance of Drive from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Drive.parse_obj(obj)

        _obj = Drive.parse_obj({
            "offense": obj.get("offense"),
            "offense_conference": obj.get("offenseConference"),
            "defense": obj.get("defense"),
            "defense_conference": obj.get("defenseConference"),
            "game_id": obj.get("gameId"),
            "id": obj.get("id"),
            "drive_number": obj.get("driveNumber"),
            "scoring": obj.get("scoring"),
            "start_period": obj.get("startPeriod"),
            "start_yardline": obj.get("startYardline"),
            "start_yards_to_goal": obj.get("startYardsToGoal"),
            "start_time": PlayClock.from_dict(obj.get("startTime")) if obj.get("startTime") is not None else None,
            "end_period": obj.get("endPeriod"),
            "end_yardline": obj.get("endYardline"),
            "end_yards_to_goal": obj.get("endYardsToGoal"),
            "end_time": PlayClock.from_dict(obj.get("endTime")) if obj.get("endTime") is not None else None,
            "plays": obj.get("plays"),
            "yards": obj.get("yards"),
            "drive_result": obj.get("driveResult"),
            "is_home_offense": obj.get("isHomeOffense"),
            "start_offense_score": obj.get("startOffenseScore"),
            "start_defense_score": obj.get("startDefenseScore"),
            "end_offense_score": obj.get("endOffenseScore"),
            "end_defense_score": obj.get("endDefenseScore")
        })
        return _obj


