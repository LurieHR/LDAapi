# ListFilings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Filing]**](Filing.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_filings200_response import ListFilings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListFilings200Response from a JSON string
list_filings200_response_instance = ListFilings200Response.from_json(json)
# print the JSON string representation of the object
print(ListFilings200Response.to_json())

# convert the object into a dict
list_filings200_response_dict = list_filings200_response_instance.to_dict()
# create an instance of ListFilings200Response from a dict
list_filings200_response_from_dict = ListFilings200Response.from_dict(list_filings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


