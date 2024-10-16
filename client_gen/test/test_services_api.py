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
from unittest.mock import patch, MagicMock
from inno_nbi_api.api.services_api import ServicesApi
from inno_nbi_api.models.service_chain_response import ServiceChainResponse

class TestServicesApi(unittest.TestCase):
    """ServicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServicesApi()

    def tearDown(self) -> None:
        pass

    @patch('inno_nbi_api.api.services_api.ServicesApi.delete_service_chain_by_id')
    def test_delete_service_chain_by_id(self, mock_delete_service_chain_by_id) -> None:
        """Test case for delete_service_chain_by_id

        Delete a deployed service chain by ID
        """
        # Arrange
        mock_delete_service_chain_by_id.return_value = None

        # Act
        service_chain_id = '123'
        response = self.api.delete_service_chain_by_id(service_chain_id)

        # Assert
        mock_delete_service_chain_by_id.assert_called_once_with(service_chain_id)
        self.assertIsNone(response)

    @patch('inno_nbi_api.api.services_api.ServicesApi.deploy_service')
    def test_deploy_service(self, mock_deploy_service) -> None:
        """Test case for deploy_service

        Deploy a new service chain
        """
        # Arrange
        mock_response = ServiceChainResponse(service_chain=None)
        mock_deploy_service.return_value = mock_response

        # Act
        service_chain_deployment = {'name': 'New Service Chain'}
        response = self.api.deploy_service(service_chain_deployment)

        # Assert
        mock_deploy_service.assert_called_once_with(service_chain_deployment)
        self.assertEqual(response, mock_response)

    @patch('inno_nbi_api.api.services_api.ServicesApi.get_all_deployed_services')
    def test_get_all_deployed_services(self, mock_get_all_deployed_services) -> None:
        """Test case for get_all_deployed_services

        Retrieve all deployed service chains
        """
        # Arrange
        mock_response = [ServiceChainResponse(service_chain=None)]
        mock_get_all_deployed_services.return_value = mock_response

        # Act
        response = self.api.get_all_deployed_services()

        # Assert
        mock_get_all_deployed_services.assert_called_once()
        self.assertEqual(response, mock_response)

    @patch('inno_nbi_api.api.services_api.ServicesApi.get_deployed_service')
    def test_get_deployed_service(self, mock_get_deployed_service) -> None:
        """Test case for get_deployed_service

        Retrieve deployed service chain by ID
        """
        # Arrange
        mock_response = ServiceChainResponse(service_chain=None)
        mock_get_deployed_service.return_value = mock_response

        # Act
        service_chain_id = '123'
        response = self.api.get_deployed_service(service_chain_id)

        # Assert
        mock_get_deployed_service.assert_called_once_with(service_chain_id)
        self.assertEqual(response, mock_response)

    @patch('inno_nbi_api.api.services_api.ServicesApi.update_service')
    def test_update_service(self, mock_update_service) -> None:
        """Test case for update_service

        Update a deployed service chain
        """
        # Arrange
        mock_response = ServiceChainResponse(service_chain=None)
        mock_update_service.return_value = mock_response

        # Act
        service_chain_id = '123'
        service_chain_update = {'name': 'Updated Service Chain'}
        response = self.api.update_service(service_chain_id, service_chain_update)

        # Assert
        mock_update_service.assert_called_once_with(service_chain_id, service_chain_update)
        self.assertEqual(response, mock_response)


if __name__ == '__main__':
    unittest.main()