# FetchBlockChartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**chart_yaml** | **str** | Contents of Chart.yaml which define the chart&#39;s metadata. | [optional] 
**overrides_yaml** | **str** | Contents of overrides.yaml which specify configuration overrides. | [optional] 

## Example

```python
from openapi_client.models.fetch_block_chart_response import FetchBlockChartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchBlockChartResponse from a JSON string
fetch_block_chart_response_instance = FetchBlockChartResponse.from_json(json)
# print the JSON string representation of the object
print(FetchBlockChartResponse.to_json())

# convert the object into a dict
fetch_block_chart_response_dict = fetch_block_chart_response_instance.to_dict()
# create an instance of FetchBlockChartResponse from a dict
fetch_block_chart_response_from_dict = FetchBlockChartResponse.from_dict(fetch_block_chart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


