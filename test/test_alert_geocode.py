# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nwsoa.models.alert_geocode import AlertGeocode

class TestAlertGeocode(unittest.TestCase):
    """AlertGeocode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertGeocode:
        """Test AlertGeocode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertGeocode`
        """
        model = AlertGeocode()
        if include_optional:
            return AlertGeocode(
                ugc = [
                    'UTZ807'
                    ],
                same = [
                    '048072'
                    ]
            )
        else:
            return AlertGeocode(
        )
        """

    def testAlertGeocode(self):
        """Test AlertGeocode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
