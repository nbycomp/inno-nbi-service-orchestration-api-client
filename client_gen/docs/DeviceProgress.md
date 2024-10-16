# DeviceProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step** | **int** |  | [optional] 
**goal** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.device_progress import DeviceProgress

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceProgress from a JSON string
device_progress_instance = DeviceProgress.from_json(json)
# print the JSON string representation of the object
print(DeviceProgress.to_json())

# convert the object into a dict
device_progress_dict = device_progress_instance.to_dict()
# create an instance of DeviceProgress from a dict
device_progress_from_dict = DeviceProgress.from_dict(device_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


