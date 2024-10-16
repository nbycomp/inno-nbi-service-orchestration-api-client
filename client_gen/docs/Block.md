# Block


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**org** | **str** |  | [optional] 
**blockchart_name** | **str** |  | [optional] 
**blockchart_version** | **str** |  | [optional] 
**blockchart_values** | **str** |  | [optional] 
**status** | [**OktoStatus**](OktoStatus.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**device_ids** | **List[str]** |  | [optional] 

## Example

```python
from inno_nbi_api.models.block import Block

# TODO update the JSON string below
json = "{}"
# create an instance of Block from a JSON string
block_instance = Block.from_json(json)
# print the JSON string representation of the object
print(Block.to_json())

# convert the object into a dict
block_dict = block_instance.to_dict()
# create an instance of Block from a dict
block_from_dict = Block.from_dict(block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


