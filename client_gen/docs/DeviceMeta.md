# DeviceMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the device. | [optional] 
**type** | **str** | The type of the device. | [optional] 

## Example

```python
from openapi_client.models.device_meta import DeviceMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceMeta from a JSON string
device_meta_instance = DeviceMeta.from_json(json)
# print the JSON string representation of the object
print(DeviceMeta.to_json())

# convert the object into a dict
device_meta_dict = device_meta_instance.to_dict()
# create an instance of DeviceMeta from a dict
device_meta_from_dict = DeviceMeta.from_dict(device_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


