# BlockArgsDeploy

Defines either a new block to be added or an existing block to be updated within a service chain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the block. | [optional] 
**block_chart_name** | **str** | The name of the block chart associated with this block. | [optional] 
**block_chart_version** | **str** | The version of the block chart to be used. | [optional] 
**site_id** | **str** | The ID of the site associated with this block. | [optional] 

## Example

```python
from inno_nbi_api.models.block_args_deploy import BlockArgsDeploy

# TODO update the JSON string below
json = "{}"
# create an instance of BlockArgsDeploy from a JSON string
block_args_deploy_instance = BlockArgsDeploy.from_json(json)
# print the JSON string representation of the object
print(BlockArgsDeploy.to_json())

# convert the object into a dict
block_args_deploy_dict = block_args_deploy_instance.to_dict()
# create an instance of BlockArgsDeploy from a dict
block_args_deploy_from_dict = BlockArgsDeploy.from_dict(block_args_deploy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


