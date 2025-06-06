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


class GridpointForecastUnits(str, Enum):
    """
    Denotes the units used in the textual portions of the forecast.
    """

    """
    allowed enum values
    """
    US = 'us'
    SI = 'si'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GridpointForecastUnits from a JSON string"""
        return cls(json.loads(json_str))


