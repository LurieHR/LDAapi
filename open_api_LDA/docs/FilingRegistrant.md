# FilingRegistrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**url** | **str** |  | [optional] [readonly] 
**house_registrant_id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**address_1** | **str** |  | [optional] [readonly] 
**address_2** | **str** |  | [optional] [readonly] 
**address_3** | **str** |  | [optional] [readonly] 
**address_4** | **str** |  | [optional] [readonly] 
**city** | **str** |  | [optional] [readonly] 
**state** | **str** |  | [optional] [readonly] 
**state_display** | **str** |  | [optional] 
**zip** | **str** |  | [optional] [readonly] 
**country** | **str** |  | [optional] [readonly] 
**country_display** | **str** |  | [optional] 
**ppb_country** | **str** |  | [optional] [readonly] 
**ppb_country_display** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] [readonly] 
**contact_telephone** | **str** |  | [optional] [readonly] 
**dt_updated** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.filing_registrant import FilingRegistrant

# TODO update the JSON string below
json = "{}"
# create an instance of FilingRegistrant from a JSON string
filing_registrant_instance = FilingRegistrant.from_json(json)
# print the JSON string representation of the object
print(FilingRegistrant.to_json())

# convert the object into a dict
filing_registrant_dict = filing_registrant_instance.to_dict()
# create an instance of FilingRegistrant from a dict
filing_registrant_from_dict = FilingRegistrant.from_dict(filing_registrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


