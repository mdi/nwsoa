# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nwsoa.models.zone_collection_json_ld import ZoneCollectionJsonLd

class TestZoneCollectionJsonLd(unittest.TestCase):
    """ZoneCollectionJsonLd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ZoneCollectionJsonLd:
        """Test ZoneCollectionJsonLd
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ZoneCollectionJsonLd`
        """
        model = ZoneCollectionJsonLd()
        if include_optional:
            return ZoneCollectionJsonLd(
                context = None,
                graph = [
                    nwsoa.models.zone.Zone(
                        @context = null, 
                        geometry = '', 
                        @id = '', 
                        @type = 'wx:Zone', 
                        id = 'UTZ807', 
                        type = 'land', 
                        name = '', 
                        effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        state = null, 
                        forecast_office = '', 
                        grid_identifier = '', 
                        awips_location_identifier = '', 
                        cwa = [
                            'AKQ'
                            ], 
                        forecast_offices = [
                            ''
                            ], 
                        time_zone = [
                            ''
                            ], 
                        observation_stations = [
                            ''
                            ], 
                        radar_station = '', )
                    ]
            )
        else:
            return ZoneCollectionJsonLd(
        )
        """

    def testZoneCollectionJsonLd(self):
        """Test ZoneCollectionJsonLd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
