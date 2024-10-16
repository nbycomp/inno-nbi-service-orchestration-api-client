# BlockArgsUpdate

Defines either a new block to be added or an existing block to be updated within a service chain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of a previously-deployed block to update. Providing this parameter implies an update to an existing block; inputs with no ID will be treated as new blocks. | [optional] 
**display_name** | **str** | The display name of the block. | [optional] 
**block_chart_name** | **str** | The name of the block chart associated with this block. | [optional] 
**block_chart_version** | **str** | The version of the block chart to be used. | [optional] 
**values** | **str** | A string of values necessary for configuring the block, typically in JSON or YAML format. | [optional] 

## Example

```python
from inno_nbi_api.models.block_args_update import BlockArgsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BlockArgsUpdate from a JSON string
block_args_update_instance = BlockArgsUpdate.from_json(json)
# print the JSON string representation of the object
print(BlockArgsUpdate.to_json())

# convert the object into a dict
block_args_update_dict = block_args_update_instance.to_dict()
# create an instance of BlockArgsUpdate from a dict
block_args_update_from_dict = BlockArgsUpdate.from_dict(block_args_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


