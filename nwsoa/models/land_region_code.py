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


class LandRegionCode(str, Enum):
    """
    Land region code. These correspond to the six NWS regional headquarters: * AR: Alaska Region * CR: Central Region * ER: Eastern Region * PR: Pacific Region * SR: Southern Region * WR: Western Region 
    """

    """
    allowed enum values
    """
    AR = 'AR'
    CR = 'CR'
    ER = 'ER'
    PR = 'PR'
    SR = 'SR'
    WR = 'WR'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LandRegionCode from a JSON string"""
        return cls(json.loads(json_str))


