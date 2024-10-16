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
from inno_nbi_api.models.device_response import DeviceResponse
from inno_nbi_api.models.device import Device
from inno_nbi_api.models.device_tags_inner import DeviceTagsInner
from inno_nbi_api.models.device_position import DevicePosition
from inno_nbi_api.models.device_progress import DeviceProgress
from inno_nbi_api.models.device_cloud_resource_chart import DeviceCloudResourceChart
from inno_nbi_api.models.chart_key import ChartKey
from inno_nbi_api.models.device_cloud_resource_chart_latest_config_inner import DeviceCloudResourceChartLatestConfigInner

class TestDeviceResponse(unittest.TestCase):
    """DeviceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceResponse:
        """Test DeviceResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return DeviceResponse(
                device=Device(
                    id='1', 
                    tags=[
                        DeviceTagsInner(
                            key='key1', 
                            value='value1'
                        )
                    ], 
                    display_name='Test Device', 
                    position=DevicePosition(
                        lat=1.337, 
                        lng=1.337
                    ), 
                    specs='test_specs', 
                    status='test_status', 
                    progress=DeviceProgress(
                        step=56, 
                        goal=56
                    ), 
                    site='test_site', 
                    cloud_resource_chart=DeviceCloudResourceChart(
                        key=ChartKey(
                            name='test_chart', 
                            version='1.0'
                        ), 
                        latest_config=[
                            DeviceCloudResourceChartLatestConfigInner(
                                label='test_label', 
                                value='test_value', 
                                json_type='string', 
                                required=True, 
                                redacted=True
                            )
                        ]
                    ), 
                    org='test_org'
                )
            )
        else:
            return DeviceResponse()

    def testDeviceResponse(self):
        """Test DeviceResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertIsNone(inst_req_only.device)

        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertIsNotNone(inst_req_and_optional.device)
        self.assertEqual(inst_req_and_optional.device.id, '1')
        self.assertEqual(inst_req_and_optional.device.tags[0].key, 'key1')
        self.assertEqual(inst_req_and_optional.device.tags[0].value, 'value1')
        self.assertEqual(inst_req_and_optional.device.display_name, 'Test Device')
        self.assertEqual(inst_req_and_optional.device.position.lat, 1.337)
        self.assertEqual(inst_req_and_optional.device.position.lng, 1.337)
        self.assertEqual(inst_req_and_optional.device.specs, 'test_specs')
        self.assertEqual(inst_req_and_optional.device.status, 'test_status')
        self.assertEqual(inst_req_and_optional.device.progress.step, 56)
        self.assertEqual(inst_req_and_optional.device.progress.goal, 56)
        self.assertEqual(inst_req_and_optional.device.site, 'test_site')
        self.assertEqual(inst_req_and_optional.device.cloud_resource_chart.key.name, 'test_chart')
        self.assertEqual(inst_req_and_optional.device.cloud_resource_chart.key.version, '1.0')
        self.assertEqual(inst_req_and_optional.device.cloud_resource_chart.latest_config[0].label, 'test_label')
        self.assertEqual(inst_req_and_optional.device.cloud_resource_chart.latest_config[0].value, 'test_value')
        self.assertEqual(inst_req_and_optional.device.cloud_resource_chart.latest_config[0].json_type, 'string')
        self.assertTrue(inst_req_and_optional.device.cloud_resource_chart.latest_config[0].required)
        self.assertTrue(inst_req_and_optional.device.cloud_resource_chart.latest_config[0].redacted)
        self.assertEqual(inst_req_and_optional.device.org, 'test_org')

if __name__ == '__main__':
    unittest.main()