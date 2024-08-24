# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.14
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class DivisionClassification(str, Enum):
    """
    DivisionClassification
    """

    """
    allowed enum values
    """
    FBS = 'fbs'
    FCS = 'fcs'
    II = 'ii'
    III = 'iii'

    @classmethod
    def from_json(cls, json_str: str) -> DivisionClassification:
        """Create an instance of DivisionClassification from a JSON string"""
        return DivisionClassification(json.loads(json_str))


