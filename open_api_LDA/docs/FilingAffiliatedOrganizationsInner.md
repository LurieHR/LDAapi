# FilingAffiliatedOrganizationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**url** | **str** |  | [optional] [readonly] 
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
**ppb_city** | **str** |  | [optional] [readonly] 
**ppb_state** | **str** |  | [optional] [readonly] 
**ppb_state_display** | **str** |  | [optional] 
**ppb_country** | **str** |  | [optional] [readonly] 
**ppb_country_display** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.filing_affiliated_organizations_inner import FilingAffiliatedOrganizationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilingAffiliatedOrganizationsInner from a JSON string
filing_affiliated_organizations_inner_instance = FilingAffiliatedOrganizationsInner.from_json(json)
# print the JSON string representation of the object
print(FilingAffiliatedOrganizationsInner.to_json())

# convert the object into a dict
filing_affiliated_organizations_inner_dict = filing_affiliated_organizations_inner_instance.to_dict()
# create an instance of FilingAffiliatedOrganizationsInner from a dict
filing_affiliated_organizations_inner_from_dict = FilingAffiliatedOrganizationsInner.from_dict(filing_affiliated_organizations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


