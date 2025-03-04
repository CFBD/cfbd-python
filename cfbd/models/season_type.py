# coding: utf-8

"""
    College Football Data API

    This is an API for query various college football datasets and analytics. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.6.5
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class SeasonType(str, Enum):
    """
    SeasonType
    """

    """
    allowed enum values
    """
    REGULAR = 'regular'
    POSTSEASON = 'postseason'
    BOTH = 'both'
    ALLSTAR = 'allstar'
    SPRING_REGULAR = 'spring_regular'
    SPRING_POSTSEASON = 'spring_postseason'

    @classmethod
    def from_json(cls, json_str: str) -> SeasonType:
        """Create an instance of SeasonType from a JSON string"""
        return SeasonType(json.loads(json_str))


