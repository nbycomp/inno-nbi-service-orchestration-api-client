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
from inno_nbi_api.models.error_response import ErrorResponse

class TestErrorResponse(unittest.TestCase):
    """ErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponse:
        """Test ErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return ErrorResponse(
                code=56,
                message='test_message',
                details=['detail1', 'detail2']
            )
        else:
            return ErrorResponse(
                code=56,
                message='test_message'
            )

    def testErrorResponse(self):
        """Test ErrorResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        self.assertEqual(inst_req_only.code, 56)
        self.assertEqual(inst_req_only.message, 'test_message')
        self.assertIsNone(inst_req_only.details)

        inst_req_and_optional = self.make_instance(include_optional=True)
        self.assertEqual(inst_req_and_optional.code, 56)
        self.assertEqual(inst_req_and_optional.message, 'test_message')
        self.assertEqual(inst_req_and_optional.details, ['detail1', 'detail2'])

if __name__ == '__main__':
    unittest.main()
