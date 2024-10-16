# inno_nbi_api.ServicesApi

All URIs are relative to *https://YOURENV.envs.nearbycomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_chain_by_id**](ServicesApi.md#delete_service_chain_by_id) | **DELETE** /services/{serviceId} | Delete a deployed service chain by ID
[**deploy_service**](ServicesApi.md#deploy_service) | **POST** /services | Deploy a new service chain
[**get_all_deployed_services**](ServicesApi.md#get_all_deployed_services) | **GET** /services | Retrieve all deployed service chains
[**get_deployed_service**](ServicesApi.md#get_deployed_service) | **GET** /services/{serviceId} | Retrieve deployed service chain by ID
[**update_service**](ServicesApi.md#update_service) | **PUT** /services/{serviceId} | Update a deployed service chain


# **delete_service_chain_by_id**
> str delete_service_chain_by_id(service_id)

Delete a deployed service chain by ID

### Example


```python
import inno_nbi_api
from inno_nbi_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://YOURENV.envs.nearbycomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = inno_nbi_api.Configuration(
    host = "https://YOURENV.envs.nearbycomputing.com"
)


# Enter a context with an instance of the API client
with inno_nbi_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = inno_nbi_api.ServicesApi(api_client)
    service_id = 'service_id_example' # str | The unique identifier of the service to operate on.

    try:
        # Delete a deployed service chain by ID
        api_response = api_instance.delete_service_chain_by_id(service_id)
        print("The response of ServicesApi->delete_service_chain_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service_chain_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service to operate on. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service chain deleted successfully. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_service**
> str deploy_service(deploy_service_chain_args)

Deploy a new service chain

### Example


```python
import inno_nbi_api
from inno_nbi_api.models.deploy_service_chain_args import DeployServiceChainArgs
from inno_nbi_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://YOURENV.envs.nearbycomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = inno_nbi_api.Configuration(
    host = "https://YOURENV.envs.nearbycomputing.com"
)


# Enter a context with an instance of the API client
with inno_nbi_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = inno_nbi_api.ServicesApi(api_client)
    deploy_service_chain_args = inno_nbi_api.DeployServiceChainArgs() # DeployServiceChainArgs | 

    try:
        # Deploy a new service chain
        api_response = api_instance.deploy_service(deploy_service_chain_args)
        print("The response of ServicesApi->deploy_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->deploy_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploy_service_chain_args** | [**DeployServiceChainArgs**](DeployServiceChainArgs.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service deployed successfully. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_deployed_services**
> List[ServiceChainResponse] get_all_deployed_services()

Retrieve all deployed service chains

### Example


```python
import inno_nbi_api
from inno_nbi_api.models.service_chain_response import ServiceChainResponse
from inno_nbi_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://YOURENV.envs.nearbycomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = inno_nbi_api.Configuration(
    host = "https://YOURENV.envs.nearbycomputing.com"
)


# Enter a context with an instance of the API client
with inno_nbi_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = inno_nbi_api.ServicesApi(api_client)

    try:
        # Retrieve all deployed service chains
        api_response = api_instance.get_all_deployed_services()
        print("The response of ServicesApi->get_all_deployed_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_all_deployed_services: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ServiceChainResponse]**](ServiceChainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list of all deployed services. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_service**
> ServiceChainResponse get_deployed_service(service_id)

Retrieve deployed service chain by ID

### Example


```python
import inno_nbi_api
from inno_nbi_api.models.service_chain_response import ServiceChainResponse
from inno_nbi_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://YOURENV.envs.nearbycomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = inno_nbi_api.Configuration(
    host = "https://YOURENV.envs.nearbycomputing.com"
)


# Enter a context with an instance of the API client
with inno_nbi_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = inno_nbi_api.ServicesApi(api_client)
    service_id = 'service_id_example' # str | The unique identifier of the service to operate on.

    try:
        # Retrieve deployed service chain by ID
        api_response = api_instance.get_deployed_service(service_id)
        print("The response of ServicesApi->get_deployed_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_deployed_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service to operate on. | 

### Return type

[**ServiceChainResponse**](ServiceChainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved service details. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service**
> ServiceChainResponse update_service(service_id, update_service_chain_args)

Update a deployed service chain

### Example


```python
import inno_nbi_api
from inno_nbi_api.models.service_chain_response import ServiceChainResponse
from inno_nbi_api.models.update_service_chain_args import UpdateServiceChainArgs
from inno_nbi_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://YOURENV.envs.nearbycomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = inno_nbi_api.Configuration(
    host = "https://YOURENV.envs.nearbycomputing.com"
)


# Enter a context with an instance of the API client
with inno_nbi_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = inno_nbi_api.ServicesApi(api_client)
    service_id = 'service_id_example' # str | The unique identifier of the service to operate on.
    update_service_chain_args = inno_nbi_api.UpdateServiceChainArgs() # UpdateServiceChainArgs | 

    try:
        # Update a deployed service chain
        api_response = api_instance.update_service(service_id, update_service_chain_args)
        print("The response of ServicesApi->update_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service to operate on. | 
 **update_service_chain_args** | [**UpdateServiceChainArgs**](UpdateServiceChainArgs.md)|  | 

### Return type

[**ServiceChainResponse**](ServiceChainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service updated successfully. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

