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

from inno_nbi_api.api.infrastructure_api import InfrastructureApi


class TestInfrastructureApi(unittest.TestCase):
    """InfrastructureApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InfrastructureApi()

    def tearDown(self) -> None:
        pass

    def test_get_device_details(self) -> None:
        """Test case for get_device_details

        Retrieve details for a specific device within an organization
        """
        pass

    def test_get_site_details(self) -> None:
        """Test case for get_site_details

        Retrieve details for a specific site within an organization
        """
        pass


if __name__ == '__main__':
    unittest.main()