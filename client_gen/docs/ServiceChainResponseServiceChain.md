# ServiceChainResponseServiceChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**revision** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**blocks** | [**List[Block]**](Block.md) |  | [optional] 
**status** | **str** |  | [optional] 
**org** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.service_chain_response_service_chain import ServiceChainResponseServiceChain

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceChainResponseServiceChain from a JSON string
service_chain_response_service_chain_instance = ServiceChainResponseServiceChain.from_json(json)
# print the JSON string representation of the object
print(ServiceChainResponseServiceChain.to_json())

# convert the object into a dict
service_chain_response_service_chain_dict = service_chain_response_service_chain_instance.to_dict()
# create an instance of ServiceChainResponseServiceChain from a dict
service_chain_response_service_chain_from_dict = ServiceChainResponseServiceChain.from_dict(service_chain_response_service_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


