# DeviceTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.device_tags_inner import DeviceTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceTagsInner from a JSON string
device_tags_inner_instance = DeviceTagsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceTagsInner.to_json())

# convert the object into a dict
device_tags_inner_dict = device_tags_inner_instance.to_dict()
# create an instance of DeviceTagsInner from a dict
device_tags_inner_from_dict = DeviceTagsInner.from_dict(device_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


