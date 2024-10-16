# OktoResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**status** | [**OktoStatus**](OktoStatus.md) |  | [optional] 
**namespace** | **str** |  | [optional] 
**manifest** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.okto_resource import OktoResource

# TODO update the JSON string below
json = "{}"
# create an instance of OktoResource from a JSON string
okto_resource_instance = OktoResource.from_json(json)
# print the JSON string representation of the object
print(OktoResource.to_json())

# convert the object into a dict
okto_resource_dict = okto_resource_instance.to_dict()
# create an instance of OktoResource from a dict
okto_resource_from_dict = OktoResource.from_dict(okto_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


