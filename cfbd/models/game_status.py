# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.11
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class GameStatus(str, Enum):
    """
    GameStatus
    """

    """
    allowed enum values
    """
    SCHEDULED = 'scheduled'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    @classmethod
    def from_json(cls, json_str: str) -> GameStatus:
        """Create an instance of GameStatus from a JSON string"""
        return GameStatus(json.loads(json_str))


