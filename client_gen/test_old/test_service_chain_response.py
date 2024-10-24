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

from inno_nbi_api.models.service_chain_response import ServiceChainResponse

class TestServiceChainResponse(unittest.TestCase):
    """ServiceChainResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceChainResponse:
        """Test ServiceChainResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceChainResponse`
        """
        model = ServiceChainResponse()
        if include_optional:
            return ServiceChainResponse(
                service_chain = inno_nbi_api.models.service_chain_response_service_chain.ServiceChainResponse_serviceChain(
                    id = '', 
                    revision = 56, 
                    name = '', 
                    blocks = [
                        inno_nbi_api.models.block.Block(
                            id = '', 
                            display_name = '', 
                            owner = '', 
                            org = '', 
                            blockchart_name = '', 
                            blockchart_version = '', 
                            blockchart_values = '', 
                            status = 'OKTOSTATUS_IN_SYNC', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            device_ids = [
                                ''
                                ], )
                        ], 
                    status = '', 
                    org = '', 
                    owner = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return ServiceChainResponse(
        )
        """

    def testServiceChainResponse(self):
        """Test ServiceChainResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
