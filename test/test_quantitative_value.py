# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nwsoa.models.quantitative_value import QuantitativeValue

class TestQuantitativeValue(unittest.TestCase):
    """QuantitativeValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuantitativeValue:
        """Test QuantitativeValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuantitativeValue`
        """
        model = QuantitativeValue()
        if include_optional:
            return QuantitativeValue(
                value = 1.337,
                max_value = 1.337,
                min_value = 1.337,
                unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H\'qT\\{<?\'es#)#iK.YM{Rag2/!KB!k@5oXh.:',
                quality_control = 'Z'
            )
        else:
            return QuantitativeValue(
        )
        """

    def testQuantitativeValue(self):
        """Test QuantitativeValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
