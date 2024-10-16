# UpdateServiceChainArgs

Arguments to update a service chain including identification and block configuration details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the service chain to be updated. | [optional] 
**name** | **str** | The name of the service chain. | [optional] 
**blocks** | [**List[BlockArgsUpdate]**](BlockArgsUpdate.md) | A list of blocks to be updated or added to the service chain. | [optional] 

## Example

```python
from openapi_client.models.update_service_chain_args import UpdateServiceChainArgs

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServiceChainArgs from a JSON string
update_service_chain_args_instance = UpdateServiceChainArgs.from_json(json)
# print the JSON string representation of the object
print(UpdateServiceChainArgs.to_json())

# convert the object into a dict
update_service_chain_args_dict = update_service_chain_args_instance.to_dict()
# create an instance of UpdateServiceChainArgs from a dict
update_service_chain_args_from_dict = UpdateServiceChainArgs.from_dict(update_service_chain_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


