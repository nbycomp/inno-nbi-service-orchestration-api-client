# DeviceCloudResourceChartLatestConfigInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**json_type** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**redacted** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.device_cloud_resource_chart_latest_config_inner import DeviceCloudResourceChartLatestConfigInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCloudResourceChartLatestConfigInner from a JSON string
device_cloud_resource_chart_latest_config_inner_instance = DeviceCloudResourceChartLatestConfigInner.from_json(json)
# print the JSON string representation of the object
print(DeviceCloudResourceChartLatestConfigInner.to_json())

# convert the object into a dict
device_cloud_resource_chart_latest_config_inner_dict = device_cloud_resource_chart_latest_config_inner_instance.to_dict()
# create an instance of DeviceCloudResourceChartLatestConfigInner from a dict
device_cloud_resource_chart_latest_config_inner_from_dict = DeviceCloudResourceChartLatestConfigInner.from_dict(device_cloud_resource_chart_latest_config_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


