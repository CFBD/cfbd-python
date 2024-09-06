# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.18
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from cfbd.models.play_clock import PlayClock

class Play(BaseModel):
    """
    Play
    """
    id: StrictStr = Field(...)
    drive_id: StrictStr = Field(default=..., alias="driveId")
    game_id: StrictInt = Field(default=..., alias="gameId")
    drive_number: Optional[StrictInt] = Field(default=..., alias="driveNumber")
    play_number: Optional[StrictInt] = Field(default=..., alias="playNumber")
    offense: StrictStr = Field(...)
    offense_conference: Optional[StrictStr] = Field(default=..., alias="offenseConference")
    offense_score: StrictInt = Field(default=..., alias="offenseScore")
    defense: StrictStr = Field(...)
    home: StrictStr = Field(...)
    away: StrictStr = Field(...)
    defense_conference: Optional[StrictStr] = Field(default=..., alias="defenseConference")
    defense_score: StrictInt = Field(default=..., alias="defenseScore")
    period: StrictInt = Field(...)
    clock: PlayClock = Field(...)
    offense_timeouts: Optional[StrictInt] = Field(default=..., alias="offenseTimeouts")
    defense_timeouts: Optional[StrictInt] = Field(default=..., alias="defenseTimeouts")
    yardline: StrictInt = Field(...)
    yards_to_goal: StrictInt = Field(default=..., alias="yardsToGoal")
    down: StrictInt = Field(...)
    distance: StrictInt = Field(...)
    yards_gained: StrictInt = Field(default=..., alias="yardsGained")
    scoring: StrictBool = Field(...)
    play_type: StrictStr = Field(default=..., alias="playType")
    play_text: Optional[StrictStr] = Field(default=..., alias="playText")
    ppa: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    wallclock: Optional[StrictStr] = Field(...)
    __properties = ["id", "driveId", "gameId", "driveNumber", "playNumber", "offense", "offenseConference", "offenseScore", "defense", "home", "away", "defenseConference", "defenseScore", "period", "clock", "offenseTimeouts", "defenseTimeouts", "yardline", "yardsToGoal", "down", "distance", "yardsGained", "scoring", "playType", "playText", "ppa", "wallclock"]

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
    def from_json(cls, json_str: str) -> Play:
        """Create an instance of Play from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of clock
        if self.clock:
            _dict['clock'] = self.clock.to_dict()
        # set to None if drive_number (nullable) is None
        # and __fields_set__ contains the field
        if self.drive_number is None and "drive_number" in self.__fields_set__:
            _dict['driveNumber'] = None

        # set to None if play_number (nullable) is None
        # and __fields_set__ contains the field
        if self.play_number is None and "play_number" in self.__fields_set__:
            _dict['playNumber'] = None

        # set to None if offense_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.offense_conference is None and "offense_conference" in self.__fields_set__:
            _dict['offenseConference'] = None

        # set to None if defense_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.defense_conference is None and "defense_conference" in self.__fields_set__:
            _dict['defenseConference'] = None

        # set to None if offense_timeouts (nullable) is None
        # and __fields_set__ contains the field
        if self.offense_timeouts is None and "offense_timeouts" in self.__fields_set__:
            _dict['offenseTimeouts'] = None

        # set to None if defense_timeouts (nullable) is None
        # and __fields_set__ contains the field
        if self.defense_timeouts is None and "defense_timeouts" in self.__fields_set__:
            _dict['defenseTimeouts'] = None

        # set to None if play_text (nullable) is None
        # and __fields_set__ contains the field
        if self.play_text is None and "play_text" in self.__fields_set__:
            _dict['playText'] = None

        # set to None if ppa (nullable) is None
        # and __fields_set__ contains the field
        if self.ppa is None and "ppa" in self.__fields_set__:
            _dict['ppa'] = None

        # set to None if wallclock (nullable) is None
        # and __fields_set__ contains the field
        if self.wallclock is None and "wallclock" in self.__fields_set__:
            _dict['wallclock'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Play:
        """Create an instance of Play from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Play.parse_obj(obj)

        _obj = Play.parse_obj({
            "id": obj.get("id"),
            "drive_id": obj.get("driveId"),
            "game_id": obj.get("gameId"),
            "drive_number": obj.get("driveNumber"),
            "play_number": obj.get("playNumber"),
            "offense": obj.get("offense"),
            "offense_conference": obj.get("offenseConference"),
            "offense_score": obj.get("offenseScore"),
            "defense": obj.get("defense"),
            "home": obj.get("home"),
            "away": obj.get("away"),
            "defense_conference": obj.get("defenseConference"),
            "defense_score": obj.get("defenseScore"),
            "period": obj.get("period"),
            "clock": PlayClock.from_dict(obj.get("clock")) if obj.get("clock") is not None else None,
            "offense_timeouts": obj.get("offenseTimeouts"),
            "defense_timeouts": obj.get("defenseTimeouts"),
            "yardline": obj.get("yardline"),
            "yards_to_goal": obj.get("yardsToGoal"),
            "down": obj.get("down"),
            "distance": obj.get("distance"),
            "yards_gained": obj.get("yardsGained"),
            "scoring": obj.get("scoring"),
            "play_type": obj.get("playType"),
            "play_text": obj.get("playText"),
            "ppa": obj.get("ppa"),
            "wallclock": obj.get("wallclock")
        })
        return _obj


