# inno_nbi_api.InfrastructureApi

All URIs are relative to *https://YOURENV.envs.nearbycomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_details**](InfrastructureApi.md#get_device_details) | **GET** /infrastructure/devices/{deviceId} | Retrieve details for a specific device within an organization
[**get_site_details**](InfrastructureApi.md#get_site_details) | **GET** /infrastructure/sites/{siteId} | Retrieve details for a specific site within an organization


# **get_device_details**
> DeviceResponse get_device_details(device_id)

Retrieve details for a specific device within an organization

### Example


```python
import inno_nbi_api
from inno_nbi_api.models.device_response import DeviceResponse
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
    api_instance = inno_nbi_api.InfrastructureApi(api_client)
    device_id = 'device_id_example' # str | The unique identifier of the device to fetch details for.

    try:
        # Retrieve details for a specific device within an organization
        api_response = api_instance.get_device_details(device_id)
        print("The response of InfrastructureApi->get_device_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->get_device_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The unique identifier of the device to fetch details for. | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved device details. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_details**
> SiteResponse get_site_details(site_id)

Retrieve details for a specific site within an organization

### Example


```python
import inno_nbi_api
from inno_nbi_api.models.site_response import SiteResponse
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
    api_instance = inno_nbi_api.InfrastructureApi(api_client)
    site_id = 'site_id_example' # str | The unique identifier of the site to fetch.

    try:
        # Retrieve details for a specific site within an organization
        api_response = api_instance.get_site_details(site_id)
        print("The response of InfrastructureApi->get_site_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->get_site_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The unique identifier of the site to fetch. | 

### Return type

[**SiteResponse**](SiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved site details. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

