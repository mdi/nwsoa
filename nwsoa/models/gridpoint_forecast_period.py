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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from nwsoa.models.gridpoint_forecast_period_temperature import GridpointForecastPeriodTemperature
from nwsoa.models.gridpoint_forecast_period_wind_gust import GridpointForecastPeriodWindGust
from nwsoa.models.gridpoint_forecast_period_wind_speed import GridpointForecastPeriodWindSpeed
from nwsoa.models.quantitative_value import QuantitativeValue
from typing import Optional, Set
from typing_extensions import Self

class GridpointForecastPeriod(BaseModel):
    """
    An object containing forecast information for a specific time period (generally 12-hour or 1-hour). 
    """ # noqa: E501
    number: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Sequential period number.")
    name: Optional[StrictStr] = Field(default=None, description="A textual identifier for the period. This value will not be present for hourly forecasts. ")
    start_time: Optional[datetime] = Field(default=None, description="The starting time that this forecast period is valid for.", alias="startTime")
    end_time: Optional[datetime] = Field(default=None, description="The ending time that this forecast period is valid for.", alias="endTime")
    is_daytime: Optional[StrictBool] = Field(default=None, description="Indicates whether this period is daytime or nighttime.", alias="isDaytime")
    temperature: Optional[GridpointForecastPeriodTemperature] = None
    temperature_unit: Optional[StrictStr] = Field(default=None, description="The unit of the temperature value (Fahrenheit or Celsius). This property is deprecated. Future versions will indicate the unit within the quantitative value object for the temperature property. To make use of the future standard format now, set the \"forecast_temperature_qv\" feature flag on the request. ", alias="temperatureUnit")
    temperature_trend: Optional[StrictStr] = Field(default=None, description="If not null, indicates a non-diurnal temperature trend for the period (either rising temperature overnight, or falling temperature during the day) ", alias="temperatureTrend")
    probability_of_precipitation: Optional[QuantitativeValue] = Field(default=None, alias="probabilityOfPrecipitation")
    dewpoint: Optional[QuantitativeValue] = None
    relative_humidity: Optional[QuantitativeValue] = Field(default=None, alias="relativeHumidity")
    wind_speed: Optional[GridpointForecastPeriodWindSpeed] = Field(default=None, alias="windSpeed")
    wind_gust: Optional[GridpointForecastPeriodWindGust] = Field(default=None, alias="windGust")
    wind_direction: Optional[StrictStr] = Field(default=None, description="The prevailing direction of the wind for the period, using a 16-point compass.", alias="windDirection")
    icon: Optional[StrictStr] = Field(default=None, description="A link to an icon representing the forecast summary.")
    short_forecast: Optional[StrictStr] = Field(default=None, description="A brief textual forecast summary for the period.", alias="shortForecast")
    detailed_forecast: Optional[StrictStr] = Field(default=None, description="A detailed textual forecast for the period.", alias="detailedForecast")
    __properties: ClassVar[List[str]] = ["number", "name", "startTime", "endTime", "isDaytime", "temperature", "temperatureUnit", "temperatureTrend", "probabilityOfPrecipitation", "dewpoint", "relativeHumidity", "windSpeed", "windGust", "windDirection", "icon", "shortForecast", "detailedForecast"]

    @field_validator('temperature_unit')
    def temperature_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['F', 'C']):
            raise ValueError("must be one of enum values ('F', 'C')")
        return value

    @field_validator('temperature_trend')
    def temperature_trend_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['rising', 'falling']):
            raise ValueError("must be one of enum values ('rising', 'falling')")
        return value

    @field_validator('wind_direction')
    def wind_direction_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']):
            raise ValueError("must be one of enum values ('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW')")
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
        """Create an instance of GridpointForecastPeriod from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of temperature
        if self.temperature:
            _dict['temperature'] = self.temperature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of probability_of_precipitation
        if self.probability_of_precipitation:
            _dict['probabilityOfPrecipitation'] = self.probability_of_precipitation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dewpoint
        if self.dewpoint:
            _dict['dewpoint'] = self.dewpoint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relative_humidity
        if self.relative_humidity:
            _dict['relativeHumidity'] = self.relative_humidity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wind_speed
        if self.wind_speed:
            _dict['windSpeed'] = self.wind_speed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wind_gust
        if self.wind_gust:
            _dict['windGust'] = self.wind_gust.to_dict()
        # set to None if temperature_trend (nullable) is None
        # and model_fields_set contains the field
        if self.temperature_trend is None and "temperature_trend" in self.model_fields_set:
            _dict['temperatureTrend'] = None

        # set to None if wind_gust (nullable) is None
        # and model_fields_set contains the field
        if self.wind_gust is None and "wind_gust" in self.model_fields_set:
            _dict['windGust'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GridpointForecastPeriod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "number": obj.get("number"),
            "name": obj.get("name"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "isDaytime": obj.get("isDaytime"),
            "temperature": GridpointForecastPeriodTemperature.from_dict(obj["temperature"]) if obj.get("temperature") is not None else None,
            "temperatureUnit": obj.get("temperatureUnit"),
            "temperatureTrend": obj.get("temperatureTrend"),
            "probabilityOfPrecipitation": QuantitativeValue.from_dict(obj["probabilityOfPrecipitation"]) if obj.get("probabilityOfPrecipitation") is not None else None,
            "dewpoint": QuantitativeValue.from_dict(obj["dewpoint"]) if obj.get("dewpoint") is not None else None,
            "relativeHumidity": QuantitativeValue.from_dict(obj["relativeHumidity"]) if obj.get("relativeHumidity") is not None else None,
            "windSpeed": GridpointForecastPeriodWindSpeed.from_dict(obj["windSpeed"]) if obj.get("windSpeed") is not None else None,
            "windGust": GridpointForecastPeriodWindGust.from_dict(obj["windGust"]) if obj.get("windGust") is not None else None,
            "windDirection": obj.get("windDirection"),
            "icon": obj.get("icon"),
            "shortForecast": obj.get("shortForecast"),
            "detailedForecast": obj.get("detailedForecast")
        })
        return _obj


