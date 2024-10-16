# ChartKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from inno_nbi_api.models.chart_key import ChartKey

# TODO update the JSON string below
json = "{}"
# create an instance of ChartKey from a JSON string
chart_key_instance = ChartKey.from_json(json)
# print the JSON string representation of the object
print(ChartKey.to_json())

# convert the object into a dict
chart_key_dict = chart_key_instance.to_dict()
# create an instance of ChartKey from a dict
chart_key_from_dict = ChartKey.from_dict(chart_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


