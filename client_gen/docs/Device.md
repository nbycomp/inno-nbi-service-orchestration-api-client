# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**tags** | [**List[DeviceTagsInner]**](DeviceTagsInner.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**position** | [**DevicePosition**](DevicePosition.md) |  | [optional] 
**specs** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**progress** | [**DeviceProgress**](DeviceProgress.md) |  | [optional] 
**site** | **str** |  | [optional] 
**cloud_resource_chart** | [**DeviceCloudResourceChart**](DeviceCloudResourceChart.md) |  | [optional] 
**org** | **str** |  | [optional] 

## Example

```python
from inno_nbi_api.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


