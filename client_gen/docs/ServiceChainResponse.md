# ServiceChainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_chain** | [**ServiceChainResponseServiceChain**](ServiceChainResponseServiceChain.md) |  | [optional] 

## Example

```python
from inno_nbi_api.models.service_chain_response import ServiceChainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceChainResponse from a JSON string
service_chain_response_instance = ServiceChainResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceChainResponse.to_json())

# convert the object into a dict
service_chain_response_dict = service_chain_response_instance.to_dict()
# create an instance of ServiceChainResponse from a dict
service_chain_response_from_dict = ServiceChainResponse.from_dict(service_chain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


