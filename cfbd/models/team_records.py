# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.14
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.team_record import TeamRecord

class TeamRecords(BaseModel):
    """
    TeamRecords
    """
    year: StrictInt = Field(...)
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    classification: Optional[DivisionClassification] = Field(...)
    conference: StrictStr = Field(...)
    division: StrictStr = Field(...)
    expected_wins: Union[StrictFloat, StrictInt] = Field(default=..., alias="expectedWins")
    total: TeamRecord = Field(...)
    conference_games: TeamRecord = Field(default=..., alias="conferenceGames")
    home_games: TeamRecord = Field(default=..., alias="homeGames")
    away_games: TeamRecord = Field(default=..., alias="awayGames")
    neutral_site_games: TeamRecord = Field(default=..., alias="neutralSiteGames")
    __properties = ["year", "teamId", "team", "classification", "conference", "division", "expectedWins", "total", "conferenceGames", "homeGames", "awayGames", "neutralSiteGames"]

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
    def from_json(cls, json_str: str) -> TeamRecords:
        """Create an instance of TeamRecords from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of total
        if self.total:
            _dict['total'] = self.total.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conference_games
        if self.conference_games:
            _dict['conferenceGames'] = self.conference_games.to_dict()
        # override the default output from pydantic by calling `to_dict()` of home_games
        if self.home_games:
            _dict['homeGames'] = self.home_games.to_dict()
        # override the default output from pydantic by calling `to_dict()` of away_games
        if self.away_games:
            _dict['awayGames'] = self.away_games.to_dict()
        # override the default output from pydantic by calling `to_dict()` of neutral_site_games
        if self.neutral_site_games:
            _dict['neutralSiteGames'] = self.neutral_site_games.to_dict()
        # set to None if classification (nullable) is None
        # and __fields_set__ contains the field
        if self.classification is None and "classification" in self.__fields_set__:
            _dict['classification'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamRecords:
        """Create an instance of TeamRecords from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamRecords.parse_obj(obj)

        _obj = TeamRecords.parse_obj({
            "year": obj.get("year"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "classification": obj.get("classification"),
            "conference": obj.get("conference"),
            "division": obj.get("division"),
            "expected_wins": obj.get("expectedWins"),
            "total": TeamRecord.from_dict(obj.get("total")) if obj.get("total") is not None else None,
            "conference_games": TeamRecord.from_dict(obj.get("conferenceGames")) if obj.get("conferenceGames") is not None else None,
            "home_games": TeamRecord.from_dict(obj.get("homeGames")) if obj.get("homeGames") is not None else None,
            "away_games": TeamRecord.from_dict(obj.get("awayGames")) if obj.get("awayGames") is not None else None,
            "neutral_site_games": TeamRecord.from_dict(obj.get("neutralSiteGames")) if obj.get("neutralSiteGames") is not None else None
        })
        return _obj


