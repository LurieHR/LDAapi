# FilingForeignEntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**contribution** | **decimal.Decimal** |  | [optional] [readonly] 
**ownership_percentage** | **decimal.Decimal** |  | [optional] [readonly] 
**address** | **str** |  | [optional] [readonly] 
**city** | **str** |  | [optional] [readonly] 
**state** | **str** |  | [optional] [readonly] 
**state_display** | **str** |  | [optional] 
**country** | **str** |  | [optional] [readonly] 
**country_display** | **str** |  | [optional] 
**ppb_city** | **str** |  | [optional] [readonly] 
**ppb_state** | **str** |  | [optional] [readonly] 
**ppb_state_display** | **str** |  | [optional] 
**ppb_country** | **str** |  | [optional] [readonly] 
**ppb_country_display** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.filing_foreign_entities_inner import FilingForeignEntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilingForeignEntitiesInner from a JSON string
filing_foreign_entities_inner_instance = FilingForeignEntitiesInner.from_json(json)
# print the JSON string representation of the object
print(FilingForeignEntitiesInner.to_json())

# convert the object into a dict
filing_foreign_entities_inner_dict = filing_foreign_entities_inner_instance.to_dict()
# create an instance of FilingForeignEntitiesInner from a dict
filing_foreign_entities_inner_from_dict = FilingForeignEntitiesInner.from_dict(filing_foreign_entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


