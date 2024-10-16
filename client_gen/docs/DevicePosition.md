# DevicePosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 

## Example

```python
from inno_nbi_api.models.device_position import DevicePosition

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePosition from a JSON string
device_position_instance = DevicePosition.from_json(json)
# print the JSON string representation of the object
print(DevicePosition.to_json())

# convert the object into a dict
device_position_dict = device_position_instance.to_dict()
# create an instance of DevicePosition from a dict
device_position_from_dict = DevicePosition.from_dict(device_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


