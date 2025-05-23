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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from nwsoa.models.icons_summary200_response_icons_value import IconsSummary200ResponseIconsValue
from nwsoa.models.json_ld_context import JsonLdContext
from typing import Optional, Set
from typing_extensions import Self

class IconsSummary200Response(BaseModel):
    """
    IconsSummary200Response
    """ # noqa: E501
    context: Optional[JsonLdContext] = Field(default=None, alias="@context")
    icons: Dict[str, IconsSummary200ResponseIconsValue]
    __properties: ClassVar[List[str]] = ["@context", "icons"]

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
        """Create an instance of IconsSummary200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in icons (dict)
        _field_dict = {}
        if self.icons:
            for _key_icons in self.icons:
                if self.icons[_key_icons]:
                    _field_dict[_key_icons] = self.icons[_key_icons].to_dict()
            _dict['icons'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IconsSummary200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@context": JsonLdContext.from_dict(obj["@context"]) if obj.get("@context") is not None else None,
            "icons": dict(
                (_k, IconsSummary200ResponseIconsValue.from_dict(_v))
                for _k, _v in obj["icons"].items()
            )
            if obj.get("icons") is not None
            else None
        })
        return _obj


