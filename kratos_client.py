from dotenv import load_dotenv
from typing import Dict, Any
import requests
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Initialize logging
logging.basicConfig(level=logging.INFO)

class AuthenticationError(Exception):
    pass

class CommunicationError(Exception):
    pass

class KratosClient:
    def __init__(self):
        self.user_email = os.getenv('NBY_ENV_EMAIL')
        self.password = os.getenv('NBY_ENV_PASSWORD')
        self.org = os.getenv('NBY_ORGANIZATION_ID')
        self.env_name = os.getenv('NBY_ENV_NAME')

        if not self.user_email:
            raise ValueError("Environment variable NBY_ENV_EMAIL is not set. Action required: configure your .env file!")
        if not self.password:
            raise ValueError("Environment variable NBY_ENV_PASSWORD is not set. Action required: configure your .env file!")
        if not self.org:
            raise ValueError("Environment variable NBY_ORGANIZATION_ID is not set. Action required: configure your .env file!")
        if not self.env_name:
            raise ValueError("Environment name NBY_ENV_NAME is not set. Action required: configure your .env file!")

        self.kratos_public = f"https://{self.env_name}.nearbycomputing.com/.ory/kratos/public"
        self.base_url = f"https://{self.env_name}.nearbycomputing.com/inno-nbi-api/"
        self.session_token = None
        self.headers = {"Content-Type": "application/json"}

    def fetch_action_url(self) -> str:
        try:
            response = requests.get(f"{self.kratos_public}/self-service/login/api", headers={"Accept": "application/json"})
            response.raise_for_status()
            return response.json().get('ui', {}).get('action')
        except requests.RequestException as e:
            raise CommunicationError(f"Failed to fetch action URL from Kratos: {e}")

    def fetch_token(self, action_url: str) -> str:
        login_payload = {
            "identifier": self.user_email,
            "password": self.password,
            "method": "password",
            "org": self.org
        }

        logging.info("KratosClient - Fetching token...")
        try:
            response = requests.post(action_url, json=login_payload, headers={"Content-Type": "application/json"})
            response.raise_for_status()
            self.session_token = response.json().get('session_token')
            logging.info("KratosClient - Token request successful")
            return self.session_token
        except requests.RequestException as e:
            logging.error(f"KratosClient - Request failed: {e}")
            raise AuthenticationError(f"Failed to fetch token from Kratos: {e}")

    def make_authenticated_request(self, method: str, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        if not self.session_token:
            raise AuthenticationError("No session token available. Please fetch a token first.")

        headers = {
            "Authorization": f"Bearer {self.session_token}",
            "x-org": self.org,  # Add this line to include the x-org header
            **self.headers
        }
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"KratosClient - Request failed: {e}")
            raise CommunicationError(f"Failed to make authenticated request: {e}")

if __name__ == "__main__":
    kratos_client = KratosClient()
    try:
        action_url = kratos_client.fetch_action_url()
        session_token = kratos_client.fetch_token(action_url)
        print(f"Session Token: {session_token}")

        # Example of making an authenticated request
        response = kratos_client.make_authenticated_request("GET", "some-endpoint")
        print(f"Response: {response}")
    except (AuthenticationError, CommunicationError) as e:
        print(f"Error: {e}")
