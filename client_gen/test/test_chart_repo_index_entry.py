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
from inno_nbi_api.models.chart_repo_index_entry import ChartRepoIndexEntry

class TestChartRepoIndexEntry(unittest.TestCase):
    """ChartRepoIndexEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChartRepoIndexEntry:
        """Test ChartRepoIndexEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return ChartRepoIndexEntry(
                id='1',
                name='test_name',
                display_name='Test Display Name',
                description='Test description',
                vendor='Test Vendor',
                categories=['category1', 'category2'],
                all_versions=['v1.0', 'v2.0']
            )
        else:
            return ChartRepoIndexEntry(
                id='1',
                name='test_name'
            )

    def testChartRepoIndexEntry(self):
        """Test ChartRepoIndexEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertEqual(inst_req_only.id, '1')
        self.assertEqual(inst_req_only.name, 'test_name')
        self.assertIsNone(inst_req_only.display_name)
        self.assertIsNone(inst_req_only.description)
        self.assertIsNone(inst_req_only.vendor)
        self.assertIsNone(inst_req_only.categories)
        self.assertIsNone(inst_req_only.all_versions)

        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertEqual(inst_req_and_optional.id, '1')
        self.assertEqual(inst_req_and_optional.name, 'test_name')
        self.assertEqual(inst_req_and_optional.display_name, 'Test Display Name')
        self.assertEqual(inst_req_and_optional.description, 'Test description')
        self.assertEqual(inst_req_and_optional.vendor, 'Test Vendor')
        self.assertEqual(inst_req_and_optional.categories, ['category1', 'category2'])
        self.assertEqual(inst_req_and_optional.all_versions, ['v1.0', 'v2.0'])

if __name__ == '__main__':
    unittest.main()
