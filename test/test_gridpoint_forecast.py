# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nwsoa.models.gridpoint_forecast import GridpointForecast

class TestGridpointForecast(unittest.TestCase):
    """GridpointForecast unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridpointForecast:
        """Test GridpointForecast
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridpointForecast`
        """
        model = GridpointForecast()
        if include_optional:
            return GridpointForecast(
                context = None,
                geometry = '',
                units = 'us',
                forecast_generator = '',
                generated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                valid_times = None,
                elevation = nwsoa.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H\'qT\\{<?\'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                periods = [
                    nwsoa.models.gridpoint_forecast_period.GridpointForecastPeriod(
                        number = 1, 
                        name = 'Tuesday Night', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_daytime = True, 
                        temperature = null, 
                        temperature_unit = 'F', 
                        temperature_trend = 'rising', 
                        probability_of_precipitation = nwsoa.models.quantitative_value.QuantitativeValue(
                            value = 1.337, 
                            max_value = 1.337, 
                            min_value = 1.337, 
                            unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H\'qT\\{<?\'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                            quality_control = 'Z', ), 
                        dewpoint = nwsoa.models.quantitative_value.QuantitativeValue(
                            value = 1.337, 
                            max_value = 1.337, 
                            min_value = 1.337, 
                            quality_control = 'Z', ), 
                        relative_humidity = , 
                        wind_speed = null, 
                        wind_gust = null, 
                        wind_direction = 'N', 
                        icon = '', 
                        short_forecast = '', 
                        detailed_forecast = '', )
                    ]
            )
        else:
            return GridpointForecast(
        )
        """

    def testGridpointForecast(self):
        """Test GridpointForecast"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
