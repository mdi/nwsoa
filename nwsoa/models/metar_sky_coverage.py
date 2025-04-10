# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MetarSkyCoverage(str, Enum):
    """
    MetarSkyCoverage
    """

    """
    allowed enum values
    """
    OVC = 'OVC'
    BKN = 'BKN'
    SCT = 'SCT'
    FEW = 'FEW'
    SKC = 'SKC'
    CLR = 'CLR'
    VV = 'VV'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MetarSkyCoverage from a JSON string"""
        return cls(json.loads(json_str))


