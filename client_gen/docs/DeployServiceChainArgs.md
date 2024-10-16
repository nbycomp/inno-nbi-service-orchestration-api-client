# DeployServiceChainArgs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**blocks** | [**List[BlockArgsDeploy]**](BlockArgsDeploy.md) |  | [optional] 

## Example

```python
from inno_nbi_api.models.deploy_service_chain_args import DeployServiceChainArgs

# TODO update the JSON string below
json = "{}"
# create an instance of DeployServiceChainArgs from a JSON string
deploy_service_chain_args_instance = DeployServiceChainArgs.from_json(json)
# print the JSON string representation of the object
print(DeployServiceChainArgs.to_json())

# convert the object into a dict
deploy_service_chain_args_dict = deploy_service_chain_args_instance.to_dict()
# create an instance of DeployServiceChainArgs from a dict
deploy_service_chain_args_from_dict = DeployServiceChainArgs.from_dict(deploy_service_chain_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


