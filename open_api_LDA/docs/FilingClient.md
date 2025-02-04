# FilingClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**url** | **str** |  | [optional] [readonly] 
**client_id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**general_description** | **str** |  | [optional] [readonly] 
**client_government_entity** | **bool** |  | [optional] [readonly] 
**client_self_select** | **bool** |  | [optional] [readonly] 
**state** | **str** |  | [optional] [readonly] 
**state_display** | **str** |  | [optional] 
**country** | **str** |  | [optional] [readonly] 
**country_display** | **str** |  | [optional] 
**ppb_state** | **str** |  | [optional] [readonly] 
**ppb_state_display** | **str** |  | [optional] 
**ppb_country** | **str** |  | [optional] [readonly] 
**ppb_country_display** | **str** |  | [optional] 
**effective_date** | **date** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.filing_client import FilingClient

# TODO update the JSON string below
json = "{}"
# create an instance of FilingClient from a JSON string
filing_client_instance = FilingClient.from_json(json)
# print the JSON string representation of the object
print(FilingClient.to_json())

# convert the object into a dict
filing_client_dict = filing_client_instance.to_dict()
# create an instance of FilingClient from a dict
filing_client_from_dict = FilingClient.from_dict(filing_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


