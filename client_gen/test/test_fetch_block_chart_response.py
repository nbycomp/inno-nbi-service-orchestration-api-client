# coding: utf-8

"""
    NBI Service Orchestration API

    Provides a robust interface for orchestrating service chains across cloud and edge computing environments, facilitating deployment, management, and updates of service chains to ensure dynamic, efficient operations across diverse infrastructure setups.

    The version of the OpenAPI document: 1.0.0
    Contact: support@nearbycomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
from inno_nbi_api.models.fetch_block_chart_response import FetchBlockChartResponse

class TestFetchBlockChartResponse(unittest.TestCase):
    """FetchBlockChartResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FetchBlockChartResponse:
        """Test FetchBlockChartResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return FetchBlockChartResponse(
                display_name='Test Display Name',
                description='Test Description',
                version='1.0',
                chart_yaml='test_chart_yaml',
                overrides_yaml='test_overrides_yaml'
            )
        else:
            return FetchBlockChartResponse()

    def testFetchBlockChartResponse(self):
        """Test FetchBlockChartResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertIsNone(inst_req_only.display_name)
        self.assertIsNone(inst_req_only.description)
        self.assertIsNone(inst_req_only.version)
        self.assertIsNone(inst_req_only.chart_yaml)
        self.assertIsNone(inst_req_only.overrides_yaml)

        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertEqual(inst_req_and_optional.display_name, 'Test Display Name')
        self.assertEqual(inst_req_and_optional.description, 'Test Description')
        self.assertEqual(inst_req_and_optional.version, '1.0')
        self.assertEqual(inst_req_and_optional.chart_yaml, 'test_chart_yaml')
        self.assertEqual(inst_req_and_optional.overrides_yaml, 'test_overrides_yaml')

if __name__ == '__main__':
    unittest.main()
