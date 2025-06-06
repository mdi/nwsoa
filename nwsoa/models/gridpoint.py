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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from nwsoa.models.gridpoint_hazards import GridpointHazards
from nwsoa.models.gridpoint_weather import GridpointWeather
from nwsoa.models.iso8601_interval import ISO8601Interval
from nwsoa.models.json_ld_context import JsonLdContext
from nwsoa.models.quantitative_value import QuantitativeValue
from typing import Optional, Set
from typing_extensions import Self

class Gridpoint(BaseModel):
    """
    Raw forecast data for a 2.5km grid square. This is a list of all potential data layers that may appear. Some layers may not be present in all areas. * temperature * dewpoint * maxTemperature * minTemperature * relativeHumidity * apparentTemperature * heatIndex * windChill * wetBulbGlobeTemperature * skyCover * windDirection * windSpeed * windGust * weather * hazards: Watch and advisory products in effect * probabilityOfPrecipitation * quantitativePrecipitation * iceAccumulation * snowfallAmount * snowLevel * ceilingHeight * visibility * transportWindSpeed * transportWindDirection * mixingHeight * hainesIndex * lightningActivityLevel * twentyFootWindSpeed * twentyFootWindDirection * waveHeight * wavePeriod * waveDirection * primarySwellHeight * primarySwellDirection * secondarySwellHeight * secondarySwellDirection * wavePeriod2 * windWaveHeight * dispersionIndex * pressure: Barometric pressure * probabilityOfTropicalStormWinds * probabilityOfHurricaneWinds * potentialOf15mphWinds * potentialOf25mphWinds * potentialOf35mphWinds * potentialOf45mphWinds * potentialOf20mphWindGusts * potentialOf30mphWindGusts * potentialOf40mphWindGusts * potentialOf50mphWindGusts * potentialOf60mphWindGusts * grasslandFireDangerIndex * probabilityOfThunder * davisStabilityIndex * atmosphericDispersionIndex * lowVisibilityOccurrenceRiskIndex * stability * redFlagThreatIndex 
    """ # noqa: E501
    context: Optional[JsonLdContext] = Field(default=None, alias="@context")
    geometry: Optional[StrictStr] = Field(default=None, description="A geometry represented in Well-Known Text (WKT) format.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[StrictStr] = Field(default=None, alias="@type")
    update_time: Optional[datetime] = Field(default=None, alias="updateTime")
    valid_times: Optional[ISO8601Interval] = Field(default=None, alias="validTimes")
    elevation: Optional[QuantitativeValue] = None
    forecast_office: Optional[StrictStr] = Field(default=None, alias="forecastOffice")
    grid_id: Optional[StrictStr] = Field(default=None, alias="gridId")
    grid_x: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="gridX")
    grid_y: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="gridY")
    weather: Optional[GridpointWeather] = None
    hazards: Optional[GridpointHazards] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["@context", "geometry", "@id", "@type", "updateTime", "validTimes", "elevation", "forecastOffice", "gridId", "gridX", "gridY", "weather", "hazards"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['wx:Gridpoint']):
            raise ValueError("must be one of enum values ('wx:Gridpoint')")
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
        """Create an instance of Gridpoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of valid_times
        if self.valid_times:
            _dict['validTimes'] = self.valid_times.to_dict()
        # override the default output from pydantic by calling `to_dict()` of elevation
        if self.elevation:
            _dict['elevation'] = self.elevation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of weather
        if self.weather:
            _dict['weather'] = self.weather.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hazards
        if self.hazards:
            _dict['hazards'] = self.hazards.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if geometry (nullable) is None
        # and model_fields_set contains the field
        if self.geometry is None and "geometry" in self.model_fields_set:
            _dict['geometry'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Gridpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@context": JsonLdContext.from_dict(obj["@context"]) if obj.get("@context") is not None else None,
            "geometry": obj.get("geometry"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "updateTime": obj.get("updateTime"),
            "validTimes": ISO8601Interval.from_dict(obj["validTimes"]) if obj.get("validTimes") is not None else None,
            "elevation": QuantitativeValue.from_dict(obj["elevation"]) if obj.get("elevation") is not None else None,
            "forecastOffice": obj.get("forecastOffice"),
            "gridId": obj.get("gridId"),
            "gridX": obj.get("gridX"),
            "gridY": obj.get("gridY"),
            "weather": GridpointWeather.from_dict(obj["weather"]) if obj.get("weather") is not None else None,
            "hazards": GridpointHazards.from_dict(obj["hazards"]) if obj.get("hazards") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


