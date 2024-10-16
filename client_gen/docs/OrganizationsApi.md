# openapi_client.OrganizationsApi

All URIs are relative to *https://YOURENV.envs.nearbycomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organizations**](OrganizationsApi.md#get_organizations) | **GET** /organizations | Retrieve details for all organizations accessible to the user


# **get_organizations**
> List[Organization] get_organizations()

Retrieve details for all organizations accessible to the user

### Example


```python
import openapi_client
from openapi_client.models.organization import Organization
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://YOURENV.envs.nearbycomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://YOURENV.envs.nearbycomputing.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OrganizationsApi(api_client)

    try:
        # Retrieve details for all organizations accessible to the user
        api_response = api_instance.get_organizations()
        print("The response of OrganizationsApi->get_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organizations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Organization]**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved organizations. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

