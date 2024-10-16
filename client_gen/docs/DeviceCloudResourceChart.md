# DeviceCloudResourceChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ChartKey**](ChartKey.md) |  | [optional] 
**latest_config** | [**List[DeviceCloudResourceChartLatestConfigInner]**](DeviceCloudResourceChartLatestConfigInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_cloud_resource_chart import DeviceCloudResourceChart

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCloudResourceChart from a JSON string
device_cloud_resource_chart_instance = DeviceCloudResourceChart.from_json(json)
# print the JSON string representation of the object
print(DeviceCloudResourceChart.to_json())

# convert the object into a dict
device_cloud_resource_chart_dict = device_cloud_resource_chart_instance.to_dict()
# create an instance of DeviceCloudResourceChart from a dict
device_cloud_resource_chart_from_dict = DeviceCloudResourceChart.from_dict(device_cloud_resource_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


