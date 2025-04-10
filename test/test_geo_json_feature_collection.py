# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nwsoa.models.geo_json_feature_collection import GeoJsonFeatureCollection

class TestGeoJsonFeatureCollection(unittest.TestCase):
    """GeoJsonFeatureCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeoJsonFeatureCollection:
        """Test GeoJsonFeatureCollection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeoJsonFeatureCollection`
        """
        model = GeoJsonFeatureCollection()
        if include_optional:
            return GeoJsonFeatureCollection(
                context = None,
                type = 'FeatureCollection',
                features = [
                    nwsoa.models.geo_json_feature.GeoJsonFeature(
                        @context = null, 
                        id = '', 
                        type = 'Feature', 
                        geometry = null, 
                        properties = nwsoa.models.properties.properties(), )
                    ]
            )
        else:
            return GeoJsonFeatureCollection(
                type = 'FeatureCollection',
                features = [
                    nwsoa.models.geo_json_feature.GeoJsonFeature(
                        @context = null, 
                        id = '', 
                        type = 'Feature', 
                        geometry = null, 
                        properties = nwsoa.models.properties.properties(), )
                    ],
        )
        """

    def testGeoJsonFeatureCollection(self):
        """Test GeoJsonFeatureCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
