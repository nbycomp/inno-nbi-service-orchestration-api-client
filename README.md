![image](https://github.com/user-attachments/assets/a1726e23-59a0-430c-b6a0-f07a631db274)

# 🚀 NBI Client: Your Gateway to Service Orchestration

Welcome to the NBI Client, a powerful Python library that simplifies interaction with the NBI Service Orchestration API. This client provides a seamless interface for managing service chains across cloud and edge computing environments.

## 🌟 Features

- 🔐 Secure authentication with Kratos
- 🏢 Organization management
- 🖥️ Infrastructure operations
- 🛒 Marketplace interactions
- ⚙️ Service deployment and management

## 🛠️ Setup

### Python Environment

1. Ensure you have Python 3.7 or later installed on your system.

2. Create a virtual environment:
   ```
   python -m venv nbi-client-env
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     nbi-client-env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source nbi-client-env/bin/activate
     ```

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/nbi-client.git
   cd nbi-client
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Environment Variables

1. Create a `.env` file in the root directory of the project:
   ```
   touch .env
   ```

2. Add the following environment variables to the `.env` file:
   ```
   NBY_ENV_EMAIL=your-email@example.com
   NBY_ENV_PASSWORD=your-password
   NBY_ORGANIZATION_ID=your-org-id
   NBY_ENV_NAME=your-env-name
   ```

   Replace the values with your actual information:
   - `NBY_ENV_EMAIL` and `NBY_ENV_PASSWORD`: Use the email and password combination you use to log in to the environment.
   - `NBY_ENV_NAME`: Extract this from your environment URL. For example, if your URL is `https://nearbyone.innovationlab.nearbycomputing.com`, your env name would be `nearbyone.innovationlab`.
   - `NBY_ORGANIZATION_ID`: You can find this in the dashboard under the Infrastructure section. Click on your organization name, and you'll see the ID in the details.

3. Save the `.env` file.

**Important:** Keep your `.env` file secure and never commit it to version control. Add `.env` to your `.gitignore` file to prevent accidental commits.

## 🚀 Quick Start

1. In your Python script or interactive shell, load the environment variables:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

2. Start using the client:
   ```python
   from nbi_client import NbiClient

   client = NbiClient()
   organizations = client.get_organizations()
   print(f"Your organizations: {organizations}")
   ```

## 🏃‍♂️ Running the Example Script

After setting up your environment variables, you can run the example script to test the NBI Client functionality:

1. Navigate to the project directory:
   ```
   cd path/to/nbi-client
   ```

2. Run the example script:
   ```
   python client/nbi_client_examples.py
   ```

This script will demonstrate various operations using the NBI Client, including:
- Fetching organizations
- Getting site and device details
- Listing marketplace charts
- Deploying a service
- Updating and deleting services

The script will prompt you to press Enter between each operation, allowing you to observe the results step by step.

For a sample output of this script, refer to the `nbi_client_examples_output.txt` file in the project directory.

## 🔧 Advanced Usage

Check out our [examples](examples/) directory for more advanced use cases, including:

- Deploying service chains
- Updating existing services
- Fetching marketplace charts
- Managing infrastructure

## 📚 API Reference

For a complete list of available methods and their parameters, refer to our [API documentation](docs/api_reference.md).

## 🐛 Troubleshooting

Encountering issues? Check out our [troubleshooting guide](docs/troubleshooting.md) or reach out to our support team.

## 🤝 Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for more information.

## 📄 License

This project is proprietary and confidential. Unauthorized copying, transferring or reproduction of the contents of this project, via any medium is strictly prohibited.

## 🙋‍♀️ Support

For any questions or support needs, please contact our team at support@nearbycomputing.com.

Happy orchestrating! 🎉
# inno-nbi-service-orchestration-api-client
# inno-nbi-service-orchestration-api-client
