import logging
import time
from nbi_client import NbiClient
from client_gen.inno_nbi_api.models.deploy_service_chain_args import DeployServiceChainArgs
from client_gen.inno_nbi_api.models.block_args_deploy import BlockArgsDeploy
from client_gen.inno_nbi_api.models.update_service_chain_args import UpdateServiceChainArgs
from client_gen.inno_nbi_api.models.block_args_update import BlockArgsUpdate
import yaml

# Initialize logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def test_get_organizations(client):
    logging.info("Starting test_get_organizations")
    try:
        organizations = client.get_organizations()
        logging.info("Called get_organizations")
        logging.info(f"Organizations fetched: {organizations}")
        
        if organizations:
            logging.info("test_get_organizations passed.")
            return organizations
        else:
            logging.warning("test_get_organizations returned an empty list.")
            return None
    except Exception as e:
        logging.error(f"test_get_organizations failed: {e}")
        return None
    finally:
        logging.info("Finished test_get_organizations\n" + "-"*50 + "\n")

def test_get_site_details(client, site_id):
    logging.info(f"Starting test_get_site_details for site_id: {site_id}")
    try:
        site_details = client.get_site_details(site_id)
        logging.info("Called get_site_details")
        logging.info(f"Site details fetched: {site_details}")
        
        if site_details:
            logging.info("test_get_site_details passed.")
            return site_details
        else:
            logging.warning("test_get_site_details returned None.")
            return None
    except Exception as e:
        logging.error(f"test_get_site_details failed: {e}")
        return None
    finally:
        logging.info("Finished test_get_site_details\n" + "-"*50 + "\n")

def test_get_device_details(client, device_id):
    logging.info(f"Starting test_get_device_details for device_id: {device_id}")
    try:
        device_details = client.get_device_details(device_id)
        logging.info("Called get_device_details")
        logging.info(f"Device details fetched: {device_details}")
        
        if device_details:
            logging.info("test_get_device_details passed.")
            return device_details
        else:
            logging.warning("test_get_device_details returned None.")
            return None
    except Exception as e:
        logging.error(f"test_get_device_details failed: {e}")
        return None
    finally:
        logging.info("Finished test_get_device_details\n" + "-"*50 + "\n")

def test_list_marketplace_charts(client):
    logging.info("Starting test_list_marketplace_charts")
    try:
        charts_response = client.list_marketplace_charts()
        logging.info("Called list_marketplace_charts")
        
        nginx_chart = next((chart for chart in charts_response.charts if chart.name == "NginxSimpleContainer"), None)
        
        if nginx_chart:
            logging.info(f"NGINX chart found: {nginx_chart}")
        else:
            logging.warning("NGINX chart not found in marketplace charts. Using the first available chart.")
            nginx_chart = charts_response.charts[0] if charts_response.charts else None
        
        return nginx_chart
    except Exception as e:
        logging.error(f"test_list_marketplace_charts failed: {e}")
        return None
    finally:
        logging.info("Finished test_list_marketplace_charts\n" + "-"*50 + "\n")

def test_fetch_block_chart(client, chart_name, chart_version):
    logging.info(f"Starting test_fetch_block_chart for {chart_name} version {chart_version}")
    try:
        block_chart = client.fetch_block_chart(chart_name, chart_version)
        logging.info("Called fetch_block_chart")
        logging.info(f"Block chart fetched: {block_chart}")
        
        if block_chart:
            logging.info("test_fetch_block_chart passed.")
            return block_chart
        else:
            logging.warning("test_fetch_block_chart returned None.")
            return None
    except Exception as e:
        logging.error(f"test_fetch_block_chart failed: {e}")
        return None
    finally:
        logging.info("Finished test_fetch_block_chart\n" + "-"*50 + "\n")

def test_deploy_service(client, site_id, chart_name, chart_version, display_name):
    logging.info("Starting test_deploy_service")
    try:
        service_name = f"NBI API Test Script - {chart_name}"
        
        # Ask user if they want to override values with the file parameters
        override_values = input(f"Do you want to override the default values with parameters from 'nginx_values_override.yml'? (y/n): ").lower() == 'y'
        
        values = None
        if override_values:
            values_yaml = read_yaml_file('nginx_values_override.yml')
            values = yaml.dump(values_yaml)
            logging.info(f"Using override values from 'nginx_values_override.yml': {values}")
        else:
            logging.info("Using default values")
        
        block_args = BlockArgsDeploy(
            site_id=site_id,
            display_name=display_name,
            block_chart_name=chart_name,
            block_chart_version=chart_version,
            values=values
        )
        logging.debug(f"BlockArgs created: {block_args}")
        
        deploy_args = DeployServiceChainArgs(
            name=service_name,
            blocks=[block_args.model_dump()]
        )
        logging.info(f"DeployServiceChainArgs created: {deploy_args}")
        
        deploy_args_dict = deploy_args.model_dump()
        
        response = client.deploy_service(deploy_args_dict)
        logging.info("Called deploy_service")
        logging.info(f"Deploy service response: {response}")
        
        if response:
            logging.info("test_deploy_service passed.")
        else:
            logging.warning("test_deploy_service returned None.")
    except Exception as e:
        logging.error(f"test_deploy_service failed: {e}")
    finally:
        logging.info("Finished test_deploy_service\n" + "-"*50 + "\n")

def test_get_all_deployed_services(client):
    logging.info("Starting test_get_all_deployed_services")
    try:
        services = client.get_all_deployed_services()
        logging.info("Called get_all_deployed_services")
        logging.info(f"All deployed services fetched: {services}")
        
        if services:
            logging.info("test_get_all_deployed_services passed.")
            return services
        else:
            logging.warning("test_get_all_deployed_services returned an empty list.")
            return []
    except Exception as e:
        logging.error(f"test_get_all_deployed_services failed: {e}")
        return []
    finally:
        logging.info("Finished test_get_all_deployed_services\n" + "-"*50 + "\n")


def test_get_deployed_service_by_id(client, service_id):
    logging.info(f"Starting test_get_deployed_service_by_id for service_id: {service_id}")
    try:
        service = client.get_deployed_service(service_id)
        logging.info("Called get_deployed_service")
        logging.info(f"Deployed service fetched: {service}")
        
        if service:
            logging.info("test_get_deployed_service_by_id passed.")
            return service
        else:
            logging.warning("test_get_deployed_service_by_id returned None.")
            return None
    except Exception as e:
        logging.error(f"test_get_deployed_service_by_id failed: {e}")
        return None
    finally:
        logging.info("Finished test_get_deployed_service_by_id\n" + "-"*50 + "\n")

def test_update_service_node_ports(client, service_id, new_http_port, new_https_port):
    logging.info(f"🔧 Testing update_service_node_ports for service_id: {service_id}")
    try:
        service = client.get_deployed_service(service_id)
        logging.info("Called get_deployed_service")
        
        if service and service.service_chain and service.service_chain.blocks:
            updated_blocks = []
            for block in service.service_chain.blocks:
                block_values = block.blockchart_values
                if block_values:
                    values_dict = yaml.safe_load(block_values)
                    logging.info(f"Original blockchart_values for block ID {block.id}: {values_dict}")

                    if 'deployments' in values_dict and 'nginx' in values_dict['deployments']:
                        nginx_values = values_dict['deployments']['nginx'].get('values', {})
                        service_values = nginx_values.get('service', {})

                        if new_https_port:
                            service_values['httpsPort'] = new_https_port
                        if new_http_port:
                            service_values['httpPort'] = new_http_port

                        nginx_values['service'] = service_values
                        values_dict['deployments']['nginx']['values'] = nginx_values

                    updated_blockchart_values = yaml.dump(values_dict, default_flow_style=False)
                    logging.info(f"Updated blockchart_values YAML for block ID {block.id}: {updated_blockchart_values}")

                    block.blockchart_values = updated_blockchart_values

                updated_block = BlockArgsUpdate(
                    id=block.id,
                    display_name=block.display_name,
                    block_chart_name=block.blockchart_name,
                    block_chart_version=block.blockchart_version,
                    values=block.blockchart_values
                )
                updated_blocks.append(updated_block.model_dump())

            update_args = UpdateServiceChainArgs(
                id=service.service_chain.id,
                name=service.service_chain.name,
                blocks=updated_blocks
            )
            logging.info(f"UpdateServiceChainArgs created: {update_args}")

            response = client.update_service(service_id, update_args.model_dump())
            logging.info("Called update_service")
            logging.info(f"Update service response: {response}")

            if response:
                logging.info("test_update_service_node_ports passed.")
            else:
                logging.warning("test_update_service_node_ports returned None.")
        else:
            logging.info("Service or blocks not found")
    except Exception as e:
        logging.error(f"test_update_service_node_ports failed: {e}")
    finally:
        logging.info("Finished test_update_service_node_ports\n" + "-"*50 + "\n")

def select_service_to_delete(services):
    print("\nAvailable services:")
    for i, service in enumerate(services, 1):
        print(f"{i}. {service.service_chain.name} (ID: {service.service_chain.id})")
    
    while True:
        try:
            choice = int(input("\nEnter the number of the service you want to delete (0 to cancel): "))
            if choice == 0:
                return None
            if 1 <= choice <= len(services):
                selected_service = services[choice - 1]
                confirm = input(f"Are you sure you want to delete '{selected_service.service_chain.name}'? (y/n): ")
                if confirm.lower() == 'y':
                    return selected_service.service_chain.id
                else:
                    print("Deletion cancelled.")
                    return None
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Example usage
if __name__ == "__main__":
    nbi_client = NbiClient()
    
    logging.info("🚀 Testing get_organizations")
    organizations = test_get_organizations(nbi_client)

    input("✅ Organizations fetched! Press Enter to continue to fetch site details...")

    if organizations:
        site_id = organizations[0].sites[0]
        device_meta = organizations[0].device_metas[0] if organizations[0].device_metas else None
        device_id = device_meta.id if device_meta else None
        
        logging.info("🔍 Testing get_site_details")
        site_details = test_get_site_details(nbi_client, site_id)
        input("✅ Site details fetched! Press Enter to continue to fetch device details...")
        
        logging.info("📡 Testing get_device_details")
        device_details = test_get_device_details(nbi_client, device_id)
        input("✅ Device details fetched! Press Enter to continue to list marketplace charts...")
        
        logging.info("🛒 Testing list_marketplace_charts")
        selected_chart = test_list_marketplace_charts(nbi_client)
        input("✅ Marketplace charts listed! Press Enter to continue to fetch block chart...")
        
        if selected_chart:
            logging.info("📦 Testing fetch_block_chart")
            block_chart = test_fetch_block_chart(nbi_client, selected_chart.name, selected_chart.all_versions[0])
            input("✅ Block chart fetched! Press Enter to continue to deploy service...")
            
            if block_chart:
                logging.info("⚙️ Testing deploy_service")
                test_deploy_service(nbi_client, site_id, selected_chart.name, selected_chart.all_versions[0], selected_chart.display_name)
                input("✅ Service deployed! Press Enter to get all deployed services...")

    logging.info("🗂️ Testing get_all_deployed_services")
    services = test_get_all_deployed_services(nbi_client)
    input("✅ All deployed services fetched! Press Enter to select a service to update...")
    
    if services:
        print("\nAvailable services:")
        for i, service in enumerate(services, 1):
            print(f"{i}. {service.service_chain.name} (ID: {service.service_chain.id})")
        
        while True:
            try:
                choice = int(input("\nEnter the number of the service you want to update (0 to skip): "))
                if choice == 0:
                    break
                if 1 <= choice <= len(services):
                    selected_service = services[choice - 1]
                    service_id = selected_service.service_chain.id
                    
                    logging.info(f"📡 Testing get_deployed_service_by_id for service ID: {service_id}")
                    service_details = test_get_deployed_service_by_id(nbi_client, service_id)
                    
                    if service_details:
                        new_http_port = int(input("Enter new HTTP port (or press Enter to keep current): ") or 0)
                        new_https_port = int(input("Enter new HTTPS port (or press Enter to keep current): ") or 0)
                        
                        if new_http_port or new_https_port:
                            logging.info("🔧 Testing update_service_node_ports")
                            test_update_service_node_ports(nbi_client, service_id, new_http_port, new_https_port)
                            input("✅ Service updated! Press Enter to continue...")
                        else:
                            print("No changes made to node ports.")
                    else:
                        print("Failed to fetch service details.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        logging.info("No services available to update.")

    logging.info("🗂️ Testing get_all_deployed_services")
    services = test_get_all_deployed_services(nbi_client)
    input("✅ All deployed services fetched! Press Enter to select a service to delete...")
    
    if services:
        service_id_to_delete = select_service_to_delete(services)
        if service_id_to_delete:
            logging.info(f"🗑️ Deleting service by ID: {service_id_to_delete}")
            response = nbi_client.delete_service_chain_by_id(service_id_to_delete)
            logging.info(f"🗑️ Delete service response: {response}")
        else:
            logging.info("Service deletion cancelled or no service selected.")
    else:
        logging.info("No services available to delete.")
