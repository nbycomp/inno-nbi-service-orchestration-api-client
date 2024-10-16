# ChartRepoIndexEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**all_versions** | **List[str]** |  | [optional] 

## Example

```python
from inno_nbi_api.models.chart_repo_index_entry import ChartRepoIndexEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ChartRepoIndexEntry from a JSON string
chart_repo_index_entry_instance = ChartRepoIndexEntry.from_json(json)
# print the JSON string representation of the object
print(ChartRepoIndexEntry.to_json())

# convert the object into a dict
chart_repo_index_entry_dict = chart_repo_index_entry_instance.to_dict()
# create an instance of ChartRepoIndexEntry from a dict
chart_repo_index_entry_from_dict = ChartRepoIndexEntry.from_dict(chart_repo_index_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


