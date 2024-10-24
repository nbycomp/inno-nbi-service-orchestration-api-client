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

from inno_nbi_api.api.marketplace_api import MarketplaceApi


class TestMarketplaceApi(unittest.TestCase):
    """MarketplaceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MarketplaceApi()

    def tearDown(self) -> None:
        pass

    def test_fetch_block_chart(self) -> None:
        """Test case for fetch_block_chart

        Retrieve specific block chart details from the marketplace
        """
        pass

    def test_list_marketplace_charts(self) -> None:
        """Test case for list_marketplace_charts

        List all available block charts in the marketplace
        """
        pass


if __name__ == '__main__':
    unittest.main()