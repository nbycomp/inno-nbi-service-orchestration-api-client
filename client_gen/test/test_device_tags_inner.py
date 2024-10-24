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
from inno_nbi_api.models.device_tags_inner import DeviceTagsInner

class TestDeviceTagsInner(unittest.TestCase):
    """DeviceTagsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceTagsInner:
        """Test DeviceTagsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return DeviceTagsInner(
                key='test_key',
                value='test_value'
            )
        else:
            return DeviceTagsInner(
                key='test_key'
            )

    def testDeviceTagsInner(self):
        """Test DeviceTagsInner"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertEqual(inst_req_only.key, 'test_key')
        self.assertIsNone(inst_req_only.value)

        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertEqual(inst_req_and_optional.key, 'test_key')
        self.assertEqual(inst_req_and_optional.value, 'test_value')

if __name__ == '__main__':
    unittest.main()
