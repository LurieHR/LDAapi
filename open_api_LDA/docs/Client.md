# Client


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
**registrant** | [**ContributionReportRegistrant**](ContributionReportRegistrant.md) |  | [optional] 

## Example

```python
from openapi_client.models.client import Client

# TODO update the JSON string below
json = "{}"
# create an instance of Client from a JSON string
client_instance = Client.from_json(json)
# print the JSON string representation of the object
print(Client.to_json())

# convert the object into a dict
client_dict = client_instance.to_dict()
# create an instance of Client from a dict
client_from_dict = Client.from_dict(client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


