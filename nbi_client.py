import sys
import os
import logging
from typing import List

# Ensure the client_gen directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'client_gen')))

from kratos_client import KratosClient, AuthenticationError, CommunicationError
from client_gen.inno_nbi_api import ApiClient, Configuration
from client_gen.inno_nbi_api.api.organizations_api import OrganizationsApi
from client_gen.inno_nbi_api.api.infrastructure_api import InfrastructureApi
from client_gen.inno_nbi_api.api.marketplace_api import MarketplaceApi
from client_gen.inno_nbi_api.api.services_api import ServicesApi
from client_gen.inno_nbi_api.models import *

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

class NbiClient:
    def __init__(self):
        self.api_client = None
        self.org_api = None
        self.infra_api = None
        self.marketplace_api = None
        self.services_api = None
        self._initialize_client()

    def _initialize_client(self):
        kratos_client = KratosClient()
        try:
            action_url = kratos_client.fetch_action_url()
            session_token = kratos_client.fetch_token(action_url)
            self.env_name = kratos_client.env_name
            self.org = kratos_client.org  # Store the org ID
            logging.debug(f"Fetched session token: {session_token}")
        except (AuthenticationError, CommunicationError) as e:
            logging.error(f"Error: {e}")
            exit(1)

        config = Configuration(
            host=f"https://{self.env_name}.envs.nearbycomputing.com/inno-nbi-api",
        )
        self.api_client = ApiClient(configuration=config)
        self.api_client.set_default_header('Authorization', f'Bearer {session_token}')
        self.api_client.set_default_header('x-org', self.org)  # Set the x-org header

        self.org_api = OrganizationsApi(api_client=self.api_client)
        self.infra_api = InfrastructureApi(api_client=self.api_client)
        self.marketplace_api = MarketplaceApi(api_client=self.api_client)
        self.services_api = ServicesApi(api_client=self.api_client)

    def get_organizations(self) -> List[Organization]:
        try:
            organizations = self.org_api.get_organizations()
            return organizations
        except Exception as e:
            logging.error(f"Error fetching organizations: {e}")
            if hasattr(e, 'body'):
                logging.error(f"Error response body: {e.body}")
            return []
        
    def list_marketplace_charts(self) -> MarketplaceChartsResponse:
        try:
            charts = self.marketplace_api.list_marketplace_charts()
            return charts
        except Exception as e:
            logging.error(f"Error listing marketplace charts: {e}")
            return None
        

    def fetch_block_chart(self, block_name: str, block_version: str) -> FetchBlockChartResponse:
        try:
            block_chart = self.marketplace_api.fetch_block_chart(block_name, block_version)
            return block_chart
        except Exception as e:
            logging.error(f"Error fetching block chart: {e}")
            return None
        
        
    def deploy_service(self, deploy_args: DeployServiceChainArgs) -> str:
        try:
            response = self.services_api.deploy_service(deploy_args)
            return response
        except Exception as e:
            logging.error(f"Error deploying service: {e}")
            return None

    def get_site_details(self, site_id: str) -> SiteResponse:
        try:
            site_details = self.infra_api.get_site_details(site_id)
            return site_details
        except Exception as e:
            logging.error(f"Error fetching site details: {e}")
            return None

    def get_device_details(self, device_id: str) -> DeviceResponse:
        try:
            device_details = self.infra_api.get_device_details(device_id)
            return device_details
        except Exception as e:
            logging.error(f"Error fetching device details: {e}")
            return None

    def get_all_deployed_services(self) -> List[ServiceChainResponse]:
        try:
            services = self.services_api.get_all_deployed_services()
            return services
        except Exception as e:
            logging.error(f"Error fetching all deployed services: {e}")
            return []
        
    def get_deployed_service(self, service_id: str) -> ServiceChainResponse:
        try:
            service = self.services_api.get_deployed_service(service_id)
            return service
        except Exception as e:
            logging.error(f"Error fetching deployed service by ID: {e}")
            return None


    def update_service(self, service_id: str, update_args: UpdateServiceChainArgs) -> ServiceChainResponse:
        try:
            service = self.services_api.update_service(service_id, update_args)
            return service
        except Exception as e:
            logging.error(f"Error updating service: {e}")
            return None

    def delete_service_chain_by_id(self, service_id: str) -> str:
        try:
            response = self.services_api.delete_service_chain_by_id(service_id)
            return response
        except Exception as e:
            logging.error(f"Error deleting service chain: {e}")
            return None
        
# Example usage:
if __name__ == "__main__":
    nbi_client = NbiClient()
    organizations = nbi_client.get_organizations()
    for org in organizations:
        print(org)
