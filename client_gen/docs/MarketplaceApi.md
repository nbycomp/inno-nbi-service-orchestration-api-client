# openapi_client.MarketplaceApi

All URIs are relative to *https://YOURENV.envs.nearbycomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_block_chart**](MarketplaceApi.md#fetch_block_chart) | **GET** /marketplace/blockcharts/{blockName}/{blockVersion} | Retrieve specific block chart details from the marketplace
[**list_marketplace_charts**](MarketplaceApi.md#list_marketplace_charts) | **GET** /marketplace/blockcharts | List all available block charts in the marketplace


# **fetch_block_chart**
> FetchBlockChartResponse fetch_block_chart(block_name, block_version)

Retrieve specific block chart details from the marketplace

### Example


```python
import openapi_client
from openapi_client.models.fetch_block_chart_response import FetchBlockChartResponse
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
    api_instance = openapi_client.MarketplaceApi(api_client)
    block_name = 'block_name_example' # str | The unique name of the BlockChart to retrieve.
    block_version = 'block_version_example' # str | The version of the BlockChart to retrieve.

    try:
        # Retrieve specific block chart details from the marketplace
        api_response = api_instance.fetch_block_chart(block_name, block_version)
        print("The response of MarketplaceApi->fetch_block_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->fetch_block_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_name** | **str**| The unique name of the BlockChart to retrieve. | 
 **block_version** | **str**| The version of the BlockChart to retrieve. | 

### Return type

[**FetchBlockChartResponse**](FetchBlockChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the BlockChart details. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_marketplace_charts**
> MarketplaceChartsResponse list_marketplace_charts()

List all available block charts in the marketplace

### Example


```python
import openapi_client
from openapi_client.models.marketplace_charts_response import MarketplaceChartsResponse
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
    api_instance = openapi_client.MarketplaceApi(api_client)

    try:
        # List all available block charts in the marketplace
        api_response = api_instance.list_marketplace_charts()
        print("The response of MarketplaceApi->list_marketplace_charts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->list_marketplace_charts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MarketplaceChartsResponse**](MarketplaceChartsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed marketplace charts. |  -  |
**400** | Bad request due to invalid format or parameters. |  -  |
**403** | Forbidden access, authorization failed. |  -  |
**404** | Resource not found. |  -  |
**500** | Internal server error. |  -  |
**503** | Service unavailable or under maintenance. |  -  |
**0** | Default response for unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

