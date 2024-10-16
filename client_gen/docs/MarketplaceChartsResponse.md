# MarketplaceChartsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charts** | [**List[ChartRepoIndexEntry]**](ChartRepoIndexEntry.md) |  | [optional] 

## Example

```python
from inno_nbi_api.models.marketplace_charts_response import MarketplaceChartsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceChartsResponse from a JSON string
marketplace_charts_response_instance = MarketplaceChartsResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceChartsResponse.to_json())

# convert the object into a dict
marketplace_charts_response_dict = marketplace_charts_response_instance.to_dict()
# create an instance of MarketplaceChartsResponse from a dict
marketplace_charts_response_from_dict = MarketplaceChartsResponse.from_dict(marketplace_charts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


