# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class GridpointHazardsValuesInnerValueInner(BaseModel):
    """
    A value object representing an expected hazard.
    """ # noqa: E501
    phenomenon: Annotated[str, Field(strict=True)] = Field(description="Hazard code. This value will correspond to a P-VTEC phenomenon code as defined in NWS Directive 10-1703. ")
    significance: Annotated[str, Field(strict=True)] = Field(description="Significance code. This value will correspond to a P-VTEC significance code as defined in NWS Directive 10-1703. This will most frequently be \"A\" for a watch or \"Y\" for an advisory. ")
    event_number: Optional[StrictInt] = Field(description="Event number. If this hazard refers to a national or regional center product (such as a Storm Prediction Center convective watch), this value will be the sequence number of that product. ")
    __properties: ClassVar[List[str]] = ["phenomenon", "significance", "event_number"]

    @field_validator('phenomenon')
    def phenomenon_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\w{2}$", value):
            raise ValueError(r"must validate the regular expression /^\w{2}$/")
        return value

    @field_validator('significance')
    def significance_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\w$", value):
            raise ValueError(r"must validate the regular expression /^\w$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GridpointHazardsValuesInnerValueInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if event_number (nullable) is None
        # and model_fields_set contains the field
        if self.event_number is None and "event_number" in self.model_fields_set:
            _dict['event_number'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GridpointHazardsValuesInnerValueInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "phenomenon": obj.get("phenomenon"),
            "significance": obj.get("significance"),
            "event_number": obj.get("event_number")
        })
        return _obj


