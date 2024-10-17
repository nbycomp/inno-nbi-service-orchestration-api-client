![NearbyOne Logo](https://github.com/user-attachments/assets/a1726e23-59a0-430c-b6a0-f07a631db274)

# NearbyOne Innovation NBI Client

## Overview

The NearbyOne Innovation NBI (North-Bound Interface) Client is a robust Python library designed to streamline interactions with the NearbyOne Innovation NBI Service Orchestration API. This client facilitates efficient management of service chains across cloud and edge computing environments, providing a seamless interface for deployment, management, and updates.

## Key Features

- **Secure Authentication**: Integrated Kratos authentication system
- **Organization Management**: Comprehensive tools for managing organizational structures
- **Infrastructure Operations**: Efficient handling of infrastructure-related tasks
- **Marketplace Integration**: Seamless interaction with the NearbyOne marketplace
- **Service Lifecycle Management**: Full suite of tools for deploying, updating, and managing services

## Installation

### Prerequisites

- Python 3.7 or later
- pip (Python package manager)

### Steps

1. Clone the repository

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Environment Setup

1. Create and activate a virtual environment:
   ```
   python3 -m venv venv-nbi-client
   source venv-nbi-client/bin/activate  # On Windows use `venv-nbi-client\Scripts\activate`
   ```

2. Configure environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   NBY_ENV_EMAIL=your-email@example.com
   NBY_ENV_PASSWORD=your-password
   NBY_ORGANIZATION_ID=your-org-id
   NBY_ENV_NAME=your-env-name
   ```

   Replace placeholders with your actual credentials and information.

   Note: For `NBY_ENV_NAME`, use everything before `.nearbycomputing.com` in your environment URL.

   Examples:
   - For https://nearbyone.innovationlab.nearbycomputing.com/, use `NBY_ENV_NAME=nearbyone.innovationlab`
   - For https://berendgort.envs.nearbycomputing.com/, use `NBY_ENV_NAME=berendgort.envs`

## Quick Start Guide

For a comprehensive example of how to use the NearbyOne Innovation NBI Client, refer to the `nbi_client_examples.py` file in the project root. This script demonstrates various API calls and can be run directly without any specific parameters.

1. Run the example script:
   ```
   python nbi_client_examples.py
   ```

2. The script will guide you through various API calls, including:
   - Fetching organizations
   - Getting site and device details
   - Listing marketplace charts
   - Deploying a service
   - Updating service node ports
   - Deleting a service

For a sample output of what to expect when running the script, refer to `nbi_client_examples_output.txt` in the project root. This file shows the typical responses you should receive from the API calls.

For more detailed usage, you can refer to the following sections of the `nbi_client_examples.py` file:

## Advanced Usage

For more complex operations and examples, refer to the `examples/` directory in the project repository. These examples cover:

- Service chain deployment and management
- Infrastructure queries and modifications
- Marketplace interactions

## API Reference

For a comprehensive list of available methods and their parameters, please consult our [API documentation](docs/api_reference.md).

## Running Tests

Execute the test suite to ensure everything is functioning correctly:
