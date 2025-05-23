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
from nwsoa.models.glossary200_response_glossary_inner import Glossary200ResponseGlossaryInner
from nwsoa.models.json_ld_context import JsonLdContext
from typing import Optional, Set
from typing_extensions import Self

class Glossary200Response(BaseModel):
    """
    Glossary200Response
    """ # noqa: E501
    context: Optional[JsonLdContext] = Field(default=None, alias="@context")
    glossary: Optional[List[Glossary200ResponseGlossaryInner]] = Field(default=None, description="A list of glossary terms")
    __properties: ClassVar[List[str]] = ["@context", "glossary"]

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
        """Create an instance of Glossary200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in glossary (list)
        _items = []
        if self.glossary:
            for _item_glossary in self.glossary:
                if _item_glossary:
                    _items.append(_item_glossary.to_dict())
            _dict['glossary'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Glossary200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@context": JsonLdContext.from_dict(obj["@context"]) if obj.get("@context") is not None else None,
            "glossary": [Glossary200ResponseGlossaryInner.from_dict(_item) for _item in obj["glossary"]] if obj.get("glossary") is not None else None
        })
        return _obj


