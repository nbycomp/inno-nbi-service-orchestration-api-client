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

from openapi_client.models.site_response import SiteResponse

class TestSiteResponse(unittest.TestCase):
    """SiteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SiteResponse:
        """Test SiteResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SiteResponse`
        """
        model = SiteResponse()
        if include_optional:
            return SiteResponse(
                site = openapi_client.models.site.Site(
                    id = '', 
                    display_name = '', 
                    description = '', 
                    ancestors = [
                        ''
                        ], 
                    sites = [
                        ''
                        ], 
                    devices = [
                        ''
                        ], 
                    org = '', )
            )
        else:
            return SiteResponse(
        )
        """

    def testSiteResponse(self):
        """Test SiteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
