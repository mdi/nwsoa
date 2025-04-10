# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nwsoa.models.gridpoint_hazards import GridpointHazards

class TestGridpointHazards(unittest.TestCase):
    """GridpointHazards unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridpointHazards:
        """Test GridpointHazards
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridpointHazards`
        """
        model = GridpointHazards()
        if include_optional:
            return GridpointHazards(
                values = [
                    nwsoa.models.gridpoint_hazards_values_inner.Gridpoint_hazards_values_inner(
                        valid_time = null, 
                        value = [
                            nwsoa.models.gridpoint_hazards_values_inner_value_inner.Gridpoint_hazards_values_inner_value_inner(
                                phenomenon = 'eH', 
                                significance = 'e', 
                                event_number = 56, )
                            ], )
                    ]
            )
        else:
            return GridpointHazards(
                values = [
                    nwsoa.models.gridpoint_hazards_values_inner.Gridpoint_hazards_values_inner(
                        valid_time = null, 
                        value = [
                            nwsoa.models.gridpoint_hazards_values_inner_value_inner.Gridpoint_hazards_values_inner_value_inner(
                                phenomenon = 'eH', 
                                significance = 'e', 
                                event_number = 56, )
                            ], )
                    ],
        )
        """

    def testGridpointHazards(self):
        """Test GridpointHazards"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
