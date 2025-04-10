# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nwsoa.models.observation_cloud_layers_inner import ObservationCloudLayersInner

class TestObservationCloudLayersInner(unittest.TestCase):
    """ObservationCloudLayersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationCloudLayersInner:
        """Test ObservationCloudLayersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationCloudLayersInner`
        """
        model = ObservationCloudLayersInner()
        if include_optional:
            return ObservationCloudLayersInner(
                base = nwsoa.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H\'qT\\{<?\'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                amount = 'OVC'
            )
        else:
            return ObservationCloudLayersInner(
                base = nwsoa.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H\'qT\\{<?\'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                amount = 'OVC',
        )
        """

    def testObservationCloudLayersInner(self):
        """Test ObservationCloudLayersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
