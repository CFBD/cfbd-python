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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from cfbd.models.draft_pick_hometown_info import DraftPickHometownInfo

class DraftPick(BaseModel):
    """
    DraftPick
    """
    college_athlete_id: Optional[StrictInt] = Field(default=..., alias="collegeAthleteId")
    nfl_athlete_id: StrictInt = Field(default=..., alias="nflAthleteId")
    college_id: StrictInt = Field(default=..., alias="collegeId")
    college_team: StrictStr = Field(default=..., alias="collegeTeam")
    college_conference: Optional[StrictStr] = Field(default=..., alias="collegeConference")
    nfl_team_id: StrictInt = Field(default=..., alias="nflTeamId")
    nfl_team: StrictStr = Field(default=..., alias="nflTeam")
    year: StrictInt = Field(...)
    overall: StrictInt = Field(...)
    round: StrictInt = Field(...)
    pick: StrictInt = Field(...)
    name: StrictStr = Field(...)
    position: StrictStr = Field(...)
    height: Optional[StrictInt] = Field(...)
    weight: Optional[StrictInt] = Field(...)
    pre_draft_ranking: Optional[StrictInt] = Field(default=..., alias="preDraftRanking")
    pre_draft_position_ranking: Optional[StrictInt] = Field(default=..., alias="preDraftPositionRanking")
    pre_draft_grade: Optional[StrictInt] = Field(default=..., alias="preDraftGrade")
    hometown_info: DraftPickHometownInfo = Field(default=..., alias="hometownInfo")
    __properties = ["collegeAthleteId", "nflAthleteId", "collegeId", "collegeTeam", "collegeConference", "nflTeamId", "nflTeam", "year", "overall", "round", "pick", "name", "position", "height", "weight", "preDraftRanking", "preDraftPositionRanking", "preDraftGrade", "hometownInfo"]

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
    def from_json(cls, json_str: str) -> DraftPick:
        """Create an instance of DraftPick from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of hometown_info
        if self.hometown_info:
            _dict['hometownInfo'] = self.hometown_info.to_dict()
        # set to None if college_athlete_id (nullable) is None
        # and __fields_set__ contains the field
        if self.college_athlete_id is None and "college_athlete_id" in self.__fields_set__:
            _dict['collegeAthleteId'] = None

        # set to None if college_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.college_conference is None and "college_conference" in self.__fields_set__:
            _dict['collegeConference'] = None

        # set to None if height (nullable) is None
        # and __fields_set__ contains the field
        if self.height is None and "height" in self.__fields_set__:
            _dict['height'] = None

        # set to None if weight (nullable) is None
        # and __fields_set__ contains the field
        if self.weight is None and "weight" in self.__fields_set__:
            _dict['weight'] = None

        # set to None if pre_draft_ranking (nullable) is None
        # and __fields_set__ contains the field
        if self.pre_draft_ranking is None and "pre_draft_ranking" in self.__fields_set__:
            _dict['preDraftRanking'] = None

        # set to None if pre_draft_position_ranking (nullable) is None
        # and __fields_set__ contains the field
        if self.pre_draft_position_ranking is None and "pre_draft_position_ranking" in self.__fields_set__:
            _dict['preDraftPositionRanking'] = None

        # set to None if pre_draft_grade (nullable) is None
        # and __fields_set__ contains the field
        if self.pre_draft_grade is None and "pre_draft_grade" in self.__fields_set__:
            _dict['preDraftGrade'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DraftPick:
        """Create an instance of DraftPick from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DraftPick.parse_obj(obj)

        _obj = DraftPick.parse_obj({
            "college_athlete_id": obj.get("collegeAthleteId"),
            "nfl_athlete_id": obj.get("nflAthleteId"),
            "college_id": obj.get("collegeId"),
            "college_team": obj.get("collegeTeam"),
            "college_conference": obj.get("collegeConference"),
            "nfl_team_id": obj.get("nflTeamId"),
            "nfl_team": obj.get("nflTeam"),
            "year": obj.get("year"),
            "overall": obj.get("overall"),
            "round": obj.get("round"),
            "pick": obj.get("pick"),
            "name": obj.get("name"),
            "position": obj.get("position"),
            "height": obj.get("height"),
            "weight": obj.get("weight"),
            "pre_draft_ranking": obj.get("preDraftRanking"),
            "pre_draft_position_ranking": obj.get("preDraftPositionRanking"),
            "pre_draft_grade": obj.get("preDraftGrade"),
            "hometown_info": DraftPickHometownInfo.from_dict(obj.get("hometownInfo")) if obj.get("hometownInfo") is not None else None
        })
        return _obj


